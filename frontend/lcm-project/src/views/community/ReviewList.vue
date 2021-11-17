<template>
  <div id="ReviewList">
    <h1 v-if="reviewlist">게시글이 있습니다
      <button @click="getReviewList">게시글 받아오기</button>
    </h1>
    <h2 v-else>게시글이 없습니다.</h2>

  </div>
  
</template>

<script>
import axios from 'axios'
export default {
  name: 'ReviewList',
  // 받아온 게시글 데이터의 유무를 위해서 변수 정의
  data: function(){
    return {
      reviewlist : {}
    }
  },
  methods: {
    getReviewList: function(){
      axios({
        method: 'get',
        url: `http://9049-125-134-86-234.ngrok.io/community/`
      })
      .then(res => {
        console.log(res)
      })
    }
  }
}
</script>

<style>

</style>