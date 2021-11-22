<template>
  <div class="navbar">
    <div class="overlay">
      <div class="header">
        <div>
          <router-link class="logo" :to="{ name: 'Home' }">LCM</router-link>
        </div>
        <div v-if="currentUser" class="nav">
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
        <div class="menu" v-if="!currentUser">
          <router-link class="menu-item" :to="{ name: 'Signup' }"
            >Signup</router-link
          >
          <router-link class="menu-item" :to="{ name: 'Login' }"
            >Login</router-link
          >
        </div>
        <div class="menu" v-else>
          <router-link class="serach" to="#"
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
              src="./search.png"
              alt="search"
            />
          </router-link>
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
const SERVER_URL = process.env.VUE_APP_SERVER_URL;
import axios from "axios";
import { mapGetters } from "vuex";

export default {
  name: "navbar",
  data: function () {
    return {
      isLogin: false,
      isSearch: false,
      content: "",
      userName: this.$store.state.getUserName,
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
  created: function () {
    if (localStorage.getItem("JWT")) {
      this.isLogin = true;
    } else {
      this.$router.push({ name: "Login" }).catch(() => {});
    }
  },
  computed: {
    ...mapGetters(["currentUser"]),
  },
};
</script>
  
<style scoped src="./css/navbar.css">
</style>


