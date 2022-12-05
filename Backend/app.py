"""App.py reads in endpoints and does specified actions based on form informaiton"""
import math
import datetime
import psycopg2
from flask import Flask, render_template, request,Response
#Error above will vanish when frontend combines with backend, and Math might be used, review later
#if math is actually needed
from flask_cors import CORS
from psycopg2.extras import RealDictCursor
from DBquery import (search_room_db, search_building_db, search_dept_db,
                    search_asset_location_db, search_ticket_history_db)
from DBquery import add_ticket_db,add_ticket_asset_db,add_asset_db,valid_status_id,valid_asset
from util import safe_int, safe_date, safe_id

conn = psycopg2.connect(
    "host=db dbname=postgres user=postgres password=postgres",
    cursor_factory=RealDictCursor)

app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

def add_asset_option(barcode:int,model:str,purch_date:datetime,type:int):
    """DOC:Ran by new ticket IF ticket is making new asset, insert inputed data into the asset table
    by running add_asset_db in DBQuery. Note: Type is a default data type, so we're renaming it,
    which is fine, so long as we don't need it"""
    with conn.cursor() as cur:
        result = add_asset_db(cur,barcode,model,purch_date,type)
        return result

@app.route("/room", methods=['GET'])
def search_room():
    """DOC: will return all assets in room in a json"""
    room_num = request.args.get('room_num', "Student Success Center")
    building_id = safe_int(request.args.get('building_id', 1), 1)
    with conn.cursor() as cur:
        results = search_room_db(cur, room_num, building_id)
        return results




@app.route("/building", methods=['GET'])
def search_building():
    """DOC: will return all assets in room in a json"""
    building_id = safe_int(request.args.get('building_id', 1), 1)
    with conn.cursor() as cur:
        results = search_building_db(cur, building_id)
        return results


@app.route("/dept", methods=['GET'])
def search_dept():
    """Returns room numbers, building name and which department it's from,
    so long as safe_int checks that A, it's an Int, and B, that Dept ID is valid"""
    dept_id = safe_int(request.args.get('dept_id', 1), 1)
    with conn.cursor() as cur:
        results = search_dept_db(cur, dept_id)
        return results


@app.route("/computerspecs", methods=['GET'])
def search_computer_specs():
    """TODO: ZANE"""


@app.route("/computerlocation", methods=['GET'])
def search_computer_location():
    """DOC: Searches for an assets location (Room number, flooor, building name, and asset)
    By searching for ticket's that match the barcode, ordered by the latest ticket,
    in order to identify where it was last"""
    barcode = safe_int(request.args.get('barcode', 1), 1)
    with conn.cursor() as cur:
        results = search_asset_location_db(cur, barcode)
        return results


@app.route("/tickethistory", methods=['GET'])
def search_ticket_history():
    """DOC: See Search_Ticket_History in DBQuery for better sight of what happens.
    This reads in all our variables, making sure they're safe.
    This selects everything from the ticket table, technician first/last
    name, client name, everything you'd need to know about a ticket"""
    ticket_num = request.args.get("ticket_num", "")
    end_year = request.args.get("end_year")
    end_month = request.args.get("end_month")
    end_day = request.args.get("end_day")
    status = safe_int(request.args.get("status"),None)
    room_num = request.args.get("room_num", "")
    building_id = safe_int(request.args.get("building_id"),None)
    tech_first_name = request.args.get("tech_first_name", "")
    tech_last_name = request.args.get("tech_last_name", "")
    client_name = request.args.get("client_name", "")
    barcode = safe_int(request.args.get("barcode"),None)
    end_date = safe_date(end_year, end_month, end_day,
                         None)
    with conn.cursor() as cur:
        result = search_ticket_history_db(cur,ticket_num,end_date,status,room_num,
                                        building_id,tech_first_name,tech_last_name,
                                        client_name,barcode)
        return result

@app.route("/newticket", methods=['PUT'])
def add_ticket():
    """DOC: adds a new tickets, first checks if status and barcode are valid
    to make sure we don't add an element into the ticket table that doesn't correspond
    ticket asset table. Then inset into both tables first tickets then ticket assets"""
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
    adding_asset =  request.form["adding_asset"] or False
    if adding_asset:
        model = request.form["model"] or ""
        purch_year = request.form["purch_year"]
        purch_month = request.form["purch_month"]
        purch_day = request.form["purch_day"]
        purch_date = safe_date(purch_year, purch_month,
                           purch_day, datetime.datetime(1900, 1, 1))
        type = request.form["type"]
        add_asset_option(barcode,model,purch_date,type)

    with conn.cursor() as cur:
        if (safe_id(status,[i["id"] for i in valid_status_id(cur)])
        and safe_id(barcode,[i["barcode"] for i in valid_asset(cur)])):
            result1 = add_ticket_db(cur, ticket_num, start_date, end_date,
                        room_num, building_id, tech_id, client_name, descr)
            result2 = add_ticket_asset_db(cur,ticket_num,barcode,status)
            if result1 and result2:
                return Response(status=200, mimetype='application/json')
            else:
                Response("{'error_message':'Insert failed'}",
                            status=500, mimetype='application/json')
        else:
            return Response(
            "{'field_name': 'barcode or status','error_message':'Status or barcode not regonized'}",
                            status=400, mimetype='application/json')
    conn.commit()
