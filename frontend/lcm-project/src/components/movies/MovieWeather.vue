<template>
  <div id="MovieWeather">
    <div class="contents">
      <p class="title">Based on the weather in your city</p>
      <div v-if="WeatherMovies" class="div-img">
        <ModalView v-if="isModal" @close-modal="isModal = false">
          <Content movie="this.movie" />
        </ModalView>
        <img
          @click="createMovieReview(movie)"
          v-for="(movie, idx) in WeatherMovies"
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
import axios from "axios";
import { mapGetters } from "vuex";
import Content from "@/components/movies/Modal/Content";
import ModalView from "@/components/movies/Modal/ModalView";
const SERVER_URL = process.env.VUE_APP_SERVER_URL;

export default {
  name: "MovieWeather",
  data: function () {
    return {
      movieList: [],
      isModal: false,
      movie: null,
    };
  },
  components: {
    Content,
    ModalView,
  },
  methods: {
    getMovieList: function () {
      this.$store.dispatch("WeatherMovies", this.$store.state.token);
    },
    createMovieReview: function (data) {
      this.isModal = true;
      this.$store.dispatch("getMovieInfo", data);
    },

    //POST요청일 때는 function(movie)로 바꿔주시고
    //method 바꾸신 후 data주석처리 해제하면 작동됩니다
    watchedMovie: function (movie) {
      axios({
        method: "POST",
        url: `${SERVER_URL}movies/watched_movie/`,
        headers: this.$store.state.token,
        data: movie,
      })
        .then((res) => {
          console.log(res);
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
  computed: {
    ...mapGetters(["WeatherMovies", "genreMovies"]),
  },

  created: function () {
    this.getMovieList();
  },
};
</script>

<style scoped src='./css/movielist.css'>
/* 전체 글자 색깔 마진 없애주기 */
</style>