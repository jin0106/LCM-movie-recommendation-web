<template>
  <div id="Main">
    <header>
      <div>
        <movie-random />
        <MovieWeather />
        <user-recommend />
        <genre-1 />
        <genre-2 />
        <genre-3 />
        <genre-4 />
      </div>
    </header>
  </div>
</template>

<script>
import MovieWeather from "@/components/movies/MovieWeather.vue";
import UserRecommend from "@/components/movies/UserRecommend.vue";
import Genre1 from "@/components/movies/Main-row/Genre1.vue";
import Genre2 from "../../components/movies/Main-row/Genre2.vue";
import Genre4 from "../../components/movies/Main-row/Genre4.vue";
import Genre3 from "../../components/movies/Main-row/Genre3.vue";
import MovieRandom from "../../components/movies/MovieRandom.vue";

// import MoviesRecommend from "@/components/movies/MoviesRecommend.vue";

export default {
  name: "Main",
  components: {
    MovieRandom,
    MovieWeather,
    UserRecommend,
    Genre1,
    Genre2,
    Genre4,
    Genre3,
  },
};
</script>

<style>
#Main {
  padding: 0 3rem;
  margin-top: 5rem;
}
</style>