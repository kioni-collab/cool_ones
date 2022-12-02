from psycopg2.extensions import cursor, AsIs
import datetime

#DOC: Returns valid building id for paramets checking
def valid_building_id(cur:cursor):
    cur.execute("select id from building")
    return list(cur)

#DOC: Returns valid dept id for paramets checking
def valid_dept_id(cur:cursor):
    cur.execute("select id from dept")
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
    group by a.barcode) as latest""", {"room_num":room_num,"building":AsIs(building)})
    return list(cur)

#DOC: retuns all rooms in a building and the building name
def search_building_db(cur: cursor, building: int):
    cur.execute(""" 
    select r.room_num, b.name as building
    from building b 
    inner join room r on r.building = b.id
    where b.id = %(building)s
    """, {"building":AsIs(building)})
    return list(cur)

#DOC: return all rooms assocaited with a department 
def search_dept_db(cur: cursor, dept: int):
    cur.execute(""" select r.room_num, b.name as building , d.name as dept
    from dept d
    inner join dept_room dr on dr.dept = d.id
    inner join room r on r.room_num = dr.room_num and r.building = dr.building
    inner join building b on r.building = b.id
    where d.id =%(dept)s
    """, {"dept":AsIs(dept)})
    return list(cur)

def add_ticket_db(cur:cursor,ticket_num:int,start_date:datetime,
end_date:datetime,room_num:str,building:int,tech_id:int,client_name:str,
descr:str):
    cur.execute("""
    insert into Ticket(ticket_num,start_date,end_date,room_num,building,technician_id,client_name,Description)
    values (%(ticket_num)s,%(start_date)s,%(end_date)s,%(room_num)s,%(building)s, %(tech_id)s,%(cliend_name)s, %(descr)s)
    """, {"ticket_num":ticket_num, "start_date":start_date, "end_date":end_date, "room_num":room_num,"building":building,"tech_id":tech_id,"descr":descr}
    )
    print(cur)

