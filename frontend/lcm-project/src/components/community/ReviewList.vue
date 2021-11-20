<template>
  <div id="ReviewList">
    <div v-if="check.length">
      <div v-for="(review, idx) in reviews" :key="idx">
        <p  @click="detail(review)">{{ review.title }}</p>
      </div>
    </div>
  

    
  </div>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  name: "ReviewList",
  // 받아온 게시글 데이터의 유무를 위해서 변수 정의
  data: function(){
    return{
      movietitle: this.$store.state.movieInfo.title,
      check: this.$store.state.reviews
    }
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
      console.log(this.check)
      this.$router.push({
        name: "ReviewDetail",
        params: {
          reviewId: review.id,
        },
      });
    },
  },

  computed: {
    ...mapGetters(["reviews"]),
  },
};
</script>

<style>
</style>