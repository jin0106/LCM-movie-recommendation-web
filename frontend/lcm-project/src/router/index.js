import Vue from 'vue'
import VueRouter from 'vue-router'
import Signup from '@/views/accounts/Signup'
import Login from '@/views/accounts/Login'
import Profile from '@/views/accounts/Profile'
import Movies from '@/views/movies/Movies'
import MovieSearchResult from '@/components/movies/MovieSearchResult'
import MovieMyList from '@/components/movies/MovieMyList'
import Home from '@/views/mainpage/Home'
import Community from '@/views/community/Community'
import ReviewDetail from '@/components/community/ReviewDetail'
import ReviewForm from '@/components/community/ReviewForm'
import ReviewUpdated from '@/components/community/ReviewUpdate'

Vue.use(VueRouter)

const routes = [
  {
    path:'/home',
    name:'Home',
    component:Home,
  },
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
    props:true,
  },
  {
    path:'/community/create',
    name: 'ReviewForm',
    component: ReviewForm,
  },
  {
    path:'/community/update/:reviewId',
    name:'ReviewUpdate',
    component: ReviewUpdated,
  },
  {
    path:'/movies',
    name: "Movies",
    component: Movies,
  },

  {
    path:'/movies/searchresult/',
    name: 'MovieSearchResult',
    component : MovieSearchResult
  },
  {
    path:'/movies/mylist/',
    name: 'MovieMyList',
    component : MovieMyList
  },
  



]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router