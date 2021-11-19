import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import createPersistedState from 'vuex-persistedstate';
import _ from 'lodash'
Vue.use(Vuex)
const SERVER_URL = process.env.VUE_APP_SERVER_URL


export default new Vuex.Store({
  plugins: [
    createPersistedState()
  ],
  state: {
    reviews: [],
    getUserName:'',
    totalMovieList: [],
    userlikegenres:[],
    token:'',
    weatherMovies:[],
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
    },
    GET_MOVIELIST: function(state, data){
      state.totalMovieList = data
    },
    GET_LIKEGENRE: function(state, data){
      state.userlikegenres = data
    },
    GET_TOKEN(state, data){
      state.token = data
    },
    GET_WEATHERMOVIES(state,data){
      state.weatherMovies = data
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
        data: item.info,
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
    },
    getMovieList: function({commit}, data){
      axios({
        method: "GET",
        url : `${SERVER_URL}movies/`,
        headers: data
      })
      .then(res => {
        commit('GET_MOVIELIST', res.data)
      })
      .catch(err => {
        console.log('getmovieaction')
        console.log(err)
      })
    },
    getLikeGenre: function ({commit},token) {
      console.log('!!!!!!!!')
      axios({
        method: "get",
        url: `${SERVER_URL}accounts/likegenre/`,
        headers: token,
      })
        .then((res) => {
          const likeGenre = res.data;
          commit('GET_LIKEGENRE', likeGenre)
          console.log(this.likeGenre);
        })
        .catch((err) => {
          console.log(err);
        });
    },
    setHeader: function () {
      const token = localStorage.getItem("JWT");
      const header = {
        Authorization: `Bearer ${token}`,
      };
      this.commit('GET_TOKEN', header)
    },
    WeatherMovies({commit},token){
      axios({
        method:'get',
        url: `${SERVER_URL}movies/weather_recommend/`,
        headers: token,
      })
      .then((res) =>{
        commit('GET_WEATHERMOVIES', res.data)
      })
      .catch((err)=>{
        console.log(err)
      })
    }
  },
  getters: {
    getUserName : function(state){
      return state.getUserName
    },
    reviews: function(state){
      return state.reviews
    },
    totalMovieList: function(state){
      return _.sampleSize(state.totalMovieList,10)
    },
    WeatherMovies(state){
      return state.weatherMovies
    }
    }
  })