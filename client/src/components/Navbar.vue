<template>
  <v-bottom-nav
    :value="true"
    :active.sync="e2"
    :color="color"
    shift
    fixed
  >
    <v-btn dark to="/">
      <span>Home</span>
      <v-icon>home</v-icon>
    </v-btn>
    <v-btn dark to="/form">
      <span>Form</span>
      <v-icon>fas fa-edit</v-icon>
    </v-btn>
    <v-btn dark to="/private-policy">
      <span>Private policy</span>
      <v-icon>fas fa-list</v-icon>
    </v-btn>
  </v-bottom-nav>
</template>

<script>
  export default {
    name: 'Navbar',
    data () {
      return {
        e2: 1
      }
    },
    computed: {
      color () {
        switch (this.e2) {
          case 0: return 'brown darken-2'
          case 1: return 'brown darken-3'
          case 2: return 'brown darken-4'
        }
      }
    }
  }
</script>

<style scoped>

</style>
