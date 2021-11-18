import Vue from 'vue'
import VueRouter from 'vue-router'
import Signup from '@/views/accounts/Signup'
import Login from '@/views/accounts/Login'
import temp from '@/views/accounts/temp'
import Profile from '@/views/accounts/Profile'
import ReviewDetail from '@/views/communities/ReviewDetail'
import ReviewList from '@/views/communities/ReviewList'

import CreateReview from '@/views/communities/CreateReview'


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
    path: '/communities',
    name: 'ReviewList',
    component: ReviewList,
  },
  {
    path: '/profile',
    name: 'Profile',
    component: Profile,
  },
  {
    path:'/communities/:reviewId',
    name:'ReviewDetail',
    component: ReviewDetail,
  },
  {
    path:'/communities/create/:',
    name:'CreateReview',
    component: CreateReview,
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
