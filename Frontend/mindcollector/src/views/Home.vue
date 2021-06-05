<template>
  <v-main class="main">
    <section class="card" v-if="isAuth">
      <h1>Willkommen {{ notes }}</h1>
    </section>
    <section class="card" v-if="!isAuth">
      <div>
        <h1>Erreiche mehr dank besserer Notizen</h1>
      </div>
      <div>
        <h2>
          MindCollector hilft dir, deine Ideen festzuhalten und schnell
          wiederzufinden.
        </h2>
      </div>
      <div>
        <v-btn to="/register" color="success">Kostenlos registrieren</v-btn>
      </div>
      <div>
        <v-btn to="/login">Du besitzt bereits ein Konto? Anmelden</v-btn>
      </div>
    </section>
    <section class="containerCard">
      <div class="imgContainer">
        <img src="..\assets\meinNotizen.png" alt="" />
      </div>

      <div class="textContainer">
        <div class="alignTextContainer">
          <div>
            <h3>test</h3>
            <p>
              Halte wichtige Informationen stets griffbereit, indem du sie
              geräteübergreifend synchronisierst.
            </p>
          </div>
          <div>
            <h3>test</h3>
            <p>
              Halte wichtige Informationen stets griffbereit, indem du sie
              geräteübergreifend synchronisierst.
            </p>
          </div>
          <div>
            <h3>test</h3>
            <p>
              Halte wichtige Informationen stets griffbereit, indem du sie
              geräteübergreifend synchronisierst.
            </p>
          </div>
        </div>
      </div>
    </section>
    <section class="card">
      <div>
        <h1>Lorem ipsum dolor sit amet consectetur adipisicing elit.</h1>
      </div>
      <div>
        <h2>
          Lorem ipsum, dolor sit amet consectetur adipisicing elit. Quae non
          omnis in voluptatem, odit iusto, facilis porro voluptates iure
          perspiciatis adipisci eaque explicabo laudantium rerum blanditiis.
          Repellat recusandae odio vero! Dicta asperiores repellat eius officiis
          rem illo, quo nisi cum sint nulla corrupti aut reprehenderit quos eos
          commodi enim ex a eveniet, numquam ipsam quibusdam id.
        </h2>
      </div>
    </section>
    <section class="containerCard">
      <div class="imgContainer">
        <img src="..\assets\meinNotizen.png" alt="" />
      </div>

      <div class="textContainer">
        <div class="alignTextContainer">
          <div>
            <h3>test</h3>
            <p>
              Halte wichtige Informationen stets griffbereit, indem du sie
              geräteübergreifend synchronisierst.
            </p>
          </div>
          <div>
            <h3>test</h3>
            <p>
              Halte wichtige Informationen stets griffbereit, indem du sie
              geräteübergreifend synchronisierst.
            </p>
          </div>
          <div>
            <h3>test</h3>
            <p>
              Halte wichtige Informationen stets griffbereit, indem du sie
              geräteübergreifend synchronisierst.
            </p>
          </div>
        </div>
      </div>
    </section>
  </v-main>
</template>

<script>
export default {
  data() {
    return {};
  },
  computed: {
    notes() {
      return this.$store.getters.getUsername;
    },
    isAuth() {
      return this.$store.getters.isAuthenticated;
    },
  },
};
</script>

<style scoped>
.main {
  background: url(../assets/background.jpg);
  background-size: cover;
  background-attachment: fixed;
  background-position: center center;
  text-align: center;
  color: rgb(65, 65, 65);
  min-height: 100%;
}
section {
  margin: 50px 0;
}
.containerCard {
  display: flex;
  background-color: rgba(255, 255, 255, 0.664);
  margin: 0 50px;
}
.imgContainer {
  text-align: center;
  align-items: center;
  display: flex;
  margin: 0 10px;
}
.textContainer {
  align-items: center;
  text-align: center;
}
.alignTextContainer {
  text-align: left;
}
img {
  width: 100%;
}
h1 {
  font-size: 3em;
}
h2 {
  font-size: 1.5em;
}
</style>
