<template>
  <v-app id="inspire">
    <v-app-bar color="white" flat>
      <v-tabs centered class="ml-n9" color="grey darken-1">
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
        { title: "Login", to: "/login", icon: "" },
      ],
    };
  },
};
</script>

<style>
#logo v-img {
  width: 125px;
}
</style>


 
