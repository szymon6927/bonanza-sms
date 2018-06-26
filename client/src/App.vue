<template>
  <div id="app">
    <Navbar></Navbar>
    <!--<img src="./assets/logo.png">-->
    <router-view/>
  </div>
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
