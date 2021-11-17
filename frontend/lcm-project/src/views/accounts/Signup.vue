<template>
  <div>
    <h2>회원가입</h2>
    <div>
      <label for="username">ID : </label>
      <input 
        v-model="credentials.username" 
        type="text" 
        id="username"
        >
    </div>

    <div>
      <label for="password">PASSWORD : </label>
      <input
        v-model="credentials.password"
        type="password"
        id="password"
        >
    </div>

    <div>
      <label for="username">PASSWORD CONFIRM : </label>
      <input 
        v-model="credentials.passwordconfirm"
        @keyup.enter="signup" 
        type="password" 
        id="passwordcomfirm"
        >
    </div>
    <button @click="signup">회원가입</button>
  </div>
</template>

<script>
import axios from 'axios'
const SERVER_URL = process.env.VUE_APP_SERVER_URL


export default {
  name : 'Signup',
  data: function() {
    return {
      credentials: {
        username: '',
        password: '',
        passwordconfirm: '',
      }
    }
  },
  methods: {
    signup: function(){
      console.log(SERVER_URL)
      axios({
        method: 'post',
        url: `http://127.0.0.1:8000/accounts/signup/`,
        data: this.credentials
      })
      .then(res => {
        console.log(res)
        this.$router.push({ name: 'Login' })
      })
      .catch(err => {
        alert(err)
      })
    }
  }
}
</script>

<style>

</style>