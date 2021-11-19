<template>
  <div id="ReviewDetail">
    <div v-if="data">
      <h2>제목 : {{ data.title }}</h2>
      <p>작성자: {{ data.user["username"] }}</p>
      <p>시청 영화 :{{ data.movie["title"] }}</p>
      <p>내용 :{{ data.content }}</p>
      <p>작성일자 : {{ data.created_at }}</p>
      <button @click="Delete">Delete</button>
      <button @click="Update">Update</button>
    </div>
    <div>
      <form>
        <input v-model.trim="content" type="text" id="comments" />
        <button @click="Comment">작성</button>
      </form>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { mapGetters } from "vuex";

export default {
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
      url: `http://127.0.0.1:8000/communities/${this.reviewId}`,
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
      axios({
        method: "put",
        url: `http://127.0.0.1:8000/communities/${this.reviewId}/`,
      })
        .then((res) => {
          console.log(res);
          // this.$router.push({ name: "ReviewList" });
        })
        .catch((err) => {
          console.log(err);
        });
    },
    Comment: function () {
      axios({
        method: "post",
        url: `http://127.0.0.1:8000/communities/${this.reviewId}/comments/`,
        data: this.content,
      })
        .then((res) => {
          console.log(res);
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
  computed: {
    ...mapGetters(["getUserName"]),
  },
};
</script>

<style>
</style>