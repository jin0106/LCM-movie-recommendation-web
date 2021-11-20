<template>
  <div id="MovieGenre">
    <h2>check</h2>
  </div>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  name: "MovieGenre",
  data: function () {
    return {
      movieList: [],
    };
  },
  methods: {
    GenreMovies: function () {
      const data1 = {
        token : this.$store.state.token,
        genre : 'Adventure'
      }
      const data2 = {
        token : this.$store.state.token,
        genre : 'Fantasy'
      }
      const data3 = {
        token : this.$store.state.token,
        genre : 'Science Fiction'
      }
      this.$store.dispatch("GenreMovies", data1);
      this.$store.dispatch("GenreMovies", data2);
      this.$store.dispatch("GenreMovies", data3);
    },
    createMovieReview: function (data) {
      this.$store.dispatch("getMovieInfo", data);
    },
  },
  computed: {
    ...mapGetters(["totalMovieList"]),
  },

  created: function () {
    this.GenreMovies();
  },
};
</script>

<style scoped src='./css/movielist.css'>
/* 전체 글자 색깔 마진 없애주기 */
</style>