<template>
  <div id="ReviewDetail">
    <div v-if="data">
      <h2>제목 : {{ getUserName }}</h2>
      <p>작성자: {{ data.user }}</p>
      <p>내용 :{{ data.content }}</p>
      <p>작성일자 : {{ data.created_at }}</p>
      <button @click="Delete">Delete</button>
      <button>Update</button>
    </div>
    <div>
      <form>
        <input v-model.trim="content" type="text" id="comments" />
        <button @click="Comment">작성</button>
      </form>
    </div>

    <h2>제목 : {{ data.title }}</h2>
    <p>작성자: {{ data.user }}</p>
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
=======
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
<<<<<<< HEAD
  // beforeMount: function () {
  //   axios({
  //     method: "get",
  //     url: `http://127.0.0.1:8000/communities/${this.reviewId}/comments`,
  //   })
  //     .then((res) => {
  //       console.log(res);
  //     })
  //     .catch((err) => {
  //       console.log(err);
  //     });
  // },
  methods: {
    Delete: function () {
      axios({
        method: "delete",
        url: `http://127.0.0.1:8000/communities/${this.reviewId}`,
      })
        .then((res) => {
          console.log(res);
          this.$router.push({ name: "ReviewList" });
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

</script>

<style>
</style>