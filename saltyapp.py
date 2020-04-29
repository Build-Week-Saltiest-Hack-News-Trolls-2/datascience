"""Saltiest Hacker with Flask."""
from flask import Flask
import requests
from hackernews import HackerNews 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import pandas as pd
import os
from dotenv import load_dotenv
import psycopg2
from psycopg2.extras import execute_values


hn = HackerNews()

# request last 2000 items
last = hn.get_last(2000)


# view item type and item text
items_dict = []
for item in last:
    #only keep users and text from comments
  if item.item_type == 'comment':
    user = item.by
    text = item.text

    #output metrics as a row
    dictionary_data = {"User":user, "Text":text}
    items_dict.append(dictionary_data) 

# create dataframe for modelling use
df = pd.DataFrame.from_dict(items_dict)


# ** LOAD AND RUN MODEL HERE **


# Put model results into database
app = Flask(__name__)

load_dotenv()
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')

connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
print("CONNECTION:", connection)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# convert df to list of tuples
tuples = list(df.itertuples(index=False,name=None))

# create cursor connection
cursor = connection.cursor()
print("CURSOR:", cursor)

#execute queries
cursor.execute("CREATE TABLE IF NOT EXISTS Comment (id serial PRIMARY KEY, user VARCHAR(10), text VARCHAR(30));")   # rating INTEGER
result = cursor.fetchall()

insertion_query = "INSERT INTO  Comment (id, user, text) VALUES %s"     # rating
execute_values(cursor,insertion_query,tuples)

connection.commit()

# create Comment class
# class Comment(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     user = db.Column(db.String(25))
#     text = db.Column(db.String(25))
    #rating = db.Column(db.String(25))



@app.route('/')
def root():
    """Refreshes data in database"""
    db.drop_all()
    db.create_all()

     # Get data from  api, make objects with it, and add to db
    for row in df.index:
        db_comment = Comment(user=df.User[row],text=df.Text[row])     # rating = df.Rating[row]
        db.session.add(db_comment)

    db.session.commit()
    return 'Data stored'


# def parse_records(database_records):
#     """
#     A helper method for converting a list of database record objects into a list of dictionaries, so they can be returned as JSON
#     Param: database_records (a list of db.Model instances)
#     Example: parse_records(User.query.all())
#     Returns: a list of dictionaries, each corresponding to a record, like...
#         [
#             {"id": 1, "title": "Book 1"},
#             {"id": 2, "title": "Book 2"},
#             {"id": 3, "title": "Book 3"},
#         ]
#     """
#     parsed_records = []
#     for record in database_records:
#         print(record)
#         parsed_record = record.__dict__
#         del parsed_record["_sa_instance_state"]
#         parsed_records.append(parsed_record)

#     return parsed_records