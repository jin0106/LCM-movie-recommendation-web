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
      // direction이 true면 오름차순 false면 내림차순
      const data1 = {
        token : this.$store.state.token,
        genre : 'Adventure',
        orderby : 'random',
        direction : true,
      }
      this.$store.dispatch("GenreMovies", data1);
    },
    createMovieReview: function (data) {
      this.$store.dispatch("getMovieInfo", data);
    },
  },
  computed: {
    ...mapGetters([""]),
  },

  created: function () {
    this.GenreMovies();
  },
};
</script>

<style scoped src='./css/movielist.css'>
/* 전체 글자 색깔 마진 없애주기 */
</style>