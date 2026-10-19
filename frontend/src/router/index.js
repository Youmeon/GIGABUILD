import { createRouter, createWebHistory } from 'vue-router'
import About from '../views/About.vue'
import ApartInspection from '../views/ApartInspection.vue'
import Home from '../views/Home.vue'
import Services from '../views/Services.vue'
import DetailServices from '../views/DetailServices.vue'
import NotFound from '../views/NotFound.vue'
import detailServicesData from '../data/detail_services.json'
import { applySeo } from '../seo'

// Обрезает текст до ~160 символов по границе слова — длина описания в выдаче поисковиков
const shorten = (text, max = 160) => {
  if (text.length <= max) return text
  return text.slice(0, text.lastIndexOf(' ', max)) + '…'
}

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
    meta: {
      seo: {
        title: 'Приёмка квартир и строительная экспертиза в Хабаровске',
        description:
          'Приёмка квартир в новостройках, строительный контроль, обследование зданий и строительно-судебные экспертизы в Хабаровске. Ежедневно с 08:00 до 19:00.',
      },
    },
  },
  {
    path: '/about',
    name: 'About',
    component: About,
    meta: {
      seo: {
        title: 'О компании',
        description:
          'ООО «СК Дионис» — многопрофильная строительная компания в Хабаровске: технический надзор, проектирование и строительство, от проектной документации до сдачи объекта.',
      },
    },
  },
  {
    path: '/services',
    name: 'Services',
    component: Services,
    meta: {
      seo: {
        title: 'Услуги',
        description:
          'Инженерные изыскания, строительный контроль, авторский надзор, обследование зданий, проектирование и строительно-судебные экспертизы в Хабаровске.',
      },
    },
  },
  {
    path: '/services/:id',
    name: 'DetailServices',
    component: DetailServices,
    meta: {
      seo: (route) => {
        const service = detailServicesData.find(
          (s) => s.id === parseInt(route.params.id)
        )
        if (!service) return { title: 'Страница не найдена', noindex: true }
        return {
          title: `${service.title} в Хабаровске`,
          description: shorten(service.description),
        }
      },
    },
  },
  {
    path: '/apartment-inspection',
    name: 'ApartamentInspection',
    component: ApartInspection,
    meta: {
      seo: {
        title: 'Приёмка квартир в новостройке в Хабаровске',
        description:
          'Проверим квартиру перед подписанием акта приёма-передачи: тщательный осмотр по СП, ГОСТ и ПУЭ, фиксация всех выявленных недостатков.',
      },
    },
  },
  {
    path: '/:pathMatch(.*)*',
    name: 'NotFound',
    component: NotFound,
    meta: { seo: { title: 'Страница не найдена', noindex: true } },
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

router.afterEach((to) => applySeo(to))

export default router
