<template>
  <v-expansion-panels class="v-expansion-panels" focusable>
    <v-expansion-panel v-for="notiz in notes" :key="notiz.KATEGORIE_ID">
      <v-expansion-panel-header color="rgb(240, 240, 240)">
        <span>{{ notiz.KATEGORIE_TITEL }}</span>
        <span id="btn-plus">
          <!-- Dialog -->
          <DeleteKategorie :notiz="notiz" />
          <!-- Menu add -->
          <AddMenu :notiz="notiz" />
        </span>
      </v-expansion-panel-header>
      <v-expansion-panel-content
        color="rgb(247, 247, 247)"
        class="expanContent"
      >
        <Notiz
          v-for="i in notiz.EINTRAG"
          :key="i.EINTRAG_ID"
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
import DeleteKategorie from "@/components/deleteKategorie";
import AddMenu from "@/components/addNotizen/addMenu";

export default {
  components: {
    Notiz,
    addNotizText,
    DeleteKategorie,
    AddMenu,
  },
  data() {
    return {
      test: null,
      deleteKatDialog: false,
    };
  },
  computed: {
    notes() {
      return this.$store.getters.getNotes;
    },
  },
  methods: {},
};
</script>

<style scoped>
#btn-plus {
  text-align: right;
}
.expanContent {
  padding: 0 20%;
}

@media screen and (max-width: 700px) {
  .expanContent {
    padding: 0;
  }
}
</style>
