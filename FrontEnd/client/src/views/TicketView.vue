<template>
    <div class="mw6 center pa3 sans-serif">
      <h1 class="mb4">tickets</h1>
  
      <p v-if="state == 'error'" class="orange">{{ error }}</p>
      <div v-else-if="state == 'ready'">
        <ticket v-for="tickets in tickets" :tickets="tickets" />
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
        state: "loading"
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
    }
  };
  </script>