<template>
  <div id="MoviesRecommend">
    <button @click="getRecommendMovieList">check</button>
  </div>
</template>

<script>
import axios from "axios";
const SERVER_URL = process.env.VUE_APP_SERVER_URL;
export default {
  name: "MoviesRecommend",
  methods: {
    setHeader: function () {
      const token = localStorage.getItem("JWT");
      const header = {
        Authorization: `Bearer ${token}`,
      };
      return header;
    },

    getRecommendMovieList: function () {
      axios({
        method: "GET",
        url: `${SERVER_URL}movies/user_recommend/`,
        headers: this.setHeader(),
      })
        .then((res) => {
          a = res;
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
};
</script>

<style scoped src='./css/movielist.css'>
</style>