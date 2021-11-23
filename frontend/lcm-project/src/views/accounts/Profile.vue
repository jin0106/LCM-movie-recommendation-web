<template>
  <div id="Profile">
    <div class="profile-tab">
      <h2>Edit Profile</h2>
      <hr />

      <div class="input-div">
        <span class="label">NickName : </span>
        <input class="input" v-model="credentials.nickname" type="text" />
      </div>

      <hr />
      <div class="select-genre">
        <p>Select genres you love</p>
        <select
          multiple
          class="genre"
          v-model="credentials.genre"
          required
          v-if="credentials.genre.length < 3"
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
    };
  },
  methods: {
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
          alert("수정이 성공적으로 완료되었습니다.");
          this.$router.push({ name: "Home" });
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