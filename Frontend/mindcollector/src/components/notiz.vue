<template>
  <v-card outlined light elevation="24" max-width="600">
    <v-card-title> {{ titel }} </v-card-title>
    <v-card-text class="v-cardtext">
      {{ text }}
    </v-card-text>

    <v-card-actions>
      <div id="ac">
        <span
          ><v-dialog v-model="dialogEdit" persistent max-width="400">
            <template v-slot:activator="{ on, attrs }">
              <v-btn color="primary" dark v-bind="attrs" v-on="on">
                Ändern
              </v-btn>
            </template>
            <v-card>
              <v-card-title class="headline">
                Notiz ändern:
              </v-card-title>
              <v-spacer></v-spacer>
              <v-card-text>
                <v-text-field
                  v-model="titel"
                  label="Titel"
                  outlined
                  clearable
                  required
                ></v-text-field>
                <v-textarea
                  outlined
                  label="Text"
                  v-model="text"
                  required
                ></v-textarea>
              </v-card-text>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="orange darken-1" dark @click="abbruch()">
                  Abbrechen
                </v-btn>
                <v-btn color="green darken-1" dark @click="editNote()">
                  Speichern
                </v-btn>
              </v-card-actions>
            </v-card>
          </v-dialog></span
        >
        <span>
          <v-dialog v-model="dialogDelete" persistent max-width="400">
            <template v-slot:activator="{ on, attrs }">
              <v-btn color="primary" dark v-bind="attrs" v-on="on">
                Löschen
              </v-btn>
            </template>
            <v-card>
              <v-card-title class="headline">
                - {{ titel }} - löschen?
              </v-card-title>
              <v-card-text
                >Diese Notiz wird unwideruflich gelöscht. Bist du damit
                einverstanden?</v-card-text
              >
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn
                  color="orange darken-1"
                  dark
                  @click="dialogDelete = false"
                >
                  Nein, Abbruch!
                </v-btn>
                <v-btn color="green darken-1" dark @click="deleteNote()">
                  Ja, löschen!
                </v-btn>
              </v-card-actions>
            </v-card>
          </v-dialog>
        </span>
        <span>
          <v-dialog v-model="dialogAnzeige" width="700px">
            <template v-slot:activator="{ on, attrs }">
              <v-btn color="primary" dark v-bind="attrs" v-on="on">
                Anzeigen
              </v-btn>
            </template>
            <v-card>
              <v-card-title>
                <span class="headline">{{ titel }}</span>
              </v-card-title>
              <v-card-text>
                <span>
                  {{ text }}
                </span>
              </v-card-text>
              <v-card-actions>
                <v-btn
                  color="primary"
                  dark
                  block
                  @click="dialogAnzeige = false"
                >
                  Close
                </v-btn>
              </v-card-actions>
            </v-card>
          </v-dialog>
        </span>
      </div>
    </v-card-actions>
  </v-card>
</template>

<script>
export default {
  data() {
    return {
      dialogDelete: false,
      dialogAnzeige: false,
      dialogEdit: false,
      titel: this.notiz[1],
      text: this.notiz[2],
    };
  },
  props: ["notiz", "katID"],
  methods: {
    async deleteNote() {
      await this.$store.dispatch("deleteNote", [this.notiz, this.katID]);
      this.dialogDelete = false;
    },
    abbruch() {
      this.dialogEdit = false;
      this.titel = this.notiz[1];
      this.text = this.notiz[2];
    },
    async editNote() {
      let note = {
        EINTRAG_ID: this.notiz[0],
        EINTRAG_TITEL: this.titel,
        EINTRAG_BESCHREIBUNG: this.text,
      };
      console.log(note);
      this.dialogEdit = false;
    },
  },
};
</script>

<style scoped>
span {
  margin: 0 2px;
}
#ac {
  text-align: center;
}
.v-card {
  overflow: hidden auto;
  text-align: left;

  margin: 5px 0 0 0;
}

.v-cardtext {
  overflow: hidden auto;
  display: block;
  max-height: 200px;
}
.v-card__actions {
  background-color: rgb(119, 119, 119);
  padding: 0 0;
  text-align: center;
}

@media screen and (max-width: 1000px) {
  .v-card {
    text-align: left;
    margin: 3px 0;
  }
  .v-card__title {
    zoom: 0.75;
  }
  .v-cardtext {
    overflow: hidden auto;
    max-height: 100px;
  }
  .v-card__actions {
    background-color: rgb(119, 119, 119);
    zoom: 0.75;
    text-align: center;
  }
}
</style>
