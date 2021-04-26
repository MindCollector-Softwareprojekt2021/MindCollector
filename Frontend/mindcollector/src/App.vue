<template>
  <v-app>
    <v-app-bar color="blue" app>
      <v-tabs centered class="ml-n9" color="white">
        <v-tab v-for="item in items" :key="item" :to="item.to">
          <v-icon>{{ item.icon }}</v-icon
          >{{ item.title }}
        </v-tab>
      </v-tabs>
    </v-app-bar>

    <v-main class="grey lighten-3">
      <router-view></router-view>
    </v-main>

    <Footer />
  </v-app>
</template>

<script>
import Footer from "./components/footer.vue";
import logo from "./assets/mind.png";
export default {
  components: {
    Footer,
  },
  data() {
    return {
      logo: logo,
      items: [
        { title: "Home", to: "/", icon: "mdi-domain" },
        { title: "About", to: "/about", icon: "mdi-dialpad" },
        { title: "Meine Sammlung", to: "/sammlung", icon: "" },
        { title: "Login", to: "/login", icon: "" },
        { title: "SignUp", to: "/sign-up", icon: "" },
      ],
    };
  },
};
</script>

<style>
</style>


 
