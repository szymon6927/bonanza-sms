<template>
  <v-container fluid class="mb-5">
    <v-layout column align-center justify-center>
      <div class="content__wraper elevation-10 notfound text-xs-center pt-5 pb-5">
        <img class="logo mb-3" src="/static/western.png">
        <h1>Błąd 404</h1>
        <h2>Strona nie znaleziona :(</h2>
        <v-btn class="mt-5" large round block color="primary" to="/">Strona główna</v-btn>
      </div>
    </v-layout>
  </v-container>
</template>

<script>
  export default {
    name: "NotFound"
  }
</script>

<style scoped>

</style>
