<template>
  <v-container>
    <h1>Bild Notiz hinzufügen</h1>
    <v-form v-model="valid">
      <v-col>
        <v-text-field
          v-model="kat"
          label="Kategorie"
          outlined
          disabled
        ></v-text-field>
        <v-text-field
          label="Titel"
          counter="50"
          :rules="[
            required('Titel'),
            minLength('Titel', 3),
            maxLength('Titel', 50),
          ]"
        ></v-text-field>
        <v-checkbox
          v-model="enabled"
          label="Aktivieren, falls du KEINE Bild zu Text Analyse möchtest"
        ></v-checkbox>
        <v-textarea
          outlined
          label="Text"
          v-if="enabled"
          counter="500"
          :rules="[required('Text'), maxLength('Text', 500)]"
        ></v-textarea>
        <v-file-input
          v-model="file"
          show-size
          accept="image/png, image/jpeg, image/bmp"
          prepend-icon="mdi-camera"
          :rules="[checkImage('Titel')]"
          loading
        ></v-file-input>
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
      kat: "",
      enabled: false,
      file: null,
      ...validations,
    };
  },
  methods: {
    async createNote() {
      this.$router.push("/meine-notizen");
    },
  },
};
</script>

<style scoped>
@media screen and (max-width: 700px) {
}
</style>
