<template>
  <div id="Genre3">
    <div class="contents">
      <p class="title">How about {{ getgenre }} movies?</p>
      <div class="posters" v-if="genreMovies">
        <div
          class="div-img"
          v-for="(movie, idx) in genreMovies[getgenre]"
          :key="idx"
        >
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
  name: "Genre3",
  data: function () {
    return {
      movieList: [],
      getgenre: "",
    };
  },
  methods: {
    GenreMovies: function () {
      // direction이 true면 오름차순 false면 내림차순
      const data1 = {
        token: this.$store.state.token,
        genre: "Crime",
        orderby: "random",
        direction: true,
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