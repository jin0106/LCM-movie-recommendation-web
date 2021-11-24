<template>
  <div class="community">
    <header>
      <h3>Community</h3>
    </header>
    <div class="table" v-if="reviews.length > 0">
      <table>
        <thead>
          <tr>
            <th class="num">No.</th>
            <th class="title">Title</th>
            <th class="writer">User</th>
            <th class="date">Date</th>
          </tr>
        </thead>
        <tbody v-if="reviews.length > 0">
          <tr v-for="review in reviews" :key="review.id">
            <td>{{ review.id }}</td>
            <td @click="detail(review)">{{ review.title }}</td>
            <td class="comment-writer">{{ review.user.username }}</td>
            <td>{{ review.created_at.substr(0, 10) }}</td>
          </tr>
        </tbody>
        <div v-else>
          <p>작성된 글이 없습니다</p>
        </div>
      </table>

      <button class="write-btn" @click="movieCreate">글 작성</button>
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
</style>