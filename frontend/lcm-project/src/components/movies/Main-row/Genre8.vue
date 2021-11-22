<template>
  <div id="Genre1">
    <div class="contents">
      <p class="title">How about {{ getgenre }} movies?</p>
      <div v-if="genreMovies" class="div-img">
        <img
          @click="createMovieReview(movie)"
          v-for="(movie, idx) in genreMovies[getgenre]"
          :key="idx"
          class="poster"
          :src="movie.poster_path"
          alt="thumnail"
        />
      </div>

      <div v-else>
        <div>
          <b-spinner style="width: 3rem; height: 3rem" label=""></b-spinner>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  name: "Genre1",
  data: function () {
    return {
      movieList: [],
    };
  },
  methods: {
    GenreMovies: function () {
      // direction이 true면 오름차순 false면 내림차순
      const data1 = {
        token: this.$store.state.token,
        genre: "Thriller",
        orderby: "random",
        direction: true,
      };
      this.getgenre = data1["genre"];
      this.$store.dispatch("GenreMovies", data1);
    },
    GenreMovie: function (data) {
      // direction이 true면 오름차순 false면 내림차순
      const data1 = {
        ...data,
        genre: "Thriller",
      };
      this.getgenre = data1["genre"];
      this.$store.dispatch("GenreMovies", data1);
    },
    createMovieReview: function (data) {
      this.$store.dispatch("getMovieInfo", data);
    },
  },
  computed: {
    ...mapGetters(["genreMovies"]),
  },

  created: function () {
    this.GenreMovies();
  },
};
</script>

<style scoped src='../css/movielist.css'>
/* 전체 글자 색깔 마진 없애주기 */
</style>