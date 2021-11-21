<template>
  <div id="ReviewDetail">
    <div v-if="data">
      <h2>제목 : {{ data.title }}</h2>
      <p>작성자: {{ data.user["username"] }}</p>
      <p>시청 영화 :{{ data.movie["title"] }}</p>
      <p>내용 :{{ data.content }}</p>
      <p>작성일자 : {{ data.created_at }}</p>
      <p>마지막 수정 일자: {{ data.updated_at }}</p>
      <button @click="Delete">Delete</button>
      <button data="data" @click="Update">Update</button>
      <comment-form :review="data"/>
      <comments :review="data" :reviewId="reviewId"/>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { mapGetters } from "vuex";
import Comments from "./Comments.vue";
import CommentForm from "./CommentForm.vue";
const SERVER_URL = process.env.VUE_APP_SERVER_URL;

export default {
  components: { Comments, CommentForm },
  name: "ReviewDetail",
  data: function () {
    return {
      reviewId: this.$route.params.reviewId,
      data: "",
      content: "",
    };
  },

  created: function () {
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
  methods: {
    setHeader: function () {
      const token = localStorage.getItem("JWT");
      const header = {
        Authorization: `Bearer ${token}`,
      };
      return header;
    },
    Delete: function () {
      this.$store.dispatch("deleteReview", this.reviewId);
      this.$store.dispatch("getReviews");
      this.$router.push({ name: "Community" });
    },
    Update: function () {
      this.$router.push({ name: "ReviewUpdate" });
    },
  },
  computed: {
    ...mapGetters(["getUserName"]),
  },
};
</script>

<style>
</style>