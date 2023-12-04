from flask import Flask
from controllers.feedback_controller import feedback
from models.feedback import db
from flask_sqlalchemy import SQLAlchemy
from pymongo import MongoClient
from controllers.mongo_data_controller import mongo_data


app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb+srv://ashwinth:12345@cluster0.lao3ol1.mongodb.net/Users?retryWrites=true&w=majority'
mongo_client = MongoClient(app.config['MONGO_URI'])
mongo_db = mongo_client.Users

if mongo_db is not None:
    print("Connected to MongoDB")
else:
    print("Failed to connect to MongoDB")

ENV = 'dev'

if ENV == 'dev':
    app.debug = True
    # get sensitive information from .env file 
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:12345@localhost:5432/lexus'
    # move mongo db connection here 

else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = ''

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

app.register_blueprint(mongo_data)
app.register_blueprint(feedback)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=4000, debug=True)
