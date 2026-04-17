<template>
  <div class="tools-slider">
    <div class="tools-slider__header mb-6 flex items-center justify-between">
      <h3 class="text-[32px] font-semibold leading-[125%] tracking-[-3%] text-neutral-800 sm:text-[48px]">
        {{ title }}
      </h3>
      <div class="flex gap-1 sm:gap-2">
        <button
          @click="prevSlide"
          class="flex items-center justify-center rounded-lg bg-neutral-200 px-4 py-2 text-text-dark-primary transition-colors hover:bg-neutral-300 max-sm:px-1 sm:rounded-xl"
        >
          <ArrowLeft class="size-4 text-text-dark-primary sm:size-6" />
        </button>
        <button
          @click="nextSlide"
          class="flex items-center justify-center rounded-lg bg-neutral-200 px-4 py-2 text-text-dark-primary transition-colors hover:bg-neutral-300 max-sm:px-1 sm:rounded-xl"
        >
          <ArrowRight class="size-4 sm:size-6" />
        </button>
      </div>
    </div>

    <div class="w-full overflow-hidden">
      <div
        ref="sliderTrack"
        class="flex gap-4 transition-all duration-500 ease-in-out"
        :style="{ transform: `translateX(-${translateX}px)` }"
      >
        <div
          v-for="tool in tools"
          :key="tool.id"
          class="tool-card w-[280px] shrink-0 overflow-hidden rounded-[32px] bg-white sm:w-[332px]"
        >
          <img
            :src="getImageUrl(tool.image)"
            :alt="tool.title"
            class="h-[280px] w-full object-cover sm:h-[332px]"
          />
          <div class="p-6">
            <h4 class="text-[20px] font-medium leading-[135%] tracking-[-3%] text-neutral-800 sm:text-[24px]">
              {{ tool.title }}
            </h4>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue'
import { ArrowLeft, ArrowRight } from 'lucide-vue-next'
import getImageUrl from '../utils/getImageURL'

const props = defineProps({
  tools: {
    type: Array,
    required: true,
  },
  title: {
    type: String,
    default: 'Используемые инструменты',
  },
})

const sliderTrack = ref(null)
const currentSlide = ref(0)
const translateX = ref(0)
const screenWidth = ref(0)

const CARD_WIDTH = 332
const CARD_GAP = 16

const visibleCards = computed(() => {
  const containerWidth = screenWidth.value
  return Math.floor(containerWidth / (CARD_WIDTH + CARD_GAP))
})

const maxSlideIndex = computed(() => {
  const visible = Math.max(1, visibleCards.value)
  return Math.max(0, props.tools.length - visible)
})

const isFirstSlide = computed(() => currentSlide.value === 0)
const isLastSlide = computed(() => currentSlide.value >= maxSlideIndex.value)

const nextSlide = () => {
  if (isLastSlide.value) {
    currentSlide.value = 0
    updateTranslateX()
  } else {
    currentSlide.value++
    updateTranslateX()
  }
}

const prevSlide = () => {
  if (isFirstSlide.value) {
    currentSlide.value = maxSlideIndex.value
    updateTranslateX()
  } else {
    currentSlide.value--
    updateTranslateX()
  }
}

const updateTranslateX = () => {
  translateX.value = currentSlide.value * (CARD_WIDTH + CARD_GAP)
}

const handleResize = () => {
  screenWidth.value = window.innerWidth
  updateTranslateX()
}

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

onMounted(() => {
  screenWidth.value = window.innerWidth
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
.tool-card {
  transition: all 0.3s ease;
}

.tool-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
}

button {
  transition: all 0.2s ease-in-out;
}

@media (max-width: 639px) {
  button {
    min-height: 36px;
    min-width: 36px;
  }
  
  .tool-card {
    width: 280px;
  }
}
</style>
