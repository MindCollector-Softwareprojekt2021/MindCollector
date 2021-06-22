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
  data() {
    return {
      kat: this.$store.getters.getSelectedKat,
      timestamp: "",
    };
  },
  mixins: [UploaderPropsMixin],
  props: {
    record: { type: Object },
  },
  components: {
    IconButton,
  },
  created() {
    setInterval(this.getNow, 1000);
  },
  methods: {
    getNow: function() {
      const today = new Date();
      const date =
        today.getFullYear() +
        "-" +
        (today.getMonth() + 1) +
        "-" +
        today.getDate();
      const time =
        today.getHours() + ":" + today.getMinutes() + ":" + today.getSeconds();
      const dateTime = date + " " + time;
      this.timestamp = dateTime;
    },
    async upload() {
      if (!this.record.url) {
        return;
      }
      try {
        this.$eventBus.$emit("start-upload");

        const data = new FormData();

        data.append("AUDIO", this.record.blob);
        data.append("KATEGORIE_ID", this.kat[0]);
        data.append("EINTRAG_TITEL", "Audio " + this.timestamp);
        await this.$store.dispatch("createAudioNote", data);
        this.$eventBus.$emit("end-upload", {
          status: "success",
          response: "",
        });

        this.$router.push("/meine-notizen");
      } catch (error) {
        this.$eventBus.$emit("end-upload", {
          status: "fail",
          response: error,
        });
      }
    },
  },
};
</script>
