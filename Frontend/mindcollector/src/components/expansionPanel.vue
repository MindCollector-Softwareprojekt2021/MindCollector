<template>
  <div>
    <v-expansion-panels 
      class="v-expansion-panels"
      >
      <v-expansion-panel
          v-for="k in kat"
          :key="k"
      >
        <v-expansion-panel-header>
          {{k.title}}
        </v-expansion-panel-header>
        <v-expansion-panel-content>
            <VCard v-for="vc in data" :key="vc" :data="vc"> </VCard>
        </v-expansion-panel-content>
      </v-expansion-panel>
    </v-expansion-panels>
  </div>
</template>

<script>
import VCard from '../components/vcard.vue';
export default({
    components: {
        VCard
    },
    props:[
        'data',
        'kat'
    ]
})
</script>

<style>

</style>