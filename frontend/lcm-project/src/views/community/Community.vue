<template>
  <div class="community">
    <header>
      <h3>Community</h3>
      <h5>영화 제목 : {{ movietitle }}</h5>
    </header>
    <div v-if="reviews.length > 0">
      <ReviewList v-if="reviews.length" />
      <button class="write" @click="movieCreate">글 작성</button>
    </div>
    <div v-else>
      작성된 글이 없습니다
      <button class="write-btn" @click="movieCreate">글 작성</button>
    </div>
  </div>
</template>

<script>
import ReviewList from "@/components/community/ReviewList.vue";
import { mapGetters } from "vuex";
export default {
  name: "community",
  data: function () {
    return {
      movietitle: this.$store.state.movieInfo.title,
    };
  },
  components: {
    ReviewList,
  },
  computed: {
    ...mapGetters(["reviews"]),
  },
  methods: {
    movieCreate() {
      this.$router.push({ name: "ReviewForm" });
    },
  },
  created() {
    this.$store.dispatch("getReviews", this.$store.state.token);
  },
};
</script>

<style>
.community {
  width: 100%;
  margin-top: 5rem;
  padding: 0 3rem;
  display: flex;
  flex-direction: column;
}
.write {
  margin-top: 1rem;
  background: skyblue;
  border: none;
  border-radius: 8%;
}

.write-btn {
  margin-top: 1rem;
  background: skyblue;
  border: none;
  border-radius: 8%;
  width: 4rem;
  position: relative;
  right: 0;
}
</style>