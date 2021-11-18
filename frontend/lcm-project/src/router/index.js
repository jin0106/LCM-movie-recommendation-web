import Vue from 'vue'
import VueRouter from 'vue-router'
import Signup from '@/views/accounts/Signup'
import Login from '@/views/accounts/Login'
import temp from '@/views/accounts/temp'
import Profile from '@/views/accounts/Profile'

import ReviewList from '@/views/community/ReviewList'
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
    path: '/community',
    name: 'ReviewList',
    component: ReviewList,
  },
  {
    path: '/profile',
    name: 'Profile',
    component: Profile,
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
