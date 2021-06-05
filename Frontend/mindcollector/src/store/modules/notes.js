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
    commit("loadNotes", response.data);
  },
  async createNote({ commit }, note) {
    await Api().post("/notiz", note);

    //commit("createNote", note);
  },
  async createImageNote({ commit }, note) {
    await Api().post("/bildNotiz", note, {
      headers: {
        "Content-Type": "multipart/form-data",
      },
    });
    //commit("createNote", note);
  },
  async deleteNote({ commit }, note) {
    let delN = {
      EINTRAG_ID: note[0],
    };
    console.log(delN);
    await Api().post("/deleteNotiz", delN);
    commit("deleteNote", note);
  },
  async updateNote({ commit }, note) {
    console.log(note);
    await Api().put("/notiz", note);
  },
  async createKategorie({ commit }, kat) {
    let response = await Api().post("/kategorie", kat);
    commit("addKategorie", response.data);
  },
  async deleteKategorie({ commit }, kat) {
    let delK = {
      KATEGORIE_ID: kat,
    };
    console.log(delK);
    await Api().post("/deleteKategorie", delK);

    commit("deleteKat", kat);
  },
  async login({ commit }, user) {
    await Api().post("/login", user);
    commit("setUser", user.USERNAME);
  },
  async register({ commit }, user) {
    await Api().post("/user", user);
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
          .EINTRAG.map(function(d) {
            return d["EINTRAG_ID"];
          })
          .indexOf(note[0]),
        1
      );
    console.log(
      state.notes.filter(function(chain) {
        return chain.KATEGORIE_ID === note[1];
      })[0].EINTRAG.length
    );
  },
  deleteKat(state, kat) {
    state.notes.splice(
      state.notes
        .map(function(d) {
          return d["KATEGORIE_ID"];
        })
        .indexOf(kat),
      1
    );
  },
  addKategorie(state, kat) {
    state.notes.unshift(kat);
  },
  setUser(state, user) {
    state.username = user;
  },
  LogOut(state) {
    state.username = null;
    state.notes = [];
    state.selectedKat = null;
  },
};

export default {
  state,
  getters,
  actions,
  mutations,
};
