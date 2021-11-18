<template>
  <div id="Profile">
    <div>
      {{likeGenre}}
      <button @click="getLikeGenre">click</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name : "Profile",
  data: function(){
    return {
      likeGenre : []
    }
  },
  methods: {
    getLikeGenre: function(){
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/accounts/likegenre/`,
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
    this.getLikeGenre
  }
}
</script>

<style>

</style>