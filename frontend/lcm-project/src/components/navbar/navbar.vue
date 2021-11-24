<template>
  <div class="navbar">
    <div class="overlay">
      <div class="header">
        <div>
          <router-link class="logo" :to="{ name: 'Home' }">LCM</router-link>
        </div>
        <div v-if="this.isLogin" class="nav">
          <router-link class="nav-item" :to="{ name: 'Home' }"
            >Home</router-link
          >
          <router-link class="nav-item" :to="{ name: 'Movies' }"
            >Movies</router-link
          >
          <router-link class="nav-item" :to="{ name: 'Community' }"
            >Community</router-link
          >
          <router-link class="nav-item my-list" :to="{ name: 'MovieMyList' }"
            >My List</router-link
          >
          <router-link
            class="nav-item watched-list"
            :to="{ name: 'MovieWatchedList' }"
            >WatchedList</router-link
          >
        </div>
        <div class="menu" v-if="!this.isLogin">
          <router-link class="menu-item" :to="{ name: 'Signup' }"
            >Signup</router-link
          >
          <router-link class="menu-item" :to="{ name: 'Login' }"
            >Login</router-link
          >
        </div>
        <div class="menu" v-else>
          <router-link class="search" to="#"
            ><input
              class="search-bar hidden"
              type="text"
              placeholder="type movie title"
              v-model="content"
              @keyup.enter="search"
            />
            <img
              @click="show"
              class="magnifying"
              src="./glass.png"
              alt="search"
            />
          </router-link>
          <router-link class="menu-item" to="#" @click.native="Logout"
            >Logout</router-link
          >
          <router-link class="menu-item profile" :to="{ name: 'Profile' }"
            >Profile</router-link
          >
        </div>
      </div>
    </div>
    <router-view @login="setLogin" />
  </div>
</template>

<script>
const SERVER_URL = process.env.VUE_APP_SERVER_URL;
import axios from "axios";
import { mapGetters } from "vuex";

export default {
  name: "navbar",
  data: function () {
    return {
      isSearch: false,
      content: "",
      userName: this.$store.state.getUserName,
      isLogin: localStorage.getItem("JWT"),
    };
  },
  methods: {
    show() {
      const input = document.querySelector(".search-bar");
      input.classList.toggle("hidden");
      input.placeholder = "type movie title";
      this.content = "";
    },
    setLogin: function () {
      this.isLogin = true;
    },
    Logout: function () {
      localStorage.removeItem("JWT");
      this.isLogin = false;
      this.$store.state.getUserName = "";
      this.$router.push({ name: "Login" });
    },
    search() {
      if (this.content) {
        axios({
          method: "GET",
          url: `${SERVER_URL}movies/movie_search/`,
          headers: this.$store.state.token,
          params: {
            search_string: this.content,
          },
        })
          .then((res) => {
            this.content = "";
            const input = document.querySelector(".search-bar");
            input.blur();
            input.classList.add("hidden");
            this.$store.dispatch("searchMovies", res.data);
            this.$router.push({ name: "MovieSearchResult" });
          })
          .catch((err) => {
            console.log(err);
          });
      } else {
        alert("검색어를 입력하세요");
      }
    },
  },
  computed: {
    ...mapGetters(["currentUser"]),
  },
};
</script>
  
<style scoped src="./css/navbar.css">
</style>


