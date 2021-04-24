<template>
  <v-footer
    absolute
    color="primary lighten-1"
    padless
  >
    <v-row
      justify="center"
      no-gutters
    >
      <v-btn
        v-for="item in items"
        :key="item"
        :to="item.to"
        color="white"
        text
        rounded
        class="my-2"
      >
        {{ item.title }}
      </v-btn>
      <v-col
        class="primary lighten-2 py-4 text-center white--text"
        cols="12"
      >
        {{ new Date().getFullYear() }} — <strong>MindCollector</strong>
      </v-col>
    </v-row>
  </v-footer>
  
</template>

<script>
  export default {
    data: () => ({
      items: [
        {title: "Datenschutz", to: '/datenschutz'},
        {title: 'Impressum', to: '/impressum'}
      ],
      
    }),
  }
</script>