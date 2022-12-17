<template>
  <div class="container">
      <table class="table table-striped table-bordered">
          <thead>
              <tr>
                  <th>Ticket Number</th>
                  <th>Technician ID</th>
                  <th>Technican Name</th>
                  <th>Start Date</th>
                  <th>End Date</th>
                  <th>Client Name</th>
                  <th>Department</th>
                  <th>Building</th>
                  <th>Barcode</th>
                  <th>Type</th>
                  <th>Model</th>
                  <th>Description</th>
                  <th>Purchase Date</th>
                  <th>Status</th>
              </tr>
          </thead>
          <tbody>
              <tr v-for="tickets in tickets" :tickets="tickets">
                <td>{{tickets.ticket_num}}</td>
                <td>{{tickets.technician_id}}</td>
                <td>{{tickets.tech_first_name}} {{tickets.tech_last_name}}</td>
                <td>{{tickets.start_date}}</td>
                <td>{{tickets.end_date}}</td>
                <td>{{tickets.client_name}}</td>
                <td>{{tickets.dept}}</td>  
                <td>{{tickets.building}}</td> 
                <td>{{tickets.barcode}}</td> 
                <td>{{tickets.type}}</td> 
                <td>{{tickets.model}}</td> 
                <td>{{tickets.description}}</td> 
                <td>{{tickets.purch_date}}</td> 
                <td>{{tickets.status}}</td> 
                  
                  
              </tr>
          </tbody>
      </table>
  </div>    
</template>
  <script>
  export default {
    props: ["tickets"],
  };
  </script>