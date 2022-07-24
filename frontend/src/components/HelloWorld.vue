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
      v-model="text"
    >
    </v-textarea>
  </div>
</template>

<script lang="ts" setup>
import SigmaService from "../services/SigmaService.js";
import { ref } from "vue";

defineProps({ readonly: Boolean });
const text = ref("");

// function changeColor() {
//   if (text.value.includes(":")) {
//     const splitString = text.value.split(" ");
//     splitString.forEach((element) => {
//       if (element.includes(":")) {
//         const res = text.value.replace(
//           element,
//           `<span style='color:red'>${element}</span>`
//         );
//         const button = document.getElementById("area");
//         if (button != null) {
//           button.innerHTML = res;
//         }
//       }
//     });
//   }
// }
</script>

<style>
.hello {
  width: 30%;
  display: flex;
}
</style>
