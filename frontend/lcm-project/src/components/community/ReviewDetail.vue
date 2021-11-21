<template>
  <div id="ReviewDetail">
    <div v-if="data">
      <h2>제목 : {{ data.title }}</h2>
      <p>작성자: {{ data.user["username"] }}</p>
      <p>시청 영화 :{{ data.movie["title"] }}</p>
      <p>내용 :{{ data.content }}</p>
      <p>작성일자 : {{ data.created_at }}</p>
      <p>마지막 수정 일자: {{ data.updated_at }}</p>
      <button @click="DeleteReview">Delete</button>
      <button data="data" @click="UpdateReview">Update</button>
      <div>
        <h1>댓글 목록</h1>
        <div v-for="(comment, idx) in comments" :key="idx">
          <hr />
          <p>{{ comment.user.username }} : {{ comment.content }}</p>
          <button @click="deleteComment(comment)">Delete</button>
          <hr />
        </div>
        <div>
          <input @keyup.enter="createComment" v-model="content" type="text" />
          <button @click="createComment">작성</button>
        </div>
      </div>

      <!-- <comments :reviewId="reviewId" /> -->
      <!-- <comment-form :review="data" /> -->
    </div>
  </div>
</template>

<script>
import axios from "axios";
// import Comments from "./Comments.vue";
// import CommentForm from "./CommentForm.vue";
const SERVER_URL = process.env.VUE_APP_SERVER_URL;

export default {
  // components: { CommentForm },
  name: "ReviewDetail",
  data: function () {
    return {
      reviewId: parseInt(this.$route.params.reviewId),
      data: "",
      content: "",
      comments: [],
    };
  },
  methods: {
    setHeader: function () {
      const token = localStorage.getItem("JWT");
      const header = {
        Authorization: `Bearer ${token}`,
      };
      return header;
    },
    DeleteReview: function () {
      this.$store.dispatch("deleteReview", this.reviewId);
      this.$router.push({ name: "Community" });
    },
    UpdateReview: function () {
      this.$router.push({ name: "ReviewUpdate" });
    },
    getComments: function () {
      axios({
        method: "GET",
        url: `${SERVER_URL}communities/${this.reviewId}/comments/`,
        headers: this.setHeader(),
      })
        .then((res) => {
          this.comments = res.data;
        })
        .catch((err) => {
          console.log(err);
        });
    },
    getDetail: function () {
      axios({
        method: "get",
        url: `${SERVER_URL}communities/${this.reviewId}`,
      })
        .then((res) => {
          this.data = res.data;
        })
        .catch((err) => {
          console.log(err);
        });
    },
    deleteComment: function (comment) {
      axios({
        method: "DELETE",
        url: `${SERVER_URL}communities/${this.reviewId}/comments/${comment.id}`,
        headers: this.setHeader(),
      })
        .then(() => {
          // 리스트 다시 받아와서 뿌려줌
          this.getComments();
        })
        .catch((err) => {
          console.log(err);
          alert("본인이 작성한 댓글만 삭제가 가능합니다.");
        });
    },
    createComment: function () {
      const commentItem = this.content;
      if (commentItem) {
        axios({
          method: "post",
          url: `${SERVER_URL}communities/${this.reviewId}/comments/`,
          headers: this.setHeader(),
          data: { content: commentItem },
        })
          .then(() => {
            // 리스트 다시 받아와서 뿌려줌
            this.content = "";
            this.getComments();
          })
          .catch((err) => {
            console.log(err);
            alert("댓글을 입력 해주세요");
          });
      }
    },
  },
  created: function () {
    this.getDetail();
    this.getComments();
  },
};
</script>

<style>
</style>