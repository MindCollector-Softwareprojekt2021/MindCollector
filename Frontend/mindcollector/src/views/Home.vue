<template>
  <v-app :style="cssProps" >
    <v-container id="test" fill-height fluid>
      <v-row align="center" justify="center">
        <v-col outlined cols="6" md="4">
          <v-card-actions>
          <img src="https://via.placeholder.com/500x300" alt="palceholder" />
          </v-card-actions>
        </v-col>
        <v-col>
          <v-card-text>
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Aut
            consectetur deserunt asperiores, iste corrupti veritatis nesciunt
            laborum nulla quaerat maxime doloremque vitae excepturi unde sunt,
            reiciendis enim? Facilis, provident labore. Nemo animi consequuntur
            mollitia voluptatum at rem quaerat numquam consequatur
            exercitationem illum, placeat illo delectus quis? Nihil hic cumque
            accusantium corporis! Quibusdam ipsa aliquid, quaerat dolorem
            delectus libero impedit dignissimos. Labore eaque illo, facere alias
            cum ipsam excepturi dolorem vel qui deleniti tempora amet quae quos,
            minus eos. Error molestias quod velit dolor nostrum autem, incidunt
            rem cupiditate eaque delectus?
          </v-card-text>
        </v-col>
      </v-row>
      <v-row align="center" justify="center">
        <v-col>
          <v-card-text>
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Aut
            consectetur deserunt asperiores, iste corrupti veritatis nesciunt
            laborum nulla quaerat maxime doloremque vitae excepturi unde sunt,
            reiciendis enim? Facilis, provident labore. Nemo animi consequuntur
            mollitia voluptatum at rem quaerat numquam consequatur
            exercitationem illum, placeat illo delectus quis? Nihil hic cumque
            accusantium corporis! Quibusdam ipsa aliquid, quaerat dolorem
            delectus libero impedit dignissimos. Labore eaque illo, facere alias
            cum ipsam excepturi dolorem vel qui deleniti tempora amet quae quos,
            minus eos. Error molestias quod velit dolor nostrum autem, incidunt
            rem cupiditate eaque delectus?
          </v-card-text>
        </v-col>
        <v-col outlined cols="6" md="4" align="right">
          <v-card-actions>
          <img src="https://via.placeholder.com/500x300" alt="palceholder" />
          </v-card-actions>
        </v-col>
      </v-row>
      <v-row align="center" justify="center">
        <v-col outlined cols="6" md="4">
          <v-card-actions>
          <img src="https://via.placeholder.com/500x300" alt="palceholder" />
          </v-card-actions>
        </v-col>
        <v-col>
          <v-card-text>
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Aut
            consectetur deserunt asperiores, iste corrupti veritatis nesciunt
            laborum nulla quaerat maxime doloremque vitae excepturi unde sunt,
            reiciendis enim? Facilis, provident labore. Nemo animi consequuntur
            mollitia voluptatum at rem quaerat numquam consequatur
            exercitationem illum, placeat illo delectus quis? Nihil hic cumque
            accusantium corporis! Quibusdam ipsa aliquid, quaerat dolorem
            delectus libero impedit dignissimos. Labore eaque illo, facere alias
            cum ipsam excepturi dolorem vel qui deleniti tempora amet quae quos,
            minus eos. Error molestias quod velit dolor nostrum autem, incidunt
            rem cupiditate eaque delectus?
          </v-card-text>
        </v-col>
      </v-row>
    </v-container>
  </v-app>
</template>


<script>
export default {
  data() {
    return {
      cssProps: {
        backgroundImage: `url(${require("@/assets/gb.jpeg")})`,
        backgroundPosition: "center center",
        backgroundSize: "cover",
        minHeight: "100%",
      },
    };
  },
  components: {},

  async created() {},
  methods: {},
};
</script>

<style scoped>
p {
  color: rgb(255, 255, 255);
  max-width: 80%;
}
.v-card__text{
  background-color: rgba(255, 255, 255, 0.493);
  color: white;
  min-width: 200px;
}

.v-card__actions{
  justify-content: center;
  min-width: 200px;
}




#test {
  background-color: rgba(119, 107, 107, 0);
}
</style>