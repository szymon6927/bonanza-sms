<template>
  <v-container class="mb-5" text-xs-center>
    <v-layout row wrap>
      <v-flex xs12 sm10 md10 lg8 offset-xs0 offset-sm1 offset-md1 offset-lg2>
        <div class="content__wraper elevation-10 grettings text-xs-center">
          <h1 class="mb-4">Opis "Szef kuchni poleca"</h1>
          <div id="editorContainer"></div>
          <v-btn round primary @click="saveContent">Zapis</v-btn>
        </div>

        <v-snackbar :timeout="5000" :top="'top'" color="red" v-model="error">
          Coś poszło nie tak, spróbuj ponownie.
          <v-btn dark flat @click.native="error = false">Zamknij</v-btn>
        </v-snackbar>

        <v-snackbar :timeout="5000" :top="'top'" color="success" v-model="success">
          Zapisano pomyślnie
          <v-btn dark flat @click.native="success = false">Zamknij</v-btn>
        </v-snackbar>

      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
  import axios from 'axios'
  import { createEditor } from 'vueditor'
  import 'vueditor/dist/style/vueditor.min.css'

  export default {
    name: "ChefDescription",
    data() {
      return {
        inst: null,
        content: '',
        error: false,
        success: false
      }
    },
    mounted() {
      this.inst = createEditor('#editorContainer', {
        toolbar: [
          'removeFormat', 'undo', '|', 'elements', 'fontName', 'fontSize', 'foreColor', 'backColor', 'divider',
          'bold', 'italic', 'underline', 'strikeThrough', 'links', 'divider', 'subscript', 'superscript',
          'divider', 'justifyLeft', 'justifyCenter', 'justifyRight', 'justifyFull', '|', 'indent', 'outdent',
          'insertOrderedList', 'insertUnorderedList', '|', 'picture', 'tables', '|', 'switchView', 'sourceCode'
        ],
        fontName: [
          {val: 'Catamaran'},
          {val: 'arial black'},
          {val: 'times new roman'},
          {val: 'Courier New'}
        ],
        fontSize: [
          '12px', '14px', '16px', '18px', '20px', '24px', '28px', '32px', '36px'
        ],
        uploadUrl: '',
        id: '',
        classList: []
      });

      this.getContent()
    },
    methods: {
      getEditorContnet: function () {
        return this.inst.getContent();
      },

      getContent() {
        const path = '/api/get-chef-desc';
        axios.get(path)
          .then((res) => {
            this.content = res.data;
            this.inst.setContent(this.content);
          })
          .catch((error) => {
            this.error = true;
          });
      },

      saveContent() {
        const path = '/api/set-chef-desc';
        const payload = {
          'chef_desc': this.getEditorContnet(),
        };
        axios.post(path, payload)
          .then((data) => {
            console.log('successfull');
            console.log(data.data.status)
            this.success = true
          })
          .catch((error) => {
            console.log('errors', error)
            this.error = true;
          })
      }
    }
  }
</script>

<style scoped>

</style>
