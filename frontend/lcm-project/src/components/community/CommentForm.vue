<template>
  <div id="CommentForm">
    <div>
      <input @keyup.enter="createComment" v-model.trim="content" type="text" />
      <button @click="createComment">작성</button>
    </div>
  </div>
</template>

<script>
export default {
  name: "CommentForm",
  data: function(){
    return {
      reviewId: this.$route.params.reviewId,
      content : ''
    }
  },
  props: {
    review : Object
  },
  methods: {
    createComment: function(){
      const data = {
        token : this.$store.state.token,
        reviewId : this.reviewId,
        content : this.content,
        review: this.review,
      }
      this.$store.dispatch("createComment", data)
      this.content = ''
    }
  }
};
</script>

<style>
</style>