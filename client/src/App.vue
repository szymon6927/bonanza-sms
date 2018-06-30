<template>
  <v-app>
    <Topbar></Topbar>
    <router-view/>
    <Navbar></Navbar>
    <Footer></Footer>
  </v-app>
</template>

<script>
  import Topbar from './components/Topbar'
  import Navbar from "./components/Navbar"
  import Footer from './components/Footer'
  export default {
    name: 'App',
    components: {Topbar, Navbar, Footer}
  }
</script>

<style scoped>
</style>
