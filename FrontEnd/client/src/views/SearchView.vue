
<template>
    <div class="table">
        <div class ="search">
            <subtitle-1 class="mb4">Search Tickets by Ticket number: </subtitle-1>
            <input type="text" v-model='search' placeholder="Search"/>
    </div>
      <br/>
      
      <p v-if="state == 'error'" class="orange">{{ error }}</p>
      <div v-else-if="state == 'ready'">
        <ticket :tickets="filteredTickets" />
      </div>
      <p v-else-if="state == 'loading'">Loading tickets...</p>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  import ticket from "@/components/Tickets.vue";
  
  export default {
    name: "app",
    components: {
      ticket
    },
    data() {
      return {
        tickets: [],
        error: "",
        state: "loading",
        search:""
      };
    },
    created() {
      this.loadTickets();
    },
    methods: {
      async loadTickets() {
        try {
          const tickets = await fetch("http://localhost:5000/tickethistory");
          this.tickets = await tickets.json();
          this.state = "ready";
        } catch (err) {
          this.error = err;
          this.state = "error";
        }
      }
    },
    computed:{
        filteredTickets: function(){
            return this.tickets.filter((tickets) =>{
                return tickets.ticket_num.match(this.search)
           
            })
        }
    }
  };
  </script>
<style>
subtitle-1{
  padding-top: 1%;
  display: inline-block;
vertical-align: middle;
padding: 1rem 1rem;

}
input{
    width:fit-content;
}

.search{
    display: flexbox;
    vertical-align: middle;
    }
</style>