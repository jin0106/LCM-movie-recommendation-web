import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    reviews: [],
    getUserName:'',

  },
  mutations: {
    GET_REVIEWS: function(state, data){
      state.reviews = data
    },
    CREATE_REVIEWS(state,res){
      state.reviews.push(res)
    },
    DELETE_REVIEW: function(state,data){
      state.reviews.pop(data)
    },
    GET_USERNAME: function(state, data){
      state.getUserName = data

    }
  },
  actions: {
    // 리뷰 목록 가져오기
    getReviews({commit}, header) {
      axios({
        method: "get",
        url: "http://127.0.0.1:8000/communities/",
        headers: header,
      })
        .then((res) => {
          // console.log(res.data);
          commit('GET_REVIEWS', res.data)
        })
        .catch((err) => {
          console.log(err);
        });
    },
    deleteReview:function({commit}, data){
      axios({
        method: "delete",
        url: `http://127.0.0.1:8000/communities/${data}`,
      })
        .then((res) => {
          commit('DELETE_REVIEW', res);
        })
        .catch((err) => {
          console.log(err);
          console.log(data)
        });
    },
    CreateReview({commit}, item){
      axios({
        method: "POST",
        url: "http://127.0.0.1:8000/communities/",
        data: this.item.reviewItem,
        headers: item.token,
      })
        .then(() => {
          commit('CREATE_REVIEW')
          this.$router.push({name:'Community'})
        })
        .catch((err) => {
          console.log(err);
        });
    },

    getUserName : function({commit}, data){
      commit('GET_USERNAME',data)
    }
  },
  getters: {
    getUserName : function(state){
      return state.getUserName
    },
    reviews(state){
      return state.reviews
    }
    }
  })