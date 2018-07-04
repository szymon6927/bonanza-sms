<template>

</template>

<script>
  export default {
    name: "Reviews",
    data() {
      return {
        books: [],
      };
    },
    methods: {
      getReviews() {
        const path = '/api';
        axios.get(path)
          .then((res) => {
            this.books = res.data.books;
          })
          .catch((error) => {
            console.error(error);
          });
      },
    },
    created() {
      this.getReviews();
    },
  }
</script>

<style scoped>

</style>
