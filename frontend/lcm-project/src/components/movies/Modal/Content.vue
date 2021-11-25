<template>
  <div class="Content">
    <div class="trailer">
      <iframe
        :src="trailer.src"
        frameborder="0"
        width="500px"
        height="300px"
      ></iframe>
    </div>
    <h3 class="title">{{ currentMovie.title }}</h3>

    <div class="movie-info">
      <div class="info">
        <div class="genres">
          <span class="ge">Genres :</span>
          <span
            class="genre"
            v-for="(genre, idx) in currentMovie.genres"
            :key="idx"
          >
            {{ genre.name }}
          </span>
        </div>
        <!-- <p>{{ movies }}</p> -->
        <p>
          Rating : <span class="info-num">{{ currentMovie.vote_average }}</span>
        </p>
        <p>
          User Rating :
          <span class="info-num">{{ score }}</span>
        </p>
        <p>
          View : <span class="info-num">{{ currentMovie.popularity }}</span>
        </p>
        <p>
          Release Date :
          <span class="info-num">{{ currentMovie.release_date }}</span>
        </p>
        <div class="btn">
          <router-link class="nav-item" :to="{ name: 'ReviewForm' }">
            <button class="review-btn">Write Review</button></router-link
          >
          <button @click="watchedList" class="remove-list">Watched</button>
          <div class="my-list">
            <button @click="addList" class="add-list">+</button>
          </div>
        </div>
      </div>
      <img :src="currentMovie.poster_path" class="poster" alt="poster" />
    </div>
    <div class="overviews">
      <h4 class="overview">Overview</h4>
      <p>{{ currentMovie.overview }}</p>
    </div>
  </div>
  <!-- http://8c3d-125-134-86-234.ngrok.io/ -->
</template>

<script>
const SERVER_URL = process.env.VUE_APP_SERVER_URL;
import axios from "axios";
import { mapGetters } from "vuex";
export default {
  name: "Content",
  data: function () {
    return {
      movie: this.$store.state.movieInfo,
      movies: [],
      isToggled: false,
      video: "",
    };
  },
  computed: {
    ...mapGetters(["currentMovie", "trailer", "score"]),
  },
  methods: {
    addList() {
      axios({
        method: "post",
        url: `${SERVER_URL}movies/wish_list/`,
        headers: this.$store.state.token,
        data: this.movie,
      })
        .then((res) => {
          console.log(res);
          this.$store.dispatch("getMyList", this.$store.state.token);
          alert("You added this movie into the My List");
        })
        .catch((err) => {
          console.log(err);
        });
    },
    watchedList() {
      axios({
        method: "post",
        url: `${SERVER_URL}movies/watched_movie/`,
        headers: this.$store.state.token,
        data: this.movie,
      })
        .then((res) => {
          console.log(res);
          alert("You added this movie into the WatchedList");

          this.$store.dispatch("watchedList", this.$store.state.token);
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped src='./content.css'>
</style>
