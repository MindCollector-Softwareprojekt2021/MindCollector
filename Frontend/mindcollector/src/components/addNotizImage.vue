<template>
  <div class="field">
    <v-form ref="form" lazy-validation>
      <v-text-field
        :value="kat"
        label="Kategorie"
        outlined
        disabled
      ></v-text-field>
      <v-text-field label="Titel" required></v-text-field>
      <v-checkbox
        v-model="enabled"
        label="Aktivieren, falls du KEINE Bild zu Text Analyse möchtest"
      ></v-checkbox>
      <v-textarea
        outlined
        name="input-7-4"
        label="Text"
        v-if="enabled"
      ></v-textarea>
      <v-file-input show-size></v-file-input>

      <v-btn color="success"> Save </v-btn>
    </v-form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      kat: "",
      enabled: false,
    };
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