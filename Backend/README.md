# cool_ones BackEnd
## Developing in VS Code with the Remote Development Extension Pack

VS Code offers [a feature](https://code.visualstudio.com/docs/remote/containers) that lets you use a Docker container as your full-time development environment.

Install the [Remote Development Extension Pack](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack), and then when you open a project that has a `.devcontainer` folder/file, VS Code will prompt you to re-open the project inside a container. This can take several minutes to set up on the initial run, but should be quicker afterwards

This will make it so that all necessary system and project dependencies are installed all at once. Neat!

### Codebase Summary

This repo consists of a Postgres database, a pgAdmin web server, and a Python Flask web server application skeleton.

The Postgres database is populated with handmade data that will simulate IT&S ticket and asset data 

### Running the Flask Application

Inside the integrated terminal in VS Code, type
```
flask --debug run
```
This will run the server bound to TCP port 5000. You can then make HTTP calls to `http://localhost:5000`

### Connecting to the pgAdmin DBMS instance

you may need to delete  .postgress_data file first to see changes 

You can use the included dbms instance by opening `http://localhost:5050` in a browser window and entering the following credentials:

**username**: `admin@admin.com`

**password**: `root`

Lego database server credentials from the "Add New Server" dialog):

**Connection -> Host**: `db`
**Connection -> Username**: `postgres`
**Connection -> Password**: `postgres`

## ENDPOINTS

### /list_buildings
Returns a List of all the Buildings on campus
### Parameters
None

### /room 
Returns all the assets currently in a room 
#### parameters
<ul>
<li>room_num</li>
    <ul>
    <li>Description: Name of the room </li>
     <li>Type: Text </li>
    </ul>
<li>building_id</li>
    <ul>
    <li>Description: the building ID the room is located in </li>
    <li>Type: int </li>
    <li>Decode: {1:"LIBR", 2:"MRKN", 3:"ADMN"} </li>
    </ul>
<li>limit</li>
    <ul>
    <li>Description: how many results on each page </li>
    <li>Type: int </li>
    </ul>
</ul>

### /building
returns all the rooms in a building

#### parameters
<ul>
<li>building_id</li>
    <ul>
    <li>Description: the building ID the room is located in </li>
    <li>Type: int </li>
    <li>Decode: {1:"LIBR", 2:"MRKN", 3:"ADMN"} </li>
    </ul>
</ul>

### /dept
retusn all the rooms assocaited with a deptartment
<ul>
<li>dept_id</li>
    <ul>
    <li>Description: the dept ID the room is assocaited with </li>
    <li>Type: int </li>
    <li>Decode: {1:"AADV", 2:"CSCI", 3:"HUMA"} </li>
    </ul>
</ul>

### /assetspecs
returns the attributes od an asset
#### parameters 
<ul>
<li>barcode</li>
    <ul>
    <li>Description: the unique id for an asset </li>
    <li>Type: text </li>
    </ul>
</ul>

### /assetlocation
returns the room_num and building the asset is currently in 
#### parameters
<ul>
<li>barcode</li>
    <ul>
    <li>Description: the unique id for an asset </li>
    <li>Type: text </li>
    </ul>
</ul>

### /tickethistory
returns all the ticket history based of search paramets
<ul>
<li>ticket_num</li>
    <ul>
    <li>Description: the unique id for a ticket </li>
    <li>Type: text </li>
    </ul>
<li>end_year</li>
    <ul>
    <li>Description: the year the ticket was completed </li>
    <li>Type: int </li>
    </ul>
<li>end_month</li>
    <ul>
    <li>Description: the month the ticket was completed </li>
    <li>Type: int </li>
    </ul>
<li>end_day</li>
    <ul>
    <li>Description: the day the ticket was completed </li>
    <li>Type: int </li>
    </ul>
<li>status</li>
    <ul>
    <li>Description: the status of the computer after the ticket is complete </li>
    <li>Type: int </li>
    <li>Decode: {1:"redeploy", 2:"new asset", 3:"move", 4:"no change", 5:"Spare", 6:"scrapped", 7:"stolen/lost"} </li>
    </ul>
<li>room_num</li>
    <ul>
    <li>Description: Name of the room </li>
     <li>Type: Text </li>
    </ul>
<li>building_id</li>
    <ul>
    <li>Description: the building ID the room is located in </li>
    <li>Type: int </li>
    <li>Decode: {1:"LIBR", 2:"MRKN", 3:"ADMN"} </li>
    </ul>
<li>tech_first_name</li>
    <ul>
    <li>Description: first name of the technician that worked on the ticket</li>
    <li>Type: text </li>
    </ul>
<li>tech_last_name</li>
    <ul>
    <li>Description: last name of the technician that worked on the ticket</li>
    <li>Type: text </li>
    </ul>
<li>client_name</li>
    <ul>
    <li>Description: the name of the person who issed the ticket</li>
    <li>Type: text </li>
    </ul>
<li>barcode</li>
    <ul>
    <li>Description: the unique id for an asset </li>
    <li>Type: text </li>
    </ul>
</ul>

### /newticket 
addes a new ticket to database
#### parameters
<li>ticket_num</li>
    <ul>
    <li>Description: the unique id for a ticket </li>
    <li>Type: text </li>
    </ul>
<li>start_year</li>
    <ul>
    <li>Description: the year the ticket was initlaized </li>
    <li>Type: int </li>
    </ul>
<li>start_month</li>
    <ul>
    <li>Description: the month the ticket was initlaized </li>
    <li>Type: int </li>
    </ul>
<li>start_day</li>
    <ul>
    <li>Description: the day the ticket was initlaized </li>
    <li>Type: int </li>
    </ul>
<li>end_year</li>
    <ul>
    <li>Description: the year the ticket was completed </li>
    <li>Type: int </li>
    </ul>
<li>end_month</li>
    <ul>
    <li>Description: the month the ticket was completed </li>
    <li>Type: int </li>
    </ul>
<li>end_day</li>
    <ul>
    <li>Description: the day the ticket was completed </li>
    <li>Type: int </li>
    </ul>
<li>status</li>
    <ul>
    <li>Description: the status of the computer after the ticket is complete </li>
    <li>Type: int </li>
    <li>Decode: {1:"redeploy", 2:"new asset", 3:"move", 4:"no change", 5:"Spare", 6:"scrapped", 7:"stolen/lost"} </li>
    </ul>
<li>room_num</li>
    <ul>
    <li>Description: Name of the room </li>
     <li>Type: Text </li>
    </ul>
<li>building_id</li>
    <ul>
    <li>Description: the building ID the room is located in </li>
    <li>Type: int </li>
    <li>Decode: {1:"LIBR", 2:"MRKN", 3:"ADMN"} </li>
    </ul>
<li>client_name</li>
    <ul>
    <li>Description: the name of the person who issed the ticket</li>
    <li>Type: text </li>
    </ul>
<li>barcode</li>
    <ul>
    <li>Description: the unique id for an asset </li>
    <li>Type: text </li>
    </ul>
<li>tech_id</li>
    <ul>
    <li>Description: the unique id for the technician working on the ticket </li>
    <li>Type: int </li>
    </ul>
<li>descr</li>
    <ul>
    <li>Description: what happend during the ticket </li>
    <li>Type: text </li>
    </ul>
<li>add_asset</li>
    <ul>
    <li>Description: if during ths ticket we are adding a new asset</li>
    <li>Type: bool </li>
    </ul>
<li>model</li>
    <ul>
    <li> Dependentcy: only use if we are adding a asset </li>
    <li>Description: the model of the asset</li>
    <li>Type: text </li>
    </ul>
<li>purch_year</li>
    <ul>
    <li> Dependentcy: only use if we are adding a asset </li>
    <li>Description: the year the asset was purchased</li>
    <li>Type: int </li>
    </ul>
<li>purch_month</li>
    <ul>
    <li> Dependentcy: only use if we are adding a asset </li>
    <li>Description: the month the asset was purchased</li>
    <li>Type: int </li>
    </ul>
<li>purch_day</li>
    <ul>
    <li> Dependentcy: only use if we are adding a asset </li>
    <li>Description: the day the asset was purchased</li>
    <li>Type: int </li>
    </ul>
<li>type</li>
    <ul>
    <li> Dependentcy: only use if we are adding a asset </li>
    <li>Description: the type of the model aka if its a laptop, computer ect</li>
    <li>Type: int </li>
    <li>Decode: {1:"laptop", 2:"desktop", 3:"monitor", 4:"tablet", 5:"printer", 6:"scanner", 7:"Large Format Touchscreen"} </li>
    </ul>

</ul>

