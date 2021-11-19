<template>
  <div>
    <div class="contents">
      <p class="title">Based on your profile</p>
      <!-- <div class="posters" v-if="totalMovieList.length">
        <div class="div-img" v-for="(movie, idx) in totalMovieList" :key="idx">
          <img class="poster" :src="movie.poster_path" alt="thumnail" />
        </div> -->
      <!-- </div> -->

      <!-- <div v-else>
        <div>
          <b-spinner style="width: 3rem; height: 3rem" label=""></b-spinner>
        </div>
      </div> -->
    </div>
  </div>
</template>

<script>
export default {
  name: "UserRecommend",
  data: function () {
    return {
      genres: [],
    };
  },
  methods: {
    get_genres() {
      console.log(this.$store.state.userlikegenres);
    },
  },
  created() {
    this.get_genres();
  },
};
</script>

<style>
</style>