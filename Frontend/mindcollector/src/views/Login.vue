<template>
    <div class="login">
      <div>
        <v-form @submit.prevent="submit">
          <div>
            <v-text-field
              label="Username"
              placeholder="Username123"
              outlined
              v-model="form.username"
              type="text"
              name="username"
            ></v-text-field>
          </div>
          <div>
            <v-text-field
              label="Password"
              placeholder="IchBinSicher!"
              outlined
              type="password"
              name="password"
              v-model="form.password"
            ></v-text-field>
          </div>
          <button type="submit">Submit</button>
        </v-form>
        <p v-if="showError" id="error">Username or Password is incorrect</p>
      </div>
      <div>
        <p>Noch nicht Registriert?</p>
        <v-btn>
          <a href="/register"> Register</a>
        </v-btn>
      </div>
    </div>
</template>

<script>
import { mapActions } from "vuex";
export default {
  name: "Login",
  components: {},
  data() {
    return {
      form: {
        username: "",
        password: "",
      },
      showError: false,
    };
  },
  methods: {
    ...mapActions(["LogIn"]),
    async submit() {
      const User = new FormData();
      User.append("username", this.form.username);
      User.append("password", this.form.password);
      try {
        await this.LogIn(User);
        this.$router.push("/sammlung");
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
label {
  padding: 12px 12px 12px 0;
  display: inline-block;
}
button[type="submit"] {
  background-color: #4caf50;
  color: white;
  padding: 12px 20px;
  cursor: pointer;
  border-radius: 30px;
}
button[type="submit"]:hover {
  background-color: #45a049;
}
input {
  margin: 5px;
  box-shadow: 0 0 15px 4px rgba(0, 0, 0, 0.06);
  padding: 10px;
  border-radius: 30px;
}
#error {
  color: red;
}
.login {
  text-align: center;
  padding: 25px;
}

@media screen and (max-width: 700px) {
  .login {
  text-align: center;
  padding: 40px 0;
}
}
</style>