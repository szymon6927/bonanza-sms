<template>
  <v-container fluid class="mb-5">
    <v-layout column align-center justify-center>
      <div class="content__wraper grettings text-xs-center">
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
          { text: 'Imię', value: 'name' },
          { text: 'Telefon', value: 'phone' }
        ],
        clients: []
      }
    },
    methods: {
      getClients: function () {
        const path = '/api/clients'
        axios.get(path)
          .then((res) => {
            console.log(res.data)
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
