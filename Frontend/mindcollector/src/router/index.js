import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Register from "../views/Register.vue"
import Login from "../views/Login.vue"
import MeineNotizen from "../views/MeineNotizen.vue"
import store from "../store";
import addNotiz from "../views/addNotiz.vue"


Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
    meta: { guest: true },
  },
  {
    path: '/register',
    name: "Register",
    component: Register,
    meta: { guest: true },
  },
  {
    path: '/login',
    name: "Login",
    component: Login,
    meta: { guest: true },
  },
  {
    path: "/meine-notizen",
    name: "Meine Notizen",
    component: MeineNotizen,
    meta: { guest: true },
    //meta: { requiresAuth: true },
  },
  {
    path: "/add",
    name: "add",
    component: addNotiz,
    meta: { guest: true },
    //meta: { requiresAuth: true },
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

router.beforeEach((to, from, next) => {
  if (to.matched.some((record) => record.meta.requiresAuth)) {
    if (store.getters.isAuthenticated) {
      next();
      return;
    }
    next("/login");
  } else {
    next();
  }
});

export default router
