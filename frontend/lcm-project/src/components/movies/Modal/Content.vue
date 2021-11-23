<template>
  <div class="Content">
    <div class="movie-info">
      <img :src="currentMovie.poster_path" alt="poster" />
      <div class="info">
        <h2 class="title">{{ currentMovie.title }}</h2>
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

          <button @click="addList" class="add-list">+</button>

          <!-- {{ currentMovie }} -->
          <!-- <button @click="addList" class="remove-list none">-</button> -->
        </div>
      </div>
    </div>
    <div>
      <h4 class="overview">Overview</h4>
      <p>{{ currentMovie.overview }}</p>
    </div>
  </div>
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
    };
  },
  computed: {
    ...mapGetters(["currentMovie"]),
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
