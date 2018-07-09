<template>
  <v-container class="mb-5" text-xs-center>
    <v-layout row wrap>
      <v-flex xs12 sm10 md10 lg8 offset-xs0 offset-sm1 offset-md1 offset-lg2>
        <v-form class="form-wrapper elevation-10">
          <h2>Logowanie</h2>
          <v-text-field
            v-model="email"
            color="brown darken-3"
            :counter="60"
            label="E-mail"
            required
          ></v-text-field>

          <v-text-field
            v-model="password"
            :type="'password'"
            color="brown darken-3"
            label="Hasło"
            required
          ></v-text-field>

          <v-btn block color="light-blue darken-4 white--text" @click="authenticate">Zaloguj</v-btn>
        </v-form>

        <v-snackbar :timeout="5000" :top="'top'" color="red" v-model="error">
          {{ errorMsg }}
          <v-btn dark flat @click.native="error = false">Zamknij</v-btn>
        </v-snackbar>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
  import {EventBus} from "@/utils";

  export default {
    name: "Login",
    data() {
      return {
        email: '',
        password: '',
        errorMsg: '',
        error: false
      }
    },
    methods: {
      authenticate() {
        this.$store.dispatch('login', {email: this.email, password: this.password})
          .then(() => this.$router.push('/'))
      }
    },
    mounted() {
      EventBus.$on('failedAuthentication', (msg) => {
        this.errorMsg = msg
        this.error = true
      })
    },
    beforeDestroy() {
      EventBus.$off('failedAuthentication')
    }
  }
</script>

<style scoped>

</style>
