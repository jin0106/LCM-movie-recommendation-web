<template>
  <div id="MovieWatchedList">
    <div class="contents">
      <h3 class="my-list">Watched List</h3>
      <div v-if="watchedList" class="div-img">
        <ModalView v-if="isModal" @close-modal="isModal = false">
          <Content />
        </ModalView>

        <img
          @click="createMovieReview(movie)"
          v-for="(movie, idx) in watchedList"
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
import Content from "@/components/movies/Modal/Content";
import ModalView from "@/components/movies/Modal/ModalView";
import { mapGetters } from "vuex";
export default {
  name: "MovieWathcedList",
  data: function () {
    return {
      movieList: [],
      isModal: false,
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
    getMyList() {
      this.$store.dispatch("getMyList", this.$store.state.token);
    },
  },
  created() {
    this.getMyList();
  },
  computed: {
    ...mapGetters(["watchedList"]),
  },
};
</script>

<style scoped src='./css/mylist.css'>
</style>