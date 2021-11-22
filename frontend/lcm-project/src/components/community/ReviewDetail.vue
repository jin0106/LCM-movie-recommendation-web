<template>
  <div id="ReviewDetail">
    <div v-if="data">
      <h4 class="title">{{ data.title }}</h4>
      <div class="tab">
        <div class="tab-info">
          <span>{{ data.user["username"] }}</span>
          <span class="date">{{ data.created_at }}</span>
        </div>
        <div>
          <p>댓글 수 : {{ comments.length }}</p>
        </div>
      </div>
      <div class="content">
        <p>시청 영화 :{{ data.movie["title"] }}</p>
        <img :src="data.movie.poster_path" alt="" />

        <p>내용 :{{ data.content }}</p>
      </div>
      <div class="btn">
        <button @click="Back">Back</button>
        <div v-if="data.user.username == currentUser">
          <button @click="DeleteReview">Delete</button>
          <button data="data" @click="UpdateReview">Update</button>
        </div>
      </div>

      <div>
        <div class="comment-tab">
          <span>댓글</span>
          <p>{{ comments.length }}</p>
        </div>
        <div class="comments" v-if="comments.length">
          <div v-for="(comment, idx) in comments" :key="idx">
            <p class="comment-writer">{{ comment.user.username }}</p>
            <div class="comment-content">
              <span>{{ comment.content }}</span>
              <button
                v-if="comment.user.username == currentUser"
                @click="deleteComment(comment)"
              >
                Delete
              </button>
            </div>
          </div>
        </div>
        <span v-else class="no-comment">댓글이 아직 없습니다.</span>

        <div class="comment-create">
          <div class="comment-box">
            <p>{{ data.user.username }}</p>
            <textarea
              class="comment-write"
              @keyup.enter="createComment"
              v-model="content"
              type="text"
              placeholder="댓글을 남겨보세요"
            />
            <div class="create">
              <button @click="createComment">등록</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
// import { mapGetters } from "vuex";

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
      currentUser: this.$store.state.getUserName,
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
      console.log(this.$store.state.getUserName);
      this.$router.push({ name: "ReviewUpdate" });
    },
    Back() {
      this.$router.push({ name: "Community" });
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

<style scoped src='./css/reviewdetail.css'>
</style>