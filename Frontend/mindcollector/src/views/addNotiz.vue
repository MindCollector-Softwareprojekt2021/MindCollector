<template>
  <v-tabs
    centered
    mobile-breakpoint
    dark
  >
    <v-tab> Text hinzufügen </v-tab>
    <v-tab> Audio hinzufügen </v-tab>
    <v-tab> Bild hinzufügen </v-tab>

    <v-tab-item> <addNotizText></addNotizText> </v-tab-item>
    <v-tab-item> </v-tab-item>
    <v-tab-item > <addNotizImage></addNotizImage> </v-tab-item>
  </v-tabs>
</template>

<script>
import addNotizText from "../components/addNotizText.vue"
import addNotizImage from "../components/addNotizImage.vue"
export default {
  components: {
    addNotizText,
    addNotizImage,
  },
  data(){
    return {
      kat:'',
    }
  },
  mounted: function(){
    this.kat = this.$store.getters.SelectKat;
  },

};
</script>