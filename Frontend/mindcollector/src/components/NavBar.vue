<template>
  <v-tabs id="nav" centered mobile-breakpoint dark>
    <v-tab to="/"><v-icon dense>mdi-domain</v-icon> Home</v-tab>
    <v-tab to="/meine-notizen"><v-icon dense> mdi-message-text </v-icon>Meine Notizen</v-tab>
    <v-tab v-if="isLoggedIn" >Logout</v-tab>
    <v-tab v-else to="/login">Login</v-tab>
  </v-tabs>
</template>
<script>
export default {
  name: "NavBar",
  data(){
    return{
      isLoggedIn: false
    }
  }
};
</script>
<style scoped>
#nav {
  text-align: center;
  font-weight: bold;
  color: rgb(49, 49, 49);
}
#nav a {
  font-weight: bold;
  color: rgb(49, 49, 49);
}
</style>