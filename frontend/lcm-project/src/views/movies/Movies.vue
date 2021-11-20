<template>
  <div id="Movies">
    <header>
      <div>
        <MovieList />
        <MovieWeather />
        <user-recommend />
        <MovieGenre />
      </div>
    </header>
  </div>
</template>

<script>
import MovieList from "@/components/movies/MovieList.vue";
import MovieWeather from "@/components/movies/MovieWeather.vue";
import UserRecommend from "@/components/movies/UserRecommend.vue";
import MovieGenre from "@/components/movies/MovieGenre.vue";
// import MoviesRecommend from "@/components/movies/MoviesRecommend.vue";

export default {
  name: "Movies",
  components: {
    MovieList,
    MovieWeather,
    UserRecommend,
    MovieGenre,
    // MoviesRecommend,
  },
};
</script>

<style>
</style>