<template>
  <v-form v-model="valid">
    <v-text-field
      v-model="userInfo.username"
      label="Benutzername"
      placeholder="Username123"
      outlined
      :rules="[required('Benutzername')]"
    ></v-text-field>

    <v-text-field
      v-model="userInfo.password"
      label="Passwort"
      placeholder="IchBinSicher!"
      outlined
      type="password"
      :rules="[required('Passwort')]"
    ></v-text-field>

    <v-btn
      block
      color="success"
      :disabled="!valid"
      @click="submitForm(userInfo)"
      >{{ buttonText }}</v-btn
    >
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
        username: "",
        password: "",
      },
      showError: false,
    };
  },
  props: ["submitForm", "buttonText"],
};
</script>

<style>
#error {
  color: red;
}
</style>
