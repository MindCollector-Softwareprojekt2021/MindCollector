import Api from "@/services/api"

const state = {
  userID:0,
  username:''

};

const getters = {
  getUsername: state => state.username,
  getUserID: state => state.userID
};

const actions = {
  async login({commit}, user){
    let response = await Api().get('/user', user);
    commit('setUser', response.data);
  },
  async register({commit}, user){
    let response = await Api().post('/user', user);
  },
};

const mutations = {
  setUser(state, user){
    state.userID = user.userID;
    state.username = user.username;
  }
};

export default {
  state,
  getters,
  actions,
  mutations,
};