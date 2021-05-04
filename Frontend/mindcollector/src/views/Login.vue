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
          <v-btn shaped block type="submit">Login</v-btn>
        </v-form>
        <p v-if="showError" id="error">Username or Password is incorrect</p>
      </div>
      <div class="reg">
        <p>Noch nicht Registriert?</p>
        <v-btn shaped block to="/register">Register</v-btn>
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
      const User = {
          username: this.form.username,
          password: this.form.password
        };
      try {
        console.log(User);
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
.v-btn[type="submit"] {
  background-color: #4caf50;
  color: white;
  padding: 12px 20px;
  cursor: pointer;
}
.v-btn[type="submit"]:hover {
  background-color: #45a049;
}
#error {
  color: red;
}

.login {
  text-align: center;
  padding: 180px 300px;
}

.reg{
  padding: 20px;
}

@media screen and (max-width: 1000px) {
  .login {
    text-align: center;
    padding: 4rem 0;
  }
}
</style>