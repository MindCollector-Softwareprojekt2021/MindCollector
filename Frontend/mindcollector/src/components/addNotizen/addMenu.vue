<template>
  <v-menu offset-y rounded="b-xl">
    <template v-slot:activator="{ attrs, on }">
      <v-btn class="green" v-bind="attrs" v-on="on">
        <v-icon>mdi-plus</v-icon>
      </v-btn>
    </template>

    <v-list>
      <v-list-item
        @click="
          addNotiz([notiz.KATEGORIE_ID, notiz.KATEGORIE_TITEL], '/addNotizText')
        "
      >
        <v-list-item-title>
          Text Notiz hinzufügen
        </v-list-item-title>
      </v-list-item>
      <v-list-item
        @click="
          addNotiz(
            [notiz.KATEGORIE_ID, notiz.KATEGORIE_TITEL],
            '/addNotizImage'
          )
        "
      >
        <v-list-item-title>
          Bild Notiz hinzufügen
        </v-list-item-title>
      </v-list-item>
      <v-list-item
        @click="
          addNotiz(
            [notiz.KATEGORIE_ID, notiz.KATEGORIE_TITEL],
            '/addNotizAudio'
          )
        "
      >
        <v-list-item-title>
          Audio Notiz hinzufügen
        </v-list-item-title>
      </v-list-item>
    </v-list>
  </v-menu>
</template>

<script>
export default {
  data() {
    return {
      deleteKatDialog: false,
    };
  },
  props: ["notiz"],
  methods: {
    async addNotiz(k, push) {
      await this.$store.commit("setSelectedKat", k);
      this.$router.push(push);
    },
  },
};
</script>
