<template>
  <v-tabs id="nav" centered dark prev-icon show-arrows center-active>
    <v-tab to="/"><v-icon dense>mdi-domain</v-icon> Startseite</v-tab>
    <v-tab to="/meine-notizen">
      <v-icon dense> mdi-message-text </v-icon> Meine Notizen
    </v-tab>
    <v-tab v-if="isLoggedIn" @click="logout"> Abmelden </v-tab>
    <v-tab v-else to="/login"> Anmelden </v-tab>
  </v-tabs>
</template>
<script>
export default {
  name: "NavBar",
  computed: {
    isLoggedIn: function() {
      return this.$store.getters.isAuthenticated;
    },
  },
  methods: {
    async logout() {
      await this.$store.dispatch("LogOut");

      this.$router.push("/login");
    },
  },
};
</script>
<style scoped></style>
