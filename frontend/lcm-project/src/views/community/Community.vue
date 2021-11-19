<template>
  <div class="community">
    <header>
      <h2>Reviwe Board</h2>
    </header>
    <div v-if="reviews.length > 0">
      <ReviewList />
    </div>
    <div v-else>작성된 글이 없습니다.</div>
    <button>글 작성</button>
  </div>
</template>

<script>
import ReviewList from "@/components/community/ReviewList.vue";
import { mapGetters } from "vuex";
export default {
  name: "community",
  components: {
    ReviewList,
  },
  computed: {
    ...mapGetters(["reviews"]),
  },
  created: function () {
    this.$store.dispatch("getReviews");
  },
};
</script>

<style>
</style>