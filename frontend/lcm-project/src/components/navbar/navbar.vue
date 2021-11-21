<template>
  <div class="navbar">
    <div class="overlay">
      <div class="header">
        <div>
          <router-link class="logo" :to="{ name: 'Home' }">LCM</router-link>
        </div>
        <div class="nav">
          <router-link class="nav-item" :to="{ name: 'Home' }"
            >Home</router-link
          >
          <router-link class="nav-item" :to="{ name: 'Movies' }"
            >Movies</router-link
          >
          <router-link class="nav-item" :to="{ name: 'Community' }"
            >Community</router-link
          >
          <div class="nav-item">My List</div>
        </div>
        <div class="menu" v-if="!isLogin">
          <router-link class="menu-item" :to="{ name: 'Signup' }"
            >Signup</router-link
          >
          <router-link class="menu-item" :to="{ name: 'Login' }"
            >Login</router-link
          >
        </div>
        <div class="menu" v-else>
          <router-link class="menu-item" to="#" @click.native="Logout"
            >Logout</router-link
          >
          <router-link class="menu-item" :to="{ name: 'Profile' }"
            >Profile</router-link
          >
        </div>
      </div>
    </div>
    <router-view @login="setLogin" />
  </div>
</template>

<script>
export default {
  name: "navbar",
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
      this.$router.push({ name: "Home" });
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
  
<style scoped src="./css/navbar.css">
</style>


