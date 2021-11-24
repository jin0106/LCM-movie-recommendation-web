<template>
  <div id="MovieMyList">
    <div class="contents">
      <h3 class="my-list">Results</h3>
      <div v-if="SearchResultMovies" class="div-img">
        <ModalView v-if="isModal" @close-modal="isModal = false">
          <Content />
        </ModalView>

        <img
          @click="createMovieReview(movie)"
          v-for="(movie, idx) in SearchResultMovies"
          :key="idx"
          class="poster"
          :src="movie.poster_path"
          alt="thumnail"
        />
      </div>

      <div v-else>
        <h2 class="fail">검색결과가 없습니다.</h2>
      </div>
    </div>
  </div>
</template>

<script>
import Content from "@/components/movies/Modal/Content";
import ModalView from "@/components/movies/Modal/ModalView";
import { mapGetters } from "vuex";
export default {
  name: "MovieSearchResult",
  data: function () {
    return {
      isModal: false,
    };
  },
  computed: {
    ...mapGetters(["SearchResultMovies"]),
  },
  components: {
    Content,
    ModalView,
  },
  methods: {
    createMovieReview: function (data) {
      this.isModal = true;
      this.$store.dispatch("getMovieInfo", data);
    },
  },
};
</script>

<style scoped src='./css/mylist.css'>
/* 전체 글자 색깔 마진 없애주기 */
</style>