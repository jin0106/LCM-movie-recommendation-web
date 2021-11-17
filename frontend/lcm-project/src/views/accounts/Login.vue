<template>
  <div id="Login">
    <h2>로그인</h2>
    <hr>
    <div v-if="errMsg">{{ errMsg }}</div>
    <div>
      <label for="username">아이디 :</label>
      <input type="text" id="username" v-model="credentials.username">
    </div>
    <div>
      <label for="password">비밀번호 :</label>
      <input 
        type="password" 
        id="password" 
        v-model="credentials.password"
        @keyup.enter="login"
      >
    </div>
    <button @click="login">로그인</button>
  </div>
</template>

<script>
import axios from 'axios'

//const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'Login',
  data: function () {
    return {
      credentials: {
        username: '',
        password: '',
      },
      errMsg: '',
    }
  },
  methods: {
    login: function () {
      axios({
        method: 'post',
        url: `http://9049-125-134-86-234.ngrok.io/accounts/api/token/`,
        data: this.credentials
      })
      .then(res => {
        console.log(res)
        localStorage.setItem('JWT', res.data.access)
        this.$emit('login')
        this.$router.push({ name: 'temp' })
      })
      .catch(err => {
        console.dir(err.response.data)
        this.errMsg = err.response.data.detail
      })
    }
  }
}
</script>