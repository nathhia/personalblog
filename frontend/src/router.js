import Auth from "./pages/Auth.vue";
import ListPosts from './pages/ListPosts.vue'
import VueRouter from 'vue-router'

const Routes =[
  {
    path: '/auth',
    name: 'Auth',
    component: Auth,
  },
  {
    path: '/',
    name: 'ListPosts',
    component: ListPosts,
  },
]

export default new VueRouter({
  mode:'history',
  routes: Routes
}
)
// export default[
//   {
//     path: '/auth',
//     name: 'Auth',
//     component: Auth
//   },
//   {
//     path: '/',
//     name: 'ListPosts',
//     component: ListPosts
//   },

// ]