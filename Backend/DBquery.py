from psycopg2.extensions import cursor, AsIs
import datetime

# DOC: Returns valid building id for paramets checking


def valid_building_id(cur: cursor):
    cur.execute("select id from building")
    return list(cur)

# DOC: Returns valid dept id for paramets checking


def valid_dept_id(cur: cursor):
    cur.execute("select id from dept")
    return list(cur)

def valid_status_id(cur: cursor):
    cur.execute("select id from asset_status")
    return list(cur)

def valid_asset(cur:cursor):
    cur.execute("select barcode from asset")
    return list(cur)

# DOC: Finds all the assets in a room
# works by finding the latest tickets associeted
# with a asset and filters by room and building


def search_room_db(cur: cursor, room_num: str, building: int):
    cur.execute(""" select barcode,model,purch_date,type from
    (select a.*, max(t.end_date)
    from asset a
    inner join ticket_asset ta on ta.barcode = a.barcode
    inner join ticket t on t.ticket_num = ta.ticket_num
    inner join room r on t.room_num = r.room_num and t.building = r.building
    inner join building b on b.id = r.building
    where r.room_num = %(room_num)s and  r.building  = %(building)s 
    group by a.barcode) as latest""", {"room_num": room_num, "building": AsIs(building)})
    return list(cur)

# DOC: retuns all rooms in a building and the building name


def search_building_db(cur: cursor, building: int):
    cur.execute(""" 
    select r.room_num, b.name as building
    from building b 
    inner join room r on r.building = b.id
    where b.id = %(building)s
    """, {"building": AsIs(building)})
    return list(cur)

# DOC: return all rooms assocaited with a department


def search_dept_db(cur: cursor, dept: int):
    cur.execute(""" select r.room_num, b.name as building , d.name as dept
    from dept d
    inner join dept_room dr on dr.dept = d.id
    inner join room r on r.room_num = dr.room_num and r.building = dr.building
    inner join building b on r.building = b.id
    where d.id =%(dept)s
    """, {"dept": AsIs(dept)})
    return list(cur)


def add_ticket_db(cur: cursor, ticket_num: int, start_date: datetime, end_date: datetime,
                  room_num: str, building: int, tech_id: int, client_name: str,
                  descr: str):
    cur.execute("""
    insert into Ticket(ticket_num,start_date,end_date,room_num,building,technician_id,client_name,Description)
    values (%(ticket_num)s,%(start_date)s,%(end_date)s,%(room_num)s,%(building)s, %(tech_id)s,%(client_name)s, %(descr)s) 
    ON CONFLICT DO NOTHING""", {"ticket_num": ticket_num, "start_date": start_date.strftime("%m/%d/%Y"), "end_date": end_date.strftime("%m/%d/%Y"), "room_num": room_num, "building": AsIs(building), "tech_id": AsIs(tech_id),"client_name":client_name, "descr": descr}
    )
    return bool(cur)

#todo need to figure out how to add ticket only if status is valid so all tickets have a status
def add_ticket_asset_db(cur:cursor,ticket_num:int,barcode:int,status:int):
    cur.execute("""
    insert into ticket_Asset (ticket_num,barcode,status)
    values (%(ticket_num)s,%(barcode)s,%(status)s)
    ON CONFLICT DO NOTHING
    """, {"ticket_num":ticket_num,"barcode":barcode,"status":status})
    return bool(cur)

def add_asset_db(cur:cursor,barcode:int,model:str,purch_date:datetime,type:int):
    cur.execute("""
    insert into asset (barcode,model,purch_date,type)
    values (%(barcode)s,%(model)s,%(purch_date)s,%(type)s)
    ON CONFLICT DO NOTHING
    """, {"barcode":barcode, "model":model,"purch_date":purch_date, "type":type})
    return bool(cur)

def search_asset_location_db(cur: cursor, barcode: int):
    cur.execute("""
   select room_num, building,floor from
        (select r.room_num as room_num, r.floor as floor,b.name as building, t.ticket_num, t.end_date
        from asset a
        inner join ticket_asset ta on ta.barcode = a.barcode
        inner join ticket t on t.ticket_num = ta.ticket_num
        inner join room r on t.room_num = r.room_num and t.building = r.building
        inner join building b on b.id = r.building
		where a.barcode = %(barcode)s
        group by r.room_num, r.floor, b.name,t.ticket_num
		order by t.end_date desc
		limit 1) as latest
    """, {"barcode": barcode})
    return list(cur)

def search_ticket_history_db(cur:cursor,ticket_num,end_date:datetime,status,room_num,building_id,tech_first_name,tech_last_name,client_name,barcode ):
    status_where = ""
    end_where = ""
    building_where = ""
    barcode_where = ""
    if isinstance(status, int):
        status_where = f"AND ts.status = {status}"
    if isinstance(end_date, datetime.datetime):
        end_date_formated = end_date.strftime("%m/%d/%Y") 
        end_where = f" AND t.end_date = {end_date_formated}"
    if isinstance(building_id, int):
        building_where = f"AND t.building = {building_id}"
    if isinstance(barcode, int):
        barcode_where = f"AND a.barcode = {barcode}"
    

    cur.execute("""
    select t.*,s.name as Status, a.*,ty.name as Type, b.name as Building ,d.name as Dept, te.first_name, te.last_name
    from ticket t
    inner join ticket_asset ts on t.ticket_num = ts.ticket_num
    inner join asset_status s on s.id = ts.status
    inner join asset a on a.barcode = ts.barcode
    inner join asset_type ty on ty.id = a.type
    inner join Technician te on te.technician_id  = t.technician_id
    inner join room r on r.room_num = t.room_num
    inner join building b on b.id = r.building
    inner join Dept_Room dr on dr.room_num = r.room_num and dr.building  = r.building
    inner join dept d on d.id = dr.dept
    where t.ticket_num Like %(ticket_num)s AND lower(t.room_num) like lower(%(room_num)s) AND lower(t.client_name) like lower(%(client_name)s) AND lower(te.first_name) like lower(%(tech_first_name)s) And lower(te.last_name) like lower(%(tech_last_name)s)
    %(status_where)s %(end_where)s %(building_where)s %(barcode_where)s 
    """, {"ticket_num":"%"+ticket_num+"%", "room_num":"%"+room_num + "%", "client_name": "%"+client_name+"%", "status_where":AsIs(status_where),
    "tech_first_name": "%"+tech_first_name+"%", "tech_last_name":"%"+tech_last_name+"%", 
    "end_where": AsIs(end_where),"building_where":AsIs(building_where), "barcode_where":AsIs(barcode_where) })
    return list(cur)