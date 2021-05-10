import Api from "@/services/api";

const state = {
  notes: []
};

const getters = {
  getNotes: (state) => state.notes,
};

const actions = {
  async loadNotes({ commit }) {
    let response = await Api().get("/notiz");
    console.log(response.data);
    commit("loadNotes", response.data);
  },
  async createNote({ commit }, note) {
    Api().post("/notiz", note);
    commit("createNote", note);
  },
  async deleteNote({ commit }, note) {
    Api().delete("/notiz", note);
    commit("deleteNote", note);
  },
  async updateNote({ commit }, note) {
    Api().put("/notiz");
    commit("deleteNote", note);
  },
};

const mutations = {
  loadNotes(state, notes) {
    state.notes = notes;
  },
};

export default {
  state,
  getters,
  actions,
  mutations,
};
