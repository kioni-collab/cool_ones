import psycopg2
from flask import Flask, render_template, request
from flask_cors import CORS
from psycopg2.extras import RealDictCursor
import math
conn = psycopg2.connect(
    "host=db dbname=postgres user=postgres password=postgres",
    cursor_factory=RealDictCursor)

app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# TODO: create /sets HTML endpoint
@app.route("/room", methods=['GET'])
def search_room():
    pass

@app.route("/building", methods=['GET'])
def search_building():
    pass
@app.route("/dept", methods=['GET'])
def search_dept():
    pass
@app.route("/computerspecs", methods=['GET'])
def search_computer_specs():
    pass

@app.route("/computerlocation", methods=['GET'])
def search_computer_location():
    pass

@app.route("/tickethistory", methods=['GET'])
def search_ticket_history():
    pass
@app.route("/login", methods=['GET'])
def login():
    pass

@app.route("/profile", methods=['GET'])
def profile_info():
    pass

@app.route("/newticket", methods=['POST'])
def add_ticket():
    pass

@app.route("/newasset", methods=['Post'])
def add_asset():
    pass

