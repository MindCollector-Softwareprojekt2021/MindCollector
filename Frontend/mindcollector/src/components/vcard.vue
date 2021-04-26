<template>
  <v-card outlined class="flexcard">
    <v-list-item three-line>
      <v-list-item-content>
        <v-list-item-title text-align:left>
          {{ data.headline }}
        </v-list-item-title>
        {{ data.text }}
      </v-list-item-content>
    </v-list-item>

    <v-card-actions>
      <v-btn outlined rounded text> Edit </v-btn>
      <v-btn outlined rounded text> Delete </v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
export default {
  props: ["data"],
};
</script>

<style>
.flexcard {
  display: flex;
  flex-direction: column;
}

.flexcard .v-toolbar {
  flex: 0;
}
</style>
