<template>
  <div class="Modal">
    <div class="overlay" @click="$emit('close-modal')"></div>
    <div class="modal-card">
      <slot />
    </div>
  </div>
</template>

<script>
export default {
  name: "Modal",
};
</script>

<style scoped>
/* Modal */
.Modal,
.overlay {
  width: 100%;
  height: 100%;
  position: fixed;
  left: 0;
  top: 0;
  z-index: 1;
  margin-top: 2rem;
}
.overlay {
  opacity: 0.5;
  background-color: black;
}
.modal-card {
  display: flex;
  justify-items: center;
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
  width: 600px;
  height: 700px;
  padding: 0 30px;
  background-color: black;
  min-height: 500px;
  z-index: 10;
  opacity: 1;
  border-radius: 10px;
}

@media screen and (max-width: 375px) {
  .Modal,
  .overlay {
    width: 100%;
    margin: 0;
  }

  .modal-card {
    width: 85%;
    height: 90%;
    overflow-y: scroll;
    border: 0.5px solid #4b4a54;
    padding: 0 1rem;
  }
}
</style>