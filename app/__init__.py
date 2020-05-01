from flask import Flask
import requests
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.stat_routes import stat_routes
from app.models import db, migrate


def create_app():
    app = Flask(__name__)

    # load_dotenv()

    app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://bmszptoo:I5aJwqm9vFBWYp0rpS2tS1FyV5IEcId6@drona.db.elephantsql.com:5432/bmszptoo"

    # db = SQLAlchemy(app)
    # migrate = Migrate(app, db)

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(stat_routes)
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)