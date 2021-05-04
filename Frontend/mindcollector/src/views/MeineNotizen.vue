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
      user: '',
      items: [
        {
          headline: "head1",
          
          text: "Lorem ipsum dolor sit amet consectetur, adipisicing elit. Atque dicta, rerum officia sunt eos fuga quae, nihil doloremque perferendis veritatis eveniet dolore ipsam aperiam hic aut laborum commodi asperiores fugiat! Iure error quo magni aspernatur vitae deserunt saepe voluptas sunt unde officiis mollitia reprehenderit praesentium dignissimos quis, placeat dolore id nobis ad debitis. Ipsa, inventore? Numquam recusandae accusantium inventore possimus! Non nihil fugit, quibusdam enim natus, maiores fugiat iure consectetur repellat error alias dolorum dignissimos suscipit vero tempore laboriosam. Deleniti nemo, quaerat vero doloribus earum fuga odio explicabo nihil atque",
        },
        {
          headline: "head1",
          text: "text2",
        },
      ],
      kategorie: [
        { title: "kategorie1" },
        { title: "kategorie2" },
        { title: "kategorie3" },
      ],
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