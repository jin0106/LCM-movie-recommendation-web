<template>
  <div id="Movies">
    <header>
      <div class="sort">
        <span>Sort</span>
        <select @change="runSort" v-model="data.orderby" name="select" id="">
          <option value="" selected disabled hidden>Choose here</option>
          <option value="release_date">Year Released (desc)</option>
          <option value="-release_date">Year Released (asc)</option>
          <option value="popularity">Popularirty (desc)</option>
          <option value="-popularity">Popularirty (asc)</option>
          <option value="title">A-Z</option>
          <option value="-title">Z-A</option>
          <option value="vote_average">Ratings (desc)</option>
          <option value="-vote_average">Ratings (asc)</option>
          <option value="random">Random</option>
        </select>
      </div>
      <div>
        <genre-1 ref="Genre1" />
        <genre-2 ref="Genre2" />
        <genre-3 ref="Genre3" />
        <genre-4 ref="Genre4" />
        <genre-5 ref="Genre5" />
        <genre-6 ref="Genre6" />
        <genre-7 ref="Genre7" />
        <genre-8 ref="Genre8" />
        <genre-9 ref="Genre9" />
        <genre-10 ref="Genre10" />
        <genre-11 ref="Genre11" />
        <genre-12 ref="Genre12" />
      </div>
    </header>
  </div>
</template>

<script>
import Genre1 from "@/components/movies/Main-row/Genre1.vue";
import Genre2 from "../../components/movies/Main-row/Genre2.vue";
import Genre3 from "../../components/movies/Main-row/Genre3.vue";
import Genre4 from "../../components/movies/Main-row/Genre4.vue";
import Genre5 from "../../components/movies/Main-row/Genre5.vue";
import Genre6 from "../../components/movies/Main-row/Genre6.vue";
import Genre7 from "../../components/movies/Main-row/Genre7.vue";
import Genre8 from "../../components/movies/Main-row/Genre8.vue";
import Genre9 from "../../components/movies/Main-row/Genre9.vue";
import Genre10 from "../../components/movies/Main-row/Genre10.vue";
import Genre11 from "../../components/movies/Main-row/Genre11.vue";
import Genre12 from "../../components/movies/Main-row/Genre12.vue";

// import MoviesRecommend from "@/components/movies/MoviesRecommend.vue";

export default {
  name: "Movies",
  data: function () {
    return {
      orderby: "",
      data: {
        token: this.$store.state.token,
        genre: "Adventure",
        orderby: "",
        direction: true,
      },
    };
  },
  methods: {
    value() {
      this.$store.dispatch("", this.orderby);
    },
    runSort() {
      this.$refs.Genre1.GenreMovie(this.data);
      this.$refs.Genre2.GenreMovie(this.data);
      this.$refs.Genre3.GenreMovie(this.data);
      this.$refs.Genre4.GenreMovie(this.data);
      this.$refs.Genre5.GenreMovie(this.data);
      this.$refs.Genre6.GenreMovie(this.data);
      this.$refs.Genre7.GenreMovie(this.data);
      this.$refs.Genre8.GenreMovie(this.data);
      this.$refs.Genre9.GenreMovie(this.data);
      this.$refs.Genre10.GenreMovie(this.data);
      this.$refs.Genre11.GenreMovie(this.data);
      this.$refs.Genre12.GenreMovie(this.data);
    },
  },
  components: {
    Genre1,
    Genre2,
    Genre4,
    Genre3,
    Genre5,
    Genre6,
    Genre9,
    Genre8,
    Genre7,
    Genre10,
    Genre11,
    Genre12,
  },
};
</script>

<style>
#Movies {
  margin-top: 5rem;
  padding: 0 2rem;
  background-color: black;
}
select {
  padding: 5px;
  border: 0.5px solid white;
  color: gray;
  background-color: black;
  -webkit-overflow-scrolling: none;
}
.sort {
  padding: 0 1rem;
  display: flex;
  justify-content: flex-end;
  align-items: center;
  color: white;
}
.sort span {
  margin-right: 10px;
}
</style>