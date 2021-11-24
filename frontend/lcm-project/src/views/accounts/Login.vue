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
        <span class="or">or</span>
        <div class="google">
          <a href="#" @click="GoogleLoginBtn"
            ><img
              src="https://images.theconversation.com/files/93616/original/image-20150902-6700-t2axrz.jpg?ixlib=rb-1.1.0&q=45&auto=format&w=1000&fit=clip"
              alt=""
            />
            Sign in with Google</a
          >
        </div>

        <div id="my-signin2"></div>
        <div id="naver_id_login"></div>
        <div id="naver_login">
          <a
            href="https://nid.naver.com/oauth2.0/authorize?response_type=token&amp;client_id=CjWEtcN_SVhkWFE6lD8B&amp;redirect_uri=http%3A%2F%2Flocalhost%3A8080%2Faccounts%2Flogin&amp;state=4a95b6fa-73fd-493a-b2f5-0ca47828ab79"
            id="naver-id-login-anchor"
            ><img src="http://static.nid.naver.com/oauth/button_g.PNG" />Sign in
            with Naver</a
          >
        </div>
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
import createPersistedState from "vuex-persistedstate";
const SERVER_URL = process.env.VUE_APP_SERVER_URL;
const PASSWORD = process.env.VUE_APP_PASSWORD;

export default {
  plugins: [createPersistedState()],
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
            // this.$router.push({ name: "Home" });
          })
          .catch((res) => {
            console.log(res);
          });
      }
      // this.$router.push({ name: "Profile" });

      // this.$router.go();
    },
    //구글 로그인 콜백함수 (실패)
    GoogleLoginFailure(error) {
      console.log(error);
    },
  },
  mounted() {
    const naver_id_login = new window.naver_login(
      "CjWEtcN_SVhkWFE6lD8B",
      "http://localhost:8080/accounts/login"
    );

    if (naver_id_login.getAccessToken()) {
      // 네이버 사용자 프로필 조회
      console.log(naver_id_login.getAccessToken());
      axios({
        method: "post",
        url: `${SERVER_URL}accounts/naver/`,
        data: {
          token: naver_id_login.getAccessToken(),
        },
      })
        .then((res) => {
          (this.credentials = {
            username: res.data["username"],
            password: PASSWORD,
          }),
            this.login();
        })
        .catch((err) => {
          console.log(err);
        });
    } else {
      const state = naver_id_login.getUniqState();
      // naver_id_login.setButton("green", 1);
      // 버튼 설정
      naver_id_login.setState(state);
      //naver_id_login.setPopup(); // popup 설정을 위한 코드
      naver_id_login.init_naver_id_login();
    }
  },
};
</script>

<style scoped src='./css/login.css'>
</style>