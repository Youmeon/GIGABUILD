<template>
  <div class="flex min-w-0 w-full max-w-full flex-col overflow-x-hidden">
    <div class="mb-6 flex items-center justify-between sm:mb-10">
      <h2
        class="max-w-[200px] text-[20px] leading-[125%] tracking-[-3%] text-neutral-100 sm:max-w-none sm:text-[32px] lg:text-[48px]"
      >
        Что говорят наши клиенты
      </h2>
      <div v-if="!isGridLayout" class="flex gap-1 sm:gap-2">
        <button
          type="button"
          @click="scrollPrev"
          class="flex items-center justify-center rounded-lg bg-neutral-200 px-4 py-2 text-text-dark-primary transition-colors hover:bg-neutral-300 sm:rounded-xl"
        >
          <ArrowLeft class="size-4 text-text-dark-primary sm:size-6" />
        </button>
        <button
          type="button"
          @click="scrollNext"
          class="flex items-center justify-center rounded-lg bg-neutral-200 px-4 py-2 text-text-dark-primary transition-colors hover:bg-neutral-300 max-sm:px-1 sm:rounded-xl"
        >
          <ArrowRight class="size-4 sm:size-6" />
        </button>
      </div>
    </div>

    <div
      ref="sliderContainer"
      :class="[
        'reviews-scroll w-full min-w-0 max-w-full gap-3 pb-4 sm:gap-4',
        isGridLayout
          ? 'grid grid-cols-2 overflow-y-auto overflow-x-hidden'
          : 'flex touch-pan-x overflow-x-auto overflow-y-hidden scroll-smooth max-[744px]:snap-x max-[744px]:snap-mandatory',
      ]"
      @scroll.passive="updateScrollState"
    >
      <div
        v-for="review in reviews"
        :key="review.id"
        :class="[
          'review-card flex min-w-0 max-w-full flex-col gap-4 rounded-xl bg-neutral-100 p-4 min-[745px]:max-h-[30rem] sm:gap-6 sm:rounded-2xl sm:p-6 lg:p-8',
          isGridLayout
            ? 'review-card--grid w-full'
            : 'review-card--scroll w-[min(564px,100%,calc(100vw-4rem))] flex-none max-[744px]:snap-start',
        ]"
      >
        <div class="review-card__header flex items-center justify-start gap-3 sm:gap-4">
          <div
            class="review-card__avatar size-12 shrink-0 overflow-hidden rounded-full sm:size-16 lg:size-[4.5rem]"
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
              class="review-card__name mb-2 truncate text-base font-semibold leading-tight tracking-[-2%] sm:mb-3 sm:text-lg lg:text-[24px]"
            >
              {{ review.nameAuthor }}
            </p>
            <div class="review-card__stars flex">
              <div v-for="n in 5" :key="n">
                <svg
                  :width="isMobile ? '16' : '20'"
                  :height="isMobile ? '17' : '21'"
                  viewBox="0 0 24 25"
                  fill="none"
                  xmlns="http://www.w3.org/2000/svg"
                  class="review-card__star shrink-0"
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
              'review-card__text w-full leading-[140%] tracking-[-2%] text-text-dark-primary sm:leading-[150%]',
              isMobile ? 'text-sm' : 'text-base sm:text-lg lg:text-[24px]',
            ]"
          >
            {{ review.review }}
          </p>
        </div>
      </div>
    </div>

    <div v-if="isMobile && !isGridLayout" class="mt-4 flex justify-center gap-2">
      <button
        v-for="(_, index) in reviews"
        :key="index"
        type="button"
        :aria-label="`Отзыв ${index + 1}`"
        @click="goToSlide(index)"
        :class="[
          'size-2 rounded-full transition-all',
          currentSlide === index ? 'bg-neutral-100' : 'bg-neutral-100/30',
        ]"
      />
    </div>
  </div>
</template>

<script setup>
import reviewsData from '@/data/reviews.json'
import { ArrowLeft, ArrowRight } from 'lucide-vue-next'
import { computed, nextTick, onMounted, onUnmounted, reactive, ref } from 'vue'
import getImageUrl from '../utils/getImageURL'

const reviews = reactive(reviewsData)

const sliderContainer = ref(null)
const screenWidth = ref(0)
const currentSlide = ref(0)
const isGridLayout = ref(false)

const isMobile = computed(() => screenWidth.value < 640)

const updateLayoutMode = () => {
  const root = sliderContainer.value
  if (!root) return

  // Практика показала, что на узких ширинах горизонтальный режим может визуально
  // "наслаиваться" из-за ограничений родителя. Поэтому используем простой, стабильный
  // порог по реальной ширине контейнера: если контейнер слишком узкий — уходим в 2 колонки.
  const containerWidth = root.getBoundingClientRect().width
  isGridLayout.value = containerWidth < 520
}

const getScrollStep = () => {
  if (isGridLayout.value) return 0
  const root = sliderContainer.value
  if (!root) return 0
  const card = root.querySelector('.review-card')
  if (!card) return 0
  const styles = getComputedStyle(root)
  const gap = parseFloat(styles.columnGap || styles.gap) || 0
  return card.getBoundingClientRect().width + gap
}

const updateScrollState = () => {
  if (isGridLayout.value) return
  const el = sliderContainer.value
  if (!el || !reviews.length) return
  const step = getScrollStep()
  if (step <= 0) return
  const idx = Math.round(el.scrollLeft / step)
  currentSlide.value = Math.min(reviews.length - 1, Math.max(0, idx))
}

const scrollNext = () => {
  if (isGridLayout.value) return
  const el = sliderContainer.value
  if (!el) return
  const { scrollLeft, scrollWidth, clientWidth } = el
  const maxScrollLeft = scrollWidth - clientWidth
  const step = getScrollStep()
  if (step <= 0) return
  if (scrollLeft >= maxScrollLeft - 2) {
    el.scrollTo({ left: 0, behavior: 'smooth' })
  } else {
    el.scrollBy({ left: step, behavior: 'smooth' })
  }
}

const scrollPrev = () => {
  if (isGridLayout.value) return
  const el = sliderContainer.value
  if (!el) return
  const { scrollLeft, scrollWidth, clientWidth } = el
  const maxScrollLeft = scrollWidth - clientWidth
  const step = getScrollStep()
  if (step <= 0) return
  if (scrollLeft <= 2) {
    el.scrollTo({ left: maxScrollLeft, behavior: 'smooth' })
  } else {
    el.scrollBy({ left: -step, behavior: 'smooth' })
  }
}

const goToSlide = (index) => {
  if (isGridLayout.value) return
  const el = sliderContainer.value
  if (!el) return
  const step = getScrollStep()
  if (step <= 0) return
  const maxIndex = reviews.length - 1
  const i = Math.min(maxIndex, Math.max(0, index))
  el.scrollTo({ left: i * step, behavior: 'smooth' })
  currentSlide.value = i
}

const handleResize = () => {
  screenWidth.value = window.innerWidth
  nextTick(() => {
    updateLayoutMode()
    updateScrollState()
  })
}

let resizeObserver = null

onMounted(() => {
  screenWidth.value = window.innerWidth
  window.addEventListener('resize', handleResize)
  nextTick(() => {
    updateLayoutMode()
    updateScrollState()
    const el = sliderContainer.value
    if (el && typeof ResizeObserver !== 'undefined') {
      resizeObserver = new ResizeObserver(() => {
        updateLayoutMode()
        updateScrollState()
      })
      resizeObserver.observe(el)
    }
  })
})

onUnmounted(() => {
  window.removeEventListener('resize', handleResize)
  resizeObserver?.disconnect()
})

const handleImageError = (event) => {
  event.target.src = `${getImageUrl('service1.jpg')}`
}
</script>

<style scoped>
.line-clamp-8 {
  display: -webkit-box;
  -webkit-box-orient: vertical;
  overflow: hidden;
  text-overflow: ellipsis;
}

button {
  transition: all 0.2s ease-in-out;
}

@media (max-width: 639px) {
  button {
    min-height: 36px;
    min-width: 36px;
  }
}

.reviews-scroll {
  scrollbar-width: none;
  -ms-overflow-style: none;
}

.reviews-scroll::-webkit-scrollbar {
  height: 0;
  display: none;
}

@media (max-width: 744px) {
  /* Плавное "диагональное" уменьшение — только в режиме горизонтального скролла */
  .review-card--scroll {
    width: clamp(16rem, calc(100vw - 4rem), 28rem);
    max-height: clamp(18.5rem, 50vw, 21.875rem);
    gap: clamp(0.875rem, 1.6vw, 1rem);
    padding: clamp(0.875rem, 1.8vw, 1.25rem);
    border-radius: clamp(1rem, 2vw, 1.5rem);
  }

  .review-card__header {
    gap: clamp(0.75rem, 1.5vw, 1rem);
  }

  .review-card__avatar {
    width: clamp(2.75rem, 6vw, 4rem);
    height: clamp(2.75rem, 6vw, 4rem);
  }

  .review-card__name {
    margin-bottom: clamp(0.375rem, 1vw, 0.75rem);
    font-size: clamp(1rem, 2vw, 1.125rem);
  }

  .review-card__stars {
    gap: 0.125rem;
  }

  .review-card__star {
    width: clamp(1rem, 2vw, 1.25rem);
    height: clamp(1rem, 2.1vw, 1.3125rem);
  }

  .review-card__text {
    font-size: clamp(0.875rem, 1.7vw, 1rem) !important;
    line-height: 1.45 !important;
  }
}
</style>
