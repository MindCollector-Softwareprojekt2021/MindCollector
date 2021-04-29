<template>
  <v-expansion-panels class="v-expansion-panels">
    <v-expansion-panel v-for="k in kat" :key="k.headline">
      <v-expansion-panel-header>
        <span>{{ k.title }}</span>

        <span id="btn-plus">
          <v-tooltip left>
            <template v-slot:activator="{ on, attrs }">
              <v-fab-transition>
                <v-btn
                  
                  @click.stop="addNotiz(k)"
                  color="green"
                  dark
                  app
                  v-bind="attrs"
                  v-on="on"
                  right
                >
                  <v-icon>mdi-plus</v-icon>
                </v-btn>
              </v-fab-transition>
            </template>
            <span>TOOLTIP</span>
          </v-tooltip>
        </span>
      </v-expansion-panel-header>
      <v-expansion-panel-content>
        <Notiz v-for="vc in data" :key="vc" :data="vc"> </Notiz>
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
  props: ["data", "kat"],
  methods:{
    addKategory(){
        console.log("add Kategorie")
    },
    addNotiz(kategorie){
        console.log("add Notiz to:" + kategorie)
    },
}
};
</script>

<style scoped>
#btn-plus,
.fab-transition {
  text-align: center;
}
</style>>
