<template>
  <div class="hello">
    <v-textarea
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
//import { ref } from "vue";

defineProps({ readonly: Boolean });
</script>

<style>
.hello {
  width: 30%;
  display: flex;
}
</style>
