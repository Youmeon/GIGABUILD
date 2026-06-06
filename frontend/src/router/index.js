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
  scrollBehavior(to, from, savedPosition) {
    // Если есть сохраненная позиция (например, при навигации назад)
    if (savedPosition) {
      return savedPosition
    }
    // Всегда скроллим в начало страницы при переходе
    return { top: 0, behavior: 'smooth' }
  },
})

export default router
