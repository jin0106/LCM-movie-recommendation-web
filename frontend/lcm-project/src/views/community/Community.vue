<template>
  <div class="community">
    <header>
      <h2>Reviwe Board</h2>
      <h2>영화 제목 : {{movietitle}}</h2>
    </header>
    <div v-if="reviews.length > 0">
      <ReviewList />
    </div>
    <div v-else>작성된 글이 없습니다.</div>
    <button @click="moveCreate">글 작성</button>
  </div>
</template>

<script>
import ReviewList from "@/components/community/ReviewList.vue";
import { mapGetters } from "vuex";
export default {
  name: "community",
    data: function(){
    return{
      movietitle: this.$store.state.movieInfo.title
    }
  },
  components: {
    ReviewList,
  },
  computed: {
    ...mapGetters(["reviews"]),
  },
  methods: {
    moveCreate() {
      this.$router.push({ name: "ReviewForm" });
    },
  },
  created: function () {
    const data = {
      token : this.$store.state.token,
      movie : this.$store.state.movieInfo
    }
    this.$store.dispatch("getReviews", data);
  },
};
</script>

<style>
</style>