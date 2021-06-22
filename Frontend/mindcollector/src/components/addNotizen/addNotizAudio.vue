<template>
  <v-container>
    <v-row> <h1>Audio Notiz hinzufügen</h1> </v-row
    ><v-row>
      <v-text-field
        v-model="kat[1]"
        label="Kategorie"
        outlined
        disabled
      ></v-text-field> </v-row
    ><v-row style="justifyContent:center">
      <audio-recorder
        v-if="showRecorder"
        upload-url="https://mccurly.pythonanywhere.com/api/audioNotiz"
        filename="filename"
        format="wav"
        :attempts="3"
        :time="2"
        :headers="headers"
        :before-recording="callback"
        :pause-recording="callback"
        :after-recording="callback"
        :select-record="callback"
        :before-upload="callback"
        :successful-upload="callback"
        :failed-upload="callback"
        :bit-rate="192"
      />
      <audio-player :src="mp3" v-if="!showRecorder" />
    </v-row>
  </v-container>
</template>

<script>
import validations from "@/utils/validations";
export default {
  name: "app",
  data() {
    return {
      mp3: "/demo/example.mp3",
      showRecorder: true,
      headers: {
        "X-Custom-Header": "some data",
      },
      valid: false,
      kat: this.$store.getters.getSelectedKat,
      note: {
        EINTRAG_TITEL: "",
      },
      ...validations,
    };
  },
  methods: {
    callback(msg) {
      console.debug("Event: ", msg);
    },
    toggle() {
      this.showRecorder = !this.showRecorder;
    },
  },
};
</script>
