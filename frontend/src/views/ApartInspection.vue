<template>
  <main>
    <section
      className="w-full h-[52.625rem] max-sm:h-full absolute top-0 left-0 bg-center bg-cover pb-16 max-sm:px-4"
      :style="{ backgroundImage: 'url(' + heroImage + ')' }"
    >
      <div className="mt-[566px] max-sm:mt-[314px] max-sm:px-4 px-8">
        <div class="mb-20">
          <h1 className=" text-neutral-100 xl:text-[5rem]">Приемка квартир</h1>
        </div>
        <div className="rounded-2xl">
          <router-link
            to="#"
            class="size-full rounded-2xl bg-neutral-100 px-[55px] py-[18px] text-center align-middle text-[20px] font-medium leading-none tracking-[-3%] text-blue-600 transition-all duration-300 ease-out hover:bg-blue-500 hover:text-neutral-100 focus:bg-blue-400 focus:text-neutral-100 max-lg:px-4 max-lg:py-3 max-sm:text-[16px]"
          >
            Записаться на приёмку
          </router-link>
        </div>
      </div>
    </section>
    <section
      className="bg-blue-600 pb-28 max-sm:h-[953px] h-full px-8 z-[6] py-16 max-sm:py-3 w-full rounded-2xl relative translate-y-[835px] mt-[-16px] max-sm:translate-y-[648px]"
    >
      <div
        className="flex-col mb-[64px] justify-between max-w-[850px] flex gap-10 max-md:flex-col max-sm:gap-0 max-sm:px-4 text-neutral-100 max-sm:py-0"
      >
        <div className="flex mb-6 max-sm:mb-4 flex-col max-sm:max-w-full">
          <div className="mb-6 max-sm:mb-4 flex items-center gap-[4.5px]">
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
              className="uppercase text-neutral-100/80 max-sm:text-[0.7rem] max-sm:p-1 font-bold"
              >Об услуге</span
            >
          </div>
          <h2
            className="leading-[125%] text-[48px] tracking-[-3%] max-sm:text-[28px] max-sm:text-center"
          >
            Что входит в приёмку квартиры?
          </h2>
        </div>
        <div className="flex flex-col gap-4 max-sm:hidden text-neutral-100/80">
          <p className="leading-[150%] text-[24px] align-middle tracking-[-3%]">
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
      className="bg-neutral-200 px-8 z-20 py-16 max-sm:py-2 w-full rounded-2xl relative translate-y-[825px] mt-[-16px] max-sm:translate-y-[640px]"
    >
      <div class="flex gap-4 pb-16">
        <div class="flex flex-1 flex-col justify-between">
          <div>
            <div
              className="flex items-center gap-[4.5px] mb-6 tracking-[-4%] text-sm leading-[110%] align-middle"
            >
              <span
                ><svg
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
                className="uppercase text-text-dark-secondary max-sm:text-[0.7rem] max-sm:p-1 font-bold"
                >Оборудование</span
              >
            </div>
            <h2
              className="font-semibold leading-[125%] text-5xl tracking-[-3%] mb-10"
            >
              Используемые инструменты
            </h2>
          </div>
          <p
            className="tracking-[-3%] pr-[68px] align-middle text-xl leading-[135%] font-normal text-text-dark-secondary"
          >
            Наши специалисты приезжают со своим набором поверенных и
            сертифицированных инструментов — всё откалибровано и соответствует
            стандартам, чтобы вы получили объективную и надёжную оценку
          </p>
        </div>
        <div class="max-w-[912px]">
          <img
            src="@/assets/images/secondmer.jpg"
            alt="Секундомер"
            class="rounded-[32px]"
          />
        </div>
      </div>
      <div class="flex flex-col gap-4 pb-16">
        <div
          className="flex items-center gap-[4.5px] mb-6 tracking-[-4%] text-sm leading-[110%] align-middle"
        >
          <span
            ><svg
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
            className="uppercase text-text-dark-secondary max-sm:text-[0.7rem] max-sm:p-1 font-bold"
            >Тарифы</span
          >
        </div>
        <h2
          className="font-semibold leading-[125%] text-5xl tracking-[-3%] mb-10"
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
                    class="text-[16px] font-normal leading-[135%] tracking-[-3%] text-gray-500"
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
                    class="text-[16px] font-normal leading-[135%] tracking-[-3%] text-neutral-200/80"
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
</script>

<style scoped>
.bg {
  width: 100vw;
  height: 100vh;
  position: absolute;
  top: 0;
  left: 0;
  background-position: center;
  background-size: cover;
  z-index: -5;
}

.relative {
  position: relative;
}

.priemka {
  background-image: url(../assets/images/schempomoch.png);
  background-size: cover;
  background-repeat: no-repeat;
}
</style>
