<template>
  <div class="service-include-slider">
    <div v-if="items && items.length > 0" class="service-include-slider__content">
      <div 
        ref="sliderRef"
        class="slider-cards flex gap-4 overflow-x-auto pb-4 scroll-smooth scrollbar-hide"
        @scroll="updateScrollState"
      >
        <div 
          v-for="(item, index) in items[0]?.items"
          :key="index"
          class="slider-card flex-shrink-0 w-[448px] max-sm:w-[343px] bg-white rounded-[32px] p-8 max-sm:p-6 hover:shadow-lg transition-all duration-300"
        >
          <div class="card-content flex flex-col h-full">
            <span class="card-number text-neutral-500 text-[14px] font-medium mb-4">0{{ index + 1 }}</span>
            <p class="card-text text-neutral-800 text-[32px] max-lg:text-[24px] max-sm:text-[20px] font-medium leading-[125%] tracking-[-4%]">
              {{ item }}
            </p>
          </div>
        </div>
      </div>
      <div class="flex gap-2 mt-4">
        <button 
          @click="scrollLeft"
          class="w-12 h-12 rounded-full bg-white shadow-md flex items-center justify-center hover:bg-neutral-100 transition-colors"
          :disabled="!canScrollLeft"
        >
          <ChevronLeft class="w-5 h-5 text-blue-600" />
        </button>
        <button 
          @click="scrollRight"
          class="w-12 h-12 rounded-full bg-white shadow-md flex items-center justify-center hover:bg-neutral-100 transition-colors"
          :disabled="!canScrollRight"
        >
          <ChevronRight class="w-5 h-5 text-blue-600" />
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { ChevronLeft, ChevronRight } from 'lucide-vue-next'

const props = defineProps({
  items: {
    type: Array,
    default: () => []
  },
  visibleSlides: {
    type: Number,
    default: 3
  }
})

const sliderRef = ref(null)
const canScrollLeft = ref(false)
const canScrollRight = ref(true)

const updateScrollState = () => {
  if (!sliderRef.value) return
  const { scrollLeft, scrollWidth, clientWidth } = sliderRef.value
  canScrollLeft.value = scrollLeft > 0
  canScrollRight.value = scrollLeft < scrollWidth - clientWidth - 10
}

const scrollLeft = () => {
  if (!sliderRef.value) return
  sliderRef.value.scrollBy({ left: -468, behavior: 'smooth' })
}

const scrollRight = () => {
  if (!sliderRef.value) return
  sliderRef.value.scrollBy({ left: 468, behavior: 'smooth' })
}
</script>

<style scoped>
.slider-card {
  transition: all 0.3s ease;
}

.slider-card:hover {
  transform: translateY(-4px);
}

.scrollbar-hide {
  -ms-overflow-style: none;
  scrollbar-width: none;
}
.scrollbar-hide::-webkit-scrollbar {
  display: none;
}
</style>
