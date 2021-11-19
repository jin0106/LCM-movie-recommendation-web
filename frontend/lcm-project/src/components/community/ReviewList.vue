<template>
  <div id="ReviewList">
    <div v-for="(review, idx) in reviews" :key="idx">
      <p @click="detail(review)">{{ review.title }}</p>
    </div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  name: "ReviewList",
  // 받아온 게시글 데이터의 유무를 위해서 변수 정의
  methods: {
    setHeader: function () {
      const token = localStorage.getItem("JWT");
      const header = {
        Authorization: `Bearer ${token}`,
      };
      return header;
    },
    detail: function (review) {
      this.$router.push({
        name: "ReviewDetail",
        params: {
          reviewId: review.id,
        },
      });
    },
  },
  created: function () {
    this.$store.dispatch("getReviews", this.setHeader());
  },
  computed: {
    ...mapGetters(["reviews"]),
  },
};
</script>

<style>
</style>