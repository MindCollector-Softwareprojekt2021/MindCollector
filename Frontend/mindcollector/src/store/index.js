import Vuex from "vuex";
import Vue from "vue";
import createPersistedState from "vuex-persistedstate";
import notes from "./modules/notes";
import AudioRecorder from "@/index";

// Load Vuex
Vue.use(Vuex);
Vue.use(AudioRecorder);
// Create store
export default new Vuex.Store({
  modules: {
    notes,
  },
  plugins: [createPersistedState()],
});
