<template>
  <v-bottom-nav
      :active.sync="bottomNav"
      :value="true"
      fixed
      color="brown darken-3"
      class="hidden-md-and-up"
    >

    <template v-for="item in items">
      <v-btn dark :to="item.href">
        <span>{{ item.title }}</span>
        <v-icon>{{ item.icon }}</v-icon>
      </v-btn>
    </template>

    </v-bottom-nav>
</template>

<script>
  import routes from '../router/routes'
  export default {
    name: 'Navbar',
    data () {
      return {
        bottomNav: 'home',
        items: routes
      }
    }
  }
</script>

<style scoped>

</style>
