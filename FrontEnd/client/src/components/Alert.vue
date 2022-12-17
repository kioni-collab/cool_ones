<template>
  <div >
     <ticket :tickets="filteredTickets" />
  </div>
</template>

<script>
import ticket from "@/components/Tickets.vue";
export default {
  props: {
    text: String
  },
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
  computed: {
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