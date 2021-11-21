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
      isLogin: false,
    };
  },
  methods: {
    setLogin: function () {
      this.isLogin = true;
    },
    Logout: function () {
      localStorage.removeItem("JWT");
      this.isLogin = false;
    },
  },
  created: function () {
    if (localStorage.getItem("JWT")) {
      this.isLogin = true;
    } else {
      this.$router.push({ name: "Login" }).catch(() => {});
    }
  },
};
</script>


<style>
#app {
  display: flex;
  flex-direction: column;
}

body {
  height: 100vh;
}
/* #app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
} */
</style>
