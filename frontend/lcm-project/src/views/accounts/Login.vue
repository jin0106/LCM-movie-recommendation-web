<template>
  <div id="Login">
    <div class="login">
      <h2>Sign In</h2>

      <div v-if="errMsg">{{ errMsg }}</div>
      <div class="login-info">
        <input
          placeholder="type your ID"
          type="text"
          id="username"
          v-model="credentials.username"
        />
        <input
          type="password"
          id="password"
          v-model="credentials.password"
          @keyup.enter="login"
          placeholder="Password"
        />
      </div>
      <button @click="login">Sign In</button>
      <div class="social">
        <p>or</p>
        <p>Sign In with Facebook</p>
        <p>Sign In with Naver</p>
      </div>
    </div>
    <div class="signup">
      <span>Are you New?</span>
      <router-link class="nav-item" :to="{ name: 'Signup' }"
        >Signup</router-link
      >
    </div>
  </div>
</template>

<script>
import axios from "axios";

const SERVER_URL = process.env.VUE_APP_SERVER_URL;

export default {
  name: "Login",
  data: function () {
    return {
      credentials: {
        username: "",
        password: "",
      },
      errMsg: "",
    };
  },
  methods: {
    login: function () {
      axios({
        method: "post",
        url: `${SERVER_URL}accounts/api/token/`,
        data: this.credentials,
      })
        .then((res) => {
          localStorage.setItem("JWT", res.data.access);
          this.$emit("login");
          this.$store.dispatch("setHeader");
          this.$router.push({ name: "Home" });
        })
        .catch((err) => {
          console.dir(err.response.data);
          this.errMsg = err.response.data.detail;
        });
    },
  },
  created() {
    this.$store.dispatch("getReviews", this.$store.state.token);
  },
};
</script>

<style scoped src='./css/login.css'>
</style>