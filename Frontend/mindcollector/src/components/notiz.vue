<template>
  <div>
    <v-card outlined>
      <v-card-title>
        {{ data.headline }}
      </v-card-title>
      <v-card-text>
        {{ data.text }}
      </v-card-text>

      <v-card-actions>
        <v-btn outlined rounded text> Edit </v-btn>
        <v-btn outlined rounded text> Delete </v-btn>
      </v-card-actions>
    </v-card>
  </div>
</template>

<script>
export default {
  props: ["data"],
};
</script>

<style scoped>
.v-card {
  display: flex;
  flex-direction: column;
  flex: 0;
  overflow: hidden auto;
  text-align: left;
}
.v-card__text {
  overflow: hidden auto;
  max-height: 150px;
  
}
</style>
