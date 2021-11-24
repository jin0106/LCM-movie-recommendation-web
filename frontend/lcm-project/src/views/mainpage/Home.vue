<template>
  <div id="home">
    <div v-if="currentUser">
      <div id="player">
        <iframe
          class="Main-Movie"
          :src="mainMovie.src"
          allowfullscreen="false"
          frameborder="0"
        ></iframe>
        <div class="movie-title">
          <h3>{{ mainMovie.movie.title }}</h3>
          <p></p>
          <ModalView v-if="isModal" @close-modal="isModal = false">
            <Content />
          </ModalView>

          <button class="more-info" @click="createMovieReview(mainMovie.movie)">
            More Info
          </button>
        </div>
      </div>

      <Main />
    </div>
    <div v-else>
      <movie-guest />
    </div>
  </div>
</template>

<script>
import Content from "@/components/movies/Modal/Content";
import ModalView from "@/components/movies/Modal/ModalView";
import Main from "../movies/Main.vue";
import { mapGetters } from "vuex";
export default {
  name: "home",
  components: { Main, Content, ModalView },
  data: function () {
    return {
      currentUser: this.$store.state.getUserName,
      MainMovie: null,
      isModal: false,
    };
  },
  methods: {
    setHeader: function () {
      const token = localStorage.getItem("JWT");
      const header = {
        Authorization: `Bearer ${token}`,
      };
      return header;
    },
    createMovieReview: function (data) {
      this.isModal = true;
      this.$store.dispatch("getMovieInfo", data);
    },
  },
  computed: {
    ...mapGetters(["mainMovie"]),
  },
};
</script>

<style scoped>
#home {
  width: 100%;
  background-color: black;
}
.Main-Movie {
  /* margin-top: 5rem; */
  margin-bottom: 0;
  padding: 0 3rem;
  width: 100%;
  height: 600px;
  position: relative;
}
.movie-title {
  position: absolute;
  top: 400px;
  left: 3rem;
}
.more-info {
  background-color: rgb(102, 124, 135, 0.5);
  color: #ffffff;
  font-weight: 600;
  width: 100px;
  height: 40px;
  border-radius: 10px;
  border: none;
}

@media screen and (max-width: 375px) {
  .Main-Movie {
    width: 100%;
    height: 250px;
  }
  .movie-title {
    top: 10rem;
  }
  .movie-title h3 {
    font-size: 15px;
  }
  .more-info {
    width: 80px;
    height: 30px;
    font-size: 12px;
  }
}
</style>