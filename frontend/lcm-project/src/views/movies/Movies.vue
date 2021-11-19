<template>
  <div id="Movies">
    <header>
      <MovieList />
    </header>
  </div>
</template>

<script>
import MovieList from "@/components/movies/MovieList.vue";
// import MoviesRecommend from "@/components/movies/MoviesRecommend.vue";

export default {
  name: "Movies",
  components: {
    MovieList,
    // MoviesRecommend,
  },
};
</script>

<style>
</style>