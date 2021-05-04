<template>
  <div class="register">
    <v-form @submit.prevent="submit">
      <v-container fluid>
        <v-row>
          <v-col>
            <v-text-field
              v-model="title"
              :rules="[rules.required, rules.counter]"
              label="Username"
              counter
              outlined
              maxlength="50"
            ></v-text-field>
            <v-text-field
              v-model="title"
              :rules="[rules.required, rules.counter]"
              label="Full Name"
              counter
              outlined
              maxlength="50"
            ></v-text-field>
            <v-text-field
              v-model="form.full_name"
              :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
              :rules="[rules.required, rules.min]"
              :type="show1 ? 'text' : 'password'"
              name="input-10-1"
              label="Password"
              hint="At least 8 characters"
              counter
              outlined
              @click:append="show1 = !show1"
            ></v-text-field>
            <v-select
              :items="sf1"
              label="Sicherheitsfrage 1"
              dense
              outlined
            ></v-select>
            <v-text-field
              v-model="message4"
              label="Antwort Sicherheitsfrage 1"
              outlined
              clearable
            ></v-text-field>
            <v-select
              :items="sf2"
              label="Sicherheitsfrage 2"
              dense
              outlined
            ></v-select>
            <v-text-field
              v-model="message4"
              label="Antwort Sicherheitsfrage 2"
              outlined
              clearable
            ></v-text-field>
          </v-col>
        </v-row>
        <v-row>
          <v-col>
            <v-btn type="submit">Submit</v-btn>
          </v-col>
        </v-row>
        <p v-if="showError" id="error">Username already exists</p>
      </v-container>
    </v-form>
  </div>
</template>

<script>
import { mapActions } from "vuex";
export default {
  name: "Register",
  components: {},
  data() {
    return {
      show1: false,
      form: {
        username: "",
        full_name: "",
        password: "",
      },
      sf1: ["Wo wurdest du geboren?", "Wie heißt dein erstes Haustier?"],
      sf2: ["Was ist dein Lieblingsessen", "Was ist deine Lieblingszahl"],
      showError: false,
      rules: {
        required: (value) => !!value || "Required.",
        counter: (value) => value.length <= 20 || "Max 20 characters",
        min: (v) => v.length >= 8 || "Min 8 characters",
      },
    };
  },
  methods: {
    ...mapActions(["Register"]),
    async submit() {
      try {
        await this.Register(this.form);
        this.$router.push("/login");
        this.showError = false;
      } catch (error) {
        this.showError = true;
      }
    },
  },
};
</script>

<style scoped>
* {
  box-sizing: border-box;
}
.v-btn[type="submit"] {
  background-color: #4caf50;
  color: white;
  padding: 12px 20px;
  cursor: pointer;
}
.v-btn[type="submit"]:hover {
  background-color: #4caf50;
}
#error {
  color: red;
}
.register {
  text-align: center;
  padding: 70px 500px;
}

@media screen and (max-width: 1000px) {
  .register {
    text-align: center;
    padding: 20px 0;
  }
}
</style>