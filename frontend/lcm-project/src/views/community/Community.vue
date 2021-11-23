<template>
  <div class="community">
    <header>
      <h3>Community</h3>
      <h5>영화 제목 : {{ movietitle }}</h5>
    </header>
    <div v-if="reviews.length > 0">
      <table>
        <thead>
          <tr>
            <th class="num">No.</th>
            <th class="title">제목</th>
            <th class="writer">작성자</th>
            <th class="date">날짜</th>
          </tr>
        </thead>
        <tbody v-if="reviews.length > 0">
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

      <button class="write" @click="movieCreate">글 작성</button>
    </div>
    <div v-else>
      작성된 글이 없습니다
      <button class="write-btn" @click="movieCreate">글 작성</button>
    </div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
export default {
  name: "community",
  data: function () {
    return {
      movietitle: this.$store.state.movieInfo.title,
    };
  },

  methods: {
    movieCreate() {
      this.$router.push({ name: "ReviewForm" });
    },
    detail: function (review) {
      this.$router.push({
        name: "ReviewDetail",
        params: {
          reviewId: review.id,
          review: review,
        },
      });
    },
  },
  created() {
    this.$store.dispatch("getReviews", this.$store.state.token);
  },
  computed: {
    ...mapGetters(["reviews"]),
  },
};
</script>

<style scoped src='./reviewlist.css'>
.community {
  width: 100%;
  margin-top: 5rem;
  padding: 0 3rem;
  display: flex;
  flex-direction: column;
}
.write {
  margin-top: 1rem;
  border: none;
  border-radius: 8%;
}

.write-btn {
  margin-top: 1rem;
  border: none;
  border-radius: 8%;
  width: 4rem;
  position: relative;
  right: 0;
}
</style>