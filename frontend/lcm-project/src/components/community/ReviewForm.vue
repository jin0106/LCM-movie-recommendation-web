<template>
  <div id="CreateReview">
    <div class="create">
      <h2>Create Review</h2>
    </div>
    <div class="review-create">
      <div class="data">
        <h4 class="movie-title">Movie : {{ movietitle }}</h4>
        <hr />
        <div class="title">
          <label for="title">Title : </label>
          <input v-model="info.title" type="text" />
        </div>
        <br />
        <div class="ratings">
          <span>Ratings:</span>
          <div class="star-rating">
            <input
              type="radio"
              id="5-stars"
              name="rating"
              value="5"
              v-model="info.score"
            />
            <label for="5-stars" class="star pr-4">★</label>
            <input
              type="radio"
              id="4-stars"
              name="rating"
              value="4"
              v-model="info.score"
            />
            <label for="4-stars" class="star">★</label>
            <input
              type="radio"
              id="3-stars"
              name="rating"
              value="3"
              v-model="info.score"
            />
            <label for="3-stars" class="star">★</label>
            <input
              type="radio"
              id="2-stars"
              name="rating"
              value="2"
              v-model="info.score"
            />
            <label for="2-stars" class="star">★</label>
            <input
              type="radio"
              id="1-star"
              name="rating"
              value="1"
              v-model="info.score"
            />
            <label for="1-star" class="star">★</label>
          </div>
        </div>
        <div class="content">
          <label for="content">Content :</label>
          <textarea
            v-model="info.content"
            name="content"
            id="conent"
            cols="30"
            rows="10"
          ></textarea>
        </div>
      </div>
    </div>

    <div class="btn">
      <button @click="goList">목록</button>
      <button @click="Create">등록</button>
    </div>
  </div>
</template>

<script>
export default {
  name: "ReviewForm",
  data: function () {
    return {
      info: {
        movie: null,
        title: null,
        content: null,
        is_private: false,
        score: null,
      },
      movietitle: this.$store.state.movieInfo.title,
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
    goList: function () {
      this.$router.push({ name: "Community" });
    },
    Create() {
      this.info.movie = this.$store.state.movieInfo;
      this.info.score = parseInt(this.info.score);
      const reviewItem = {
        info: this.info,
        token: this.setHeader(),
      };
      this.$store.dispatch("CreateReview", reviewItem);
      this.movie = null;
      this.like_users = null;
      this.title = null;
      this.content = null;
      this.is_private = false;
      this.score = null;
      this.$router.push({ name: "Community" });
    },
  },
};
</script>

<style scoped src='./css/reviewform.css'>
</style>