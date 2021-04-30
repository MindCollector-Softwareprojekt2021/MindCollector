<template>
  <div class="notizen">
    <div>
      <div><h1>Meine Notizen</h1></div>
      <div class="btn-kat">
        <v-tooltip left>
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
  </div>
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
        },
      ],
      kategorie: [
        { title: "kategorie1" },
        { title: "kategorie2" },
        { title: "kategorie3" },
      ],
      cssProps: {
        backgroundImage: `url(${require("@/assets/gb.jpeg")})`,
        backgroundPosition: "center center",
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

.notizen {
  margin: 2rem;
  text-align: center;
  overflow: auto;
}

h1 {
  color: white;
  text-decoration: underline;
  text-transform: uppercase;
  text-align: center;
  white-space: nowrap;
  direction: rtl;
}

.btn-kat {
  text-align: right;
  padding: 2rem 0 0 0;
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