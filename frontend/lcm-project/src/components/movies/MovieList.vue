<template>
  <div id="MovieList">
    <h2>MovieList</h2>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
export default {
  name : "MovieList",
  data: function () {
    return {
      movieList: {
        
      }
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
    }
  },
  computed: {
    ...mapGetters(['getUserName']),
  },
  created: function(){
    this.getMovieList()
  }
}
</script>

<style>

</style>