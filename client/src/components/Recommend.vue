<template>
  <v-container class="mb-5" text-xs-center>
    <v-layout row wrap>
      <v-flex xs12 sm10 md10 lg8 offset-xs0 offset-sm1 offset-md1 offset-lg2>
        <div class="content__wraper elevation-10 text-xs-center pt-5 pb-5">
          <h1 class="black--text mb-3">Dziś polecamy!</h1>
          <v-spacer></v-spacer>
          <img class="recommend img__responsive elevation-10" src="/static/recommended/recommend1.jpg" />
          <v-btn round large block color="light-blue darken-4 white--text mt-4" href="https://goo.gl/maps/L9mCSVHPvW92">
            <span class="pr-3">Odwiedź nas</span>
            <v-icon style="font-size: 18px;">fas fa-thumbs-up</v-icon>
          </v-btn>
        </div>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
  export default {
    name: "Recommend"
  }
</script>

<style scoped>

</style>
