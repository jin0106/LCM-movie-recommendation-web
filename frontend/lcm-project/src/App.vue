<template>
  <div id="app">
    <navbar />
  </div>
</template>
<script>
import Navbar from "./components/navbar/navbar.vue";

export default {
  components: { Navbar },
  name: "App",
  data: function () {
    return {
      isLogin: localStorage.getItem("JWT"),
    };
  },
  methods: {
    backGround() {
      const nav = document.querySelector(".overlay");
      console.log("test");
      if (window.scrollY >= 50) {
        nav.classList.add("back-ground");
      } else {
        nav.classList.remove("back-ground");
      }
    },
    setLogin: function () {
      this.isLogin = true;
    },
    Logout: function () {
      localStorage.removeItem("JWT");
      this.isLogin = false;
    },
  },
  mounted() {
    this.$store.dispatch("mainMovie");
    this.$router.push({ name: "Login" });
  },
};
</script>


<style>
#app {
  display: flex;
  height: 100vh;

  flex-direction: column;
}
</style>
