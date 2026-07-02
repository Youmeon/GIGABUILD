<template>
  <main>
    <section
      class="w-full h-[52.625rem] relative bg-center bg-cover max-[744px]:h-[100dvh]"
      :style="{ backgroundImage: 'url(' + heroImage + ')' }"
    >
      <div class="absolute bottom-16 left-0 right-0 px-8">
        <div class="flex flex-col">
          <h1 class="text-neutral-100 text-[5rem] leading-[0.95] mb-8">
            Приемка квартир
          </h1>
          <router-link
            @click="openRequestModal"
            to="#"
            class="inline-block w-fit rounded-2xl bg-neutral-100 px-[55px] py-[18px] text-center align-middle text-[20px] font-medium leading-none tracking-[-3%] text-blue-600 transition-all duration-300 ease-out hover:bg-blue-500 hover:text-neutral-100 focus:bg-blue-400 focus:text-neutral-100"
          >
            Записаться на приёмку
          </router-link>
        </div>
      </div>
    </section>

    <section
      class="bg-blue-600 pb-28 px-8 z-[6] py-16 w-full rounded-2xl relative -mt-6"
    >
      <div
        class="flex-col mb-[64px] justify-between max-w-[850px] flex gap-10 text-neutral-100"
      >
        <div class="flex mb-6 flex-col">
          <div class="mb-6 flex items-center gap-[4.5px]">
            <span
              ><svg
                width="6"
                height="7"
                viewBox="0 0 6 7"
                fill="none"
                xmlns="http://www.w3.org/2000/svg"
              >
                <circle cx="3" cy="3.5" r="3" fill="white" fill-opacity="0.8" />
              </svg>
            </span>
            <span
              class="uppercase text-neutral-100/80 font-bold"
              >Об услуге</span
            >
          </div>
          <h2
            class="leading-[125%] text-[48px] tracking-[-3%]"
          >
            Что входит в приёмку квартиры?
          </h2>
        </div>
        <div class="flex flex-col gap-4 text-neutral-100/80">
          <p class="leading-[150%] text-[24px] align-middle tracking-[-3%]">
            Согласуем удобное время, приедем и проведём тщательный осмотр по
            стандартам СП, ГОСТ и ПУЭ. Зафиксируем все выявленные недостатки, в
            том числе на фото и видео, а в конце передадим вам подробный акт
            осмотра с рекомендациями от эксперта.
          </p>
        </div>
      </div>
      <!-- add slider! -->
      <InspectionSlider />
      <!-- add slider! -->
    </section>
    <section
      class="bg-neutral-200 px-[clamp(1rem,5vw,2rem)] z-20 py-16 w-full rounded-2xl relative -mt-6"
    >
      <div class="pb-16">
        <ToolsBanner :tools="toolsData" />
      </div>
      <div class="flex flex-col gap-4 pb-4">
        <div
          class="flex items-center gap-[4.5px] mb-0 tracking-[-4%] text-sm leading-[110%] align-middle"
        >
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
            class="uppercase text-text-dark-secondary font-bold"
            >Тарифы</span
          >
        </div>
        <h2
          class="font-semibold leading-[125%] text-5xl tracking-[-3%] mb-0"
        >
          Сколько стоит приёмка квартиры
        </h2>
        <div>
          <div
            class="flex justify-center gap-4 p-4 text-center max-md:flex-col max-sm:gap-2"
          >
            <!-- Левая карточка (Tariff 1) -->
             <div
              class="flex flex-1 flex-col justify-between rounded-[32px] border-blue-600 bg-neutral-100 p-4 text-center shadow-sm"
            >
              <div class="px-4 pt-4">
                <div
                  class="mx-auto mb-10 flex max-w-fit items-center justify-center rounded-xl border-2 border-blue-300/20 px-4 py-2 text-center"
                >
                  <span class="mr-2 size-2 rounded-full bg-gray-500"></span>
                  <span
                    class="tariff-label text-[16px] font-normal leading-[135%] tracking-[-3%] text-gray-500"
                    >Тариф 1</span
                  >
                </div>
                <div class="mb-8 text-center">
                  <h2
                    class="mb-1 text-center align-middle text-[32px] font-medium leading-[125%] tracking-[-4%] text-text-dark-primary"
                  >
                    Площадь квартиры
                  </h2>
                  <span
                    class="text-center align-middle text-[48px] font-semibold leading-[125%] tracking-[-3%] text-blue-600"
                    >До 40 м²</span
                  >
                </div>
                <p
                  class="mx-auto mb-[48px] max-w-[392px] text-center align-bottom text-[20px] font-normal leading-[150%] tracking-[-3%] text-gray-600"
                >
                  Оптимальное решение для студий<br />
                  и небольших квартир. Полная проверка<br />
                  за фиксированную цену
                </p>
                <div class="mb-8">
                  <p
                    class="mb-1 text-center align-bottom text-[20px] font-medium leading-[135%] tracking-[-3%] text-gray-600"
                  >
                    Стоимость
                  </p>
                  <p
                    class="text-center align-middle text-[48px] font-semibold leading-[125%] tracking-[-3%] text-blue-600"
                  >
                    4 000 руб.
                  </p>
                </div>
              </div>
              <button
                @click="openRequestModal"
                class="w-full rounded-[16px] bg-blue-600 py-[18px] align-middle font-normal leading-none tracking-[-3%] text-white hover:bg-blue-700"
              >
                Заказать приёмку
              </button>
            </div>

            <!-- Правая карточка (Tariff 2) -->
            <div
              class="flex flex-1 flex-col justify-between rounded-[32px] bg-blue-600 p-4 text-center shadow-sm"
            >
              <div class="px-4 pt-4">
                <div
                  class="mx-auto mb-10 flex max-w-fit items-center justify-center rounded-xl border border-solid border-blue-200/30 bg-blue-500 px-4 py-2 text-center"
                >
                  <span
                    class="mr-2 size-2 rounded-full bg-neutral-200/80"
                  ></span>
                  <span
                    class="tariff-label text-[16px] font-normal leading-[135%] tracking-[-3%] text-neutral-200/80"
                    >Тариф 2</span
                  >
                </div>
                <div class="mb-8 text-center text-neutral-100">
                  <h2
                    class="mb-1 text-center align-middle text-[32px] font-medium leading-[125%] tracking-[-4%]"
                  >
                    Площадь квартиры
                  </h2>
                  <span
                    class="text-center align-middle text-[48px] font-semibold leading-[125%] tracking-[-3%]"
                    >До 40 м²</span
                  >
                </div>
                <p
                  class="mx-auto mb-[48px] max-w-[392px] text-center align-bottom text-[20px] font-normal leading-[150%] tracking-[-3%] text-neutral-200/80"
                >
                  Подходит для просторных<br />
                  квартир и апартаментов.<br />
                  Стоимость зависит от метража
                </p>
                <div class="mb-8">
                  <p
                    class="mb-1 text-center align-bottom text-[20px] font-medium leading-[135%] tracking-[-3%] text-neutral-200/80"
                  >
                    Стоимость
                  </p>
                  <p
                    class="text-center align-middle text-[48px] font-semibold leading-[125%] tracking-[-3%] text-neutral-100"
                  >
                    100 руб. / м²
                  </p>
                </div>
              </div>
              <button
                @click="openRequestModal"
                class="w-full rounded-[16px] bg-neutral-100 py-[18px] align-middle font-normal leading-none tracking-[-3%] text-blue-600"
              >
                Заказать приёмку
              </button>
            </div>
          </div>
        </div>
      </div>
    </section>
  </main>
</template>

<script setup>
import heroImage from '@/assets/images/apart-insp.jpg'
import InspectionSlider from '@/components/InspectionSlider.vue'
import ToolsBanner from '@/components/ToolsBanner.vue'
import toolsData from '@/data/acceptance-of-apartments-tools.json'
import { inject } from 'vue'
const openRequestModal = inject('openRequestModal')
</script>
<style scoped>
/* 744px — плавно от десктопа */
@media screen and (max-width: 744px) {
  section:first-of-type a {
    font-size: clamp(1rem, 2.5vw, 1.25rem) !important;
    padding-left: 1.5rem !important;
    padding-right: 1.5rem !important;
    width: fit-content !important;
  }

  section:first-of-type h1 {
    margin-bottom: clamp(1.25rem, 2.7vw, 2rem) !important;
  }

  section:first-of-type > div {
    padding-left: 1.25rem !important;
    padding-right: 1.25rem !important;
    bottom: clamp(4rem, 8vw, 4rem) !important;
  }

  /* Секция 2 */
  section:nth-of-type(2) h2 {
    font-size: clamp(2rem, 5.6vw, 3rem) !important;
    text-align: left !important;
  }

  section:nth-of-type(2) > div:first-child > div:first-child > div:first-child {
    margin-bottom: clamp(1.5rem, 3.2vw, 3rem) !important;
  }

  section:nth-of-type(2) > div:first-child {
    gap: clamp(2rem, 3.5vw, 2.5rem) !important;
    margin-bottom: clamp(3rem, 5.4vw, 4rem) !important;
    padding-left: 1.25rem !important;
    padding-right: 1.25rem !important;
  }

  section:nth-of-type(2) > div:first-child > div:last-child p {
    font-size: clamp(1.25rem, 2.7vw, 1.5rem) !important;
  }
}

/* 640px и ниже */
@media screen and (max-width: 640px) {
  section:first-of-type h1 {
    font-size: clamp(2.5rem, 8vw, 3.5rem) !important;
  }

  section:first-of-type > div {
    bottom: 4rem !important;
    padding-left: 1rem !important;
    padding-right: 1rem !important;
  }

  section:first-of-type a {
    width: fit-content !important;
    display: inline-block !important;
    padding-left: 1.5rem !important;
    padding-right: 1.5rem !important;
  }

  section:nth-of-type(2) {
    padding-left: 1rem !important;
    padding-right: 1rem !important;
    padding-bottom: 3rem !important;
  }

  section:nth-of-type(2) h2 {
    font-size: clamp(2rem, 5.6vw, 3rem) !important;
    text-align: left !important;
  }

  section:nth-of-type(2) > div:first-child > div:first-child > div:first-child {
    margin-bottom: clamp(1.5rem, 4vw, 3rem) !important;
  }

  section:nth-of-type(2) > div:first-child {
    gap: clamp(2rem, 3.5vw, 2.5rem) !important;
    margin-bottom: clamp(2rem, 4.8vw, 3rem) !important;
    padding-left: 0 !important;
  }

  section:nth-of-type(2) > div:first-child > div:last-child p {
    font-size: clamp(1.25rem, 2.7vw, 1.5rem) !important;
  }
}

@media (max-width: 744px) {
  /* Заголовок "Сколько стоит приёмка квартиры" */
  section:nth-of-type(3) .flex.flex-col.gap-4 > h2 {
    font-size: clamp(2rem, 5.6vw, 3rem) !important;
  }

  /* Площадь квартиры */
  section:nth-of-type(3) .flex.flex-1.flex-col h2 {
    font-size: clamp(1.25rem, 3.7vw, 2rem) !important;
  }

  /* До 40 м² — только span внутри div.mb-8 */
  section:nth-of-type(3) .flex.flex-1.flex-col .mb-8 span {
    font-size: clamp(2rem, 5.6vw, 3rem) !important;
  }

  /* Тариф 1 / Тариф 2 — фиксируем 16px */
  section:nth-of-type(3) .tariff-label {
    font-size: 1rem !important;
  }

  /* Описание тарифа и стоимость лейбл */
  section:nth-of-type(3) .flex.flex-1.flex-col p {
    font-size: clamp(1rem, 2.7vw, 1.25rem) !important;
  }

  /* Цена (4000 руб / 100 руб м²) */
  section:nth-of-type(3) .flex.flex-1.flex-col .mb-8 p:last-child {
    font-size: clamp(2rem, 5.6vw, 3rem) !important;
  }
}
</style>