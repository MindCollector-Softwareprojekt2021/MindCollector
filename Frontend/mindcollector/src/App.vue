<template>
  <v-app id="inspire">
    <v-app-bar
      app
      color="white"
      flat
    >
      <img :src="image" style="width:5%;" alt="Mind">
        
      

      <v-tabs
        centered
        class="ml-n9"
        color="grey darken-1"
      >
        <v-tab
          v-for="item in items"
          :key="item"
          :to="item.to"
        >
          <v-icon>{{ item.icon }}</v-icon>{{ item.title }}
        </v-tab>
      </v-tabs>

      <div class="text-center">
        <v-btn
          rounded
          color="primary"
          dark
        >
          Login
        </v-btn>
      </div>
    </v-app-bar>

    <v-main class="grey lighten-3">
      <router-view></router-view>
      
    </v-main>
    <Footer/>
  </v-app>
</template>

<script>
  import Footer from './components/footer.vue';
  export default {
    components: {
    Footer
    },

    data: () => ({
      image: '/assets/gehirn.png',
      items: [
        {title: "Home", to: '/', icon:'mdi-domain'},
        {title: 'About', to: '/about', icon:'mdi-dialpad'}
      ],
      
    }),
  }
</script>

<style>

.logo{
  width: 30%;
}

</style>


 
