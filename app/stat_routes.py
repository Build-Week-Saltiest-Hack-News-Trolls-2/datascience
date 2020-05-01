#from app.haxor_analysis import df
from app.models import Comment, db, parse_records
from flask import Blueprint, render_template, jsonify

stat_routes = Blueprint("stat_routes", __name__)


# @stat_routes.route('/stats/refresh')
# def refresh():
#     """Refreshes data in database"""
#     db.drop_all()
#     db.create_all()

#      # Get data from  api, make objects with it, and add to db
#     for row in df.index:
#         db_comment = Comment(user=df.User[row],text=df.Text[row],sentiment=df.vader_pred[row])     # rating = df.Rating[row]
#         db.session.add(db_comment)

#     db.session.commit()
#     return 'Data stored'

# GET /api/comments

# @stat_routes.route('/stats/comments')
# def return_by_id():

    #return render_template("users.html", users=db_comment)

# GET /api/comments/all

@stat_routes.route('/stats/comments/all')
def return_all():
    db_comments = Comment.query.all()
    comments_response = parse_records(db_comments)
    json_comments = jsonify(comments_response)
    
    return json_comments

    #return render_template("users.html", users=db_comments.user,
    #                       text=db_comments.text, sentiment=db_comments.sentiment)

#json_ids = jsonify(db_comment.id)
    #json_users = jsonify(db_comment.user)
    #json_text = jsonify(db_comment.text)
    #json_sentiment = jsonify(db_comment.sentiment)

# @stat_routes.route('/stats/comments/ids')
# def return_ids():
#     db_comments = Comment.query.all()

#     comments_response = parse_records(db_comments)
#     db_ids = comments_response['user']
#     json_ids = jsonify(db_ids)
    
#     return json_ids

# @stat_routes.route('/stats/comments/users')
# def return_users():
#     db_comments = Comment.query.all()
#     db_users = db_comments.user
#     comments_response = parse_records(db_users)
#     json_users = jsonify(comments_response)
    
#     return json_users

# @stat_routes.route('/stats/comments/text')
# def return_text():
#     db_comments = Comment.query.all()
#     db_text = db_comments.text
#     comments_response = parse_records(db_text)
#     json_text = jsonify(comments_response)
    
#     return json_text

# @stat_routes.route('/stats/comments/sentiment')
# def return_sentiment():
#     db_comments = Comment.query.all()
#     db_sentiment = db_comments.sentiment
#     comments_response = parse_records(db_sentiment)
#     json_sentiment = jsonify(comments_response)
    
#     return json_sentiment