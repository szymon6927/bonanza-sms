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
            label="Opinia"
            hint="Dodaj opinie"
          ></v-textarea>
          <v-btn class="mb-3" round block color="light" @click="onReset">Wyczyść</v-btn>
          <v-btn round block color="light-blue darken-4 white--text" @click="onSubmit">Dodaj opinię</v-btn>
        </v-form>

        <v-snackbar :timeout="5000" :top="'top'" color="red" v-model="form.error">
          Coś poszło nie tak, spróbuj ponownie.
          <v-btn dark flat @click.native="form.error = false">Zamknij</v-btn>
        </v-snackbar>

        <v-snackbar auto-height :timeout="5000" :top="'top'" color="red" v-model="opinionExist">
          Użytkownik o tym numerze telefonu wystawił już opinie, dziękujemy :)
          <v-btn dark flat @click.native="form.error = false">Zamknij</v-btn>
        </v-snackbar>

      </v-flex>
    </v-layout>

    <v-layout row wrap v-if="grettings">
      <v-flex xs12 sm10 md10 lg8 offset-xs0 offset-sm1 offset-md1 offset-lg2>
        <div class="content__wraper grettings elevation-10 text-xs-center">
          <img class="logo" src="/static/western.png">
          <h2 class="mb-3">Dziękujemy za dodanie opinii :)</h2>
          <v-spacer></v-spacer>
          <v-btn round large block color="light-blue darken-4 white--text" to="/about">O nas</v-btn>
          <v-spacer></v-spacer>
          <v-btn round large block color="light-blue darken-4 white--text mb-3" to="/reviews">Zobacz inne opinie</v-btn>
        </div>
      </v-flex>
    </v-layout>

  </v-container>
</template>

<script>
  import axios from 'axios'
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
          error: false,
        },
        opinionExist: false,
        show: true,
        grettings: false
      }
    },
    methods: {
      onSubmit: function () {
        if (this.$refs.form.validate()) {
          this.sendForm()
        }
      },
      onReset: function () {
        this.$refs.form.reset()
      },
      sendForm: function () {
        const path = '/api/add-opinion';
        const payload = {
          'name': this.form.name,
          'phone': this.form.phone,
          'opinion': this.form.opinion
        };
        axios.post(path, payload)
          .then((res) => {
            console.log('successfull');
            console.log(res.data.status)
            if (res.data.status === "duplicate") {
              this.opinionExist = true;
            }
            else {
              this.show = false;
              this.grettings = true;
            }
          })
          .catch((error) => {
            console.log('errors', error)
            this.form.error = true;
          })
      }
    }
  }
</script>

<style scoped>

</style>
