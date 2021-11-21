<template>
  <div id="Comments">
    <h1>댓글 목록</h1>
      <div v-for="(comment, idx) in comments" :key="idx">
        <hr>
        <p>내용 : {{comment.content}} 유저이름 : {{comment.user.username}}</p>
        <button @click="deleteComment(comment)">Delete</button>
        <hr>
      </div>
  </div>
</template>

<script>
const SERVER_URL = process.env.VUE_APP_SERVER_URL
import axios from 'axios';
export default {
  name : "Comments",
  data: function(){
    return {
      comments : this.$store.state.comments
    }
  },
  props: {
    review : Object,
    reviewId : Number,
  },
  methods: {
    getCommentList: function(){
      const data = {
        token : this.$store.state.token,
        review: this.review,
        reviewId: this.reviewId,
      }
      this.$store.dispatch("getCommentList", data)
    },
    deleteComment: function(comment){
      axios({
        method: "DELETE",
        url: `${SERVER_URL}communities/${this.reviewId}/comments/${comment.id}`
      })
      .then(() => {
        // 리스트 다시 받아와서 뿌려줌
        this.comments = this.$store.state.comments
      })
      .catch((err) => {
        console.log(err)
      })
    },
  },
  created: function(){
    this.getCommentList()
  }
};
</script>

<style>
</style>