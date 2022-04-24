// import Vue from 'vue'
// import VueRouter from 'vue-router'

// // COMPONENTS
// import Home from '../components/HelloWorld.vue'
// import Login from '../components/Login.vue'

// // VIEWS
// import Task from '../views'
// import About from '../views/AboutView.vue'
// import CustomerView from '../views/CustomerView.vue'
// import ProviderView from '../views/ProviderView.vue'
// import BankView from '../views/BankView.vue'


// Vue.use(VueRouter)

//   const routes = [
//   {
//     path: '/',
//     name: 'Home',
//     component: Home
//   },
//   {
//     path: '/about',
//     name: 'About',
//     component: About
//   },
//   {
//     path: '/task',
//     name: 'Task',
//     component: Task
//   },
//   {
//     path: '/login',
//     name: 'Login',
//     component: Login
//   },
//   {
//     path: '/bob',
//     name: 'CustomerView',
//     component: CustomerView,
//     beforeEnter: (to, from, next) => {
//       if(store.state.authenticated == false) {
//           next(false);
//       } else {
//           next();
//       }
//   }
//   },
//   {
//     path: '/bob',
//     name: 'ProviderView',
//     component: ProviderView
//   },
//   {
//     path: '/baob',
//     name: 'BankView',
//     component: BankView
//   }
  
// ]

// const router = new VueRouter({
//   mode: 'history',
//   base: process.env.BASE_URL,
//   routes
// })

// export default router