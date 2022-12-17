<template>
  <div >
     <ticket :tickets="filteredTickets" />
  </div>
</template>

<script>
import ticket from "@/components/Tickets.vue";
export default {
  props: {
    type: {
      type: String,
      value: 'error' | 'info' | 'success' | 'warning'
    },
    text: String
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
  computed: {
    color () {
      switch (this.type) {
        case 'error':
          return 'red'
        case 'success':
          return 'teal'
        case 'warning':
          return 'orange'
        case 'info':
        default:
          return 'gray'
      }
    },
    filteredTickets: function(){
            return this.tickets.filter((tickets) =>{
                return tickets.room_num.match(text)
           
            })
        }

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