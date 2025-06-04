import { createRouter, createWebHistory } from 'vue-router'
import About from '../views/About.vue'
import ApartInspection from '../views/ApartInspection.vue'
import Home from '../views/Home.vue'
import Services from '../views/Services.vue'

const routes = [
  { path: '/', name: 'Home', component: Home },
  { path: '/about', name: 'About', component: About },
  { path: '/services', name: 'Services', component: Services },
  {
    path: '/apartment-inspection',
    name: 'ApartamentInspection',
    component: ApartInspection,
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
