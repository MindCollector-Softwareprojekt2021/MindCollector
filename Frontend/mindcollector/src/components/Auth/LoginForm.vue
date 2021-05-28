<template>
  <v-form v-model="valid">
    <v-text-field
      v-model="userInfo.USERNAME"
      label="Benutzername"
      placeholder="Username123"
      outlined
      :rules="[required('Benutzername')]"
    ></v-text-field>

    <v-text-field
      v-model="userInfo.PASSWORT"
      label="Passwort"
      placeholder="IchBinSicher!"
      outlined
      type="password"
      :rules="[required('Passwort')]"
    ></v-text-field>

    <v-btn block color="success" :disabled="!valid" @click="login(userInfo)">{{
      buttonText
    }}</v-btn>
    <p v-if="showError" id="error">Benutzername oder Passwort ist falsch</p>
  </v-form>
</template>

<script>
import validations from "@/utils/validations";

export default {
  data() {
    return {
      ...validations,
      valid: false,
      userInfo: {
        USERNAME: "",
        PASSWORT: "",
      },
      showError: false,
    };
  },
  methods: {
    async login(loginInfo) {
      try {
        await this.$store.dispatch("login", loginInfo);
        this.$router.push("/meine-notizen");
        this.showError = false;
      } catch (error) {
        this.showError = true;
      }
    },
  },
  props: ["submitForm", "buttonText"],
};
</script>

<style scoped>
#error {
  color: red;
}
</style>
