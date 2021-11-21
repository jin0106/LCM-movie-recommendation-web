<template>
  <div id="MovieSearchResult">
    <div class="contents">
      <div class="posters" v-if="SearchResultMovies.length">
        <div
          class="div-img"
          v-for="(movie, idx) in SearchResultMovies"
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
        <h2 class="fail">검색결과가 없습니다.</h2>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
export default {
  name: "MovieSearchResult",
  computed: {
    ...mapGetters(["SearchResultMovies"]),
  },
};
</script>

<style scoped src='./css/movieSearch.css'>
/* 전체 글자 색깔 마진 없애주기 */
</style>