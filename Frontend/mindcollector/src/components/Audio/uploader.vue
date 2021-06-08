<style lang="scss">
@import "../scss/icons";
</style>

<template>
  <icon-button
    name="save"
    class="ar-icon ar-icon__xs ar-icon--no-border"
    @click.native="upload"
  />
</template>

<script>
import IconButton from "./icon-button";
import UploaderPropsMixin from "@/mixins/uploader-props";

export default {
  mixins: [UploaderPropsMixin],
  props: {
    record: { type: Object },
  },
  components: {
    IconButton,
  },
  methods: {
    async upload() {
      if (!this.record.url) {
        return;
      }

      this.$eventBus.$emit("start-upload");

      const data = new FormData();
      console.log(this.record);
      data.append("AUDIO", this.record);
      data.append("USERNAME", this.$store.getters.getUsername);
      data.append("KATEGORIE_ID", this.$store.getters.getSelectedKat[0]);
      data.append("EINTRAG_TITEL", "Das ist nur ein Test");
      data.append("EINTRAG_BESCHREIBUNG", "");
      console.log(data);
      await this.$store.dispatch("createAudioNote", data);
      this.$router.push("/meine-notizen");

      /*
      const headers = Object.assign(this.headers, {});
      headers[
        "Content-Type"
      ] = `multipart/form-data; boundary=${data._boundary}`;



      this.$http
        .post(this.uploadUrl, data, { headers: headers })
        .then((resp) => {
          this.$eventBus.$emit("end-upload", {
            status: "success",
            response: resp,
          });
        })
        .catch((error) => {
          this.$eventBus.$emit("end-upload", {
            status: "fail",
            response: error,
          });
        });
        */
    },
  },
};
</script>
