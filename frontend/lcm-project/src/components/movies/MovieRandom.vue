<template>
  <div id="MovieRandom">
    <div class="contents">
      <p class="title">How about this movies?</p>
      <div class="posters" v-if="totalMovieList.length">
        <div class="div-img" v-for="(movie, idx) in totalMovieList" :key="idx">
          <img
            @click="createMovieReview(movie)"
            class="poster"
            :src="movie.poster_path"
            alt="thumnail"
          />
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
  name: "MovieRandom",
  data: function () {
    return {
      movieList: [],
    };
  },
  methods: {
    getMovieList: function () {
      this.$store.dispatch("getMovieList", this.$store.state.token);
    },
    createMovieReview: function (data) {
      this.$store.dispatch("getMovieInfo", data);
      //this.$router.push({ name: "Community" });
    },
  },
  computed: {
    ...mapGetters(["totalMovieList"]),
  },

  created: function () {
    this.getMovieList();
  },
};
</script>

<style scoped src='./css/movielist.css'>
/* 전체 글자 색깔 마진 없애주기 */
</style>