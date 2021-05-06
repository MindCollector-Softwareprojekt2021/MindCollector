import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Register from "../views/Register.vue"
import Login from "../views/Login.vue"
import MeineNotizen from "../views/MeineNotizen.vue"
import addNotiz from "../views/addNotiz.vue"


Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/register',
    name: "Register",
    component: Register
  },
  {
    path: '/login',
    name: "Login",
    component: Login
  },
  {
    path: "/meine-notizen",
    name: "Meine Notizen",
    component: MeineNotizen
  },
  {
    path: "/add",
    name: "add",
    component: addNotiz
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})



export default router
