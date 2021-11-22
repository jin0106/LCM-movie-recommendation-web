<template>
  <div id="MovieDetail">
    <div class="modal">
      <div class="modal_body">Modal</div>
    </div>
    <button @click="modal" class="btn-open-popup">Modal 띄우기</button>
  </div>
</template>

<script>
export default {
  name: "MovieDetail",
  methods: {
    modal() {
      const modal = document.querySelector(".modal");
      const body = document.body;
      modal.style.display = "block";
      body.style.overflow = "hidden";
    },
  },
};
</script>

<style>
#MovieDetail {
  margin-top: 5rem;
}
.modal {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  display: none;
  background-color: rgba(0, 0, 0, 0.4);
}
.modal.show {
  display: block;
}
.modal_body {
  position: absolute;
  top: 50%;
  left: 50%;
  width: 400px;
  height: 600px;
  padding: 40px;
  text-align: center;
  background-color: rgb(255, 255, 255);
  border-radius: 10px;
  box-shadow: 0 2px 3px 0 rgba(34, 36, 38, 0.15);
  transform: translateX(-50%) translateY(-50%);
}
</style>