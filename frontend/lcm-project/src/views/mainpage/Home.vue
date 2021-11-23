<template>
  <div id="home">
    <div v-if="currentUser">
      <video
        src=""
        poster="https://i.ytimg.com/vi/PWK8EuUSMSI/hq720.jpg?sqp=-oaymwEcCOgCEMoBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLAjU_qRq1tTQGSQj-TcFvsU3tmXWA"
        autoplay
      ></video>
      <Main />
    </div>
    <div v-else>
      <movie-guest />
    </div>
  </div>
</template>

<script>
import Main from "../movies/Main.vue";
import MovieGuest from "../../components/movies/MovieGuest.vue";
export default {
  name: "home",
  components: { Main, MovieGuest },
  data: function () {
    return {
      currentUser: this.$store.state.getUserName,
    };
  },
};
</script>

<style>
#home {
  width: 100%;
  background-color: black;
}
video {
  margin-top: 5rem;
  padding: 0 3rem;
  width: 100%;
}
</style>