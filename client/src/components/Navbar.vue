<template>
  <b-navbar class="shadow" toggleable="md" type="dark" variant="danger">

    <b-navbar-toggle target="nav_collapse"></b-navbar-toggle>

    <b-navbar-brand to="/">Promocje Bonanza</b-navbar-brand>

    <b-collapse is-nav id="nav_collapse">

      <b-navbar-nav>
        <b-nav-item to="/">Home</b-nav-item>
        <b-nav-item to="/ping">ping</b-nav-item>
        <b-nav-item to="/form">form</b-nav-item>
      </b-navbar-nav>

    </b-collapse>
  </b-navbar>

</template>

<script>
export default {
  name: 'Navbar'
}
</script>

<style scoped>

</style>
