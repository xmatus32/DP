<template>
  <v-card class="d-flex flex-row justify-space-around" flat tile>
    <hello-world :readonly="false" />
    <hello-world :readonly="true" />
  </v-card>
</template>

<script lang="ts" setup>
// Components
import HelloWorld from "../components/HelloWorld.vue";
</script>
