import Vue from 'vue'
import VueRouter from 'vue-router'
import Signup from '@/views/accounts/Signup'
import Login from '@/views/accounts/Login'
import temp from '@/views/accounts/temp'
import Profile from '@/views/accounts/Profile'
import Community from '@/views/community/Community'
import ReviewDetail from '@/components/community/ReviewDetail'
import ReviewForm from '@/components/community/ReviewForm'

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
    path:'community/create',
    name: 'ReviewForm',
    component: ReviewForm,
  }
  
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
