<template>
  <div class="hidden-xs-only">
    <v-navigation-drawer v-model="drawer" fixed temporary app>
      <v-list class="pa-1">
        <v-list-tile avatar>
          <v-list-tile-avatar>
            <img src="/static/western.png">
          </v-list-tile-avatar>

          <v-list-tile-content>
            <v-list-tile-title>Bar Bonanza</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>
      </v-list>

      <v-list class="pt-0" dense>

        <v-divider></v-divider>

        <template v-for="item in items">
          <v-list-tile :to="item.href">
            <v-list-tile-action>
              <v-icon>{{ item.icon }}</v-icon>
            </v-list-tile-action>
            <v-list-tile-content>
              <v-list-tile-title>{{ item.title }}</v-list-tile-title>
            </v-list-tile-content>
          </v-list-tile>
        </template>

        <v-divider></v-divider>

        <v-list-tile avatar v-if="isAuthenticated">
          <v-list-tile-avatar>
            <img src="/static/western.png">
          </v-list-tile-avatar>

          <v-list-tile-content v-if="isAuthenticated">
            <v-list-tile-title>Funkcje admina</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>


        <v-list-tile v-if="isAuthenticated" to="/clients">
          <v-list-tile-content>
            <v-list-tile-title>Zobacz zapisanych</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>

        <v-list-tile v-if="isAuthenticated" to="/chef-desc">
          <v-list-tile-content>
            <v-list-tile-title>Dodaj opis "szef kuchni poleca"</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>

      </v-list>
    </v-navigation-drawer>

    <v-toolbar dark color="brown darken-1" class="white--text elevation-10">
      <v-toolbar-side-icon @click.stop="drawer = !drawer"></v-toolbar-side-icon>
      <v-toolbar-title>Bar Bonanza</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-toolbar-items class="hidden-sm-and-down">
        <template v-for="item in items">
          <v-btn flat :to="item.href">{{ item.title }}</v-btn>
        </template>
      </v-toolbar-items>
    </v-toolbar>
  </div>
</template>

<script>
  import routes from '../router/routes'

  export default {
    name: "Topbar",
    data() {
      return {
        drawer: false,
        items: routes
      }
    },
    computed: {
      isAuthenticated() {
        return this.$store.getters.isAuthenticated
      }
    }
  }
</script>

<style scoped>

</style>
