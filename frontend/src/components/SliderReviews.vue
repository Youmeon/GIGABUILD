<template>
  <div class="flex flex-col">
    <div class="mb-6 flex items-center justify-between sm:mb-10">
      <h2
        class="max-w-[200px] text-[20px] leading-[125%] tracking-[-3%] text-neutral-100 sm:max-w-none sm:text-[32px] lg:text-[48px]"
      >
        Что говорят наши клиенты
      </h2>
      <!-- Кнопки навигации -->
      <div class="flex gap-1 sm:gap-2">
        <button
          @click="prevSlide"
          :disabled="isFirstSlide"
          :class="[
            'flex items-center justify-center rounded-lg px-4 py-2 transition-colors sm:rounded-xl',
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
        :style="{
          transform: `translateX(-${translateX}px)`,
          gap: isMobile ? '12px' : '16px',
        }"
        ref="sliderTrack"
      >
        <!-- Карточки отзывов -->
        <div
          v-for="review in reviews"
          :key="review.id"
          :class="[
            'flex shrink-0 flex-col gap-4 rounded-xl bg-neutral-100 p-4 sm:gap-6 sm:rounded-2xl sm:p-6 lg:p-8',
            isMobile
              ? 'max-h-[350px] w-[280px]'
              : 'max-h-[30rem] w-[340px] sm:w-[450px] lg:w-[564px]',
          ]"
        >
          <div class="flex items-center justify-start gap-3 sm:gap-4">
            <div
              class="size-12 shrink-0 overflow-hidden rounded-full sm:size-16 lg:size-[4.5rem]"
            >
              <img
                :src="getImageUrl(review.avatarAuthor)"
                :alt="review.nameAuthor"
                @error="handleImageError"
                class="size-full object-cover"
              />
            </div>
            <div class="min-w-0 flex-1">
              <p
                class="mb-2 truncate text-base font-semibold leading-tight tracking-[-2%] sm:mb-3 sm:text-lg lg:text-[24px]"
              >
                {{ review.nameAuthor }}
              </p>
              <div class="flex">
                <div v-for="n in 5" :key="n">
                  <svg
                    :width="isMobile ? '16' : '20'"
                    :height="isMobile ? '17' : '21'"
                    viewBox="0 0 24 25"
                    fill="none"
                    xmlns="http://www.w3.org/2000/svg"
                    class="shrink-0"
                  >
                    <path
                      d="M8.58699 8.73594L11.185 3.50394C11.2606 3.35253 11.3769 3.22517 11.5209 3.13616C11.6648 3.04715 11.8307 3 12 3C12.1692 3 12.3351 3.04715 12.4791 3.13616C12.6231 3.22517 12.7394 3.35253 12.815 3.50394L15.413 8.73594L21.221 9.57994C21.3885 9.60317 21.5461 9.67303 21.6759 9.78155C21.8056 9.89007 21.9022 10.0329 21.9546 10.1937C22.0071 10.3545 22.0133 10.5268 21.9725 10.6909C21.9317 10.855 21.8456 11.0044 21.724 11.1219L17.522 15.1919L18.514 20.9419C18.641 21.6799 17.861 22.2419 17.194 21.8939L12 19.1779L6.80499 21.8939C6.13899 22.2429 5.35899 21.6799 5.48599 20.9409L6.47799 15.1909L2.27599 11.1209C2.15498 11.0033 2.06939 10.8541 2.02896 10.6903C1.98852 10.5264 1.99487 10.3545 2.04726 10.1941C2.09966 10.0337 2.19601 9.89116 2.32536 9.78277C2.45471 9.67439 2.61188 9.60446 2.77899 9.58094L8.58699 8.73594Z"
                      fill="#FFAD28"
                      stroke="#FFAD28"
                      stroke-width="1.5"
                      stroke-linecap="round"
                      stroke-linejoin="round"
                    />
                  </svg>
                </div>
              </div>
            </div>
          </div>
          <div class="flex-1 overflow-hidden">
            <p
              :class="[
                'w-full leading-[140%] tracking-[-2%] text-text-dark-primary sm:leading-[150%]',
                isMobile ? 'text-sm' : 'text-base sm:text-lg lg:text-[24px]',
              ]"
            >
              {{ review.review }}
            </p>
          </div>
        </div>
      </div>
    </div>

    <!-- Индикаторы для мобильных устройств -->
    <div v-if="isMobile" class="mt-4 flex justify-center gap-2">
      <div
        v-for="(_, index) in Math.ceil(reviews.length)"
        :key="index"
        @click="goToSlide(index)"
        :class="[
          'size-2 cursor-pointer rounded-full transition-all',
          currentSlide === index ? 'bg-neutral-100' : 'bg-neutral-100/30',
        ]"
      />
    </div>
  </div>
</template>

<script setup>
import reviewsData from '@/data/reviews.json'
import { ArrowLeft, ArrowRight } from 'lucide-vue-next'
import { computed, onMounted, onUnmounted, reactive, ref } from 'vue'
import getImageUrl from '../utils/getImageURL'
// Данные отзывов
const reviews = reactive(reviewsData)

// Реактивные переменные
const currentSlide = ref(0)
const translateX = ref(0)
const sliderTrack = ref(null)
const screenWidth = ref(0)

// Вычисляемые свойства
const isMobile = computed(() => screenWidth.value < 640)
const isTablet = computed(
  () => screenWidth.value >= 640 && screenWidth.value < 1024
)

const cardWidth = computed(() => {
  if (isMobile.value) return 280
  if (isTablet.value) return 340
  return 564
})

const cardGap = computed(() => {
  return isMobile.value ? 12 : 16
})

const cardsPerView = computed(() => {
  if (isMobile.value) return 1
  if (isTablet.value) return 1.3
  return 2.5
})

const isFirstSlide = computed(() => currentSlide.value === 0)
const isLastSlide = computed(() => {
  const maxSlides = Math.max(0, reviews.length - Math.floor(cardsPerView.value))
  return currentSlide.value >= maxSlides
})

// Обработка ошибок загрузки изображений
const handleImageError = (event) => {
  event.target.src = `${getImageUrl('service1.jpg')}`
}

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
  currentSlide.value = index
  updateTranslateX()
}

const updateTranslateX = () => {
  translateX.value = currentSlide.value * (cardWidth.value + cardGap.value)
}

// Обработка изменения размера экрана
const handleResize = () => {
  screenWidth.value = window.innerWidth
  // Пересчитываем позицию слайдера при изменении размера экрана
  updateTranslateX()
}

// Touch события для свайпа на мобильных устройствах
let touchStartX = 0
let touchEndX = 0

const handleTouchStart = (e) => {
  touchStartX = e.changedTouches[0].screenX
}

const handleTouchEnd = (e) => {
  touchEndX = e.changedTouches[0].screenX
  handleSwipe()
}

const handleSwipe = () => {
  const swipeThreshold = 50
  const diff = touchStartX - touchEndX

  if (Math.abs(diff) > swipeThreshold) {
    if (diff > 0) {
      // Свайп влево - следующий слайд
      nextSlide()
    } else {
      // Свайп вправо - предыдущий слайд
      prevSlide()
    }
  }
}

// Lifecycle hooks
onMounted(() => {
  screenWidth.value = window.innerWidth
  window.addEventListener('resize', handleResize)

  // Добавляем touch события для мобильных устройств
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
/* Утилита для ограничения количества строк текста на мобильных */
.line-clamp-8 {
  display: -webkit-box;
  -webkit-box-orient: vertical;
  overflow: hidden;
  text-overflow: ellipsis;
}

/* Плавные переходы для всех интерактивных элементов */
button {
  transition: all 0.2s ease-in-out;
}

/* Улучшенная область касания для мобильных устройств */
@media (max-width: 639px) {
  button {
    min-height: 36px;
    min-width: 36px;
  }
}
</style>
