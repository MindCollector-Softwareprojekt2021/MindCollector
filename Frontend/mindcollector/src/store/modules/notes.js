import Api from "@/services/api";

const state = {
  selectedKat: null,
  notes: null,
  username: null,
};

const getters = {
  getNotes: (state) => state.notes,
  getSelectedKat: (state) => state.selectedKat,
  isAuthenticated: (state) => !!state.username,
  getUsername: (state) => state.username,
};

const actions = {
  async loadNotes({ commit }) {
    let response = await Api().get("/notiz");
    commit("loadNotes", response.data);
  },
  async createNote({ commit }, note) {
    let response = await Api().post("/notiz", note);

    //commit("createNote", note);
  },
  async deleteNote({ commit }, note) {
    await Api().delete(`/notiz/delete/${note[0][0]}`);
    commit("deleteNote", note);
  },
  async updateNote({ commit }, note) {
    await Api().put("/notiz");
    commit("deleteNote", note);
  },
  async createKategorie({ commit }, kat) {
    let response = await Api().post("/kategorie", { KATEGORIE_TITEL: kat });
    commit("addKategorie", response.data);
  },
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

    commit("LogOut", username);
  },
};

const mutations = {
  loadNotes(state, notes) {
    state.notes = notes;
  },
  setSelectedKat(state, kat) {
    state.selectedKat = kat;
  },
  deleteNote(state, note) {
    state.notes
      .filter(function(chain) {
        return chain.KATEGORIE_ID === note[1];
      })[0]
      .EINTRAG.splice(
        state.notes
          .filter(function(chain) {
            return chain.KATEGORIE_ID === note[1];
          })[0]
          .EINTRAG.indexOf(note[0]),
        1
      );
  },
  updateNote() {},
  addKategorie(state, kat) {
    state.notes.push(kat);
  },
  LogOutNotes(state) {
    state.notes = null;
  },
  setUser(state, user) {
    state.username = user;
  },
  LogOut(state) {
    state.username = null;
    state.notes = null;
  },
};

export default {
  state,
  getters,
  actions,
  mutations,
};
