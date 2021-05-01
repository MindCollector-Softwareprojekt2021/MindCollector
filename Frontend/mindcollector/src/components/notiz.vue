<template>
  <v-card outlined light elevation="24">
    <v-card-title>
      {{ data.headline }}
    </v-card-title>
    <v-card-text class="v-cardtext">
      {{ data.text }}
    </v-card-text>

    <v-card-actions>
      <div id="ac">
        <span><v-btn color="primary" dark> Edit </v-btn></span>
        <span><v-btn color="primary" dark> Delete </v-btn></span>
        <span>
          <v-dialog v-model="dialog" width="auto">
            <template v-slot:activator="{ on, attrs }">
              <v-btn color="primary" dark v-bind="attrs" v-on="on">
                Open Dialog
              </v-btn>
            </template>
            <v-card>
              <v-card-title>
                <span class="headline">{{ data.headline }}</span>
              </v-card-title>
              <v-card-text>
                <span>
                  {{ data.text }}
                </span>
              </v-card-text>
              <v-card-actions>
                <v-btn
                color="primary" 
                dark
                block
                @click="dialog = false"
                
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
  data () {
      return {
        dialog: false,
      }
    },
  props: ["data"],
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
