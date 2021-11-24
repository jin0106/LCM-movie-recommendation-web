<template>
  <div id="Profile">
    <div class="profile-tab">
      <h2>Edit Profile</h2>
      <hr />

      <div class="input-div">
        <span class="label">NickName : </span>
        <input
          class="input"
          v-model="credentials.nickname"
          type="text"
          maxlength="30"
        />
      </div>

      <hr />
      <div class="select-genre">
        <p>Selected genres you love</p>
        <div class="genres">
          <span v-for="(num, idx) in credentials.genre" :key="idx"
            >{{ genres[num] }}
          </span>
        </div>
        <select
          @change="limitOption"
          multiple
          class="genre"
          v-model="credentials.genre"
          required
        >
          <option value="12">Adventure</option>
          <option value="14">Fantasy</option>
          <option value="16">Animation</option>
          <option value="18">Drama</option>
          <option value="27">Horror</option>
          <option value="28">Action</option>
          <option value="35">Comedy</option>
          <option value="36">Horror</option>
          <option value="37">Western</option>
          <option value="53">Thriller</option>
          <option value="80">Crime</option>
          <option value="99">Documentary</option>
          <option value="878">Science Fiction</option>
          <option value="9648">Mystery</option>
          <option value="10402">Music</option>
          <option value="10749">Romance</option>
          <option value="10751">Family</option>
          <option value="10752">War</option>
          <option value="10770">TV Movie</option>
        </select>
      </div>
      <div class="btn">
        <button @click="updateUser">Save</button>
        <button class="go-home">
          <router-link class="router" :to="{ name: 'Home' }"
            >Cancel</router-link
          >
        </button>
      </div>
      <button @click="deleteAccount" class="delete">Delete Account</button>
    </div>
  </div>
</template>

<script>
import axios from "axios";
const SERVER_URL = process.env.VUE_APP_SERVER_URL;
export default {
  name: "Profile",
  data: function () {
    return {
      likeGenre: [],
      credentials: {
        username: "",
        nickname: "",
        genre: [],
      },
      genres: {
        12: "Adventure",
        14: "Fantasy",
        16: "Animation",
        18: "Drama",
        27: "Horror",
        28: "Action",
        35: "Comedy",
        36: "Horro",
        37: "Western",
        53: "Thriller",
        80: "Crime",
        99: "Documentary",
        878: "Science Fiction",
        9648: "Mystery",
        10402: "Music",
        10749: "Romance",
        10751: "Family",
        10752: "War",
        10770: "TV Movie",
      },
    };
  },
  methods: {
    limitOption() {
      const select = document.querySelector(".genre");
      if (this.credentials.genre.length > 3) {
        alert("We recommend you to choose maximum 3 genres");

        select.value = 0;
      }
    },
    setHeader: function () {
      const token = localStorage.getItem("JWT");
      const header = {
        Authorization: `Bearer ${token}`,
      };
      return header;
    },
    getLikeGenres() {
      this.likeGenre = this.$store.state.userlikegenres;
    },
    getUser: function () {
      axios({
        method: "get",
        url: `${SERVER_URL}accounts/getuserinfo/`,
        headers: this.setHeader(),
      })
        .then((res) => {
          this.credentials = res.data;
          // console.log(res.data);
        })
        .catch((err) => {
          console.log(err);
        });
    },

    updateUser: function () {
      console.log(this.credentials);
      axios({
        method: "put",
        url: `${SERVER_URL}accounts/updateuserinfo/`,
        headers: this.setHeader(),
        data: this.credentials,
      })
        .then((res) => {
          console.log(res);
          alert("You info was updated");
        })
        .catch((err) => {
          console.log(err);
        });
    },
    deleteAccount() {
      if (confirm("Are you sure??")) {
        axios({
          method: "delete",
          url: `${SERVER_URL}accounts/signup/`,
          headers: this.$store.state.token,
        })
          .then((res) => {
            console.log(res);
            alert("Your account was deleted!");
            this.$router.push({ name: "Login" });
          })
          .catch((err) => {
            console.log(err);
          });
      }
    },
  },

  created() {
    this.getUser();
    this.$store.dispatch("getLikeGenre", this.$store.state.token);
  },
  mounted() {
    this.getLikeGenres();
  },
};
</script>

<style scoped src='./css/profile.css'>
</style>