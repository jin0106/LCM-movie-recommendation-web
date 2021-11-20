<template>
  <div id="CommentForm">
    <div>
      <form>
        <input v-model.trim="content" type="text" id="comments" />
        <button @click="Comment">작성</button>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  name: "CommentForm",
};
</script>

<style>
</style>