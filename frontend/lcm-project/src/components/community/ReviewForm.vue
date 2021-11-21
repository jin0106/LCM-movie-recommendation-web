<template>
  <div id="CreateReview">
    <h1>Create Review</h1>
    <h2>영화 제목 : {{ movietitle }}</h2>
    <hr />
    <div>
      <label for="title">제목</label>
      <input v-model="info.title" type="text" />
    </div>
    <br />

    <label for="content">내용</label>
    <textarea
      v-model="info.content"
      name="content"
      id="conent"
      cols="30"
      rows="10"
    ></textarea>
    <div class="btn">
      <button @click="goList">목록</button>
      <button @click="Create">등록</button>
    </div>
  </div>
</template>

<script>
export default {
  name: "ReviewForm",
  data: function () {
    return {
      info: {
        movie: null,
        title: null,
        content: null,
        is_private: false,
      },
      movietitle: this.$store.state.movieInfo.title,
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
    goList: function () {
      this.$router.push({ name: "Community" });
    },
    Create() {
      this.info.movie = this.$store.state.movieInfo;
      const reviewItem = {
        info: this.info,
        token: this.setHeader(),
      };
      this.$store.dispatch("CreateReview", reviewItem);
      this.movie = null;
      this.like_users = null;
      this.title = null;
      this.content = null;
      this.is_private = false;
      this.$router.push({ name: "Community" });
    },
  },
};
</script>

<style>
</style>