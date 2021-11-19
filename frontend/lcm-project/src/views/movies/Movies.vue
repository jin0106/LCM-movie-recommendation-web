<template>
  <div id="Movies">
    <header>
      <MovieList />
      <MovieWeather />
    </header>
  </div>
</template>

<script>
import MovieList from "@/components/movies/MovieList.vue";
import MovieWeather from "@/components/movies/MovieWeather.vue";
// import MoviesRecommend from "@/components/movies/MoviesRecommend.vue";

export default {
  name: "Movies",
  components: {
    MovieList,
    MovieWeather,
    // MoviesRecommend,
  },
};
</script>

<style>
</style>