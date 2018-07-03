<template>
  <v-container class="mb-5">
    <v-layout row wrap>
      <v-flex xs12 sm10 md10 lg8 offset-xs0 offset-sm1 offset-md1 offset-lg2>
        <div class="content__wraper elevation-10 notfound text-xs-center pt-5 pb-5">
          <img class="logo mb-3" src="/static/western.png">
          <h1>Błąd 404</h1>
          <h2>Strona nie znaleziona :(</h2>
          <v-btn class="mt-5" large round block color="primary" to="/">Strona główna</v-btn>
        </div>
      </v-flex>
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
