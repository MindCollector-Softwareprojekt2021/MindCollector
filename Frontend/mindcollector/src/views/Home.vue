<template>
  <v-app>
    <div :style="cssProps">
      <div class="center">
        <h1 style="color:white">Meine Ideen</h1>
      </div>
      <div id="test">
        <div style="width: 90%">
          <VExpansionPanel :data="items" :kat="kategorie"> </VExpansionPanel>
        </div>
        
      </div>
    </div>
  </v-app>
</template>
<script>
import AuthService from '@/services/AuthService.js';
import VExpansionPanel from '../components/expansionPanel.vue';
export default {
  data() {
    
    return {
      secretMessage: '',
      username: '',
      items: [
          {headline: "head1", text: 'text'},
          {headline: "head2", text: 'text'},
          {headline: "head3", text: 'text'},
          {headline: 'head4', text: 'text'}
        ],
      kategorie: [
        {title: "kategorie1"},
        {title: "kategorie2"}
      ],

      cssProps: {
          backgroundImage: `url(${require('@/assets/gb.jpeg')})`,
          backgroundPosition: 'center center',
          backgroundSize: 'cover',
          minHeight: '100%'
        }
    };
  },
  components: {
    VExpansionPanel
  },

  async created() {
    if (!this.$store.getters.isLoggedIn) {
      //this.$router.push('/login');
    }
    this.username = this.$store.getters.getUser.username;
    this.secretMessage = await AuthService.getSecretContent();
  },
  methods: {
    logout() {
      this.$store.dispatch('logout');
      this.$router.push('/login');
    }
  }
};
</script>

<style>
  .center {
    text-align: center;
  }

  #test{
    display: flex;
    align-items: center;
    justify-content: center;
    
  }
</style>