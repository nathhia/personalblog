import Auth from "./pages/Auth.vue";
import ListPosts from './pages/ListPosts.vue'
import RegisterUser from './pages/NewUser.vue'
import VueRouter from 'vue-router'

const Routes =[
  {
    path: '/auth',
    name: 'Auth',
    component: Auth,
    // meta: {
    //   requiresAuth: false,
    // }
  },
  {
    path: '/',
    name: 'ListPosts',
    component: ListPosts,
    // meta: {
    //   requiresAuth: true,
    // }
  },
  {
    path: '/register',
    name: 'RegisterUser',
    component: RegisterUser,
    // meta: {
    //   requiresAuth: false,
    // }
  },
]

export default new VueRouter({
  mode:'history',
  routes: Routes
})
