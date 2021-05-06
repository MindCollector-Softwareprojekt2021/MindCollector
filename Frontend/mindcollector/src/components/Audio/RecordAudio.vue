<template>
  <div> 
      <v-btn
      fab
      :class="{
      'active': isRecording,
      'paused': isPaused
        }"
      medium
      color="primary"
    >
      <v-icon dark>
        mdi-text-to-speech
      </v-icon>
      
    </v-btn>
    <v-btn
      fab
      
      medium
      color="primary"
    >
      <v-icon dark>
        mdi-text-to-speech-off 
      </v-icon>
      
    </v-btn>
  </div>
</template>
<script>
</script>

<style scoped>
    .active {
      background-color: #ef5350;
      -webkit-animation: pulse 1.25s infinite cubic-bezier(0.66, 0, 0, 1);
      -moz-animation: pulse 1.25s infinite cubic-bezier(0.66, 0, 0, 1);
      animation: pulse 1.25s infinite cubic-bezier(0.66, 0, 0, 1);
    }

 @keyframes pulse {
    to {
      box-shadow: 0 0 0 10px rgba(239, 83, 80, 0.1);
      background-color: #E53935;
      transform: scale(0.9);
    }
  }
</style>