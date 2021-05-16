import Api from "@/services/api";

const state = {
  username: null,
};

const getters = {
  isAuthenticated: (state) => !!state.username,
  getUsername: (state) => state.username,
};

const actions = {
  async login({ commit }, user) {
    let response = await Api().post("/login", user);
    commit("setUser", user.USERNAME);
    console.log(response.data);
  },
  async register({ commit }, user) {
    let response = await Api().post("/register", user);
  },
  async LogOut({ commit }) {
    let username = null;
    console.log();
    await this.$store.dispatch("LogOutNotes");
    commit("LogOut", username);
  },
};

const mutations = {
  setUser(state, user) {
    state.username = user;
  },
  LogOut(state) {
    state.user = null;
  },
};

export default {
  state,
  getters,
  actions,
  mutations,
};
