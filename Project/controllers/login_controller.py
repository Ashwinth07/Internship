from flask import Blueprint, request, jsonify, render_template
from pymongo import MongoClient
from models.login import MongoData
from app import mongo_db

mongo_data = Blueprint('mongo_data', __name__)
@mongo_data.route('/')
def index():
    return render_template('Forms.html')

@mongo_data.route('/add_mongo_data', methods=['POST'])
def add_mongo_data():
    field1 = request.form['field1']
    field2 = request.form['field2']
    new_data = MongoData(field1, field2)
    data_dict = new_data.to_dict()
    mongo_db['sample'].insert_one(data_dict)

    return jsonify({'message': 'Data added to MongoDB successfully'})


