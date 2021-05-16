<template>
  <v-container>
    <v-col>
      <h1>Anmelden</h1>
    </v-col>
    <v-spacer />
    <v-col>
      <LoginForm buttonText="Anmelden" />
    </v-col>
    <v-spacer />
    <v-col>
      <h4>Noch nicht Registriert?</h4>
      <v-btn to="/register" color="success">Registrieren</v-btn>
    </v-col>
  </v-container>
</template>

<script>
import LoginForm from "@/components/Auth/LoginForm";

export default {
  components: {
    LoginForm,
  },
  data() {
    return {};
  },
};
</script>

<style scoped>
@media screen and (max-width: 1000px) {
}
</style>
