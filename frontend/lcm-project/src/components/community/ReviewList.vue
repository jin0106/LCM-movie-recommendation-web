<template>
  <div id="ReviewList">
    <table>
      <thead>
        <tr>
          <th class="num">No.</th>
          <th class="title">제목</th>
          <th class="writer">작성자</th>
          <th class="date">날짜</th>
        </tr>
      </thead>
      <tbody v-if="reviews.length">
        <tr v-for="review in reviews" :key="review.id">
          <td>{{ review.id }}</td>
          <td @click="detail(review)">{{ review.title }}</td>
          <td>{{ review.user.username }}</td>
          <td>{{ review.created_at }}</td>
        </tr>
      </tbody>
      <div v-else>
        <p>작성된 글이 없습니다</p>
      </div>
    </table>
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
  beforemount() {
    this.$store.dispatch("getReviews", this.setHeader());
  },
  computed: {
    ...mapGetters(["reviews"]),
  },
};
</script>

<style scoped src='./css/reviewlist.css'>
</style>