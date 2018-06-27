<template>
  <v-container grid-list-md text-xs-center>
    <v-layout row wrap>
      <v-flex xs12>
        <v-form class="form-wrapper mx-auto mt-5" ref="form" lazy-validation v-if="show">
          <h1>BAR BONANZA PROMOCJE!</h1>
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
            color="brown darken-3"
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
            color="brown darken-3"
            value="marketing-policy"
            label="Wyrażam zgodę na otrzymywanie informacji handlowej za pomocą środków komunikacji
            elektronicznej, zgodnie z Ustawą o świadczeniu usług drogą elektroniczną."
            required
          ></v-checkbox>
          <v-btn class="mb-3" round block color="light" @click="onReset">Wyczyść</v-btn>
          <v-btn round block color="primary white--text" @click="onSubmit">Wyślij</v-btn>
        </v-form>
        <v-snackbar
          :timeout="5000"
          :top="'top'"
          color="red"
          v-model="form.snackbar"
        >Proszę zaakcpetować polityki prywatności
        <v-btn dark flat @click.native="form.snackbar = false">Zamknij</v-btn>
        </v-snackbar>
      </v-flex>
    </v-layout>
    <v-layout row wrap v-if="grettings">
      <h1>Dziękujemy za rejestrację i życzymy udanego wypoczynku</h1>
      <v-btn color="success" to="/">Home</v-btn>
    </v-layout>
  </v-container>
</template>

<script>
export default {
  name: 'Form',
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
        snackbar: false
      },
      show: true,
      grettings: false
    }
  },
  methods: {
    onSubmit: function () {
      if (this.$refs.form.validate()) {
        console.log("submit")
        console.log(this.form.name, this.form.phone, this.form.selected)
        console.log(this.form.selected.length)
        if (this.form.selected.length < 2) {
          this.form.snackbar = true;
        }
        else {
          this.show = false
          this.grettings = true
        }

      }
    },
    onReset: function() {
      this.$refs.form.reset()
    }
  }
}
</script>

<style scoped>

</style>
