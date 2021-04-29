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
export default {
  components: {
    Footer,
  },
  data() {
    return {
      items: [
        { title: "Home", to: "/", icon: "mdi-domain" },
        { title: "Meine Notizen", to: "/sammlung", icon: "" },
        { title: "Login", to: "/login", icon: "" },
      ],
    };
  },
};
</script>

<style>

</style>


 
