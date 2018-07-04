<template>
  <v-container class="mb-5" text-xs-center>
    <v-layout row wrap>
      <v-flex xs12 sm10 md10 lg8 offset-xs0 offset-sm1 offset-md1 offset-lg2>
        <v-form class="form-wrapper elevation-10" ref="form" lazy-validation v-if="show">
          <img class="logo" src="/static/western.png">
          <h2>Dodaj opinię</h2>
          <p>Dodaj imię i nr.tel w celach weryfikacji</p>
          <v-text-field
            v-model="form.name"
            color="brown darken-3"
            :counter="20"
            :rules="form.nameRules"
            label="Imię"
            required
          ></v-text-field>
          <v-text-field
            v-model="form.phone"
            color="brown darken-3"
            :rules="form.phoneRules"
            label="Telefon"
            required
          ></v-text-field>
          <v-textarea
            v-model="form.opinion"
            :rules="form.opinionRules"
            color="brown darken-3"
            label="Dodaj opinie"
            hint="Dodaj opinie"
          ></v-textarea>
          <v-btn class="mb-3" round block color="light" @click="onReset">Wyczyść</v-btn>
          <v-btn round block color="light-blue darken-4 white--text" @click="onSubmit">Dodaj opinię</v-btn>
        </v-form>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
  export default {
    name: "AddOpinion",
    data() {
      return {
        form: {
          name: '',
          nameRules: [
            v => !!v || 'Proszę podać imię',
            v => (v && v.length >= 3) || 'Imię musi być dłuższe niż 3 litery'
          ],
          phone: '',
          phoneRules: [
            v => !!v || 'Proszę podaj nr. telefonu',
            v => /^(?:\(?\+?48)?(?:[-\.\(\)\s]*(\d)){9}\)?$/.test(v) || 'Proszę podać poprawny numer tel'
          ],
          opinion: '',
          opinionRules: [
            v => !!v || 'Dodaj opinię aby kontynuować'
          ],
          snackbar: false,
          error: false,
        },
        show: true
      }
    },
    methods: {
      onSubmit: function () {
        console.log("add opinion")
        console.log(this.form.opinion)
      },
      onReset: function () {
        console.log("reset")
      }
    }
  }
</script>

<style scoped>

</style>
