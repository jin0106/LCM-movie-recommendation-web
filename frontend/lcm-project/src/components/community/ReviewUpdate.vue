<template>
  <div id="CreateReview" v-if="data.title">
    <h1>Create Review</h1>
    <h4>영화 제목 : {{ data.movie.title }}</h4>
    <hr />
    <div>
      <label for="title">제목</label>
      <input v-model="data.title" type="text" />
    </div>
    <br />

    <div>
      <label for="content">내용</label>
      <textarea
        v-model="data.content"
        name="content"
        id="conent"
        cols="30"
        rows="10"
      ></textarea>
    </div>
    <div class="btn">
      <button @click="goList">목록</button>
      <button @click="Create">등록</button>
    </div>
  </div>
</template>

<script>
import axios from "axios";
const SERVER_URL = process.env.VUE_APP_SERVER_URL;
export default {
  name: "ReviewUpdate",
  data: function () {
    return {
      reviewId: this.$route.params.reviewId,
      data: {
        movie: "",
        title: "",
        content: "",
        is_private: false,
      },
      content: "",
    };
  },
  created() {
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
    goList: function () {
      this.$router.push({ name: "Community" });
    },
    Create() {
      console.log(this.data);
      axios({
        method: "put",
        url: `${SERVER_URL}communities/${this.reviewId}/`,
        headers: this.$store.state.token,
        data: this.data,
      })
        .then((res) => {
          console.log(res);
          this.$router.push({
            name: "ReviewDetail",
            params: { reviewId: this.reviewId },
          });
        })
        .catch((err) => {
          console.log(err);
          console.log("요청실패 ");
        });
      // console.log(this.data);
      // const reviewItem = {
      //   info: this.data,
      //   token: this.$store.state.token,
      // };
      // this.$store.dispatch("CreateReview", reviewItem);
      this.$router.push({ name: "Community" });
    },
  },
};
</script>

<style>
</style>