<template>
  <v-container fluid class="mb-5">
    <v-layout column align-center justify-center>
      <v-form class="form-wrapper elevation-10" ref="form" lazy-validation v-if="show">
        <img class="logo" src="/static/western.png">
        <h2>Łap rabaty, zapisz się już dziś!</h2>
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
        <v-checkbox
          class="form-checkbox"
          v-model="form.selected"
          color="primary"
          value="rodo-policy"
          hide-details
          required
        >
          <template slot="label">
            Wyrażam zgodę na przetwarzanie moich danych osobowych w celu obsługi
            zapytania i realizacji usług. Przeczytałem.
            <router-link tag="a" to="/private-policy">
              <a>politykę prywatności</a>
            </router-link>
          </template>
        </v-checkbox>
        <v-checkbox
          class="form-checkbox"
          v-model="form.selected"
          color="primary"
          value="marketing-policy"
          label="Wyrażam zgodę na otrzymywanie informacji handlowej za pomocą środków komunikacji
          elektronicznej, zgodnie z Ustawą o świadczeniu usług drogą elektroniczną."
          required
        ></v-checkbox>
        <v-btn class="mb-3" round block color="light" @click="onReset">Wyczyść</v-btn>
        <v-btn round block color="light-blue darken-4 white--text" @click="onSubmit">Wyślij</v-btn>
      </v-form>

      <v-snackbar :timeout="5000" :top="'top'" color="red" v-model="form.snackbar">
        Proszę zaakcpetować polityki prywatności
        <v-btn dark flat @click.native="form.snackbar = false">Zamknij</v-btn>
      </v-snackbar>

      <v-snackbar :timeout="5000" :top="'top'" color="red" v-model="form.error">
        Coś poszło nie tak, spróbuj ponownie
        <v-btn dark flat @click.native="form.error = false">Zamknij</v-btn>
      </v-snackbar>

    </v-layout>
    <v-layout column align-center justify-center v-if="grettings">
      <Greetings></Greetings>
    </v-layout>
  </v-container>
</template>

<script>
  import Greetings from './Greetings'
  import axios from 'axios'

  export default {
    name: 'Form',
    components: { Greetings },
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
          selected: [],
          snackbar: false,
          error: false
        },
        show: true,
        grettings: false
      }
    },
    methods: {
      onSubmit: function () {
        if (this.$refs.form.validate()) {
          if (this.form.selected.length < 2) {
            this.form.snackbar = true;
          }
          else {
            this.sendForm()
          }
        }
      },
      onReset: function() {
        this.$refs.form.reset()
      },
      sendForm: function() {
        const path = '/api/client';
        const payload = {
          'name': this.form.name,
          'phone': this.form.phone
        };
        axios.post(path, payload)
          .then((data) => {
            console.log('successfull');
            console.log(data.data.status)
            this.show = false;
            this.grettings = true;
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
