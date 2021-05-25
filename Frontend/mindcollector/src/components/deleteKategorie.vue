<template>
  <v-dialog v-model="deleteKatDialog" persistent max-width="290">
    <template v-slot:activator="{ on, attrs }">
      <v-btn color="red" max-width="100" v-bind="attrs" v-on="on">
        <v-icon>mdi-minus</v-icon>
      </v-btn>
    </template>
    <v-card>
      <v-card-title class="headline">
        Soll die Kategorie gelöscht werden?
      </v-card-title>

      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn color="green darken-1" text @click="deleteKatDialog = false">
          Abbrechen
        </v-btn>
        <v-btn color="green darken-1" text @click="deleteKategorie()">
          Löschen
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
export default {
  data() {
    return {
      deleteKatDialog: false,
    };
  },
  props: ["notiz"],
  computed: {
    img() {
      return this.notiz.EINTRAG.length == 0;
    },
  },
  methods: {
    async deleteKategorie() {
      try {
        await this.$store.dispatch("deleteKategorie", this.notiz.KATEGORIE_ID);
        this.deleteKatDialog = false;
      } catch (error) {
        console.log(error);
      }
    },
  },
};
</script>
