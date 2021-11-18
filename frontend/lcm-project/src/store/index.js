import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    reviewList: [],
    getUserName:'',

  },
  mutations: {
    GETREVIEWLIST: function(state, data){
      state.reviewList = data

    },
    GETUSERNAME: function(state, data){
      state.getUserName = data

    }
  },
  actions: {
    getReviewList: function({commit}, data){
      commit('GETREVIEWLIST',data)

    },
    getUserName : function({commit}, data){
      commit('GETUSERNAME',data)
    }
  },
  getters: {
    getUserName : function(state){
      return state.getUserName
    }
    }
  })
