<template>
  <v-app>
    <v-app-bar app rounded color="black">
      <v-toolbar-title
        style="max-width: 400px"
        class="d-flex justify-space-around"
      >
        <router-link
          to="/"
          style="text-decoration: none; color: inherit; cursor: pointer"
        >
          {{ appTitle }}
        </router-link>
      </v-toolbar-title>
      <div class="vertical-line"></div>
      <v-tabs align-with-title>
        <v-tab
          to="/"
          style="text-decoration: none; color: inherit; cursor: pointer"
        >
          Sigma converter</v-tab
        >
        <v-tab
          to="/about"
          style="text-decoration: none; color: inherit; cursor: pointer"
        >
          Rules</v-tab
        >
      </v-tabs>
    </v-app-bar>

    <!-- Sizes your content based upon application components -->
    <v-main>
      <!-- Provides the application the proper gutter -->
      <v-container fluid>
        <!-- If using vue-router -->
        <router-view></router-view>
      </v-container>
    </v-main>

    <v-footer app>
      <!-- -->
    </v-footer>
  </v-app>
</template>

<script lang="ts" setup>
const appTitle = "Awesome App";
</script>

<style>
div.vertical-line {
  width: 1px; /* Line width */
  background-color: white; /* Line color */
  height: 50px; /* Override in-line if you want specific height. */
}
</style>
