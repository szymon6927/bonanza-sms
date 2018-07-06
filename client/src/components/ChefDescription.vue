<template>
  <v-container class="mb-5" text-xs-center>
    <v-layout row wrap>
      <v-flex xs12 sm10 md10 lg8 offset-xs0 offset-sm1 offset-md1 offset-lg2>
        <div class="content__wraper elevation-10 grettings text-xs-center">
          <h1 class="mb-4">Opis "Szef kuchni poleca"</h1>
          <div id="editorContainer"></div>
          <v-btn @click="getContnet">get content</v-btn>
        </div>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
  import {createEditor} from 'vueditor'
  import 'vueditor/dist/style/vueditor.min.css'

  export default {
    name: "ChefDescription",
    data() {
      return {
        inst: null
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
          {val: 'arial black'},
          {val: 'times new roman'},
          {val: 'Courier New'},
          {val: 'Catamaran'}
        ],
        fontSize: [
          '12px', '14px', '16px', '18px', '20px', '24px', '28px', '32px', '36px'
        ],
        uploadUrl: '',
        id: '',
        classList: []
      });
    },
    methods: {
      getContnet: function () {
        return this.inst.getContent();
      }
    }
  }
</script>

<style scoped>

</style>
