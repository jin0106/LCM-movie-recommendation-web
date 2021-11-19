<template>
  <div id="Movies">
    <header>
      <MovieList/>
    </header>
  </div>
</template>

<script>
import MovieList from "@/components/movies/MovieList.vue"

export default {
  name: "Movies",
  components: {
    MovieList,
  }
}
</script>

<style>

</style>