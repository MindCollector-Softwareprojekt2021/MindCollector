<template>
  <v-container>
    <v-col>
      <h1>Registrieren</h1>
    </v-col>
    <v-spacer />
    <v-col>
      <RegisterForm buttonText="Registrieren" :sf1="sf1" :sf2="sf2" />
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
        "In welcher Stadt bzw. an welchem Ort wurden Sie geboren?",
        "Geben Sie Marke und Modell Ihres ersten Autos an.",
        "Welchen Gegenstand haben Sie als Kind gestohlen?",
        "In welcher Stadt bzw. welchem Ort haben sich Ihre Eltern kennengelernt?",
        "Wie lautet der Nachname des Lehrers, der Ihnen Ihre erste schlechte Note gegeben hat?",
      ],
      sf2: [
        "Welches Land möchten Sie auf keinen Fall bereisen?",
        "Wie lautete der Name Ihrer Grund-/Grundschule?",
        "In welcher Stadt wohnt Ihr nächstes Geschwisterkind?",
        "Zu welcher Tageszeit wurden Sie geboren? (hh:mm)",
        "Welches war Ihr erstes Konzert, das Sie besucht haben?",
      ],
    };
  },
};
</script>

<style scoped>
@media screen and (max-width: 500px) {
}
</style>
