<template>
  <v-expansion-panels class="v-expansion-panels" focusable>
    <v-expansion-panel v-for="notiz in notes" :key="notiz.KATEGORIE_ID">
      <v-expansion-panel-header color="rgb(240, 240, 240)">
        <span>{{ notiz.KATEGORIE_TITEL }}</span>

        <span id="btn-plus">
          <v-menu offset-y rounded="b-xl">
            <template v-slot:activator="{ attrs, on }">
              <v-btn class="green" v-bind="attrs" v-on="on">
                <v-icon>mdi-plus</v-icon>
              </v-btn>
            </template>

            <v-list>
              <v-list-item
                @click="
                  addNotiz(
                    [notiz.KATEGORIE_ID, notiz.KATEGORIE_TITEL],
                    '/addNotizText'
                  )
                "
              >
                <v-list-item-title>
                  Text Notiz hinzufügen
                </v-list-item-title>
              </v-list-item>
              <v-list-item
                @click="
                  addNotiz(
                    [notiz.KATEGORIE_ID, notiz.KATEGORIE_TITEL],
                    '/addNotizImage'
                  )
                "
              >
                <v-list-item-title>
                  Bild Notiz hinzufügen
                </v-list-item-title>
              </v-list-item>
              <v-list-item
                @click="
                  addNotiz(
                    [notiz.KATEGORIE_ID, notiz.KATEGORIE_TITEL],
                    '/addNotizAudio'
                  )
                "
              >
                <v-list-item-title>
                  Audio Notiz hinzufügen
                </v-list-item-title>
              </v-list-item>
            </v-list>
          </v-menu>
          <!--
          <v-btn @click="addNotiz([notiz.KATEGORIE_ID, notiz.KATEGORIE_TITEL])" color="green">
            
          </v-btn>
          //-->
        </span>
      </v-expansion-panel-header>
      <v-expansion-panel-content color="rgb(247, 247, 247)">
        <Notiz
          v-for="i in notiz.EINTRAG"
          :key="i.id"
          :notiz="i"
          :katID="notiz.KATEGORIE_ID"
        >
        </Notiz>
      </v-expansion-panel-content>
    </v-expansion-panel>
  </v-expansion-panels>
</template>

<script>
import Notiz from "./notiz.vue";
import addNotizText from "@/components/addNotizen/addNotizText";

export default {
  components: {
    Notiz,
    addNotizText,
  },
  data() {
    return {};
  },
  computed: {
    notes() {
      return this.$store.getters.getNotes;
    },
  },
  methods: {
    addNotiz(k, push) {
      this.$store.commit("setSelectedKat", k);
      this.$router.push(push);
    },
  },
};
</script>

<style scoped>
#btn-plus {
  text-align: right;
}</style
>>
