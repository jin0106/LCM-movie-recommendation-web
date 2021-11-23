<template>
  <div id="MovieGuest">
    <img
      v-for="movie in movies"
      :key="movie.id"
      :src="movie.poster_path"
      alt=""
    />
  </div>
</template>

<script>
import axios from "axios";
const SERVER_URL = process.env.VUE_APP_SERVER_URL;

export default {
  name: "MovieGuest",
  data: function () {
    return {
      movies: [],
    };
  },
  methods: {
    getMovieList: function () {
      axios({
        method: "GET",
        url: `${SERVER_URL}movies/`,
      })
        .then((res) => {
          console.log("tttt");
          this.movies = res.data;
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
  created: function () {
    this.getMovieList();
  },
};
</script>

<style>
#MovieGuest {
  /* max-width: 100%; */
  margin-top: 3rem;
  display: flex;
  flex-wrap: wrap;
  padding: 0 3rem;
  height: 100vh;
  justify-content: center;
}
img {
  width: 220px;
  /* width: 100%; */
  max-height: 300px;
}
</style>