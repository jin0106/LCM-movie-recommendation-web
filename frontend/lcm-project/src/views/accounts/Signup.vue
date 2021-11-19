<template>
  <div id="Signup">
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

    <div>
      <label for="nickname">NICK NAME : </label>
      <input
        v-model="credentials.nickname"
        type="text"
        id="nickname"
        >
    </div>

    <div v-if="credentials.genre.length < 3">
      <input type="checkbox" v-model="credentials.genre" value="12">Adventure
      <input type="checkbox" v-model="credentials.genre" value="14">Fantasy
      <input type="checkbox" v-model="credentials.genre" value="16">Animation
      <input type="checkbox" v-model="credentials.genre" value="18">Drama
      <input type="checkbox" v-model="credentials.genre" value="27">Horror
      <input type="checkbox" v-model="credentials.genre" value="28">Action
      <input type="checkbox" v-model="credentials.genre" value="35">Comedy
      <input type="checkbox" v-model="credentials.genre" value="36">Horror
      <input type="checkbox" v-model="credentials.genre" value="37">Western
      <input type="checkbox" v-model="credentials.genre" value="53">Thriller
      <input type="checkbox" v-model="credentials.genre" value="80">Crime
      <input type="checkbox" v-model="credentials.genre" value="99">Documentary
      <input type="checkbox" v-model="credentials.genre" value="878">Science Fiction
      <input type="checkbox" v-model="credentials.genre" value="9648">Mystery
      <input type="checkbox" v-model="credentials.genre" value="10402">Music
      <input type="checkbox" v-model="credentials.genre" value="10749">Romance
      <input type="checkbox" v-model="credentials.genre" value="10751">Family
      <input type="checkbox" v-model="credentials.genre" value="10752">War
      <input type="checkbox" v-model="credentials.genre" value="10770">TV Movie
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
        nickname: '',
        genre: [],
        profileimg: '',
      }
    }
  },
  methods: {
    signup: function(){
      console.log(this.$store.state.ngrokurl)
      axios({
        method: 'post',
        url: `${SERVER_URL}accounts/signup/`,
        data: this.credentials,
      })
      .then(res => {
        console.log(res)
        this.$router.push({ name: 'Login' })
      })
      .catch(err => {
        console.log(err)
      })
    },
  }
}
</script>

<style>

</style>