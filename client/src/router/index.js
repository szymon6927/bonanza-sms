import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import Form from '@/components/Form'
import PrivatePolicy from '@/components/PrivatePolicy'
import Clients from '@/components/Clients'
import About from '@/components/About'
import Recommend from '@/components/Recommend'
import NotFound from '@/components/NotFound'
import AddOpinion from '@/components/AddOpinion'
import Reviews from '@/components/Reviews'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/form',
      name: 'Form',
      component: Form
    },
    {
      path: '/private-policy',
      name: 'PrivatePolicy',
      component: PrivatePolicy
    },
    {
      path: '/about',
      name: 'About',
      component: About
    },
    {
      path: '/clients',
      name: 'Clients',
      component: Clients
    },
    {
      path: '/recommend',
      name: 'Recommend',
      component: Recommend
    },
    {
      path: '/add-opinion',
      name: 'AddOpinion',
      component: AddOpinion
    },
    {
      path: '/reviews',
      name: 'Reviews',
      component: Reviews
    },
    {
      path: '*',
      name: 'NotFound',
      component: NotFound
    }
  ]
})
