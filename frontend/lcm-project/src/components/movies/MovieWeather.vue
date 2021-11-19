<template>
  <div id="MovieWeather">
    <div class="contents">
      <p class="title">Based on the Weahter in your city</p>
      <div class="posters" v-if="WeatherMovies.length">
        <div class="div-img" v-for="(movie, idx) in WeatherMovies" :key="idx">
          <img class="poster" :src="movie.poster_path" alt="thumnail" />
        </div>
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
  name: "MovieWeather",
  data: function () {
    return {
      movieList: [],
    };
  },
  methods: {
    getMovieList: function () {
      this.$store.dispatch("WeatherMovies", this.$store.state.token);
    },
  },
  computed: {
    ...mapGetters(["WeatherMovies"]),
  },

  created: function () {
    this.getMovieList();
  },
};
</script>

<style>
/* 전체 글자 색깔 마진 없애주기 */
@import "css/movielist.css";
</style>