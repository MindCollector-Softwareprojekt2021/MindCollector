<template>
  <v-tabs centered show-arrows center-active>
    <v-tab> Text hinzufügen </v-tab>
    <v-tab> Audio hinzufügen </v-tab>
    <v-tab> Bild hinzufügen </v-tab>

    <v-tab-item> <addNotizText /> </v-tab-item>
    <v-tab-item> <addNotizAudio /></v-tab-item>
    <v-tab-item> <addNotizImage></addNotizImage> </v-tab-item>
  </v-tabs>
</template>

<script>
import addNotizText from "@/components/addNotizen/addNotizText";
import addNotizImage from "@/components/addNotizen/addNotizImage";
import addNotizAudio from "@/components/addNotizen/addNotizAudio";
export default {
  components: {
    addNotizText,
    addNotizImage,
    addNotizAudio,
  },
};
</script>

<style scoped>
.item {
  background-color: rgb(209, 143, 56);
}
</style>
