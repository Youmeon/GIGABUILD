<script setup>
import { inject, onMounted, onUnmounted, ref, watch } from 'vue'
import { useRoute } from 'vue-router'
import logoVar1 from '../assets/images/logo-var1.svg'
import logoVar2 from '../assets/images/logo-var2.svg'
import miniLogo from '../assets/images/mini-logo.svg' // Добавлен импорт мини-логотипа
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
}

// Получить триггерную секцию для текущей страницы
const getTriggerSection = () => {
  const path = route.path
  
  if (path === '/') {
    return document.getElementById('why-choose-us')
  } else if (path === '/apartment-inspection') {
    return document.getElementById('what-includes')
  } else if (path.startsWith('/services/')) {
    return document.getElementById('service-includes')
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
  isScrolled.value = scrolled

  if (isSpecialPage() && currentScrollY >= 100) {
    isScrolled.value = true
  }

  // Логотип: для специальных страниц всегда logoVar1, для обычных меняется
  dynamicLogoPath.value = isSpecialPage()
    ? logoVar1
    : scrolled
      ? logoVar1
      : logoVar2
  // Цвет текста ссылок мобильного меню
  navTextColor.value = scrolled ? 'text-blue-600' : 'text-white'
  // Цвет текста ссылок десктопного меню
  desktopNavTextColor.value = isSpecialPage()
    ? 'text-blue-600'
    : scrolled
      ? 'text-blue-600'
      : 'text-white'

  // Логика скрытия/показа header
  const footerFullyVisible = isFooterFullyVisible()
  const scrollingUp = currentScrollY < lastScrollY.value
  
  // Для всех страниц одинаковая логика
  if (footerFullyVisible) {
    // Footer полностью виден - скрываем header
    isHeaderHidden.value = true
  } else if (scrollingUp) {
    // Скролл вверх - показываем header
    isHeaderHidden.value = false
  } else {
    // Скролл вниз но footer не виден - header остается видимым
    isHeaderHidden.value = false
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
  <div class="container mx-auto flex items-center justify-center text-blue-600">
    <header
      :class="[
        'z-[80] flex w-full items-center gap-2.5',
        isScrolled
          ? 'fixed left-1/2 top-1 mt-2 h-14 -translate-x-1/2 rounded-2xl border-neutral-100/20 bg-neutral-200/80 text-black shadow-md'
          : 'absolute top-1 bg-none text-white',
        'px-8 py-3 transition-all duration-300 ease-in-out max-sm:px-4',
        isHeaderHidden ? '-translate-y-[120px]' : 'translate-y-0',
      ]"
    >
      <nav
        class="mx-auto flex w-full max-w-7xl items-center justify-between gap-2.5"
      >
        <!-- Логотип -->
        <router-link to="/" class="max-w-[9.82rem] pb-[0.01rem] no-underline">
          <img
            :src="isSmallScreen ? miniLogo : dynamicLogoPath"
            alt="Company Logo"
            :class="isSmallScreen ? 'max-w-[32px] h-auto' : 'h-10'"
          />
        </router-link>

        <!-- Навигация для десктопа -->
        <ul class="mx-auto hidden gap-2.5 md:flex">
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
            'mx-4 rounded-xl px-4 py-1 text-2xl hover:bg-blue-300/20 focus:bg-blue-200/20 max-sm:mx-2 md:hidden',
            isSpecialPage() || isScrolled ? 'text-blue-600' : 'text-white',
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
            'fixed right-5 top-20 w-max text-nowrap rounded-xl p-4 md:hidden',
            isScrolled ? 'bg-white text-black' : 'bg-blue-600/80 text-white',
          ]"
        >
          <ul class="flex flex-col gap-2.5">
            <li v-for="(item, index) in navItems" :key="item.to">
              <router-link
                :to="item.to"
                :class="[
                  'flex h-10 items-center rounded-xl px-5 py-2 text-center transition-all duration-300 ease-out max-sm:h-8 max-sm:px-4 max-sm:py-1 max-sm:text-sm',
                  index === 0
                    ? 'bg-neutral-100 text-blue-600 hover:bg-blue-500 hover:text-neutral-100 focus:bg-blue-400 focus:text-neutral-100'
                    : 'bg-neutral-100/20 hover:bg-blue-300/20 focus:bg-blue-200/20',
                  index !== 0 ? navTextColor : '',
                ]"
                active-class="underline"
                @click="toggleMenu"
              >
                {{ item.text }}
              </router-link>
            </li>
          </ul>
        </div>
      </transition>

      <!-- Кнопка «Оставить заявку» (для десктопа) -->
      <button
        @click="openRequestModal"
        class="h-10 text-nowrap rounded-xl bg-blue-600 px-5 py-2 font-sans text-base text-background-neutral-100 transition-all duration-300 ease-out hover:bg-blue-500 focus:bg-blue-400 md:block"
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
