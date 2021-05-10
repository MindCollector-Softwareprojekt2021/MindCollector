<template>
  <v-container>
    <v-col>
      <h1>Registrieren</h1>
    </v-col>
    <v-spacer />
    <v-col>
      <RegisterForm
        :submitForm="register"
        buttonText="Registrieren"
        :sf1="sf1"
        :sf2="sf2"
      />
    </v-col>
  </v-container>
</template>

<script>
import RegisterForm from "@/components/Auth/RegisterForm";

export default {
  components: {
    RegisterForm,
  },
  data() {
    return {
      sf1: [
        "Welchen Körperteil von Ihrem/Ihrer Freund/in finden Sie am hässlichsten?",
        "Auf welchen Ihrer Freunde könnten Sie am ehesten verzichten?",
        "Welchen Gegenstand haben Sie als Kind gestohlen?",
        "Wie lautet der Vorname der Person, die Sie zum ersten Mal geküsst haben?",
        "Wie lautet der Nachname des Lehrers, der Ihnen Ihre erste schlechte Note gegeben hat?",
      ],
      sf2: [
        "Welches Land möchten Sie auf keinen Fall bereisen?",
        "Wie lautete der Name Ihrer Grund-/Grundschule?",
        "In welcher Stadt wohnt Ihr nächstes Geschwisterkind?",
        "Zu welcher Tageszeit wurden Sie geboren? (hh:mm)",
        "Welche sexuelle Stellung mochten Sie noch nie?",
      ],
    };
  },
  methods: {
    async register(regInfo) {
      this.$router.push("/login");
    },
  },
};
</script>

<style scoped>
@media screen and (max-width: 500px) {
  
}
</style>
