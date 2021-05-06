import Api from "@/services/api"

const state = {
  notes: []
};

const getters = {
  
};

const actions = {
  async loadNotes({commit}){
    let response = await Api().get('/meineNotizen');
    commit('setNotes', response.data);
  },
  async createNote({commit}, note){
    commit('addNote', note);
  }
};

const mutations = {
  setNotes(state, notes){
    state.notes = notes;
  },
  addNote(state, note){
    console.log(note)
    state.notes.find(n => n.katTitle === "Arbeit").listNote.push(note);
    
  }
};

export default {
  state,
  getters,
  actions,
  mutations,
};