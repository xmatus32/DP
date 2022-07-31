<template>
  <v-container>
    <v-row>
      <div style="width: 600px">
        <v-row>
          <v-select
            :items="backends"
            label="Choose Backend (Target)"
            v-model="target"
          ></v-select>

          <v-select
            :items="configs"
            label="Choose Configuration (Source)"
            v-model="config"
          ></v-select>
        </v-row>
      </div>
    </v-row>
    <v-row>
      <v-spacer></v-spacer>
      <hello-world
        :readonly="false"
        :rule="rule"
        @update:rule="(newValue) => (rule = newValue)"
      />
      <v-spacer></v-spacer>
      <v-btn
        icon="mdi-swap-horizontal"
        rounded="lg"
        color="black"
        @click="convertData()"
      ></v-btn>
      <v-spacer></v-spacer>
      <text-area-result :readonly="true" :rule="convertedRule" />
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

const target = ref();
const backends = ref([]);
const configs = ref([]);
const config = ref();
const rule = ref();
const convertedRule = ref();

onMounted(() => {
  SigmaService.getBackends().then((result) => {
    backends.value = result.data;
  });
  SigmaService.getConfigs().then((result) => {
    configs.value = result.data;
  });
});

function convertData() {
  const encodedRule = btoa(rule.value);
  SigmaService.convert(target.value, config.value, encodedRule).then(
    (result) => {
      console.log(result);
      convertedRule.value = result.data;
    }
  );
}
</script>
