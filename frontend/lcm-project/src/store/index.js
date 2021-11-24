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
    genreMovies: {
      Adventure : [],
      Fantasy : [],
      Animation : [],
      Drama : [],
      Horror : [],
      Action : [],
      Comedy : [],
      History : [],
      Western : [],
      Thriller : [],
      Crime : [],
      Documentary : [],
      ScienceFiction : [],
      Mystery : [],
      Music : [],
      Romance : [],
      Family : [],
      War : [],
      TVMovie : [],
    },
    searchMovies:[],
    value:'',
    myList:[],
    mainMovie:[],
    trailer:'',
    watched:[],
    basedOnMyList:[],
    watchedMovies:[]


    
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
      const index = state.reviews.indexOf(data)
      state.reviews.slice(index,1)
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
    },
    GET_MY_LIST_MOVIES(state,data){
      state.basedOnMyList = data
    },
    GET_GENREMOVIES(state,data){
      switch(data['genre']) {
        case 'Adventure' : {
          state.genreMovies.Adventure = data['movie']
          break
        }
        case 'Fantasy' : {
          state.genreMovies.Fantasy = data['movie']
          break
        }
        case 'Animation' : {
          state.genreMovies.Animation = data['movie']
          break
        }
        case 'Drama' : {
          state.genreMovies.Drama = data['movie']
          break
        }
        case 'Horror' : {
          state.genreMovies.Horror = data['movie']
          break
        }
        case 'Action' : {
          state.genreMovies.Action = data['movie']
          break
        }
        case 'Comedy' : {
          state.genreMovies.Comedy = data['movie']
          break
        }
        case 'History' : {
          state.genreMovies.History = data['movie']
          break
        }
        case 'Western' : {
          state.genreMovies.Western = data['movie']
          break
        }
        case 'Thriller' : {
          state.genreMovies.Thriller = data['movie']
          break
        }
        case 'Crime' : {
          state.genreMovies.Crime = data['movie']
          break
        }
        case 'Documentary' : {
          state.genreMovies.Documentary = data['movie']
          break
        }
        case 'Science Fiction' : {
          state.genreMovies.ScienceFiction = data['movie']
          break
        }
        case 'Mystery' : {
          state.genreMovies.Mystery = data['movie']
          break
        }
        case 'Music' : {
          state.genreMovies.Music = data['movie']
          break
        }
        case 'Romance' : {
          state.genreMovies.Romance = data['movie']
          break
        }
        case 'Family' : {
          state.genreMovies.Family = data['movie']
          break
        }
        case 'War' : {
          state.genreMovies.War = data['movie']
          break
        }
        case 'TV Movie' : {
          state.genreMovies.TVMovie = data['movie']
          break
        }
      }
    },
    GET_SEARCHMOVIES(state,data){
      state.searchMovies = data
    },
    SENDING_VALUE(state, data){
      state.value = data
    },
    MY_LIST(state,data){
      state.myList=data
    },
    MAIN_MOVIE(state,data){
      state.mainMovie= data
    },
    GET_VIDEO(state,data){
      state.trailer = data
    },
    WATCHED_LIST(state,data){
      state.watched=data
    },
    // 봤던 영화 기반 추천 데이터
    GET_WATCHED_MOVIES(state,data){
      state.watchedMovies=data
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
    deleteReview:function({dispatch}, data){
      const header = {
        Authorization: `Bearer ${localStorage.getItem('JWT')}`,
      };
      axios({
        method: "delete",
        url: `${SERVER_URL}communities/${data['reviewId']}`,
      })
        .then((res) => {
          console.log(res)
          dispatch("getReviews", header)
        })
        .catch((err) => {
          console.log(err);
        });
    },
    CreateReview({commit,dispatch}, item){
      const header = {
        Authorization: `Bearer ${localStorage.getItem('JWT')}`,
      };
      axios({
        method: "POST",
        url: `${SERVER_URL}communities/`,
        data: item.info,
        headers: item.token,
      })
        .then(() => {
          commit('CREATE_REVIEW')
          dispatch("getReviews", header)
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
    getMovieInfo({commit,dispatch}, data){
      commit('GET_MOVIEINFO', data)
      // console.log(data)
      dispatch('getVideo',data)

    },
    // 유저 프로필 장르 기반으로 영화 받아오기
    getUserMovies({commit}, token){
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
      
    },
    // 단순 장르 기반으로 영화 받아오기
    GenreMovies({commit}, data){
      axios({
        method: "GET",
        url: `${SERVER_URL}movies/genre_recommend/`,
        headers: data['token'],
        params: {
          genre: data['genre'],
          orderby : data['orderby'],
          direction : data['direction']
        }
      })
        .then((res) => {
          const response = {
            movie : res.data,
            genre : data['genre'],
          }
          commit('GET_GENREMOVIES', response)
        })
        .catch((err) => {  
          console.log(err)
        });
    },
    searchMovies({commit}, data){
      commit('GET_SEARCHMOVIES', data)
    },
    sendingValue({commit}, data){
      commit('SENDING_VALUE', data)
    },
    getMyList({commit},token) {
      axios({
        method: "get",
        url: `${SERVER_URL}movies/wish_list/`,
        headers: token,
      })
        .then((res) => {
          commit('MY_LIST',res.data)
        })
        .catch((err) => {
          console.log(err);
        });
    },
    watchedList({commit},token) {
      axios({
        method: "get",
        url: `${SERVER_URL}movies/watched_movie/`,
        headers: token,
      })
        .then((res) => {
          commit('WATCHED_LIST',res.data)
        })
        .catch((err) => {
          console.log(err);
        });
    },
    
    mainMovie({commit}) {
      axios({
        method: "GET",
        url: `${SERVER_URL}movies/main_movies/`,
      })
        .then((res) => {
          commit('MAIN_MOVIE',res.data)
          // this.MainMovie = _.sample(res.data);
          // this.MainMovie = res.data[4];
        })
        .catch((err) => {
          console.log(err);
        });
    },
    getVideo({commit},movie) {
      const token = localStorage.getItem("JWT");
      const header = {
        Authorization: `Bearer ${token}`,
      };
      axios({
        method: "post",
        url: `${SERVER_URL}movies/trailer/`,
        headers: header,
        data :{ 
          q:movie.title}
      })
        .then((res) => {
          console.log(movie);
          console.log(res)
          commit('GET_VIDEO', res.data)
        })
        .catch((err) => {
          console.log(movie.title)
          console.log(err);
        });
    },
    // mylist 기반으로 영화 추천 받기
    basedOnMyList({commit}, token){
      axios({
        method:'get',
        url:`${SERVER_URL}movies/wish_list_recommend/`,
        headers:token,
      })
      .then((res =>{
        commit('GET_MY_LIST_MOVIES', res.data)
      }))
      .catch((err =>{
        console.log(err)
      }))
    },
    // 봤던영화 기반으로 추천
    basedOnWatched({commit}, token){
      axios({
        method:'get',
        url:`${SERVER_URL}movies/watched_recommend/`,
        headers:token,
      })
      .then((res =>{
        commit('GET_WATCHED_MOVIES', res.data)
      }))
      .catch((err =>{
        console.log(err)
      }))
    },
   
  },
  getters: {
    reviews: function(state){
      return state.reviews
    },
    totalMovieList: function(state){
      return _.sampleSize(state.totalMovieList,10)
    },
    allMovies(state){
      return state.totalMovieList
    },
    WeatherMovies(state){
      return state.weatherMovies
    },
    userMovies(state){
      return _.sampleSize(state.userMovies,10)
    },
    genreMovies(state){
      return state.genreMovies
    },
    genreMovies1(state){
      return state.genreMovies
    },
    SearchResultMovies(state){
      return state.searchMovies
    },
    currentUser(state){
      return state.getUserName
    },
    currentMovie(state){
      return state.movieInfo
    },
    myList(state){
      return state.myList
    },
    mainMovie(state){
      return _.sample(state.mainMovie)
    },
    trailer(state){
      return state.trailer
    },
    watchedList(state){
      return state.watched
    },
    myListRCMD(state){
      return state.basedOnMyList
    },
    watchedRCMD(state){
      return state.watchedMovies
    }
  

    }
  })