<template>
  <div class="notizen">
    <div>
      <div><h1>Meine Notizen</h1></div>
      <div class="btn-kat">
        <v-dialog v-model="dialog" persistent max-width="600px">
          <template v-slot:activator="{ on, attrs }">
            <v-btn color="primary" dark v-bind="attrs" v-on="on">
              Kategorie hinzufügen
            </v-btn>
          </template>
          <v-card>
            <v-card-title>
              <span class="headline">Kategorie hinzufügen</span>
            </v-card-title>
            <v-card-text>
              <v-form v-model="valid">
                <v-text-field
                  v-model="kategorieName"
                  label="Bezeichnung"
                  counter="30"
                  :rules="[
                    required('Bezeichnung'),
                    maxLength('Bezeichnung', 30),
                  ]"
                />
              </v-form>
            </v-card-text>
            <v-card-actions>
              <v-btn
                color="blue darken-1"
                text
                :disabled="!valid"
                @click="save()"
              >
                Speichern
              </v-btn>
              <v-btn color="blue darken-1" text @click="dialog = false">
                Abbrechen
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
      </div>
    </div>
    <div id="expan">
      <VExpansionPanel> </VExpansionPanel>
    </div>
  </div>
</template>
<script>
import VExpansionPanel from "../components/expansionPanel.vue";
import validations from "@/utils/validations";

export default {
  components: {
    VExpansionPanel,
  },
  data() {
    return {
      USERNAME: this.$store.getters.getUsername,
      dialog: false,
      ...validations,
      valid: false,
      kategorieName: "",
    };
  },
  mounted() {
    this.$store.dispatch("loadNotes", { USERNAME: this.USERNAME });
  },
  methods: {
    async save() {
      try {
        let kat = {
          KATEGORIE_TITEL: this.kategorieName,
          USERNAME: this.USERNAME,
        };
        await this.$store.dispatch("createKategorie", kat);
        this.dialog = false;
        this.kategorieName = "";
      } catch (error) {
        console.log(error);
      }
    },
  },
};
</script>

<style scoped>
.notizen {
  margin: 2rem;
  text-align: center;
  overflow: auto;
}

h1 {
  color: rgb(112, 112, 112);
  text-decoration: underline;
  text-transform: uppercase;
  text-align: center;
  white-space: nowrap;
  direction: rtl;
}

.btn-kat {
  text-align: right;
  padding: 0;
}

@media screen and (max-width: 700px) {
  .notizen {
    margin: 1rem 0;
    text-align: center;
  }

  .btn-kat {
    padding: 1rem 0 0 0;
  }
}
</style>
