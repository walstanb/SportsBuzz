from flask import Flask
from config import Config
from flask_mongoengine import MongoEngine
import pymongo

app = Flask(__name__)
app.config.from_object(Config)

conn = pymongo.MongoClient("mongodb+srv://sbuzzdbuser:rTZqgmtHXhpISrR7@cluster0.60uwm.gcp.mongodb.net/sportsbuzzdb?retryWrites=true&w=majority")
db = conn["sportsbuzzdb"]

from application import routes