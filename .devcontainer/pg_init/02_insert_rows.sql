copy Asset_Type(id, name)
from '/docker-entrypoint-initdb.d/seed_data/Asset_Type.csv'
delimiter ','
csv header;

copy Asset(barcode,model,purch_date,type)
from '/docker-entrypoint-initdb.d/seed_data/Asset.csv'
delimiter ','
csv header;

copy Asset_Status(id, name,Description)
from '/docker-entrypoint-initdb.d/seed_data/Asset_Status.csv'
delimiter ','
csv header;

copy Technician(technician_id,start_date,end_date,active,first_name,last_name,Manager)
from '/docker-entrypoint-initdb.d/seed_data/Technician.csv'
delimiter ','
csv header;

copy Building(id, name,Description)
from '/docker-entrypoint-initdb.d/seed_data/Building.csv'
delimiter ','
csv header;

copy Dept(id,name,Description)
from '/docker-entrypoint-initdb.d/seed_data/Dept.csv'
delimiter ','
csv header;

copy Room(room_num,building,floor)
from '/docker-entrypoint-initdb.d/seed_data/Room.csv'
delimiter ','
csv header;

copy Dept_Room(room_num,building,Dept)
from '/docker-entrypoint-initdb.d/seed_data/Dept_Room.csv'
delimiter ','
csv header;

copy   Ticket(ticket_num,start_date,end_date,room_num,building,technician_id,client_name,Description)
from '/docker-entrypoint-initdb.d/seed_data/Ticket.csv'
delimiter ','
csv header;

copy Ticket_Asset(ticket_num,barcode,status)
from '/docker-entrypoint-initdb.d/seed_data/Ticket_Asset.csv'
delimiter ','
csv header;