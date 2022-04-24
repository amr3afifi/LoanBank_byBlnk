import Vue from 'vue'
import App from './App.vue'
import Vuex from "vuex"
import vuetify from './plugins/vuetify'
import VueRouter from 'vue-router'
import createPersistedState from 'vuex-persistedstate'


// COMPONENTS
import Home from './components/HelloWorld.vue'
import Login from './components/Login.vue'

// VIEWS
import About from './views/AboutView.vue'
import CustomerView from './views/CustomerView.vue'
import ProviderView from './views/ProviderView.vue'
import BankView from './views/BankView.vue'

Vue.config.productionTip = false
Vue.use(VueRouter)
Vue.use(Vuex);

const store = new Vuex.Store(
    {
      plugins: [createPersistedState({
        storage: window.sessionStorage,
    })],
        state: {
            authenticated: false,
            user:{}
        },
        mutations: {
            setAuthentication(state, status) {
                state.authenticated = status;
            },
            setUser(state, status) {
              state.user = status;
          },
          getUserType(state) {
            return state.user['type'];
        }
        }
    }
);

const routes= [
      {
        path: '/',
        name: 'Home',
        component: Home
      },
      {
        path: '/about',
        name: 'About',
        component: About
      },
      {
        path: '/login',
        name: 'Login',
        component: Login,
        beforeEnter: (to, from, next) => {
          if(store.state.authenticated == true) {
            next("/dashboard");
          } else {
              next();
          }
      }
      },
      {
        path: '/dashboard',
        name: 'CustomerView',
        component: CustomerView,
        beforeEnter: (to, from, next) => {
          console.log(store.state);
          if(store.state.authenticated == true) {

            switch(store.state.user['type']) {
              case 'customer':
                next(true)
                break;
              case 'provider':
                next({ name: 'ProviderView' })
                break;
              case 'bank':
                next({ name: 'BankView' })
                break;
              default:
                next(false)
            }
            
          } else {
              next("/login");
          }
      }
      },
      {
        path: '/dashboard',
        name: 'ProviderView',
        component: ProviderView,
        beforeEnter: (to, from, next) => {
          if(store.state.authenticated == true) {

            switch(store.state.user.type) {
              case 'customer':
                next({ name: 'CustomerView' })
                break;
              case 'provider':
                next(true)
                break;
              case 'bank':
                next({ name: 'BankView' })
                break;
              default:
                next(false)
            }
            
          } else {
              next("/login");
          }
      }
      },
      {
        path: '/dashboard',
        name: 'BankView',
        component: BankView,
        beforeEnter: (to, from, next) => {
          if(store.state.authenticated == true) {

            switch(store.state.user.type) {
              case 'customer':
                next({ name: 'CustomerView' })
                break;
              case 'provider':
                next({ name: 'ProviderView' })
                break;
              case 'bank':
                next(true)
                break;
              default:
                next(false)
            }

          } else {
              next(false);
          }
      }
      }
      
    ]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
});

new Vue({
  vuetify,
  render: h => h(App),
  router: router,
  store: store
}).$mount('#app')
