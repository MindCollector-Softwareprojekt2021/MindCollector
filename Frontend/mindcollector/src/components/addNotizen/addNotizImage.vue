<template>
  <v-container>
    <h1>Bild Notiz hinzufügen</h1>
    <v-form v-model="valid">
      <v-col>
        <v-text-field
          v-model="kat[1]"
          label="Kategorie"
          outlined
          disabled
        ></v-text-field>
        <v-text-field
          v-model="note.EINTRAG_TITEL"
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
          v-model="note.EINTRAG_BESCHREIBUNG"
          outlined
          label="Text"
          v-if="enabled"
          counter="2500"
          :rules="[required('Text'), maxLength('Text', 2500)]"
        ></v-textarea>
        <v-file-input
          v-model="note.EINTRAG_BILD"
          show-size
          accept="image/png, image/jpeg"
          prepend-icon="mdi-camera"
          :rules="[checkImage('Titel')]"
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
      kat: this.$store.getters.getSelectedKat,
      note: {
        EINTRAG_TITEL: "",
        EINTRAG_BESCHREIBUNG: "",
        EINTRAG_BILD: null,
      },
      file: null,
      enabled: false,

      ...validations,
    };
  },
  methods: {
    handleImage(fileObject) {
      this.createBase64Image(fileObject);
    },
    createBase64Image(fileObject) {
      var reader = new FileReader();
      reader.readAsDataURL(fileObject);
      reader.onload = () => {
        this.note.EINTRAG_BILD;
        //this.note.EINTRAG_BILD = reader.result;
      };
      reader.onerror = function(error) {
        console.log("Error: ", error);
      };
    },
    async createNote() {
      let formData = new FormData();

      formData.append("EINTRAG_BILD", this.note.EINTRAG_BILD);
      formData.append("USERNAME", this.$store.getters.getUsername);
      formData.append("KATEGORIE_ID", this.kat[0]);
      formData.append("EINTRAG_TITEL", this.note.EINTRAG_TITEL);
      formData.append("EINTRAG_BESCHREIBUNG", this.note.EINTRAG_BESCHREIBUNG);

      await this.$store.dispatch("createImageNote", formData);

      this.$router.push("/meine-notizen");
      this.$store.snackbar = true;
    },
  },
};
</script>

<style scoped>
@media screen and (max-width: 700px) {
}
</style>
