<template>
  <div id="MovieRandom">
    <div class="contents">
      <p class="title">How about these movies?</p>
      <div v-if="totalMovieList" class="div-img">
        <ModalView v-if="isModal" @close-modal="isModal = false">
          <Content movie="this.movie" />
        </ModalView>
        <img
          @click="createMovieReview(movie)"
          v-for="(movie, idx) in totalMovieList"
          :key="idx"
          class="poster"
          :src="movie.poster_path"
          alt="thumnail"
        />
      </div>

      <div v-else>
        <div>
          <b-spinner style="width: 3rem; height: 3rem" label=""></b-spinner>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
import Content from "@/components/movies/Modal/Content";
import ModalView from "@/components/movies/Modal/ModalView";
export default {
  name: "MovieRandom",
  data: function () {
    return {
      movieList: [],
      isModal: false,
      movie: null,
    };
  },
  components: {
    Content,
    ModalView,
  },
  methods: {
    getMovieList: function () {
      this.$store.dispatch("getMovieList", this.$store.state.token);
    },
    createMovieReview: function (data) {
      this.isModal = true;
      this.$store.dispatch("getMovieInfo", data);
      //this.$router.push({ name: "Community" });
    },
  },
  computed: {
    ...mapGetters(["totalMovieList"]),
  },

  created: function () {
    this.getMovieList();
  },
};
</script>

<style scoped src='./css/movielist.css'>
/* 전체 글자 색깔 마진 없애주기 */
</style>