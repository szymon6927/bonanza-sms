<template>
  <v-container class="mb-5" text-xs-center>
    <v-layout row wrap>
      <v-flex xs12 sm10 md10 lg8 offset-xs0 offset-sm1 offset-md1 offset-lg2>
        <div class="content__wraper grettings elevation-10 text-xs-center">
          <h1 class="mb-4">O nas</h1>
          <p class="mb-4">Zapisz się, aby otrzymywać powiadomienia <strong>SMS</strong> dzięki
            którym możesz uzyskać rabaty na wybrane produktu Baru Bonanza.
          </p>
          <v-carousel class="mb-3" hide-delimiters>
            <v-carousel-item
              v-for="(item,i) in items"
              :key="i"
              :src="item.src"
            ></v-carousel-item>
          </v-carousel>
          <p>
            Bądź zawsze na bieżąco, przyjdź i pokaż SMS aby otrzymać <strong>rabat</strong>
          </p>
          <v-spacer></v-spacer>
          <v-btn round large block color="light-blue darken-4 white--text mb-3" to="/reviews">Zobacz opinie</v-btn>
          <v-btn round large block color="success white--text" to="/add-opinion">Dodaj opinie</v-btn>
          <v-spacer></v-spacer>
          <h2 class="pt-2">Lokalizacja</h2>
          <p class="mb-0 font-weight-bold">Bar Bonanza</p>
          <p class="mb-0">ul. Kościuszki 34</p>
          <p class="mb-0">84-360, Łeba</p>
          <p class="mb-4"><a href="tel:+48514570945">514 570 945</a></p>
          <iframe
            src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2302.1720267984933!2d17.55282521603119!3d54.75936207563372!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x46fe78327ea6129d%3A0x2b0b8c5d6693f135!2sBar+Bonanza%3A+pizzeria%2C+sma%C5%BCalnia%2C+obiady+domowe!5e0!3m2!1spl!2spl!4v1530310561508"
            width="100%" height="350" frameborder="0" style="border:0" allowfullscreen></iframe>
          <h2 class="pt-3">Autor:</h2>
          <h4><a href="https://www.szymonmiks.pl/">Szymon Miks - aplikacje i strony internetowe</a></h4>
        </div>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
  export default {
    name: "About",
    data() {
      return {
        items: [
          {
            src: '/static/carousel/bonanza3.jpg'
          },
          {
            src: '/static/carousel/bonanza2.jpg'
          },
          {
            src: '/static/carousel/bonanza1.jpg'
          }
        ]
      }
    }
  }
</script>

<style scoped>
  a {
    text-decoration: none;
    font-weight: bold;
    color: #000;
  }

  a:hover {
    color: #4e342e;
  }
</style>
