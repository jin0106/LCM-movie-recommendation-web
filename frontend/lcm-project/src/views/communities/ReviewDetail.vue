<template>
  <div id="ReviewDetail">
    <h2>제목 : {{ data.title }}</h2>
    <p>작성자: {{ data.user }}</p>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "ReviewDetail",
  data: function () {
    return {
      reviewId: this.$route.params.reviewId,
      data: null,
      info: {
        movie: null,
        user: null,
        like_users: null,
        title: null,
        content: null,
        created_at: null,
        updated_at: null,
        is_private: false,
      },
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
};
</script>

<style>
</style>