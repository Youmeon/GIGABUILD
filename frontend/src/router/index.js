import { createRouter, createWebHistory } from 'vue-router'
import About from '../views/About.vue'
import ApartInspection from '../views/ApartInspection.vue'
import Home from '../views/Home.vue'
import Services from '../views/Services.vue'
import DetailServices from '../views/DetailServices.vue'

const routes = [
  { path: '/', name: 'Home', component: Home },
  { path: '/about', name: 'About', component: About },
  { path: '/services', name: 'Services', component: Services },
  {
    path: '/services/:id',
    name: 'DetailServices',
    component: DetailServices,
  },
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
