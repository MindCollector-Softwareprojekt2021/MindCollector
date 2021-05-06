<template>
  <div class="field">
    <v-form ref="form" lazy-validation>
      <v-text-field
        :value="kat"
        label="Kategorie"
        outlined
        disabled
      ></v-text-field>
      <v-text-field label="Titel" required v-model="note.title"></v-text-field>

      <v-textarea outlined name="input-7-4" label="Text" v-model="note.text"></v-textarea>

      <v-btn color="success" @click="createNote"> Save </v-btn>
    </v-form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      kat: '',
      note:{}
    };
  },
  methods:{
    createNote(){
      this.$store.dispatch('createNote', this.note);
      this.$router.push("/meine-notizen");
    }
  }
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