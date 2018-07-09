<template>
  <v-footer height="50" class="blue-grey darken-4 hidden-sm-and-down" dark app>
    <v-container grid-list>
      <v-layout row wrap>
        <v-flex xs6 class="text-xs-left">
          <span>Copyright © 2018 Bar Bonanza - All Rights Reserved</span>
        </v-flex>
        <v-flex xs6 class="text-xs-right">
          <span><a href="https://www.szymonmiks.pl">Szymon Miks - aplikacje i strony internetowe</a></span>
        </v-flex>
      </v-layout>
    </v-container>
  </v-footer>
</template>

<script>
  export default {
    name: "Footer"
  }
</script>

<style scoped>
  a {
    color: #fff;
    text-decoration: none;
    transition: 0.25s;
  }

  a:hover {
    font-weight: bold;
  }
</style>
