import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../components/Home.vue'
import Buildings from '../components/Buildings.vue'
import Admin from '../components/Admin.vue'
import TicketView from '../views/TicketView.vue'
import SearchView from '../views/SearchView.vue'
Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home
  },
  {
    path: '/buildings',
    name: 'buildings',
    component: Buildings
  },
  { 
    path: '/Buildings/:building', 
    component: Admin 
  },{
    path: '/tickets',
    name: 'tickets',
    component: TicketView
  },{
    path: '/search',
    name: 'search',
    component: SearchView
  },{
  path: '/Admin',
  name: 'admin',
  component: Admin
},

  
  
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
