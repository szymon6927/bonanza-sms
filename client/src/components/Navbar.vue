<template>
  <v-bottom-nav
    :value="true"
    :active.sync="e2"
    :color="color"
    absolute
    shift
  >
    <v-btn dark to="/">
      <span>Home</span>
      <v-icon>home</v-icon>
    </v-btn>
    <v-btn dark to="/form">
      <span>Form</span>
      <v-icon>book</v-icon>
    </v-btn>
    <v-btn dark to="/private-policy">
      <span>Private policy</span>
      <v-icon>music_note</v-icon>
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
          case 0: return 'blue'
          case 1: return 'brown darken-1'
          case 2: return 'teal'
        }
      }
    }
  }
</script>

<style scoped>

</style>
