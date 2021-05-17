<template>
  <v-dialog v-model="dialog" persistent max-width="400">
    <template v-slot:activator="{ on, attrs }">
      <v-btn color="primary" dark v-bind="attrs" v-on="on">
        Löschen
      </v-btn>
    </template>
    <v-card>
      <v-card-title class="headline"> - {{ titel }} - löschen? </v-card-title>
      <v-card-text>{{ text }}</v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn color="orange darken-1" dark @click="dialog = false">
          {{ btn1 }}
        </v-btn>
        <v-btn color="green darken-1" dark @click="deleteNote()">
          {{ btn2 }}
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
export default {
  data() {
    return {
      dialog: false,
    };
  },
  props: ["titel", "text", "btn1", "function"],
};
</script>
