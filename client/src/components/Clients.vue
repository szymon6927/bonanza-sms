<template>
  <v-container class="mb-5" text-xs-center>
    <v-layout row wrap>
      <v-flex xs12 sm10 md10 lg8 offset-xs0 offset-sm1 offset-md1 offset-lg2>
        <div class="content__wraper elevation-10 grettings text-xs-center">
          <h2 class="mb-4">Wszyscy zarejestrowani</h2>
          <v-data-table
            :headers="headers"
            :items="clients"
            hide-actions
            class="elevation-10"
          >
            <template slot="items" slot-scope="props">
              <td class="text-xs-center">{{ props.item.name }}</td>
              <td class="text-xs-center">{{ props.item.phone }}</td>
            </template>
          </v-data-table>
        </div>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
  import axios from 'axios'

  export default {
    name: "Clients",
    data() {
      return {
        headers: [
          {text: 'Imię', value: 'name'},
          {text: 'Telefon', value: 'phone'}
        ],
        clients: []
      }
    },
    methods: {
      getClients: function () {
        const path = '/api/clients'
        axios.get(path)
          .then((res) => {
            this.clients = res.data
          })
          .catch((error) => {
            console.log("error", error)
          })
      }
    },
    created() {
      console.log("created")
      this.getClients()
    }
  }
</script>

<style scoped>

</style>
