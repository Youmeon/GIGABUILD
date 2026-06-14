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
          <h3 class="mb-3 text-[2.5rem] font-medium leading-none tracking-[-3%]">
            Приемка квартир
          </h3>
          <p class="mb-9 text-[24px] leading-[150%] tracking-[-3%] text-neutral-100/80">
            Осмотр с помощью проф-оборудования, фото и видео-фиксация дефектов и
            оформление акта по СП, ГОСТ, ПУЭ.
          </p>
          <ButtonDetails
            to="/apartment-inspection"
            variant="secondary"
            class="w-full max-w-[332px]"
          />
        </div>
      </div>
      <div
        class="mt-10 grid grid-cols-3 justify-items-center gap-8 max-[1328px]:grid-cols-2 max-[1328px]:justify-items-stretch max-[744px]:gap-[0.625rem] max-md:grid-cols-2 max-sm:grid-cols-1"
      >
        <CardService v-for="card in cards" :key="card.id" :card="card" />
      </div>
    </section>
  </main>
</template>

<script setup>
import servicesData from '@/data/services.json'
import { ref } from 'vue'
import ButtonDetails from '../components/ButtonDetails.vue'
import CardService from '../components/CardService.vue'
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
