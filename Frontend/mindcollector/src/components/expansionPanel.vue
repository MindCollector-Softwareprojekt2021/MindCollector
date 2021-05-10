<template>
  <v-expansion-panels class="v-expansion-panels" focusable>
    <v-expansion-panel v-for="notiz in notes.notes" :key="notiz.id">
      <v-expansion-panel-header color="rgb(240, 240, 240)">
        <span>{{ notiz.katTitle }}</span>
        <span id="btn-plus">
          <v-btn @click.stop="addNotiz(notiz.katTitle)" color="green">
            <v-icon>mdi-plus</v-icon>
          </v-btn>
        </span>
      </v-expansion-panel-header>
      <v-expansion-panel-content color="rgb(247, 247, 247)">
        <Notiz v-for="i in notiz.listNote" :key="i.id" :notiz="i"> </Notiz>
      </v-expansion-panel-content>
    </v-expansion-panel>
  </v-expansion-panels>
</template>

<script>
import Notiz from "./notiz.vue";

export default {
  components: {
    Notiz,
  },
  computed: {
    notes() {
      return this.$store.state.notes;
    },
  },
  methods: {
    addNotiz(k) {
      this.$router.push("/add");
    },
  },
};
</script>

<style scoped>
#btn-plus {
  text-align: right;
}</style
>>
