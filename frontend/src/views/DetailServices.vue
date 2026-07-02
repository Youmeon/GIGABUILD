<template>
  <main class="bg-neutral-200">
    <section v-if="currentService" class="relative">
      <!-- Баннер с картинкой -->
      <div 
        class="relative flex flex-col overflow-hidden pt-[468px]"
        :style="{ 
          background: `linear-gradient(0deg, rgba(2, 2, 3, 0) 60%, rgba(2, 2, 3, 0.4) 100%), url(${getImageUrl(currentService.image)}) top center / cover no-repeat`
        }"
      >
        <div class="mb-[-1px] h-[33px] flex-shrink-0 rounded-t-[32px] bg-neutral-200"></div>
      </div>

      <!-- Триггер для header -->
      <div id="service-trigger" class="h-0"></div>

      <!-- Секция с заголовком услуги -->
      <div id="service-content" class="min-h-[45vh] px-8 py-16 bg-neutral-200">
        <div class="mb-0 max-w-[1200px] mx-auto">
          <router-link
            to="/services"
            class="back-link mb-8 inline-flex items-center gap-2 text-[20px] font-medium tracking-[-3%] text-blue-600"
          >
            <svg
              width="24"
              height="24"
              viewBox="0 0 24 24"
              fill="none"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                d="M19 12H5M5 12L12 19M5 12L12 5"
                stroke="currentColor"
                stroke-width="2"
                stroke-linecap="round"
                stroke-linejoin="round"
              />
            </svg>
            Назад
          </router-link>
          <h1
            class="service-main-title mb-8 text-[80px] font-medium leading-[115%] tracking-[-4%] text-neutral-800"
          >
            {{ currentService.title }}
          </h1>
          <div class="rounded-[32px] bg-white p-8">
            <p
              class="service-description text-[24px] font-medium leading-[150%] tracking-[-3%] text-[#3b3b3c]"
            >
              {{ currentService.description }}
            </p>
          </div>
        </div>
      </div>

      <section class="rounded-2xl bg-blue-600 px-8 py-16">
        <div class="mb-6">
          <div class="mb-6 flex items-center gap-[4.5px]">
            <span>
              <svg
                width="6"
                height="7"
                viewBox="0 0 6 7"
                fill="none"
                xmlns="http://www.w3.org/2000/svg"
              >
                <circle
                  cx="3"
                  cy="3.5"
                  r="3"
                  fill="#ffffff"
                  fill-opacity="0.8"
                />
              </svg>
            </span>
            <span
              class="text-[14px] font-bold uppercase tracking-[-4%] text-white/80"
            >
              Что входит в услугу
            </span>
          </div>
          <div class="flex items-center justify-between">
            <h2
              class="service-section-title text-[48px] font-semibold leading-[125%] tracking-[-3%] text-white"
            >
              {{ includeData?.title }}
            </h2>
            <div class="slider-arrows flex gap-1 sm:gap-2">
              <button
                @click="scrollLeft"
                class="flex items-center justify-center rounded-lg bg-neutral-200 px-4 py-2 text-text-dark-primary transition-colors hover:bg-neutral-300 sm:rounded-xl"
              >
                <ArrowLeft class="size-4 text-text-dark-primary sm:size-6" />
              </button>
              <button
                @click="scrollRight"
                class="flex items-center justify-center rounded-lg bg-neutral-200 px-4 py-2 text-text-dark-primary transition-colors hover:bg-neutral-300 max-sm:px-1 sm:rounded-xl"
              >
                <ArrowRight class="size-4 sm:size-6" />
              </button>
            </div>
          </div>
        </div>

        <div
          ref="sliderContainer"
          @scroll="updateScrollState"
          class="service-cards-container flex gap-4 overflow-x-auto scroll-smooth pb-4"
        >
          <div
            v-for="(item, index) in includeData?.items"
            :key="index"
            class="service-card w-[448px] shrink-0 rounded-[32px] bg-white p-8"
          >
            <p
              class="service-slider-text text-[32px] font-medium leading-[125%] tracking-[-4%] text-neutral-800"
            >
              {{ item }}
            </p>
          </div>
        </div>
      </section>
    </section>

    <section v-else class="mt-[136px] px-8 py-16">
      <p class="text-center text-[24px] text-text-dark-secondary">
        Услуга не найдена
      </p>
      <div class="mt-8 flex justify-center">
        <router-link
          to="/services"
          class="flex items-center gap-3 rounded-2xl bg-blue-600 px-5 py-3 text-neutral-100 transition-colors hover:bg-blue-500"
        >
          Вернуться к услугам
          <ArrowUpRight class="size-5" />
        </router-link>
      </div>
    </section>
  </main>
</template>

<script setup>
import detailServicesData from '@/data/detail_services.json'
import includePartData from '@/data/include_part_detail_service.json'
import { ArrowLeft, ArrowRight, ArrowUpRight } from 'lucide-vue-next'
import { computed, inject, nextTick, onMounted, ref, watch } from 'vue'
import { useRoute } from 'vue-router'
import getImageUrl from '../utils/getImageURL'

const route = useRoute()
const openRequestModal = inject('openRequestModal')
const sliderContainer = ref(null)
const canScrollLeft = ref(false)
const canScrollRight = ref(false)

const currentService = computed(() => {
  const id = parseInt(route.params.id)
  return detailServicesData.find((s) => s.id === id)
})

const includeData = computed(() => {
  if (!currentService.value) return null
  const id = parseInt(route.params.id)
  return includePartData.find((i) => i.id === id)
})

const updateScrollState = () => {
  if (!sliderContainer.value) return

  const { scrollLeft, scrollWidth, clientWidth } = sliderContainer.value
  const maxScrollLeft = scrollWidth - clientWidth

  canScrollLeft.value = scrollLeft > 2
  canScrollRight.value = scrollLeft < maxScrollLeft - 2
}

const scrollLeft = () => {
  if (!sliderContainer.value) return
  
  const { scrollLeft, scrollWidth, clientWidth } = sliderContainer.value
  
  if (scrollLeft <= 2) {
    // Переход в конец
    sliderContainer.value.scrollTo({ left: scrollWidth - clientWidth, behavior: 'smooth' })
  } else {
    sliderContainer.value.scrollBy({ left: -464, behavior: 'smooth' })
  }
}

const scrollRight = () => {
  if (!sliderContainer.value) return
  
  const { scrollLeft, scrollWidth, clientWidth } = sliderContainer.value
  const maxScrollLeft = scrollWidth - clientWidth
  
  if (scrollLeft >= maxScrollLeft - 2) {
    // Возврат в начало
    sliderContainer.value.scrollTo({ left: 0, behavior: 'smooth' })
  } else {
    sliderContainer.value.scrollBy({ left: 464, behavior: 'smooth' })
  }
}

onMounted(() => {
  nextTick(() => {
    updateScrollState()
  })
})

watch(
  () => route.params.id,
  () => {
    nextTick(() => {
      updateScrollState()
    })
  }
)
</script>

<style scoped>
.back-link {
  position: relative;
  display: inline-flex;
  text-decoration: none;
  padding-bottom: 2px;
  width: fit-content;
}

.back-link::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  width: 0;
  height: 2px;
  background-color: currentColor;
  transition: width 0.3s ease;
}

.back-link:hover::after {
  width: 100%;
}

.back-link:not(:hover)::after {
  left: auto;
  right: 0;
  width: 0;
  transition: width 0.3s ease;
}

div::-webkit-scrollbar {
  height: 0;
}

/* Медиа-запросы для адаптивности */
@media (max-width: 744px) {
  .service-main-title {
    font-size: clamp(40px, 6.25vw, 80px);
  }
  
  .service-description {
    font-size: clamp(16px, 2.5vw, 24px);
  }
  
  .service-section-title {
    font-size: clamp(32px, 5vw, 48px);
  }
  
  .service-slider-text {
    font-size: clamp(24px, 3.75vw, 32px);
  }
}

@media (max-width: 640px) {
  /* Скрываем стрелочки */
  .slider-arrows {
    display: none;
  }
  
  /* Карточки в столбик */
  .service-cards-container {
    flex-direction: column;
    overflow-x: visible;
    overflow-y: visible;
  }
  
  .service-card {
    width: 100%;
    flex-shrink: 1;
  }
}

@media (max-width: 375px) {
  .service-main-title {
    font-size: 40px;
  }
  
  .service-description {
    font-size: 16px;
  }
  
  .service-section-title {
    font-size: 32px;
  }
  
  .service-slider-text {
    font-size: 24px;
  }
}
</style>
