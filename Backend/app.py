import psycopg2
from flask import Flask, render_template, request
from flask_cors import CORS
from psycopg2.extras import RealDictCursor
import math
from DBquery import search_room_db, search_building_db, search_dept_db
from util import safe_int
conn = psycopg2.connect(
    "host=db dbname=postgres user=postgres password=postgres",
    cursor_factory=RealDictCursor)

app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# TODO: create HTML endpoint and
# parametrs for each GET Method

# DOC: will return all assets in room in a json


@app.route("/room", methods=['GET'])
def search_room():
    room_num = request.args.get('room_num', "Student Success Center")
    building_id = safe_int(request.args.get('building_id', 1), 1)
    with conn.cursor() as cur:
        results = search_room_db(cur, room_num, building_id)
        return results

# Doc: returns all rooms in a building


@app.route("/building", methods=['GET'])
def search_building():
    building_id = safe_int(request.args.get('building_id', 1), 1)

    with conn.cursor() as cur:
        results = search_building_db(cur, building_id)
        return results


@app.route("/dept", methods=['GET'])
def search_dept():
    dept_id = safe_int(request.args.get('dept_id', 1), 1)
    with conn.cursor() as cur:
        results = search_dept_db(cur, dept_id)
        return results
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
