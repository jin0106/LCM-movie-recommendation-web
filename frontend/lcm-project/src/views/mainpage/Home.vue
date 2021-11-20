<template>
  <div id="home">
    <video
      src=""
      poster="https://i.ytimg.com/vi/PWK8EuUSMSI/hq720.jpg?sqp=-oaymwEcCOgCEMoBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLAjU_qRq1tTQGSQj-TcFvsU3tmXWA"
      autoplay
    ></video>
    <movies />
  </div>
</template>

<script>
import Movies from "../movies/Movies.vue";
export default {
  name: "home",
  components: { Movies },
};
</script>

<style>
video {
  padding: 0 1rem;
  width: 100%;
}
</style>