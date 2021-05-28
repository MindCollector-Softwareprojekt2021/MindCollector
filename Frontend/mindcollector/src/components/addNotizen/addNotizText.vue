<template>
  <v-container>
    <h1>Text Notiz hinzufügen</h1>
    <v-form v-model="valid">
      <v-col>
        <v-text-field :value="kat[1]" outlined disabled />
        <v-text-field
          v-model="note.EINTRAG_TITEL"
          label="Titel"
          counter="50"
          :rules="[
            required('Titel'),
            minLength('Titel', 3),
            maxLength('Titel', 50),
          ]"
        />
        <v-textarea
          v-model="note.EINTRAG_BESCHREIBUNG"
          outlined
          counter="500"
          label="Text"
          :rules="[required('Text'), maxLength('Text', 255)]"
        />
      </v-col>
      <v-col>
        <v-btn :disabled="!valid" @click="createNote" block color="success">
          Save
        </v-btn>
      </v-col>
      <v-col>
        <v-btn block color="primary" to="/meine-notizen"> Back </v-btn>
      </v-col>
    </v-form>
  </v-container>
</template>

<script>
import validations from "@/utils/validations";

export default {
  data() {
    return {
      valid: false,
      kat: this.$store.getters.getSelectedKat,
      note: {
        EINTRAG_TITEL: "",
        EINTRAG_BESCHREIBUNG: "",
        EINTRAG_BILD: "",
      },
      ...validations,
    };
  },
  computed: {},
  methods: {
    async createNote() {
      let neueNotiz = {
        USERNAME: this.$store.getters.getUsername,
        KATEGORIE_ID: this.kat[0],
        EINTRAG: this.note,
      };
      await this.$store.dispatch("createNote", neueNotiz);
      this.$router.push("/meine-notizen");
    },
  },
};
</script>

<style scoped>
.field {
  padding: 100px 300px;
}

@media screen and (max-width: 700px) {
  .field {
    padding: 30px;
  }
}
</style>
