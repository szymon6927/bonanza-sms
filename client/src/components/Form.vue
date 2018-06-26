<template>
  <form id="app" @submit.prevent="checkForm" method="post">

    <p>
      <label for="name">Name</label>
      <input type="text" name="name" id="name" v-model="name">
    </p>

    <p>
      <input type="submit" value="Submit">
    </p>

  </form>
</template>

<script>
export default {
  name: 'Form',
  data() {
    return {
      name: '',
    };
  },
  methods: {
    checkForm: function () {
      if (this.name === '') {
        console.log('empty')
      }
      else {
        console.log(this.name)
      }
    },
    test: function () {
      console.log('test function')
    }
  },
  created() {
    this.test()
  }
}
</script>

<style scoped>

</style>
