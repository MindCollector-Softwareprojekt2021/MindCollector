<template>
  <v-tabs
    centered
    mobile-breakpoint
    dark
  >
    <v-tab> Text hinzufügen </v-tab>
    <v-tab> Audio hinzufügen </v-tab>
    <v-tab> Bild hinzufügen </v-tab>
    
    <v-tab-item > <addNotizText></addNotizText> </v-tab-item>
    <v-tab-item> <RecordAudio/></v-tab-item>
    <v-tab-item > <addNotizImage></addNotizImage> </v-tab-item>
    
  </v-tabs>
</template>

<script>
import addNotizText from "../components/addNotizText.vue"
import addNotizImage from "../components/addNotizImage.vue"
import RecordAudio from "../components/Audio/RecordAudio.vue"
export default {
  components: {
    addNotizText,
    addNotizImage,
    RecordAudio
    },
};
</script>

<style scoped>
.item{
  background-color: rgb(209, 143, 56);
}
</style>