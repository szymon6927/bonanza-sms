<template>
  <v-app>
    <!--<img src="./assets/logo.png">-->
    <router-view/>
    <Navbar></Navbar>
  </v-app>
</template>

<script>
import Navbar from "./components/Navbar"
export default {
  name: 'App',
  components: {Navbar}
}
</script>

<style scoped>
</style>
