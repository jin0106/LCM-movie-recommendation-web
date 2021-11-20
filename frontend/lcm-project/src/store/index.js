import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import createPersistedState from "vuex-persistedstate"
import _ from 'lodash'
Vue.use(Vuex)
const SERVER_URL = process.env.VUE_APP_SERVER_URL


export default new Vuex.Store({
  plugins: [createPersistedState()],
  state: {
    reviews: [],
    getUserName:'',
    totalMovieList: [],
    userlikegenres:[],
    token:'',
    weatherMovies:[],
    movieInfo: [],
    review:'',
    userMovies:[],
  },
  mutations: {
    GET_REVIEWS: function(state, data){
      state.reviews = data
    },
    GET_REVIEW: function(state, data){
      state.review = data
    },
    CREATE_REVIEW(state,res){
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
    },
    GET_MOVIEINFO(state,data){
      state.movieInfo = data
    },
    GET_USER_MOVIES(state,data){
      state.userMovies = data
    }
  },
  actions: {
    // 리뷰 목록 가져오기
    getReviews({commit}, token) {
      axios({
        method: "GET",
        url: `${SERVER_URL}communities/`,
        headers: token,
      })
        .then((res) => {
          commit('GET_REVIEWS', res.data)
        })
        .catch((err) => {
          console.log(err);
        });
    },
    getReview({commit}, data) {
      axios({
        method: "GET",
        url: `${SERVER_URL}communities/review/`,
        headers: '',
        params: {
          movie_title: `${data['movie']['title']}`
        }
      })
        .then((res) => {
          commit('GET_REVIEW', res.data)
        })
        .catch((err) => {
          console.log(err);
        });
    },
    deleteReview:function({commit}, data){
      axios({
        method: "delete",
        url: `${SERVER_URL}communities/${data}`,
      })
        .then((res) => {
          commit('DELETE_REVIEW', res);
        })
        .catch((err) => {
          console.log(err);
        });
    },
    CreateReview({commit}, item){
      axios({
        method: "POST",
        url: `${SERVER_URL}communities/`,
        data: item.info,
        headers: item.token,
      })
        .then(() => {
          console.log('bbbbbbbbb')
          commit('CREATE_REVIEW')
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
        console.log(err)
      })
    },
    getLikeGenre: function ({commit},token) {
      axios({
        method: "get",
        url: `${SERVER_URL}accounts/likegenre/`,
        headers: token,
      })
        .then((res) => {
          const likeGenre = res.data;
          commit('GET_LIKEGENRE', likeGenre)
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
    },
    getMovieInfo({commit}, data){
      commit('GET_MOVIEINFO', data)
    },
    // 유저 프로필 장르 기반으로 영화 받아오기
    getUserMovies({commit},token){
      axios({
        method:'get',
        url:`${SERVER_URL}movies/user_recommend/`,
        headers:token,
      })
      .then((res =>{
        commit('GET_USER_MOVIES', res.data)
      }))
      .catch((err =>{
        console.log(err)
      }))
      
    }
  },
  getters: {
    reviews: function(state){
      return state.reviews
    },
    totalMovieList: function(state){
      return _.sampleSize(state.totalMovieList,10)
    },
    WeatherMovies(state){
      return state.weatherMovies
    },
    userMovies(state){
      return _.sampleSize(state.userMovies,10)
    }
    }
  })