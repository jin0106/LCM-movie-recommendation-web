<template>
  <div>
    <div class="contents">
      <p class="title">Based on your profile</p>
      <div class="posters" v-if="userMovies">
        <div class="div-img" v-for="(movie, idx) in userMovies" :key="idx">
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
  name: "UserRecommend",
  data: function () {
    return {
      genres: [],
    };
  },
  created() {
    this.$store.dispatch("getUserMovies", this.$store.state.token);
  },
  computed: {
    ...mapGetters(["userMovies"]),
  },
};
</script>

<style scoped src='./css/movielist.css'>
</style>