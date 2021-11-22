<template>
  <div id="MovieWeather">
    <div class="contents">
      <p class="title">Based on the Weahter in your city</p>
      <div class="posters" v-if="WeatherMovies.length">
        <div class="div-img" v-for="(movie, idx) in WeatherMovies" :key="idx">
          <img @click="watchedMovie(movie)" class="poster" :src="movie.poster_path" alt="thumnail" />
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
import axios from 'axios';
import { mapGetters } from "vuex";
const SERVER_URL = process.env.VUE_APP_SERVER_URL

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

    //POST요청일 때는 function(movie)로 바꿔주시고
    //method 바꾸신 후 data주석처리 해제하면 작동됩니다
    watchedMovie: function(movie) {
      axios({
        method: "POST",
        url : `${SERVER_URL}movies/watched_movie/`,
        headers: this.$store.state.token,
        data : movie
      })
      .then(res => {
        console.log(res)
      })
      .catch(err => {
        console.log(err)
      })
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

<style scoped src='./css/movielist.css'>
/* 전체 글자 색깔 마진 없애주기 */
</style>