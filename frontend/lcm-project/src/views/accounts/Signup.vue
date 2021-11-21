<template>
  <div id="Signup">
    <div class="signup">
      <h2 class="title">Sign Up</h2>
      <div>
        <input
          v-model="credentials.username"
          type="text"
          id="username"
          placeholder="Username"
        />
        <input
          v-model="credentials.password"
          type="password"
          id="password"
          placeholder="Password"
        />
        <input
          v-model="credentials.passwordconfirm"
          @keyup.enter="signup"
          type="password"
          id="passwordcomfirm"
          placeholder="Confirm Password"
        />
        <input
          v-model="credentials.nickname"
          type="text"
          id="nickname"
          placeholder="Nickname"
        />
      </div>
      <div class="select-genre">
        <p>Select genres you loved</p>
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
          <option type="checkbox" value="99">Documentary</option>
          <option value="878">Science Fiction</option>
          <option value="9648">Mystery</option>
          <option value="10402">Music</option>
          <option value="10749">Romance</option>
          <option value="10751">Family</option>
          <option value="10752">War</option>
          <option value="10770">TV Movie</option>
        </select>
      </div>
      <button class="signup-btn" @click="signup">Sign Up</button>
    </div>
    <div class="login">
      <span
        >Do you have an account?
        <router-link class="login-item" :to="{ name: 'Login' }"
          >Login</router-link
        >
      </span>
    </div>
  </div>
</template>

<script>
import axios from "axios";
const SERVER_URL = process.env.VUE_APP_SERVER_URL;

export default {
  name: "Signup",
  data: function () {
    return {
      credentials: {
        username: "",
        password: "",
        passwordconfirm: "",
        nickname: "",
        genre: [],
        profileimg: "",
      },
    };
  },
  methods: {
    signup: function () {
      console.log(this.$store.state.ngrokurl);
      axios({
        method: "post",
        url: `${SERVER_URL}accounts/signup/`,
        data: this.credentials,
      })
        .then((res) => {
          console.log(res);
          this.$router.push({ name: "Login" });
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
};
</script>

<style scoped src='./css/signup.css'>
</style>