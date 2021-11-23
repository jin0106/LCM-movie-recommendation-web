<template>
  <div id="ReviewUpdate" v-if="data.title">
    <div class="update">
      <h2>Update the review</h2>
    </div>

    <div class="reviewupdate">
      <div class="data">
        <h4 class="movie-title">Movie : {{ data.movie.title }}</h4>
        <hr />
        <div class="title">
          <label for="title">제목 </label>
          <input v-model="data.title" type="text" />
        </div>
        <br />

        <div class="content">
          <label for="content">내용</label>
          <br />
          <textarea
            v-model="data.content"
            name="content"
            id="conent"
            cols="30"
            rows="10"
          ></textarea>
        </div>
      </div>
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
      this.$router.push({ name: "Community" });
    },
  },
};
</script>

<style scoped src='./css/reviewupdate.css'>
</style>