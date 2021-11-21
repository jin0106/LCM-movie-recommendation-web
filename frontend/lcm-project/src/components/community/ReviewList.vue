<template>
  <div id="ReviewList">
    <div v-if="reviews">
      <div v-for="review in reviews" :key="review.id">
        <p @click="detail(review)">{{ review.title }}</p>
      </div>
    </div>
    <div v-else>
      <p>작성된 글이 없습니다</p>
    </div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  name: "ReviewList",
  // 받아온 게시글 데이터의 유무를 위해서 변수 정의
  data: function () {
    return {
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
    detail: function (review) {
      console.log(review)
      this.$router.push({
        name: "ReviewDetail",
        params: {
          reviewId: review.id,
        },
      });
    },
  },
  // 처음과 업데이트될 때 리뷰 리스트 다시 불러오기
  created() {
    this.$store.dispatch("getReviews", this.setHeader());
  },
  // updated() {
  //   this.$store.dispatch("getReviews", this.setHeader());
  // },
  computed: {
    ...mapGetters(["reviews"]),
  },
};
</script>

<style>
</style>