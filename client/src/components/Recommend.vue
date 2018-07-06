<template>
  <v-container class="mb-5" text-xs-center>
    <v-layout row wrap>
      <v-flex xs12 sm10 md10 lg8 offset-xs0 offset-sm1 offset-md1 offset-lg2>
        <div class="content__wraper elevation-10 text-xs-center pt-5 pb-5">
          <h1 class="black--text mb-3">Zobacz co dzisiaj poleca szef kuchni!</h1>
          <v-divider></v-divider>
          <v-spacer></v-spacer>
          <div v-if="content" class="recommend__content pt-4" v-html="content ">
            {{ content }}
          </div>
          <div v-else class="recommend__content">
            <p>Zapraszamy na pyszne jedzonko!</p>
          </div>
          <!--<img class="recommend img__responsive elevation-10" src="/static/recommended/recommend1.jpg" />-->
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
