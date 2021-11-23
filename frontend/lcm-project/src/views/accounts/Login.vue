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
        <a class="google-a" href="#" @click="GoogleLoginBtn"
          ><img
            class="google"
            src="https://image.similarpng.com/very-thumbnail/2020/12/Flat-design-Google-logo-design-Vector-PNG.png"
            alt="google"
          />
          Sign In with Google</a
        >
        <div id="my-signin2" style="display: none"></div>

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
const PASSWORD = process.env.VUE_APP_PASSWORD;
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
          this.$store.dispatch("getUserName", this.credentials.username);
          this.$emit("login");
          this.$store.dispatch("setHeader");
          this.$router.push({ name: "Home" });
        })
        .catch((err) => {
          console.dir(err.response.data);
          this.errMsg = err.response.data.detail;
        });
    },
    GoogleLoginBtn: function () {
      var self = this;

      window.gapi.signin2.render("my-signin2", {
        scope: "profile email",
        width: 240,
        height: 50,
        longtitle: true,
        theme: "dark",
        onsuccess: this.GoogleLoginSuccess,
        onfailure: this.GoogleLoginFailure,
      });

      setTimeout(function () {
        if (!self.googleLoginCheck) {
          const auth = window.gapi.auth2.getAuthInstance();
          auth.isSignedIn.get();
          document.querySelector(".abcRioButton").click();
        }
      }, 1500);
    },
    async GoogleLoginSuccess(googleUser) {
      const googleEmail = googleUser.getBasicProfile().getEmail();
      if (googleEmail !== "undefined") {
        console.log(googleEmail);
        // 장고 서버에 요청해서 로그인 시키는 부분
        axios({
          method: "post",
          url: `${SERVER_URL}accounts/google/`,
          data: {
            id: googleEmail,
          },
        })
          .then((res) => {
            this.credentials = {
              username: res.data["username"],
              password: PASSWORD,
            };
            this.login();
          })
          .catch((res) => {
            console.log(res);
          });
        this.$router.push({ name: "Home" });
      }
    },
    //구글 로그인 콜백함수 (실패)
    GoogleLoginFailure(error) {
      console.log(error);
    },
  },
};
</script>

<style scoped src='./css/login.css'>
</style>