<template>
  <v-container class="mb-5" text-xs-center>
    <v-layout row wrap>
      <v-flex xs12 sm10 md10 lg8 offset-xs0 offset-sm1 offset-md1 offset-lg2>
        <div class="content__wraper elevation-10 text-xs-center pt-5 pb-5">
          <h1 class="black--text mb-3">Zobacz co dzisiaj poleca szef kuchni!</h1>
          <v-divider></v-divider>
          <v-spacer></v-spacer>
          <v-layout row wrap class="pt-4 elevation-10 pb-3 mt-4">
          <v-flex sm3 xs12>
            <img class="recommend__img img__responsive" src="/static/chef.png" />
          </v-flex>
          <v-flex sm9 xs12>
            <div v-if="content" class="recommend__content" v-html="content ">
              {{ content }}
            </div>
            <div v-else class="recommend__content">
              <p><strong>Zapraszamy na pyszne jedzonko!</strong></p>
              <p class="mb-0 font-weight-bold">Bar Bonanza</p>
              <p class="mb-0">ul. Kościuszki 34</p>
              <p class="mb-0">84-360, Łeba</p>
              <p class="mb-4"><a href="tel:+48514570945">514 570 945</a></p>
            </div>
          </v-flex>
          </v-layout>
          <v-btn round large block color="light-blue darken-4 white--text mt-4" href="https://goo.gl/maps/L9mCSVHPvW92">
            <span class="pr-3">Odwiedź nas</span>
            <v-icon style="font-size: 18px;">fas fa-thumbs-up</v-icon>
          </v-btn>
        </div>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
  import axios from 'axios'
  export default {
    name: "Recommend",
    data() {
      return {
        content: ''
      }
    },
    created() {
      this.getContent()
    },
    methods: {
      getContent() {
        const path = '/api/get-chef-desc';
        axios.get(path)
          .then((res) => {
            this.content = res.data;
          })
          .catch((error) => {
            this.error = true;
          });
      },
    }
  }
</script>

<style scoped>

</style>
