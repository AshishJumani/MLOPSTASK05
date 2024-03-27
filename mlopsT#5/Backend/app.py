from flask import Flask, request
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient("mongodb://database:27017/")
db = client["mydatabase"]
collection = db["users"]

@app.route('/store', methods=['POST'])
def store_data():
    name = request.form['name']
    email = request.form['email']
    collection.insert_one({'name': name, 'email': email})
    return 'Data stored successfully.'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
