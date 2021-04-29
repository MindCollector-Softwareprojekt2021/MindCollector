<template>
  <v-app class="app">
    <v-app-bar color="blue" app >
      
      <v-tabs centered class="ml-n9" color="white">
        
        <v-tab v-for="item in items" :key="item" :to="item.to">
          <v-icon>{{ item.icon }}</v-icon
          >{{ item.title }}
        </v-tab>
      </v-tabs>
    </v-app-bar>

    <v-main class="main" :style="cssProps" >
        <router-view></router-view>
    </v-main>
    <Footer />
  </v-app>
</template>

<script>
import Footer from "./components/footer.vue";
import NavBar from '@/components/NavBar.vue'
export default {
  components: {
    Footer, NavBar
  },
  data() {
    return {
      items: [
        { title: "Home", to: "/", icon: "mdi-domain" },
        { title: "Meine Notizen", to: "/sammlung", icon: "" },
        { title: "Login", to: "/login", icon: "" },
      ],
      cssProps: {
        //backgroundImage: `url(${require("@/assets/gb.jpeg")})`,
        backgroundColor: "black",
        backgroundPosition:"center center",
        backgroundSize: "cover",
        minHeight: "100%",
        backgroundAttachment: "fixed",
        backgroundRepeat: "no-repeat",
      },
    };
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  justify-content: center;
  justify-items: center;
  align-content: center;
  align-items: center;
}
.main{
}
.container{
  margin: 0;
  padding: 0;
  background-color: red;
  display: flex;
  flex-direction: column;
  flex-wrap: wrap;

  width: 100%;
 
}
</style>


 
