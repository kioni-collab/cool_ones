import psycopg2
from flask import Flask, render_template, request
from flask_cors import CORS
from psycopg2.extras import RealDictCursor
import math
from DBquery import search_room_db, search_building_db, search_dept_db, search_asset_location_db 
from DBquery import add_ticket_db,add_ticket_asset_db,valid_status_id,valid_asset
from util import safe_int, safe_date, safe_id
import datetime
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
    barcode = safe_int(request.args.get('barcode', 1), 1)
    with conn.cursor() as cur:
        results = search_asset_location_db(cur, barcode)
        return results


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
#DOC: addes a new tickets, first checks if status and barcode are valid 
# to make sure we dont add an element into the ticket table that doesnt correspond 
# ticket asset table. then inset into both tables first tickets then ticket assets
def add_ticket():
    ticket_num = request.form["ticket_num"]
    start_year = request.form["start_year"]
    start_month = request.form["start_month"]
    start_day = request.form["start_day"]
    end_year = request.form["end_year"]
    end_month = request.form["end_month"]
    end_day = request.form["end_day"]
    room_num = request.form["room_num"]
    building_id = safe_int(request.form["building_id"], 1)
    tech_id = safe_int(request.form["tech_id"], 1)
    client_name = request.form["client_name"]
    descr = request.form["descr"]
    start_date = safe_date(start_year, start_month,
                           start_day, datetime.datetime(1900, 1, 1))
    end_date = safe_date(end_year, end_month, end_day,
                         datetime.datetime(1900, 1, 1))
    barcode = safe_int(request.form["barcode"],1)
    status = int(request.form["status"])
    with conn.cursor() as cur:
        if safe_id(status,[i["id"] for i in valid_status_id(cur)]) and safe_id(barcode,[i["barcode"] for i in valid_asset(cur)]):
            add_ticket_db(cur, ticket_num, start_date, end_date,
                        room_num, building_id, tech_id, client_name, descr)
            add_ticket_asset_db(cur,ticket_num,barcode,status)
    conn.commit()

        

    pass


@app.route("/newasset", methods=['Post'])
def add_asset():
    pass
