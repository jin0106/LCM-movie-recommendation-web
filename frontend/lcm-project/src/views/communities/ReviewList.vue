<template>
  <div id="ReviewList">
    <div v-for="(review, idx) in reviewList" :key="idx">
      <p @click="detail(idx)">{{ review.title }}왜 안나옴</p>
    </div>
    <!-- <h2 v-else>게시글이 없습니다.</h2> -->
  </div>
</template>

<script>
import axios from "axios";
import { mapState } from "vuex";

export default {
  name: "ReviewList",
  // 받아온 게시글 데이터의 유무를 위해서 변수 정의
  methods: {
    detail: function (idx) {
      this.$router.push({
        name: "ReviewDetail",
        params: {
          reviewId: idx + 1,
        },
      });
    },
  },
  created: function () {
    axios({
      method: "get",
      url: "http://127.0.0.1:8000/communities/",
    })
      .then((res) => {
        // console.log(res.data);
        this.$store.dispatch("getReviewList", res.data);
      })
      .catch((err) => {
        alert(err);
      });
  },
  computed: {
    ...mapState(["reviewList"]),
  },
};
</script>

<style>
</style>