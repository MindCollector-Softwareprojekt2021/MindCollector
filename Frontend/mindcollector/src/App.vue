<template>
  <v-app>
    <v-app-bar color="blue" app dark>
      <NavBar />
    </v-app-bar>

    <v-main app>
      <v-alert type="error" dense dismissible>
        "Hallo Besucher! Diese Seite/App ist noch im Aufbau. Es handelt sich um
        ein Softwareprojet der Fachhochschule Bielefeld Campus Minden SoSe21.
        Bei Rückfragen an marko.lemac@fh-bielefeld.de wenden."
      </v-alert>
      <router-view></router-view>
    </v-main>

    <v-footer color="primary lighten-1" padless app>
      <v-row justify="center" no-gutters>
        <v-col class="primary lighten-2 py-1 text-center white--text" cols="12">
          {{ new Date().getFullYear() }} — <strong>MindCollector</strong>
        </v-col>
      </v-row>
    </v-footer>
  </v-app>
</template>

<script>
import Footer from "@/components/footer.vue";
import NavBar from "@/components/NavBar.vue";
export default {
  components: {
    Footer,
    NavBar,
  },
  methods: {
    async logout() {
      this.$router.push("/login");
    },
  },
};
</script>

<style scoped>
* {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
}
#footer {
  color: white;
  text-align: center;
}
</style>
