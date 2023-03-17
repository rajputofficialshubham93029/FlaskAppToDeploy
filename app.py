import datetime
from flask import Flask , render_template , request
from pymongo import MongoClient
import urllib
import os
app = Flask(__name__)
mongo_uri = "mongodb+srv://rajputsrshubham930:" + urllib.parse.quote("Shubham123@") + "@todolistappication.tn0o23o.mongodb.net/test"
client = MongoClient(mongo_uri)
app.db = client.todolistapplicationdata

entries = []

@app.route("/")
def hello():
    entries = [(
                entry['content'] , entry['date']

        ) for entry in app.db.entries.find({})]
    return render_template("hello.html"  , entries=entries)