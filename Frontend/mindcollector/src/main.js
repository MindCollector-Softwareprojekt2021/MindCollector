import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import vuetify from './plugins/vuetify';
import firebase from 'firebase'
import Axios from 'axios';

const firebaseConfig = {
  apiKey: "AIzaSyAT29lszc6RurNrCQBREiuFNFfhCdpXRwE",
  authDomain: "mindcollector-64402.firebaseapp.com",
  projectId: "mindcollector-64402",
  storageBucket: "mindcollector-64402.appspot.com",
  messagingSenderId: "458577431446",
  appId: "1:458577431446:web:33f64bf2712d040a2a2bb7",
  measurementId: "G-475RM0HYH9"
};

firebase.initializeApp(firebaseConfig);

// set auth header
Axios.defaults.headers.common['Authorization'] = `Bearer ${store.state.token}`;

Vue.config.productionTip = false

new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount('#app')
