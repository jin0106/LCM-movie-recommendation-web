<template>
  <div id="ReviewList">
    <p v-for="(review, idx) in reviews" :key="idx">{{ review.title }}</p>
    <ReviewDetail :review="review" />
    <!-- <h2 v-else>게시글이 없습니다.</h2> -->
  </div>
</template>

<script>
import ReviewDetail from "@/components/community/ReviewDetail";
import { mapState } from "vuex";

export default {
  name: "ReviewList",
  components: {
    ReviewDetail,
  },
  // 받아온 게시글 데이터의 유무를 위해서 변수 정의
  methods: {
    setHeader: function () {
      const token = localStorage.getItem("JWT");
      const header = {
        Authorization: `Bearer ${token}`,
      };
      return header;
    },
  },
  created: function () {
    this.$store.dispatch("getReviews", this.setHeader());
  },
  computed: {
    ...mapState(["reviews"]),
  },
};
</script>

<style>
</style>