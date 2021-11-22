<template>
  <div class="Content">
    <div class="title">
      <h3>{{ currentMovie.title }}</h3>
    </div>
    <div class="movie-info">
      <img :src="currentMovie.poster_path" alt="poster" />
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
        <div class="review">
          <router-link class="nav-item" :to="{ name: 'ReviewForm' }"
            ><button>Write Review</button></router-link
          >
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
import { mapGetters } from "vuex";
export default {
  name: "Content",
  data: function () {
    return {
      movie: this.$store.state.movieInfo,
    };
  },
  computed: {
    ...mapGetters(["currentMovie"]),
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped src='./content.css'>
</style>
