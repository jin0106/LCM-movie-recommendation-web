<template>
  <div id="ReviewDetail">
    <div v-if="review">
      <h2>제목 : {{ review.title }}</h2>
      <p>작성자: {{ review.user["username"] }}</p>
      <p>시청 영화 :{{ review.movie["title"] }}</p>
      <p>내용 :{{ review.content }}</p>
      <p>작성일자 : {{ review.created_at }}</p>
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
  props: {
    review: {
      type: Object,
    },
  },
  data: function () {
    return {
      reviewId: this.$route.params.reviewId,
      data: "",
      content: "",
    };
  },

  created: function () {
    console.log("aaaa");
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
    Delete: function () {
      axios({
        method: "delete",
        url: `http://127.0.0.1:8000/communities/${this.reviewId}`,
      })
        .then((res) => {
          console.log(res);
          // this.$router.push({ name: "ReviewList" });
        })
        .catch((err) => {
          console.log(err);
        });
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