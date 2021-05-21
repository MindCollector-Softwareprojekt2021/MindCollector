<template>
  <v-card outlined light elevation="24">
    <v-card-title> {{ titel }} </v-card-title>
    <v-card-text class="v-cardtext">
      <v-row>
        <v-col class="text">
          {{ text }}
        </v-col>
        <span v-if="img.length > 0" class="bild">
          <img :src="imgURL" alt="img" />
        </span>
      </v-row>
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
          <v-dialog v-model="dialogAnzeige" max-width="800px">
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
                <div v-if="img.length > 0" style="textAlign: center">
                  <img :src="imgURL" alt="img" style="maxWidth: 100%" />
                </div>
                <div>
                  {{ text }}
                </div>
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
      titel: this.notiz.EINTRAG_TITEL,
      text: this.notiz.EINTRAG_BESCHREIBUNG,
      img: this.notiz.BILD,
    };
  },
  computed: {
    imgURL() {
      return "data:image/png;charset=utf-8;base64," + this.img;
    },
  },
  props: ["notiz", "katID"],
  methods: {
    async deleteNote() {
      await this.$store.dispatch("deleteNote", [this.notiz, this.katID]);
      this.dialogDelete = false;
    },
    abbruch() {
      this.dialogEdit = false;
      this.titel = this.notiz.EINTRAG_TITEL;
      this.text = this.notiz.EINTRAG_BESCHREIBUNG;
    },
    async editNote() {
      let note = {
        EINTRAG_ID: this.notiz.EINTRAG_ID,
        EINTRAG_TITEL: this.titel,
        EINTRAG_BESCHREIBUNG: this.text,
      };
      await this.$store.dispatch("updateNote", note);
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
<style lang="scss" scoped>
$textHeight: 250px;
$imgHeight: 200px;
.v-cardtext {
  overflow: hidden hidden;
  display: block;
  max-height: $textHeight;
  margin: 0;
}
.v-cardtext img {
  /*float: right;*/
  max-height: $imgHeight;
}
.text {
  overflow: hidden auto;
  max-height: $textHeight;
  width: 100%;
}
.bild {
  overflow: hidden hidden;
  text-align: center;
  margin: auto;
}
@media screen and (max-width: 770px) {
  .v-cardtext img {
    /*float: right;*/
    max-height: $imgHeight;
    zoom: 0.5;
  }
}
</style>
