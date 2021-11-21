<template>
  <div id="ReviewList">
    <table>
      <thead>
        <tr>
          <th class="num">No.</th>
          <th class="title">제목</th>
          <th class="writer">작성자</th>
          <th class="date">날짜</th>
        </tr>
      </thead>
      <tbody v-if="reviews.length">
        <tr v-for="review in reviews" :key="review.id">
          <td>{{ review.id }}</td>
          <td @click="detail(review)">{{ review.title }}</td>
          <td>{{ review.user.username }}</td>
          <td>{{ review.created_at }}</td>
        </tr>
      </tbody>
      <div v-else>
        <p>작성된 글이 없습니다</p>
      </div>
    </table>
  </div>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  name: "ReviewList",
  // 받아온 게시글 데이터의 유무를 위해서 변수 정의
  data: function () {
    return {
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
    detail: function (review) {
      this.$router.push({
        name: "ReviewDetail",
        params: {
          reviewId: review.id,
        },
      });
    },
  },
  // 처음과 업데이트될 때 리뷰 리스트 다시 불러오기
  created() {
    this.$store.dispatch("getReviews", this.setHeader());
  },
  beforemount() {
    this.$store.dispatch("getReviews", this.setHeader());
  },
  computed: {
    ...mapGetters(["reviews"]),
  },
};
</script>

<style scoped src='./css/reviewlist.css'>
</style>


cursor: url("data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjgiIGhlaWdodD0iMjciIHZpZXdCb3g9IjAgMCAyOCAyNyIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZD0iTTcuODI4NDMgMTIuNDg1M0M2LjI2NjMzIDEwLjkyMzIgNi4yNjYzMyA4LjM5MDUzIDcuODI4NDMgNi44Mjg0M1Y2LjgyODQzQzkuMzkwNTIgNS4yNjYzNCAxMS45MjMyIDUuMjY2MzQgMTMuNDg1MyA2LjgyODQzTDI0Ljc5OSAxOC4xNDIxQzI2LjM2MTEgMTkuNzA0MiAyNi4zNjExIDIyLjIzNjkgMjQuNzk5IDIzLjc5OVYyMy43OTlDMjMuMjM2OSAyNS4zNjExIDIwLjcwNDIgMjUuMzYxMSAxOS4xNDIxIDIzLjc5OUw3LjgyODQzIDEyLjQ4NTNaIiBmaWxsPSJibGFjayIvPgo8cGF0aCBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGNsaXAtcnVsZT0iZXZlbm9kZCIgZD0iTTI0LjA5MTkgMTguODQ5MkwxMi43NzgyIDcuNTM1NTRDMTEuNjA2NiA2LjM2Mzk3IDkuNzA3MTEgNi4zNjM5NyA4LjUzNTUzIDcuNTM1NTRDNy4zNjM5NiA4LjcwNzExIDcuMzYzOTYgMTAuNjA2NiA4LjUzNTUzIDExLjc3ODJMMTkuODQ5MiAyMy4wOTE5QzIxLjAyMDggMjQuMjYzNSAyMi45MjAzIDI0LjI2MzUgMjQuMDkxOSAyMy4wOTE5QzI1LjI2MzUgMjEuOTIwMyAyNS4yNjM1IDIwLjAyMDggMjQuMDkxOSAxOC44NDkyWk03LjgyODQzIDYuODI4NDNDNi4yNjYzMyA4LjM5MDUzIDYuMjY2MzMgMTAuOTIzMiA3LjgyODQzIDEyLjQ4NTNMMTkuMTQyMSAyMy43OTlDMjAuNzA0MiAyNS4zNjExIDIzLjIzNjkgMjUuMzYxMSAyNC43OTkgMjMuNzk5QzI2LjM2MTEgMjIuMjM2OSAyNi4zNjExIDE5LjcwNDIgMjQuNzk5IDE4LjE0MjFMMTMuNDg1MyA2LjgyODQzQzExLjkyMzIgNS4yNjYzNCA5LjM5MDUyIDUuMjY2MzQgNy44Mjg0MyA2LjgyODQzWiIgZmlsbD0id2hpdGUiLz4KPHBhdGggZD0iTTkuMjQyNjQgMTEuMDcxMUM4LjQ2MTYgMTAuMjkgOC40NjE2IDkuMDIzNyA5LjI0MjY0IDguMjQyNjVWOC4yNDI2NUMxMC4wMjM3IDcuNDYxNiAxMS4yOSA3LjQ2MTYgMTIuMDcxMSA4LjI0MjY1TDE0LjE5MjQgMTAuMzY0QzE0Ljk3MzQgMTEuMTQ1IDE0Ljk3MzQgMTIuNDExMyAxNC4xOTI0IDEzLjE5MjRWMTMuMTkyNEMxMy40MTEzIDEzLjk3MzQgMTIuMTQ1IDEzLjk3MzQgMTEuMzY0IDEzLjE5MjRMOS4yNDI2NCAxMS4wNzExWiIgZmlsbD0id2hpdGUiLz4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik01IDNINFY0SDNWNUg0VjZINVY1SDZWNEg1VjNaIiBmaWxsPSJibGFjayIvPgo8cGF0aCBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGNsaXAtcnVsZT0iZXZlbm9kZCIgZD0iTTMgMkg2VjNIN1Y2SDZWN0gzVjZIMlYzSDNWMlpNMyA1SDRWNkg1VjVINlY0SDVWM0g0VjRIM1Y1WiIgZmlsbD0id2hpdGUiLz4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik0zIDEwSDJWMTFIMVYxMkgyVjEzSDNWMTJINFYxMUgzVjEwWiIgZmlsbD0iYmxhY2siLz4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik0xIDlINFYxMEg1VjEzSDRWMTRIMVYxM0gwVjEwSDFWOVpNMSAxMkgyVjEzSDNWMTJINFYxMUgzVjEwSDJWMTFIMVYxMloiIGZpbGw9IndoaXRlIi8+CjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgY2xpcC1ydWxlPSJldmVub2RkIiBkPSJNMTIgMUgxMVYySDEwVjNIMTFWNEgxMlYzSDEzVjJIMTJWMVoiIGZpbGw9ImJsYWNrIi8+CjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgY2xpcC1ydWxlPSJldmVub2RkIiBkPSJNMTAgMEgxM1YxSDE0VjRIMTNWNUgxMFY0SDlWMUgxMFYwWk0xMCAzSDExVjRIMTJWM0gxM1YySDEyVjFIMTFWMkgxMFYzWiIgZmlsbD0id2hpdGUiLz4KPC9zdmc+Cg=="), auto;