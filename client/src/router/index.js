import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Ping from '@/components/Ping'
import Form from '@/components/Form'
import PrivatePolicy from '@/components/PrivatePolicy'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/ping',
      name: 'Ping',
      component: Ping
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
    }
  ]
})
