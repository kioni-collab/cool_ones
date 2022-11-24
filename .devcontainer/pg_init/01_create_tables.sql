create table Asset_Type (
    id int primary key,
    name text unique

);

create table Asset(
    barcode int primary key,
    model text,
    purch_date date,
    type int references Asset_Type(id)
);

create table Asset_Status(
    id int primary key,
    name text unique,
    Description text

);
create table Technician(
    technician_id int primary key,
    start_date date,
    end_date date,
    active boolean,
    first_name text,
    last_name text,
    Manager int null references Technician(technician_id)
);

create table Account(
    username text primary key,
    password text,
    technician_id int unique references Technician(technician_id)
);
create table Building(
    id int primary key,
    name text,
    Description text
);

create table Dept(
    id int primary key,
    name text,
    Description text
);
create table Room(
    room_num text,
    building int references Building(id),
    Primary key(room_num,building)
);
create table Dept_Room(
    room_num text,
	building int,
    Dept int references Dept(id),
	Foreign Key (room_num,building) REFERENCES Room(room_num,building)
);
create table Ticket(
    ticket_num text primary key,
    start_date date,
    end_date date,
    room_num text,
	building int,
    technician_id int references Technician(technician_id),
    client_name text,
    Description text,
	Foreign Key (room_num,building) REFERENCES Room(room_num,building)
);
create table Ticket_Asset(
    ticket_num text references Ticket(ticket_num),
    barcode int references Asset(barcode),
    status int references Asset_Status(id),
    primary key (ticket_num,barcode)
);