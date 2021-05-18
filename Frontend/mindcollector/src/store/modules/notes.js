import Api from "@/services/api";

const state = {
  selectedKat: null,
  notes: [],
  username: null,
};

const getters = {
  getNotes: (state) => state.notes,
  getSelectedKat: (state) => state.selectedKat,
  isAuthenticated: (state) => !!state.username,
  getUsername: (state) => state.username,
};

const actions = {
  async loadNotes({ commit }, user) {
    let response = await Api().post("/load", user);
    console.log(response.data);
    commit("loadNotes", response.data);
  },
  async createNote({ commit }, note) {
    await Api().post("/notiz", note);

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
    let response = await Api().post("/kategorie", kat);
    commit("addKategorie", response.data);
  },
  async deleteKategorie({ commit }, kat) {
    let response = await Api().delete(`/kategorie/${kat}`);
    console.log(response.data);
    commit("deleteKat", kat);
  },
  async login({ commit }, user) {
    await Api().post("/login", user);
    commit("setUser", user.USERNAME);
  },
  async register({ commit }, user) {
    let response = await Api().post("/user", user);
    console.log(response);
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
  deleteKat(state, kat) {
    let test = state.notes.splice(
      state.notes
        .filter(function(chain) {
          return chain.KATEGORIE_ID === kat.KATEGORIE_ID;
        })
        .indexOf(kat)
    );
  },
  updateNote(state) {},
  addKategorie(state, kat) {
    state.notes.push(kat);
  },
  setUser(state, user) {
    state.username = user;
  },
  LogOut(state) {
    state.username = null;
    state.notes = [];
  },
};

export default {
  state,
  getters,
  actions,
  mutations,
};
