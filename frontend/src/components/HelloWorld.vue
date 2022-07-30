<template>
  <div class="hello">
    <v-textarea
      id="rule"
      clearable
      rows="12"
      full-width
      no-resize
      auto-grow
      autofocus
      :readonly="readonly"
      clear-icon="mdi-close-circle"
      :model-value="rule"
      @update:modelValue="$emit('update:rule', $event)"
    >
    </v-textarea>
  </div>
</template>

<script lang="ts" setup>
import SigmaService from "../services/SigmaService.js";
import { ref } from "vue";

defineProps({ readonly: Boolean, rule: String });
defineEmits(["update:rule"]);
// const text = ref("");

// function handleChange(event) {
//   // `event` implicitly has `any` type
//   console.log(event.target.value);
// }

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
