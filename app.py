from flask import Flask, request, jsonify
from firebase import Firebase

# from flask_pymongo import PyMongo
import urllib.parse

app = Flask(__name__)
# app.config[
#     'MONGO_URI'] = 'mongodb+srv://fayisdev:--Fayisdevmangodb--@booksounds.b2ove.mongodb.net/booksounds?retryWrites=true&w=majority'

# mango = PyMongo(app)
# db_collection = mango.db.booksounds
config = {
    "databaseURL" : "https://booksounds-5dc91-default-rtdb.firebaseio.com/",
    "apiKey": "AIzaSyCM8hHvn9wtcCTSMJHblHH04z6-bBF3LhM",
    "authDomain": "booksounds-5dc91.firebaseapp.com",
    "projectId": "booksounds-5dc91",
    "storageBucket": "booksounds-5dc91.appspot.com",
    "messagingSenderId": "768531408149",
    "appId": "1:768531408149:web:ed3a1aeba99a4c0aff751c",
    "measurementId": "G-PDEVX9SFR2"
  }
firebase = Firebase(config)

storage = firebase.storage()
pdfref = storage.child('pdf')


@app.route('/', methods=['POST'])
def hello_world():
    d = {'Query': 'hello'}
    return jsonify(d)


ALLOWED_EXTENSIONS = {'pdf', 'png'}


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/upload', methods=['POST'])
def upload():
    if 'file' in request.files:
        file = request.files['file']
        if file.filename != '' and allowed_file(file.filename):
            pdfref.put(file)

            res = {"msg": "file uploaded"}
        else:
            res = {"msg": "no file part or not allowed extension"}
    else:
        res = {"msg": "no file"}
    return jsonify(res)


@app.route('/download', methods=['POST'])
def download():
    return jsonify({"test": "test"})


if __name__ == '__main__':
    app.run()
