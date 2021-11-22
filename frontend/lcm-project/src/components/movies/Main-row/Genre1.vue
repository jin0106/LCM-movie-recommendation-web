<template>
  <div id="Genre1">
    <div class="contents">
      <p class="title">How about {{ getgenre }} movies?</p>
      <div v-if="genreMovies" class="div-img">
        <ModalView v-if="isModal" @close-modal="isModal = false">
          <Content movie="this.movie" />
        </ModalView>
        <img
          @click="createMovieReview(movie)"
          v-for="(movie, idx) in genreMovies[getgenre]"
          :key="idx"
          class="poster"
          :v-model="movie.poster_path"
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
  name: "Genre1",
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
    GenreMovies: function () {
      // direction이 true면 오름차순 false면 내림차순
      const data1 = {
        token: this.$store.state.token,
        genre: "Adventure",
        orderby: "random",
        direction: true,
      };
      this.getgenre = data1["genre"];
      this.$store.dispatch("GenreMovies", data1);
    },
    GenreMovie: function (data) {
      // direction이 true면 오름차순 false면 내림차순

      this.getgenre = data["genre"];
      this.$store.dispatch("GenreMovies", data);
    },
    createMovieReview: function (data) {
      this.isModal = true;
      this.$store.dispatch("getMovieInfo", data);
    },
  },
  computed: {
    ...mapGetters(["genreMovies"]),
  },

  created: function () {
    this.GenreMovies();
  },
};
</script>

<style scoped src='../css/movielist.css'>
/* 전체 글자 색깔 마진 없애주기 */
</style>