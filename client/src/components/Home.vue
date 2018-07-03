<template>
  <v-container class="mb-5" text-xs-center>
    <v-layout row wrap>
      <v-flex xs12 sm10 md10 lg8 offset-xs0 offset-sm1 offset-md1 offset-lg2>
        <div class="content__wraper elevation-10 text-xs-center pt-5 pb-5">
          <img class="logo" src="/static/western.png">
          <h1 class="black--text mb-3">Łap okazje i rabaty!</h1>
          <h2 class="black--text display-1 bonanza-name we mb-3">Bar Bonanza!</h2>
          <h3 class="black--text mb-4">Bądź z nami na bieżąco!</h3>
          <v-btn round large block color="light-blue darken-4 white--text" to="/form">Zapisz się</v-btn>
        </div>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
  export default {
    name: "Home",
    data () {
      return {
        message: "Bar bonanza! Bądź na bieżąco!"
      }
    }
  }
</script>

<style scoped>
  h3 {
    font-weight: 600;
  }
  @media (min-width: 615px) {
    .logo {
      width: 40%;
    }
  }
</style>
