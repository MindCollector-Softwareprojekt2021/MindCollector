<template>
  <v-card
    class="mx-auto"
    outlined
  >
    <v-list-item three-line >
      <v-list-item-content >
        <v-list-item-title  text-align:left> 
          {{ data.headline }}
        </v-list-item-title>
        <v-list-item-subtitle>{{ data.text }}</v-list-item-subtitle>
      </v-list-item-content>
    </v-list-item>

    <v-card-actions>
      <v-btn
        outlined
        rounded
        text
      >
        Edit
      </v-btn>
      <v-btn
        outlined
        rounded
        text
      >
        Delete
      </v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
export default({
  props:[
    'data'
  ]
})
</script>
