<template>
  <main class="bg-neutral-200 text-text-dark-primary">
    <section class="mt-[176px] px-8 max-md:mt-16 max-md:px-4">
      <div
        class="mb-[80px] flex items-center justify-start gap-[132px] max-md:mb-8 max-md:flex-col max-md:items-start max-md:gap-4"
      >
        <div
          class="flex w-[332px] items-center justify-start gap-[4.5px] text-center"
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
            class="font-bold uppercase text-text-dark-secondary max-sm:p-1 max-sm:text-[0.7rem]"
          >
            О нас
          </span>
        </div>
        <h1
          class="align-middle text-[80px] font-medium leading-[115%] tracking-[-4%] text-text-dark-primary max-lg:text-[5rem] max-md:text-[2.5rem] max-sm:text-[2rem]"
        >
          О компании
        </h1>
      </div>
      <div class="flex gap-[132px] max-md:flex-col max-md:gap-8">
        <div class="max-md:order-2">
          <img
            :src="textureImage"
            alt=""
            class="max-w-[332px] max-md:w-full max-md:max-w-none"
          />
        </div>
        <div class="max-md:order-1">
          <div class="mb-[64px] flex flex-col gap-4 max-md:mb-8">
            <div
              class="flex flex-col gap-4 max-sm:flex max-sm:items-center max-sm:justify-start max-sm:gap-4"
            >
              <img
                :src="iconShortly"
                alt="icon shortly"
                class="mb-4 max-w-[62px]"
              />
              <h4
                class="align-middle text-[32px] font-medium leading-[125%] tracking-[-4%] text-text-dark-primary max-md:text-[24px] max-sm:text-[20px]"
              >
                Коротко о нас
              </h4>
            </div>

            <p
              class="text-[20px] font-normal leading-[150%] tracking-[-4%] text-text-dark-secondary max-md:text-[16px] max-sm:text-[14px]"
            >
              ООО «СК ДИОНИС» — многопрофильная строительная компания,
              объединяющая экспертов в сфере технического надзора,
              проектирования и строительства. Мы не просто проверяем качество —
              мы создаём его на всех этапах: от проектной документации до сдачи
              объекта «под ключ»
            </p>
          </div>
          <div class="mb-[64px] flex flex-col gap-4 max-md:mb-8">
            <div
              class="flex flex-col gap-4 max-sm:flex max-sm:items-center max-sm:justify-start max-sm:gap-4"
            >
              <img
                :src="iconCommand"
                alt="icon shortly"
                class="mb-4 max-w-[62px] max-sm:w-[48px]"
              />
              <h4
                class="align-middle text-[32px] font-medium leading-[125%] tracking-[-4%] text-text-dark-primary max-md:text-[24px] max-sm:text-[20px]"
              >
                О команде
              </h4>
            </div>
            <p
              class="text-[20px] font-normal leading-[150%] tracking-[-4%] text-text-dark-secondary max-md:text-[16px] max-sm:text-[14px]"
            >
              Наша команда — это инженеры, проектировщики и специалисты
              строительного контроля с официальными допусками СРО, НОСТРОЙ и
              НОПРИЗ. Мы выполняем приёмку квартир, обследование зданий и
              инженерных систем, сопровождаем перепланировки, а также реализуем
              проекты по строительству жилых и коммерческих объектов
            </p>
          </div>
          <div class="mb-[64px] flex flex-col gap-4 max-md:mb-8">
            <div
              class="flex flex-col gap-4 max-sm:flex max-sm:items-center max-sm:justify-start max-sm:gap-4"
            >
              <img
                :src="iconTech"
                alt="icon shortly"
                class="mb-4 max-w-[62px]"
              />
              <h4
                class="align-middle text-[32px] font-medium leading-[125%] tracking-[-4%] text-text-dark-primary max-md:text-[24px] max-sm:text-[20px]"
              >
                Наше оборудование
              </h4>
            </div>

            <p
              class="text-[20px] font-normal leading-[150%] tracking-[-4%] text-text-dark-secondary max-md:text-[16px] max-sm:text-[14px]"
            >
              Мы используем сертифицированное оборудование, строго следуем
              нормативам и всегда соблюдаем сроки. Нам доверяют потому, что мы
              знаем, как должно быть сделано правильно — и добиваемся этого в
              каждой детали
            </p>
          </div>
        </div>
      </div>
    </section>
    <section
      class="mb-[10px] mt-8 rounded-2xl bg-blue-600 px-8 py-16 text-white max-sm:px-4 max-sm:py-8"
    >
      <div class="mb-10 max-sm:mb-6">
        <div class="mb-6 flex items-center gap-1 max-sm:mb-4">
          <span>
            <svg
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
            class="font-bold uppercase text-white/80 max-sm:p-1 max-sm:text-xs"
            >Спектр услуг</span
          >
        </div>
        <h2
          class="text-5xl leading-tight tracking-tight max-sm:text-center max-sm:text-3xl"
        >
          Мы осуществляем
        </h2>
      </div>
      <button
        @click="toggleServices"
        class="mb-6 rounded-lg bg-white px-4 py-2 font-medium text-blue-600 transition hover:bg-gray-200 md:hidden"
      >
        {{ showServices ? 'Свернуть список услуг' : 'Показать список услуг' }}
      </button>
      <div
        :class="{ hidden: !showServices, block: showServices }"
        class="flex flex-col gap-4 max-sm:gap-6 md:block"
      >
        <div
          class="flex flex-col gap-4 max-lg:flex-wrap max-sm:gap-6 md:flex-row"
        >
          <div class="flex flex-1 flex-col justify-between gap-4">
            <div
              class="flex min-h-[302px] flex-col justify-between gap-4 rounded-3xl bg-white p-8 max-sm:min-h-[200px] max-sm:p-4"
            >
              <img
                src="@/assets/images/icon.jpg"
                alt="icon"
                class="mb-1 w-16 rounded-xl"
              />
              <h4
                class="text-3xl font-medium leading-tight tracking-tight text-gray-800 max-sm:text-2xl"
              >
                Комплексное проектирование
              </h4>
              <p
                class="text-xl font-normal leading-relaxed tracking-tight text-gray-600 max-sm:text-base"
              >
                Разработка проектов любой сложности<br />— точно, грамотно, в
                срок
              </p>
            </div>
            <div
              class="flex min-h-[383px] flex-col justify-between gap-4 rounded-3xl bg-white p-8 max-sm:min-h-[220px] max-sm:p-4"
            >
              <img
                src="@/assets/images/icon-1.jpg"
                alt="icon"
                class="mb-1 w-16 rounded-xl"
              />
              <h4
                class="text-3xl font-medium leading-tight tracking-tight text-gray-800 max-sm:text-2xl"
              >
                Подготовка документации к согласованию в частной и Гос
                Экспертизе
              </h4>
              <p
                class="text-xl font-normal leading-relaxed tracking-tight text-gray-600 max-sm:text-base"
              >
                Составим и оформим пакет документов<br />для прохождения
                экспертизы
              </p>
            </div>
            <div
              class="flex min-h-[343px] flex-col justify-between gap-4 rounded-3xl bg-white p-8 max-sm:min-h-[220px] max-sm:p-4"
            >
              <img
                src="@/assets/images/icon-2.jpg"
                alt="icon"
                class="mb-1 w-16 rounded-xl"
              />
              <h4
                class="text-3xl font-medium leading-tight tracking-tight text-gray-800 max-sm:text-2xl"
              >
                Выполнение функций генерального проектировщика
              </h4>
              <p
                class="text-xl font-normal leading-relaxed tracking-tight text-gray-600 max-sm:text-base"
              >
                Обеспечиваем разработку всех<br />проектных решений и смет
              </p>
            </div>
          </div>
          <div class="flex flex-1 flex-col justify-between gap-4">
            <div
              class="flex min-h-[353px] flex-col justify-between gap-4 rounded-3xl bg-white p-8 max-sm:min-h-[220px] max-sm:p-4"
            >
              <img
                src="@/assets/images/icon-3.jpg"
                alt="icon"
                class="mb-1 w-16 rounded-xl"
              />
              <h4
                class="text-3xl font-medium leading-tight tracking-tight text-gray-800 max-sm:text-2xl"
              >
                Организационно-техническая подготовка к строительству
              </h4>
              <p
                class="text-xl font-normal leading-relaxed tracking-tight text-gray-600 max-sm:text-base"
              >
                Этап, обеспечивающий бесперебойное ведение строительно-монтажных
                работ
              </p>
            </div>
            <div
              class="flex min-h-[332px] flex-col justify-between gap-4 rounded-3xl bg-white p-8 max-sm:min-h-[220px] max-sm:p-4"
            >
              <img
                src="@/assets/images/icon-4.jpg"
                alt="icon"
                class="mb-1 w-16 rounded-xl"
              />
              <h4
                class="text-3xl font-medium leading-tight tracking-tight text-gray-800 max-sm:text-2xl"
              >
                Ведение строительно-монтажных работ
              </h4>
              <p
                class="text-xl font-normal leading-relaxed tracking-tight text-gray-600 max-sm:text-base"
              >
                Профессиональное выполнение работ с гарантией соответствия
                техническим требованиям
              </p>
            </div>
            <div
              class="flex min-h-[343px] flex-col justify-between gap-4 rounded-3xl bg-white p-8 max-sm:min-h-[220px] max-sm:p-4"
            >
              <img
                src="@/assets/images/icon-5.jpg"
                alt="icon"
                class="mb-1 w-16 rounded-xl"
              />
              <h4
                class="text-3xl font-medium leading-tight tracking-tight text-gray-800 max-sm:text-2xl"
              >
                Инженерные изыскания и авторский надзор
              </h4>
              <p
                class="text-xl font-normal leading-relaxed tracking-tight text-gray-600 max-sm:text-base"
              >
                Проводим инженерные изыскания и следим за реализацией проекта на
                всех этапах строительства
              </p>
            </div>
          </div>
          <div
            class="flex flex-1 flex-col justify-between gap-4 max-lg:visible max-lg:hidden"
          >
            <div
              class="flex min-h-[302px] flex-col justify-between gap-4 rounded-3xl bg-white p-8 max-sm:min-h-[200px] max-sm:p-4"
            >
              <img
                src="@/assets/images/icon-6.jpg"
                alt="icon"
                class="mb-1 w-16 rounded-xl"
              />
              <h4
                class="text-3xl font-medium leading-tight tracking-tight text-gray-800 max-sm:text-2xl"
              >
                Все виды ремонтных работ
              </h4>
              <p
                class="text-xl font-normal leading-relaxed tracking-tight text-gray-600 max-sm:text-base"
              >
                Капитальный и косметический ремонт помещений любого назначения
              </p>
            </div>
            <div
              class="flex min-h-[383px] flex-col justify-between gap-4 rounded-3xl bg-white p-8 max-sm:min-h-[220px] max-sm:p-4"
            >
              <img
                src="@/assets/images/icon-7.jpg"
                alt="icon"
                class="mb-1 w-16 rounded-xl"
              />
              <h4
                class="text-3xl font-medium leading-tight tracking-tight text-gray-800 max-sm:text-2xl"
              >
                Выполнение консультационных и инжиниринговых услуг
              </h4>
              <p
                class="text-xl font-normal leading-relaxed tracking-tight text-gray-600 max-sm:text-base"
              >
                По виду: техническое обследование зданий и сооружений,
                инженерных систем с выдачей заключения
              </p>
            </div>
            <div
              class="flex min-h-[343px] flex-col justify-between gap-4 rounded-3xl bg-white p-8 max-sm:min-h-[220px] max-sm:p-4"
            >
              <img
                src="@/assets/images/icon-8.jpg"
                alt="icon"
                class="mb-1 w-16 rounded-xl"
              />
              <h4
                class="text-3xl font-medium leading-tight tracking-tight text-gray-800 max-sm:text-2xl"
              >
                Строительство домов, коттеджей и других объектов под ключ
              </h4>
              <p
                class="text-xl font-normal leading-relaxed tracking-tight text-gray-600 max-sm:text-base"
              >
                Комплексное строительство жилых и нежилых объектов
              </p>
            </div>
          </div>
        </div>
      </div>
    </section>
    <article class="mt-[-32px] rounded-2xl bg-neutral-200 px-8 py-20">
      <div class="mb-10 flex flex-col gap-6">
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
            Сертификаты
          </span>
        </div>
        <h1
          class="align-middle text-[80px] font-medium leading-[115%] tracking-[-4%] text-text-dark-primary max-lg:text-[5rem] max-md:text-[2.5rem] max-sm:text-[2rem]"
        >
          Свидетельство о допуске к строительным и проектировочным работам
        </h1>
      </div>
      <div class="flex flex-col gap-4">
        <a
          href="#"
          class="flex gap-8 rounded-[32px] bg-neutral-100 px-8 py-[34.2px]"
        >
          <img
            src="@/assets/images/pdf.jpg"
            alt="icon"
            class="mb-1 size-20 rounded-xl"
          />
          <div class="flex flex-col gap-2">
            <h4
              class="text-3xl font-medium leading-tight tracking-tight text-gray-800 max-sm:text-2xl"
            >
              ВЫПИСКА из единого реестра сведений о членах СРО
            </h4>
            <p
              class="text-xl font-normal leading-[135%] tracking-tight text-gray-600 max-sm:text-base"
            >
              в области инженерных изысканий и в области
              архитектурно-строительного проектирования и их обязательствах
            </p>
          </div>
        </a>
        <a
          href="#"
          class="flex gap-8 rounded-[32px] bg-neutral-100 px-8 py-[34.2px]"
        >
          <img
            src="@/assets/images/pdf.jpg"
            alt="icon"
            class="mb-1 size-20 rounded-xl"
          />
          <div class="flex flex-col gap-2">
            <h4
              class="text-3xl font-medium leading-tight tracking-tight text-gray-800 max-sm:text-2xl"
            >
              УВЕДОМЛЕНИЕ о включении сведений в Национальный реестр
              специалистов
            </h4>
            <p
              class="text-xl font-normal leading-[135%] tracking-tight text-gray-600 max-sm:text-base"
            >
              в области инженерных изысканий и архитектурно-строительного
              проектирования
            </p>
          </div>
        </a>
      </div>
    </article>
  </main>
</template>

<script setup>
import textureImage from '@/assets/images/asidetexture.jpg'
import iconCommand from '@/assets/images/icon-command.jpg'
import iconShortly from '@/assets/images/icon-shortly.jpg'
import iconTech from '@/assets/images/icon-tech.jpg'
import { ref } from 'vue'
const showServices = ref(false)
const toggleServices = () => {
  showServices.value = !showServices.value
}
</script>
