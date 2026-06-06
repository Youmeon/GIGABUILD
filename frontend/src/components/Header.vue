<script setup>
import { inject, onMounted, onUnmounted, ref, watch } from 'vue'
import { useRoute } from 'vue-router'
import logoVar1 from '../assets/images/logo-var1.svg'
import logoVar2 from '../assets/images/logo-var2.svg'
import navItems from '../data/nav.json'

// Инжектируем функцию открытия модального окна
const openRequestModal = inject('openRequestModal')

const isMenuOpen = ref(false)
const isScrolled = ref(false)
const route = useRoute()
const isSmallScreen = ref(false)
const isHeaderHidden = ref(false)
const lastScrollY = ref(0)

// Проверка специальных страниц
const isSpecialPage = () => {
  return ['/about', '/services'].includes(route.path)
}

// Начальные значения для логотипа и цвета текста
const dynamicLogoPath = ref(isSpecialPage() ? logoVar1 : logoVar2)
const navTextColor = ref('text-white')
const desktopNavTextColor = ref(
  isSpecialPage() ? 'text-blue-600' : 'text-white'
)

const toggleMenu = () => {
  isMenuOpen.value = !isMenuOpen.value
  // Блокируем/разблокируем скролл
  if (isMenuOpen.value) {
    document.body.style.overflow = 'hidden'
  } else {
    document.body.style.overflow = ''
  }
}

// Получить триггерную секцию для текущей страницы
const getTriggerSection = () => {
  const path = route.path
  
  if (path === '/') {
    return document.getElementById('why-choose-us')
  } else if (path === '/apartment-inspection') {
    return document.getElementById('what-includes')
  } else if (path.startsWith('/services/')) {
    return document.getElementById('service-trigger')
  }
  
  return null
}

// Проверка что пользователь доскроллил до самого конца страницы
const isFooterFullyVisible = () => {
  const footer = document.querySelector('footer')
  if (!footer) return false
  
  // Проверяем что пользователь достиг конца страницы
  const windowHeight = window.innerHeight
  const documentHeight = document.documentElement.scrollHeight
  const scrollTop = window.scrollY
  
  // Пользователь в конце страницы если осталось меньше 100px до конца
  return (scrollTop + windowHeight) >= (documentHeight - 100)
}

// Обработка прокрутки для всех страниц
const handleScroll = () => {
  const currentScrollY = window.scrollY
  const scrolled = currentScrollY >= 842
  
  // Логика скрытия/показа header
  const footerFullyVisible = isFooterFullyVisible()
  const scrollingUp = currentScrollY < lastScrollY.value
  const triggerSection = getTriggerSection()
  
  // Проверяем достигла ли триггерная секция верха экрана
  let triggerReached = false
  if (triggerSection) {
    const rect = triggerSection.getBoundingClientRect()
    // Для DetailService проверяем когда верх элемента достиг верха экрана
    if (route.path.startsWith('/services/')) {
      triggerReached = rect.top <= 0
    } else {
      // Для других страниц - когда верх достиг верха
      triggerReached = rect.top <= 0
    }
  }
  
  // Для detailService header становится fixed когда триггер достигнут
  if (route.path.startsWith('/services/') && triggerReached) {
    isScrolled.value = true
  } else {
    isScrolled.value = scrolled
  }

  if (isSpecialPage() && currentScrollY >= 100) {
    isScrolled.value = true
  }

  // Логотип: для специальных страниц всегда logoVar1, для обычных меняется
  dynamicLogoPath.value = isSpecialPage()
    ? logoVar1
    : isScrolled.value
      ? logoVar1
      : logoVar2
  // Цвет текста ссылок мобильного меню
  navTextColor.value = isScrolled.value ? 'text-blue-600' : 'text-white'
  // Цвет текста ссылок десктопного меню
  desktopNavTextColor.value = isSpecialPage()
    ? 'text-blue-600'
    : isScrolled.value
      ? 'text-blue-600'
      : 'text-white'
  
  // Для страниц с триггерной секцией
  if (triggerSection) {
    if (!triggerReached) {
      // До триггера - header статичный (видимый)
      isHeaderHidden.value = false
    } else if (footerFullyVisible) {
      // Footer виден - скрываем header
      isHeaderHidden.value = true
    } else if (scrollingUp) {
      // Скролл вверх после триггера - показываем header
      isHeaderHidden.value = false
    } else {
      // Скролл вниз после триггера - header остается видимым
      isHeaderHidden.value = false
    }
  } else {
    // Для страниц без триггера (например, /services)
    if (footerFullyVisible) {
      isHeaderHidden.value = true
    } else if (scrollingUp) {
      isHeaderHidden.value = false
    } else {
      isHeaderHidden.value = false
    }
  }

  lastScrollY.value = currentScrollY
}

// Обработка изменения размера окна
const handleResize = () => {
  isSmallScreen.value = window.innerWidth < 1024
}

// Инициализация при монтировании
onMounted(() => {
  handleScroll()
  window.addEventListener('scroll', handleScroll)
  window.addEventListener('resize', handleResize)
  handleResize() // Первоначальная проверка размера экрана
})

onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll)
  window.removeEventListener('resize', handleResize) // Очистка слушателя resize
  // Убираем блокировку скролла при размонтировании
  document.body.style.overflow = ''
})

// Отслеживание смены маршрута
watch(
  () => route.path,
  () => {
    isHeaderHidden.value = false
    lastScrollY.value = 0
    handleScroll()
  }
)
</script>

<template>
  <div class="container mx-auto flex items-center justify-center text-blue-600 max-[744px]:w-full max-[744px]:max-w-full max-[744px]:px-0">
    <header
      :class="[
        'flex w-full items-center gap-2.5',
        isScrolled
          ? 'fixed left-1/2 top-1 mt-2 h-14 -translate-x-1/2 rounded-2xl border-neutral-100/20 bg-neutral-200/80 text-black shadow-md'
          : 'absolute top-1 text-white',
        isMenuOpen ? 'max-[744px]:!bg-white' : 'bg-none',
        'px-8 py-3 transition-all duration-300 ease-in-out max-[744px]:px-[clamp(1.25rem,4vw,2rem)]',
        isHeaderHidden ? '-translate-y-[120px]' : 'translate-y-0',
        isMenuOpen ? 'z-[200]' : 'z-[80]',
      ]"
    >
      <nav
        class="mx-auto flex w-full max-w-7xl items-center justify-between gap-2.5 max-[744px]:mx-0 max-[744px]:max-w-full"
      >
        <!-- Логотип -->
        <router-link to="/" class="max-w-[9.82rem] pb-[0.01rem] no-underline z-[1000]">
          <img
            :src="isMenuOpen ? logoVar1 : dynamicLogoPath"
            alt="Company Logo"
            class="h-10"
          />
        </router-link>

        <!-- Навигация для десктопа -->
        <ul class="mx-auto hidden gap-2.5 lg:flex max-[744px]:hidden">
          <li v-for="(item, index) in navItems" :key="item.to">
            <router-link
              :to="item.to"
              :class="[
                'block h-10 text-nowrap rounded-xl px-5 py-2 transition-all duration-300 ease-out max-sm:p-2',
                index === 0
                  ? 'bg-neutral-100 text-blue-600 hover:bg-blue-500 hover:text-neutral-100 focus:bg-blue-400 focus:text-neutral-100'
                  : 'bg-neutral-100/20 hover:bg-blue-300/20 focus:bg-blue-200/20',
                index !== 0 ? desktopNavTextColor : '',
              ]"
              active-class="underline"
            >
              {{ item.text }}
            </router-link>
          </li>
        </ul>

        <!-- Кнопка бургер-меню -->
        <button
          :class="[
            'rounded-xl px-4 py-1 text-2xl transition-all z-[1000] duration-300 ease-out min-[1024px]:hidden',
            'max-[1024px]:bg-blue-600 max-[1024px]:text-white max-[1024px]:hover:bg-blue-500',
            !isMenuOpen && (isSpecialPage() || isScrolled) ? 'text-blue-600' : '',
            !isMenuOpen && !isSpecialPage() && !isScrolled ? 'text-white' : '',
          ]"
          @click="toggleMenu"
          aria-label="Toggle menu"
        >
          {{ isMenuOpen ? '✕' : '☰' }}
        </button>
      </nav>

      <!-- Мобильное меню -->
      <transition name="slide">
        <div
          v-if="isMenuOpen"
          :class="[
            'fixed inset-0 z-[100] flex min-h-[100dvh] flex-col justify-center bg-white',
            'max-[1024px]:px-4 max-[1024px]:pt-[72px]',
            'min-[1024px]:hidden min-[1024px]:inset-auto min-[1024px]:right-5 min-[1024px]:top-20 min-[1024px]:h-auto min-[1024px]:min-h-0 min-[1024px]:w-max min-[1024px]:rounded-xl min-[1024px]:p-4 md:z-50 min-[1024px]:bg-blue-600/80',
          ]"
        >
          <ul class="flex flex-col gap-3 max-w-[570px] w-full mx-auto">
            <li v-for="(item, index) in navItems" :key="item.to">
              <router-link
                :to="item.to"
                :class="[
                  'flex h-10 items-center justify-center rounded-xl px-5 py-2 text-center transition-all duration-300 ease-out',
                  'text-base font-medium',
                  index === 0
                    ? 'bg-white text-blue-600 hover:bg-blue-500 hover:text-neutral-100 focus:bg-blue-400 focus:text-neutral-100'
                    : 'bg-transparent text-blue-600 hover:bg-blue-300/20 focus:bg-blue-200/20',
                ]"
                active-class="underline"
                @click="toggleMenu"
              >
                {{ item.text }}
              </router-link>
            </li>
            <li>
              <button
                @click="openRequestModal(); toggleMenu()"
                class="flex h-10 w-full items-center justify-center rounded-xl px-5 py-2 text-center transition-all duration-300 ease-out text-base font-medium bg-blue-600 text-white hover:bg-blue-500 focus:bg-blue-400"
              >
                Оставить заявку
              </button>
            </li>
          </ul>
        </div>
      </transition>

      <!-- Кнопка «Оставить заявку» (для десктопа) -->
      <button
        @click="openRequestModal"
        class="h-10 text-nowrap rounded-xl bg-blue-600 px-5 py-2 font-sans text-base text-background-neutral-100 transition-all duration-300 ease-out hover:bg-blue-500 focus:bg-blue-400 max-[1024px]:hidden"
      >
        Оставить заявку
      </button>
    </header>
  </div>
</template>

<style scoped>
header {
  transition:
    color 0.3s ease,
    opacity 0.3s ease,
    box-shadow 0.3s ease;
}
 

</style>
