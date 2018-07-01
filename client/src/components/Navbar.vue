<template>
  <v-bottom-nav
      :active.sync="bottomNav"
      :value="true"
      fixed
      color="brown darken-3"
      class="hidden-md-and-up"
    >
    <v-btn dark value="home" to="/">
      <span>Strona główna</span>
      <v-icon>home</v-icon>
    </v-btn>

    <v-btn dark value="form" to="/form">
      <span>Formularz</span>
      <v-icon>fas fa-edit</v-icon>
    </v-btn>

    <v-btn dark value="private-policy" to="/private-policy">
      <span class="text-xs-center">Polityka pryw</span>
      <v-icon>fas fa-list</v-icon>
    </v-btn>

    <v-btn dark value="about" to="/about">
      <span>O nas</span>
      <v-icon>fas fa-users</v-icon>
    </v-btn>
    </v-bottom-nav>
</template>

<script>
  export default {
    name: 'Navbar',
    data () {
      return {
        bottomNav: 'home'
      }
    }
  }
</script>

<style scoped>

</style>
