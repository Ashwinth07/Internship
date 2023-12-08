import os
from flask import Flask
from models.feedback import db
from flask_sqlalchemy import SQLAlchemy
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

ENV = os.environ.get('FLASK_ENV', 'dev')

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
    mongo_uri = os.environ.get('MONGO_URI')
    app.config['MONGO_URI'] = mongo_uri
    mongo_client = MongoClient(app.config['MONGO_URI'])
    mongo_db = mongo_client.Users

    if mongo_db is not None:
        print("Connected to MongoDB")
    else:
        print("Failed to connect to MongoDB")

else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = ''

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
def register_blueprints():
    from controllers.feedback_controller import feedback
    from controllers.login_controller import mongo_data
    app.register_blueprint(mongo_data)
    app.register_blueprint(feedback)

if __name__ == '__main__':
    register_blueprints()
    app.run(host="0.0.0.0", port=4000, debug=True)
