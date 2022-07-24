<template>
  <div class="hello">
    <v-textarea
      id="area"
      clearable
      rows="12"
      full-width
      no-resize
      auto-grow
      autofocus
      :readonly="readonly"
      clear-icon="mdi-close-circle"
    >
    </v-textarea>
  </div>
</template>

<script lang="ts" setup>
// import SigmaService from "../services/SigmaService.js";
// import { onMounted, ref } from "vue";

defineProps({ readonly: Boolean });
</script>

<style>
.hello {
  width: 30%;
  display: flex;
}
</style>
