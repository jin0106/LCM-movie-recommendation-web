<template>
  <div id="MovieBasedMyList">
    <div class="contents">
      <p class="title">Based on your List</p>
      <!-- <p>{{ myListRCMD }}</p> -->
      <div v-if="myListRCMD" class="div-img">
        <ModalView v-if="isModal" @close-modal="isModal = false">
          <Content movie="this.movie" />
        </ModalView>
        <img
          @click="createMovieReview(movie)"
          v-for="(movie, idx) in myListRCMD"
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
  name: "MovieBasedMyList",
  data: function () {
    return {
      genres: [],
      isModal: false,
      movie: null,
    };
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
  created() {
    this.$store.dispatch("basedOnMyList", this.$store.state.token);
  },
  computed: {
    ...mapGetters(["myListRCMD", "genreMovies"]),
  },
};
</script>

<style scoped src='./css/movielist.css'>
</style>