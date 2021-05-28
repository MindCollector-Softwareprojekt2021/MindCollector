import Vue from "vue";
import VueRouter from "vue-router";
import Home from "@/views/Home.vue";
import Register from "@/views/Register.vue";
import Login from "@/views/Login.vue";
import MeineNotizen from "../views/MeineNotizen.vue";
import addNotizAudio from "@/components/addNotizen/addNotizAudio.vue";
import addNotizImage from "@/components/addNotizen/addNotizImage.vue";
import addNotizText from "@/components/addNotizen/addNotizText.vue";
import FAQ from "@/views/FAQ.vue";
import AGB from "@/views/AGB.vue";
import AboutUs from "@/views/AboutUs.vue";
import Datenschutz from "@/views/datenschutz.vue";
import Impressum from "@/views/impressum.vue";
import store from "../store";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
    meta: { guest: true },
  },
  {
    path: "/register",
    name: "Register",
    component: Register,
    meta: { guest: true },
  },
  {
    path: "/login",
    name: "Login",
    component: Login,
    meta: { guest: true },
  },
  {
    path: "/meine-notizen",
    name: "Meine Notizen",
    component: MeineNotizen,
    meta: { requiresAuth: true },
  },
  {
    path: "/addNotizAudio",
    name: "addNotizAudio",
    component: addNotizAudio,
    meta: { requiresAuth: true },
  },
  {
    path: "/addNotizImage",
    name: "addNotizImage",
    component: addNotizImage,
    meta: { requiresAuth: true },
  },
  {
    path: "/addNotizText",
    name: "addNotizText",
    component: addNotizText,
    meta: { requiresAuth: true },
  },
  {
    path: "/FAQ",
    name: "FAQ",
    component: FAQ,
    meta: { guest: true },
  },
  {
    path: "/AGB",
    name: "AGB",
    component: AGB,
    meta: { guest: true },
  },
  {
    path: "/Ueber-uns",
    name: "Ueber-uns",
    component: AboutUs,
    meta: { guest: true },
  },
  {
    path: "/Impressum",
    name: "Impressum",
    component: Impressum,
    meta: { guest: true },
  },
  {
    path: "/Datenschutz",
    name: "Datenschutz",
    component: Datenschutz,
    meta: { guest: true },
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

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

export default router;
