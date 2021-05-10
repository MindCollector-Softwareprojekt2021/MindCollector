<template>
  <v-form v-model="valid">
    <v-text-field
      v-model="regInfo.username"
      label="Benutzernamen"
      counter="255"
      clearable
      outlined
      :rules="[required('Benutzernamen'), maxLength('', 255)]"
    ></v-text-field>
    <v-text-field
      v-model="regInfo.full_name"
      label="Vor- und Nachname"
      counter="255"
      clearable
      outlined
      :rules="[required('Vor- und Nachname'), maxLength('', 255)]"
    ></v-text-field>
    <v-text-field
      v-model="regInfo.password"
      :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
      :type="show1 ? 'text' : 'password'"
      label="Passwort"
      clearable
      outlined
      @click:append="show1 = !show1"
      :rules="[required('Passwort'), minLength('Passwort', 8)]"
    ></v-text-field>
    <v-select
      v-model="regInfo.sf1"
      :items="sf1"
      label="Sicherheitsfrage 1"
      outlined
      :rules="[checkSelected('Sicherheitsfrage 1')]"
    ></v-select>
    <v-text-field
      v-model="regInfo.answer1"
      label="Antwort Sicherheitsfrage 1"
      outlined
      counter="255"
      dense
      clearable
      :rules="[
        required('Antwort'),
        minLength('Antwort', 3),
        maxLength('', 255),
      ]"
    ></v-text-field>
    <v-select
      v-model="regInfo.sf2"
      :items="sf2"
      label="Sicherheitsfrage 2"
      outlined
      :rules="[checkSelected('Sicherheitsfrage 2')]"
    ></v-select>
    <v-text-field
      v-model="regInfo.answer2"
      label="Antwort Sicherheitsfrage 2"
      outlined
      dense
      counter="255"
      clearable
      :rules="[
        required('Antwort'),
        minLength('Antwort', 3),
        maxLength('', 255),
      ]"
    ></v-text-field>
    <v-btn
      block
      color="success"
      :disabled="!valid"
      @click="submitForm(regInfo)"
      >{{ buttonText }}</v-btn
    >
    <p v-if="showError" id="error">Benutzernamen existiert bereits</p>
  </v-form>
</template>

<script>
import validations from "@/utils/validations";

export default {
  data() {
    return {
      valid: false,
      show1: false,
      regInfo: {
        username: "",
        full_name: "",
        password: "",
        sf1: "",
        sf2: "",
        answer1: "",
        answer2: "",
      },
      showError: false,
      ...validations,
    };
  },
  props: ["submitForm", "buttonText", "sf1", "sf2"],
};
</script>

<style scoped>
#error {
  color: red;
}

</style>
