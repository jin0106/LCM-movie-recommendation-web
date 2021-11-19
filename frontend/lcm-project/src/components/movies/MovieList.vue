<template>
  <div id="MovieList">
    <h2>MovieList</h2>
    <div v-if="totalMovieList.length">
      <b-container fluid class="p-4 bg-dark">
          <b-row>
            <b-col>
              <div v-for="(movie, idx) in totalMovieList" :key="idx">
                <b-img class="max-small" thumbnail fluid :src="movie.poster_path" alt="thumnail"></b-img>
              </div>
            </b-col>
          </b-row>
      </b-container>
    </div>

    <div v-else>
      <div>
        <b-spinner style="width: 3rem; height: 3rem;" label=""></b-spinner>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";


export default {
  name : "MovieList",
  data: function () {
    return {
      movieList: [],
        
    }
  },
  methods: {
    setHeader: function () {
      const token = localStorage.getItem("JWT");
      const header = {
        Authorization: `Bearer ${token}`,
      };
      return header;
    },

    getMovieList: function() {
      this.$store.dispatch('getMovieList', this.setHeader())
    },
    check: function() {
      this.movieList = this.$store.state.totalMovieList
    }


  },
  computed: {
    ...mapGetters(["totalMovieList"])
  
  },

  created: function(){
    this.getMovieList()
    this.check()
  }
}
</script>

<style>
.max-small {
    width: auto; height: auto;
    max-width: 30;
    max-height: 100px;
}
</style>