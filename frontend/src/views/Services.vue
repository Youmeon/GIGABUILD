<!-- eslint-disable tailwindcss/no-custom-classname -->
<template>
  <main class="bg-neutral-200 text-text-dark-primary">
    <section
      class="mt-[136px] px-8 py-16 max-lg:mt-20 max-md:mt-16 max-md:px-4"
    >
      <div class="mb-10 flex gap-[132px] max-lg:flex-col max-lg:gap-4">
        <div class="flex flex-col justify-between gap-[51px] max-lg:gap-4">
          <div class="flex items-center justify-start gap-[4.5px] text-center">
            <span>
              <svg
                width="6"
                height="7"
                viewBox="0 0 6 7"
                fill="none"
                xmlns="http://www.w3.org/2000/svg"
              >
                <circle cx="3" cy="3.5" r="3" fill="#3D59EB" />
              </svg>
            </span>
            <span
              class="font-bold uppercase text-text-dark-secondary max-sm:p-1 max-sm:text-[0.7rem]"
            >
              Услуги
            </span>
          </div>
          <h1
            class="text-nowrap align-middle text-[80px] font-medium leading-[115%] tracking-[-4%] text-text-dark-primary max-lg:text-[5rem] max-md:text-[2.5rem] max-sm:text-[2rem]"
          >
            Наши услуги
          </h1>
        </div>
        <div>
          <p
            class="text-[20px] font-normal leading-[150%] tracking-[-4%] text-text-dark-secondary max-md:text-[16px] max-sm:text-[14px]"
          >
            Мы сопровождаем клиента на каждом этапе — будь то приемка квартиры,
            техническое обследование здания, проектирование или строительство.
            Работаем как с частными, так и с коммерческими объектами, помогая
            разобраться в деталях, защитить интересы и добиться качественного
            результата
          </p>
        </div>
      </div>
      <div>
        <div
          class="bg flex h-[647px] flex-col justify-end rounded-2xl p-8 text-neutral-100"
        >
          <h3
            className="text-[2.5rem] font-medium leading-none tracking-[-3%] mb-3"
          >
            Приемка квартир
          </h3>
          <p
            className="leading-[150%] mb-9 text-neutral-100/80 text-[24px] align-middle tracking-[-3%]"
          >
            Осмотр с помощью проф-оборудования, фото и видео-фиксация дефектов и
            оформление акта по СП, ГОСТ, ПУЭ.
          </p>
          <div
            className="max-w-[18.3rem] bg-neutral-100 text-blue-600 rounded-2xl px-5 py-3 flex justify-center"
          >
            <router-link to="/apartment-inspection" className="flex gap-3">
              Подробнее
              <ArrowUpRight />
            </router-link>
          </div>
        </div>
      </div>
      <div class="mt-10 grid grid-cols-3 gap-8">
        <router-link
          v-for="card in cards"
          :key="card.id"
          :to="`/services/${card.id}`"
          class="flex flex-col justify-between overflow-hidden rounded-2xl bg-white shadow-[0_0_40px_0_rgba(59,130,246,0.05)] transition-shadow hover:shadow-lg"
        >
          <div class="p-8">
            <div class="flex items-start justify-between gap-4">
              <div class="flex-1">
                <h4
                  class="mb-6 text-[2rem] font-medium leading-[125%] tracking-[-4%] text-neutral-800"
                >
                  {{ card.title }}
                </h4>
                <p
                  class="text-[20px] leading-[150%] tracking-[-3%] text-neutral-700"
                >
                  {{ card.description }}
                </p>
              </div>
              <div
                class="flex size-9 shrink-0 items-center justify-center rounded-full bg-blue-600/10 text-blue-600"
              >
                <ArrowUpRight class="size-5" />
              </div>
            </div>
          </div>
          <div class="h-[245px] w-full">
            <img
              :src="getImageUrl(card.image)"
              :alt="card.title"
              class="size-full object-cover"
            />
          </div>
        </router-link>
      </div>
    </section>
  </main>
</template>

<script setup>
import servicesData from '@/data/services.json'
import { ArrowUpRight } from 'lucide-vue-next'
import { ref } from 'vue'
import getImageUrl from '../utils/getImageURL'
const cards = ref(servicesData)
</script>

<style>
.bg {
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
  background-image: url('@/assets/images/apart-insp.jpg');
}
</style>
