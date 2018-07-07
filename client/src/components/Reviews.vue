<template>
  <v-container class="mb-5" text-xs-center>
    <v-layout row wrap>
      <v-flex xs12 sm10 md10 lg8 offset-xs0 offset-sm1 offset-md1 offset-lg2>
        <div class="content__wraper elevation-10 grettings text-xs-center">
          <h1 class="mb-4">Nasze opinie</h1>
          <template v-for="opinion in reviews">
            <v-card class="mb-4 elevation-5">
              <v-card-title primary-title>
                <v-icon class="pr-2">fas fa-user-circle</v-icon>
                <div class="card__title">
                  <div class="client-name">{{ opinion.name }}</div>
                  <div class="opinion-date">({{ opinion.created_at | formatDate }})</div>
                </div>
                <v-btn v-if="opinion.rating" absolute right align-content-center color="transparent" class="elevation-2">
                  <star-rating
                  :show-rating="false"
                  :star-size="20"
                  :rating="opinion.rating"
                  :read-only="true"></star-rating>
                </v-btn>
              </v-card-title>
              <div class="card__content">
                <p>{{ opinion.opinion }}</p>
              </div>
            </v-card>
          </template>
          <v-btn round block color="light-blue darken-4 white--text" to="/add-opinion">Dodaj swoją opinię</v-btn>
        </div>

        <v-snackbar :timeout="5000" :top="'top'" color="red" v-model="error">
          Coś poszło nie tak, spróbuj ponownie.
          <v-btn dark flat @click.native="error = false">Zamknij</v-btn>
        </v-snackbar>

      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
  import axios from 'axios'
  import StarRating from 'vue-star-rating'

  export default {
    name: "Reviews",
    components: {
      StarRating
    },
    data() {
      return {
        reviews: [],
        error: false
      };
    },
    methods: {
      getReviews() {
        const path = '/api/reviews';
        axios.get(path)
          .then((res) => {
            this.reviews = res.data;
          })
          .catch((error) => {
            console.error(error);
            this.error = true;
          });
      },
    },
    created() {
      this.getReviews();
    },
  }
</script>

<style scoped>
  .opinion-date {
    font-size: 11px;
  }
  .card__title {
    line-height: 16px;
  }
</style>
