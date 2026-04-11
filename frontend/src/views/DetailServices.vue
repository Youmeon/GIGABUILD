<template>
  <main class="bg-neutral-200">
    <section v-if="currentService" class="mt-[136px]">
      <div class="relative h-[500px] w-full">
        <img
          :src="getImageUrl(currentService.image)"
          :alt="currentService.title"
          class="size-full object-cover"
        />
        <button
          @click="openRequestModal"
          class="absolute bottom-[60px] left-8 rounded-2xl bg-white px-5 py-3 text-[20px] font-medium tracking-[-3%] text-blue-600 transition-colors hover:bg-neutral-100"
        >
          Записаться на приёмку
        </button>
        <div class="absolute inset-x-0 bottom-0 h-[33px] bg-[#fafafc]"></div>
      </div>

      <div class="px-8 py-16">
        <div class="mb-16">
          <router-link
            to="/services"
            class="mb-8 inline-flex items-center gap-2 text-[20px] font-medium tracking-[-3%] text-blue-600"
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
            class="mb-8 text-[80px] font-medium leading-[115%] tracking-[-4%] text-neutral-800"
          >
            {{ currentService.title }}
          </h1>
          <div class="rounded-[32px] bg-white p-8">
            <p
              class="text-[24px] font-medium leading-[150%] tracking-[-3%] text-[#3b3b3c]"
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
              class="text-[48px] font-semibold leading-[125%] tracking-[-3%] text-white"
            >
              {{ includeData?.title }}
            </h2>
            <div class="flex gap-2">
              <button
                @click="scrollLeft"
                class="flex size-10 items-center justify-center rounded-xl bg-white/30 transition-colors hover:bg-white/40"
              >
                <svg
                  width="24"
                  height="24"
                  viewBox="0 0 24 24"
                  fill="none"
                  xmlns="http://www.w3.org/2000/svg"
                >
                  <path
                    d="M15 18L9 12L15 6"
                    stroke="white"
                    stroke-width="2"
                    stroke-linecap="round"
                    stroke-linejoin="round"
                  />
                </svg>
              </button>
              <button
                @click="scrollRight"
                class="flex size-10 items-center justify-center rounded-xl bg-white transition-colors hover:bg-neutral-100"
              >
                <svg
                  width="24"
                  height="24"
                  viewBox="0 0 24 24"
                  fill="none"
                  xmlns="http://www.w3.org/2000/svg"
                >
                  <path
                    d="M9 18L15 12L9 6"
                    stroke="#262628"
                    stroke-width="2"
                    stroke-linecap="round"
                    stroke-linejoin="round"
                  />
                </svg>
              </button>
            </div>
          </div>
        </div>

        <div
          ref="sliderContainer"
          class="flex gap-4 overflow-x-auto scroll-smooth pb-4"
        >
          <div
            v-for="(item, index) in includeData?.items"
            :key="index"
            class="w-[448px] shrink-0 rounded-[32px] bg-white p-8"
          >
            <p
              class="text-[32px] font-medium leading-[125%] tracking-[-4%] text-neutral-800"
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
import { ref, computed, inject } from 'vue'
import { useRoute } from 'vue-router'
import { ArrowUpRight } from 'lucide-vue-next'
import detailServicesData from '@/data/detail_services.json'
import includePartData from '@/data/include_part_detail_service.json'
import getImageUrl from '../utils/getImageURL'

const route = useRoute()
const openRequestModal = inject('openRequestModal')
const sliderContainer = ref(null)

const currentService = computed(() => {
  const id = parseInt(route.params.id)
  return detailServicesData.find((s) => s.id === id)
})

const includeData = computed(() => {
  if (!currentService.value) return null
  const id = parseInt(route.params.id)
  return includePartData.find((i) => i.id === id)
})

const scrollLeft = () => {
  if (!sliderContainer.value) return
  sliderContainer.value.scrollBy({ left: -464, behavior: 'smooth' })
}

const scrollRight = () => {
  if (!sliderContainer.value) return
  sliderContainer.value.scrollBy({ left: 464, behavior: 'smooth' })
}
</script>

<style scoped>
div::-webkit-scrollbar {
  height: 0;
}
</style>
