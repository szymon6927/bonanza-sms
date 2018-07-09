<template>
  <div class="content__wraper grettings elevation-10 text-xs-center">
    <img class="logo" src="/static/western.png">
    <h1>Bar Bonanza!</h1>
    <h2 class="mb-3">dziękuje za rejestrację, życzy udanego wypoczynku i pięknej pogody!</h2>
    <div class="icons__wrapper mb-4">
      <v-icon class="pr-2" large color="yellow darken-1">fas fa-sun</v-icon>
      <v-icon large color="orange darken-3">fas fa-umbrella-beach</v-icon>
    </div>
    <v-btn round block large color="success mt-3" to="/recommend">Szef kuchni poleca</v-btn>
  </div>
</template>

<script>
  export default {
    name: "Greetings",
    methods: {
      redirect: function () {
        console.log("redirect")
        setTimeout(() => {
          this.$router.push('/about');
        }, 5000)
      }
    },
    mounted() {
      this.redirect()
    }
  }
</script>

<style scoped>
  @media (min-width: 615px) {
    .logo {
      width: 40%;
    }
  }
</style>
