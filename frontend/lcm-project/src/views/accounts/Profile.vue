<template>
  <div id="Profile">
    <div v-if="likeGenre.length"> 현재 좋아하는 Genre
      <div v-for="(genre, idx) in likeGenre" :key=idx>
        <p></p>
          {{ genre.name }}
        <p></p>
      </div>
    </div>
    <div v-else>
      현재 좋아하는 장르가 없습니다.
      <button @click="getLikeGenre">click</button>
    </div>
    <hr>
    <div>
      <p>Genre 수정하기 </p>
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

    <hr>
      <label for="nickname">닉네임수정 : </label>
      <input v-model="credentials.nickname" type="text" @keyup.enter="updateUser">
      <button @click="updateUser">수정하기</button>
  </div>

</template>

<script>
import axios from 'axios'
const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name : "Profile",
  data: function(){
    return {
      likeGenre : [],
      credentials: {
        username: '',
        nickname: '',
        genre: [],
      }
    }
  },
  methods: {
    setHeader: function () {
      const token = localStorage.getItem('JWT')
      const header = {
        Authorization: `Bearer ${token}`
      }
      return header
    },
    getLikeGenre: function(){
      axios({
        method: 'get',
        url: `${SERVER_URL}accounts/likegenre/`,
        headers: this.setHeader()
      })
      .then(res => {
        this.likeGenre = res.data
      })
      .catch(err => {
        console.log(err)
      })
    },

    getUser: function(){
      axios({
        method: 'get',
        url: `${SERVER_URL}accounts/getuserinfo/`,
        headers: this.setHeader(),
      })
      .then(res => {
        this.credentials = res.data
        console.log(res.data)
      })
      .catch(err => {
        console.log(err)
      })
    },
    
    updateUser: function(){
      console.log(this.credentials)
      axios({
        method: 'put',
        url: `${SERVER_URL}accounts/updateuserinfo/`,
        headers: this.setHeader(),
        data: this.credentials
      })
      .then(res => {
        console.log(res)
      })
      .catch(err => {
        console.log(err)
      })
    }
    
  },
  created: function() {
    this.getUser(),
    this.getLikeGenre()
  }
}
</script>

<style>

</style>