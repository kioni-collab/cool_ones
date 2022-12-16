<template>
    <div class="pa2 mb3 striped--near-white">
      <header class="b mb2">{{ tickets.ticket_num }}</header>
    </div>
  </template>
  
  <script>
  export default {
    props: ["tickets"],
  };
  </script>
  