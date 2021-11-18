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
import axios from "axios";
export default {
  name: "CreateReview",
  data: function () {
    return {
      info: {
        movie: "",
        like_users: "",
        title: "",
        content: "",
        created_at: "",
        updated_at: "",
        is_private: "",
      },
    };
  },
  methods: {
    goList: function () {
      this.$router.push({ name: "ReviewList" });
    },
    Create: function () {
      axios({
        method: "POST",
        url: "http://127.0.0.1:8000/communities/",
        data: this.info,
      })
        .then((res) => {
          console.log(res);
          this.$route.push({ name: "ReviewList" });
        })
        .catch((err) => [console.log(err)]);
    },
  },
  computed: {
    ...mapGetters(["getUserName"]),
  },
};
</script>

<style>
</style>