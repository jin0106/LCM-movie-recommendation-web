<template>
  <div id="home">
    <video
      src=""
      poster="https://i.ytimg.com/vi/PWK8EuUSMSI/hq720.jpg?sqp=-oaymwEcCOgCEMoBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLAjU_qRq1tTQGSQj-TcFvsU3tmXWA"
      autoplay
    ></video>
    <Main />
  </div>
</template>

<script>
import Main from "../movies/Main.vue";
export default {
  name: "home",
  components: { Main },
};
</script>

<style>
#home {
  width: 100%;
}
video {
  margin-top: 5rem;
  padding: 0 3rem;
  width: 100%;
}
</style>