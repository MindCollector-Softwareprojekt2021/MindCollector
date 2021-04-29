<template>
  <v-app class="bg" :style="cssProps">
    <div>
      <div><h1 style="color: white">Meine Notizen</h1></div>
      <div id="btn-kat" >
        <v-tooltip left >
          <template v-slot:activator="{ on, attrs }" id="test">
            <v-fab-transition>
              <v-btn
                v-show="!hidden"
                color="green"
                dark
                app
                v-bind="attrs"
                v-on="on"
              >
                <v-icon>mdi-plus</v-icon>
              </v-btn>
            </v-fab-transition>
          </template>
          <span>TOOLTIP</span>
        </v-tooltip>
      </div>
    </div>
    <div id="expan">
      <VExpansionPanel :data="items" :kat="kategorie"> </VExpansionPanel>
    </div>
  </v-app>
</template>
<script>
import VExpansionPanel from "../components/expansionPanel.vue";
export default {
  data() {
    return {
      items: [
        {
          headline: "head1",
          text:
            "Lorem, ipsum dolor sit amet consectetur adipisicing elit.Lorem, ipsum dolor sit amet consectetur adipisicing elit. Lorem, ipsum dolor sit amet consectetur adipisicing elit. Lorem, ipsum dolor sit amet consectetur adipisicing elit. Lorem, ipsum dolor sit amet consectetur adipisicing elit. Lorem, ipsum dolor sit amet consectetur adipisicing elit. Lorem, ipsum dolor sit amet consectetur adipisicing elit. Lorem, ipsum dolor sit amet consectetur adipisicing elit. Lorem, ipsum dolor sit amet consectetur adipisicing elit. Lorem, ipsum dolor sit amet consectetur adipisicing elit. Lorem, ipsum dolor sit amet consectetur adipisicing elit. Lorem, ipsum dolor sit amet consectetur adipisicing elit.Lorem, ipsum dolor sit amet consectetur adipisicing elit.",
        },
        {
          headline: "head2",
          text:
            "Lorem, ipsum dolor sit amet consectetur adipisicing elit.Lorem, ipsum dolor sit amet consectetur adipisicing elit. Lorem, ipsum dolor sit amet consectetur adipisicing elit. Lorem, ipsum dolor sit amet consectetur adipisicing elit. Lorem, ipsum dolor sit amet consectetur adipisicing elit. Lorem, ipsum dolor sit amet consectetur adipisicing elit. Lorem, ipsum dolor sit amet consectetur adipisicing elit. Lorem, ipsum dolor sit amet consectetur adipisicing elit. Lorem, ipsum dolor sit amet consectetur adipisicing elit. Lorem, ipsum dolor sit amet consectetur adipisicing elit. Lorem, ipsum dolor sit amet consectetur adipisicing elit. Lorem, ipsum dolor sit amet consectetur adipisicing elit.Lorem, ipsum dolor sit amet consectetur adipisicing elit.",
        },
        {
          headline: "head2",
          text:
            "Lorem, ipsum dolor sit amet consectetur adipisicing elit.Lorem, ipsum dolor sit amet consectetur adipisicing elit. Lorem, ipsum dolor sit amet consectetur adipisicing elit. Lorem, ipsum dolor sit amet consectetur adipisicing elit. Lorem, ipsum dolor sit amet consectetur adipisicing elit. Lorem, ipsum dolor sit amet consectetur adipisicing elit. Lorem, ipsum dolor sit amet consectetur adipisicing elit. Lorem, ipsum dolor sit amet consectetur adipisicing elit. Lorem, ipsum dolor sit amet consectetur adipisicing elit. Lorem, ipsum dolor sit amet consectetur adipisicing elit. Lorem, ipsum dolor sit amet consectetur adipisicing elit. Lorem, ipsum dolor sit amet consectetur adipisicing elit.Lorem, ipsum dolor sit amet consectetur adipisicing elit.",
        }
      ],
      kategorie: [
        { title: "kategorie1" },
        { title: "kategorie2" },
        { title: "kategorie3" }
      ],
      cssProps: {
        backgroundImage: `url(${require("@/assets/gb.jpeg")})`,
        backgroundPosition:"center center",
        backgroundSize: "cover",
        minHeight: "100%",
        backgroundAttachment: "fixed",
        backgroundRepeat: "no-repeat",
      },
    };
  },
  components: {
    VExpansionPanel,
  },
  
};
</script>



<style scoped>


h1{
  text-align: center;
}

#btn-kat{
  text-align: right;
  margin: 0 5%;
  padding: 10px;
}

#expan {
  margin: 0 5%;
  padding: 10px;
}
</style>