import Vue from 'vue'
import Router from 'vue-router'
import About from './views/About'
import MovieDetail from './views/MovieDetail'
import Results from './views/Results'
import Login from './views/Login'
import Auth from '@/components/Auth'
import Movies from '@/components/Movies'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'Movies'
      component: Movies
    },
    {
      path: '/results',
      name: 'results',
      component: Results
    },
    {
      path: '/about',
      name: 'about',
      component: About
    },
    {
      path: '/moviedetail',
      name: 'moviedetail',
      component: MovieDetail
    },
      path: '/auth',
      name: 'Auth',
      component: Auth
  ]
})
