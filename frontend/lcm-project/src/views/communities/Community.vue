<template>
  <div class="community">
    <header>
      <h2>Reviwe Board</h2>
    </header>
    <ReviewList />
  </div>
</template>

<script>
import ReviewList from "@/components/community/ReviewList.vue";
export default {
  name: "community",
  components: {
    ReviewList,
  },
};
</script>

<style>
</style>