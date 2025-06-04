<template>
  <div class="flex flex-col">
    <div class="mb-6 flex items-center justify-between sm:mb-10">
      <h3
        class="max-w-[200px] text-[20px] font-semibold leading-[125%] tracking-[-3%] text-neutral-100 sm:max-w-none sm:text-[32px] lg:text-[48px]"
      >
        В ходе осмотра проверяем
      </h3>
      <!-- Кнопки навигации -->
      <div class="flex gap-1 sm:gap-2">
        <button
          @click="prevSlide"
          :disabled="isFirstSlide"
          :class="[
            'flex items-center justify-center rounded-lg px-4 py-2 transition-colors max-sm:px-1 sm:rounded-xl',
            isFirstSlide
              ? 'bg-blue-200/30 text-neutral-100/50'
              : 'bg-neutral-200 text-text-dark-primary hover:bg-neutral-300',
          ]"
        >
          <ArrowLeft class="size-4 text-text-dark-primary sm:size-6" />
        </button>
        <button
          @click="nextSlide"
          :disabled="isLastSlide"
          :class="[
            'flex items-center justify-center rounded-lg px-4 py-2 transition-colors max-sm:px-1 sm:rounded-xl',
            isLastSlide
              ? 'bg-blue-200/30 text-neutral-100/50'
              : 'bg-neutral-200 text-text-dark-primary hover:bg-neutral-300',
          ]"
        >
          <ArrowRight class="size-4 sm:size-6" />
        </button>
      </div>
    </div>

    <!-- Слайдер -->
    <div class="w-full overflow-hidden">
      <!-- Трек слайдера -->
      <div
        class="flex transition-all duration-500 ease-in-out"
        :style="{ transform: `translateX(-${translateX}px)`, gap: '16px' }"
        ref="sliderTrack"
      >
        <!-- Карточки осмотра -->
        <div
          v-for="item in inspectionItems"
          :key="item.id"
          class="flex max-w-[332px] shrink-0 flex-col rounded-xl bg-neutral-100 px-3 pb-6 pt-3"
        >
          <img
            :src="getImageUrl(item.image)"
            :alt="item.title"
            class="mb-[24px] h-[280px] w-full max-w-[308px] object-cover"
          />
          <div class="px-3">
            <h5
              class="mb-3 text-[24px] font-semibold leading-[125%] tracking-[-3%] text-text-dark-primary"
            >
              {{ item.title }}
            </h5>
            <p
              class="align-middle text-[20px] font-medium leading-[135%] tracking-[-3%] text-neutral-600"
            >
              {{ item.description }}
            </p>
          </div>
        </div>
      </div>
    </div>

    <!-- Индикаторы для мобильных устройств -->
    <div v-if="isMobile" class="mt-4 flex justify-center gap-2">
      <div
        v-for="(_, index) in inspectionItems.length"
        :key="index"
        @click="goToSlide(index)"
        :class="[
          'size-2 cursor-pointer rounded-full transition-all',
          currentSlide === index - 1 ? 'bg-neutral-100' : 'bg-neutral-100/30',
        ]"
      />
    </div>
  </div>
</template>

<script setup>
import inspectionItems from '@/data/apartment_checklist.json'
import { ArrowLeft, ArrowRight } from 'lucide-vue-next'
import { computed, onMounted, onUnmounted, reactive, ref } from 'vue'
import getImageUrl from '../utils/getImageURL'
// Данные осмотра
const items = reactive(inspectionItems)

// Реактивные переменные
const currentSlide = ref(0)
const translateX = ref(0)
const sliderTrack = ref(null)
const screenWidth = ref(window.innerWidth)

// Фиксированные параметры карточки
const CARD_WIDTH = 332
const CARD_GAP = 16

// Определяем мобильное устройство
const isMobile = computed(() => screenWidth.value < 640)

// Навигационные состояния
const isFirstSlide = computed(() => currentSlide.value === 0)
const isLastSlide = computed(() => currentSlide.value >= items.length - 1)

// Функции навигации
const nextSlide = () => {
  if (!isLastSlide.value) {
    currentSlide.value++
    updateTranslateX()
  }
}

const prevSlide = () => {
  if (!isFirstSlide.value) {
    currentSlide.value--
    updateTranslateX()
  }
}

const goToSlide = (index) => {
  currentSlide.value = index - 1
  updateTranslateX()
}

const updateTranslateX = () => {
  translateX.value = currentSlide.value * (CARD_WIDTH + CARD_GAP)
}

// Обработка изменения размера экрана
const handleResize = () => {
  screenWidth.value = window.innerWidth
  updateTranslateX()
}

// Свайп-события для мобильных устройств
let touchStartX = 0
let touchEndX = 0

const handleTouchStart = (e) => {
  touchStartX = e.changedTouches[0].screenX
}

const handleTouchEnd = (e) => {
  touchEndX = e.changedTouches[0].screenX
  const diff = touchStartX - touchEndX
  if (Math.abs(diff) > 50) {
    diff > 0 ? nextSlide() : prevSlide()
  }
}

// Хуки жизненного цикла
onMounted(() => {
  window.addEventListener('resize', handleResize)
  if (sliderTrack.value) {
    sliderTrack.value.addEventListener('touchstart', handleTouchStart, {
      passive: true,
    })
    sliderTrack.value.addEventListener('touchend', handleTouchEnd, {
      passive: true,
    })
  }
})

onUnmounted(() => {
  window.removeEventListener('resize', handleResize)
  if (sliderTrack.value) {
    sliderTrack.value.removeEventListener('touchstart', handleTouchStart)
    sliderTrack.value.removeEventListener('touchend', handleTouchEnd)
  }
})
</script>

<style scoped>
button {
  transition: all 0.2s ease-in-out;
}

@media (max-width: 639px) {
  button {
    min-height: 36px;
    min-width: 36px;
  }
}
</style>
