<template>
  <v-container>
    <v-row>
      <div style="width: 600px">
        <v-row>
          <v-select
            :items="backends"
            label="Choose Backend (Target)"
          ></v-select>

          <v-select
            :items="configs"
            label="Choose Configuration (Source)"
          ></v-select>
        </v-row>
      </div>
    </v-row>
    <v-row>
      <v-spacer></v-spacer>
      <hello-world :readonly="false" />
      <v-spacer></v-spacer>
      <v-btn icon="mdi-swap-horizontal" rounded="lg" color="black"></v-btn>
      <v-spacer></v-spacer>
      <text-area-result :readonly="true" />
      <v-spacer></v-spacer>
    </v-row>
  </v-container>
</template>

<script lang="ts" setup>
// Components
import SigmaService from "../services/SigmaService.js";
import { onMounted, ref } from "vue";
import HelloWorld from "../components/HelloWorld.vue";
import TextAreaResult from "../components/TextAreaResult.vue";

const backends = ref([]);
const configs = ref([]);
onMounted(() => {
  SigmaService.getBackends().then((result) => {
    backends.value = result.data;
  });
  SigmaService.getConfigs().then((result) => {
    configs.value = result.data;
  });
});
</script>
