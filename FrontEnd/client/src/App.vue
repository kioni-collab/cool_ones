<template>
  <div id="app">
    <div class ="container">
    <img src="@/assets/plu_gold.png">
    <h1>I&TS</h1>
  </div>
    <nav>
      <router-link to="/" tag="button" class="mr-3" >Home</router-link> 
      <router-link to="/Buildings" tag="button" class="mr-3" >Buildings</router-link> 
      <router-link to="/Search" tag="button" class="mr-3">Search</router-link> 
      <router-link to="/Tickets" tag="button" class="mr-3" >Tickets</router-link> 
    </nav>
    <router-view/>
  </div>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  
}
.container {
  display: flex;
  align-items: center;
  justify-content: center
}
button{
  
  padding: 10px;
  background-color: black;
  color:white;

}
h1 {

  padding-left: 30px;
  padding-top: 90px;
}
img {
  width: 20%;
  align-items: center;
  padding-top: 30px;
}
nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
