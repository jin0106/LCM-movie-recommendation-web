<template>
  <div id="CreateReview">
    <h1>Create Review</h1>
    <hr />
    <div>
      <label for="title">제목</label>
      <input v-model="info.title" type="text" />
    </div>
    <br />
    <div>
      <label for="movie">영화 이름</label>
      <input v-model="info.movie" type="text" name="movie" id="movie" />
    </div>

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
import { mapGetters } from "vuex";
export default {
  name: "ReviewForm",
  data: function () {
    return {
      info: {
        movie: null,
        like_users: null,
        title: null,
        content: null,
      },
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
      this.$router.push({ name: "ReviewList" });
    },
    Create() {
      const reviewItem = {
        reviewItem: this.info,
        token: this.setHeader(),
      };
      this.$store.dispatch("CreateReview", reviewItem);
    },
  },
  computed: {
    ...mapGetters(["getUserName"]),
  },
};
</script>

<style>
</style>