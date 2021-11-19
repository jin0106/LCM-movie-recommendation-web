import Vue from 'vue'
import VueRouter from 'vue-router'
import Signup from '@/views/accounts/Signup'
import Login from '@/views/accounts/Login'
import temp from '@/views/accounts/temp'
import Profile from '@/views/accounts/Profile'
import Community from '@/views/community/Community'
import Movies from '@/views/movies/Movies'

import ReviewDetail from '@/components/community/ReviewDetail'
import ReviewForm from '@/components/community/ReviewForm'
import MovieDetail from '@/components/movies/MovieDetail'
import MovieList from '@/components/movies/MovieList'
import UserRecommend from '@/components/movies/UserRecommend'
import MoviesRecommend from '@/components/movies/MoviesRecommend'
Vue.use(VueRouter)

const routes = [
  {
    path: '/accounts/signup',
    name: 'Signup',
    component: Signup,
  },
  {
    path: '/accounts/login',
    name: 'Login',
    component: Login,
  },
  {
    path: '/temp',
    name: 'temp',
    component: temp,
  },
  {
    path: '/profile',
    name: 'Profile',
    component: Profile,
  },
  {
    path:'/community',
    name:'Community',
    component: Community,
  },
  {
    path:'/community/:reviewId',
    name:'ReviewDetail',
    component: ReviewDetail,
  },
  {
    path:'/community/create',
    name: 'ReviewForm',
    component: ReviewForm,
  },
  {
    path:'/Movies',
    name: "Movies",
    component: Movies,
  }
  ,
  {
    path:'/movies/MovieDetail',
    name: 'MovieDetail',
    component: MovieDetail,
  },
  {
    path:'/movies/MovieList',
    name: 'MovieList',
    component: MovieList,
  },
  {
    path:'/movies/UserRecommend',
    name: 'UserRecommend',
    component: UserRecommend,
  },
  {
    path:'/movies/MoviesRecommend',
    name: 'MoviesRecommend',
    component: MoviesRecommend,
  },

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router