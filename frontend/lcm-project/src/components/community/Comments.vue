<template>
  <div id="Comments">
    <h1>댓글 목록</h1>
    <div v-for="(comment, idx) in Comments" :key="idx">
      <hr />
      <p>{{ comment.user.username }} : {{ comment.content }}</p>
      <button @click="deleteComment(comment)">Delete</button>
      <hr />
    </div>
  </div>
</template>

<script>
const SERVER_URL = process.env.VUE_APP_SERVER_URL;
import axios from "axios";
import { mapGetters } from "vuex";
export default {
  name: "Comments",
  data: function () {
    return {};
  },
  props: {
    review: Object,
    reviewId: Number,
  },
  methods: {
    getCommentList: function () {
      const data = {
        token: this.$store.state.token,
        reviewId: this.reviewId,
      };
      this.$store.dispatch("getCommentList", data);
    },
    deleteComment: function (comment) {
      axios({
        method: "DELETE",
        url: `${SERVER_URL}communities/${this.reviewId}/comments/${comment.id}`,
      })
        .then(() => {
          // 리스트 다시 받아와서 뿌려줌
          this.getCommentList();
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
  created: function () {
    this.getCommentList();
  },
  computed: {
    ...mapGetters["Comments"],
  },
};
</script>

<style>
</style>