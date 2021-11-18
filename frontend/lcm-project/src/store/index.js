import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    reviewList: [],
  },
  mutations: {
    GETREVIEWLIST: function(state, data){
      state.reviewList = data
    }
  },
  actions: {
    getReviewList: function({commit}, data){
      commit('GETREVIEWLIST',data)
    }
  },
  modules: {
  }
})
