<template>
  <main>
    <section
      className="w-full h-[52.625rem] max-sm:h-full absolute top-0 left-0 bg-center bg-cover pb-16 max-sm:px-4"
      :style="{ backgroundImage: 'url(' + heroImage + ')' }"
    >
      <div className="mt-[566px] max-sm:mt-[314px] max-sm:px-4 px-8">
        <div>
          <h1 className=" text-neutral-100 xl:text-[5rem] mb-1">
            Приемка квартир <br class="hidden max-[744px]:block" />в новостройке
          </h1>
          <p className="text-neutral-100/80 mb-10 xl:mt-8">
            Широкий профиль, гарантия качества и внимание к деталям!
          </p>
        </div>
        <ButtonDetails
          to="/apartment-inspection"
          variant="primary"
          class="w-full max-w-[18.3rem]"
        />
      </div>
    </section>
    <section
      className="bg-blue-600 px-8 z-[6] py-16 max-sm:py-2 w-full rounded-2xl relative translate-y-[835px] mt-[-16px] max-sm:translate-y-[648px]"
    >
      <div
        className="max-sm:flex-col justify-between flex  xl:gap-[273px] lg:gap-[20px] max-md:gap-[20px] max-lg:gap-[20px] max-md:flex-col max-sm:gap-0 max-sm:px-4 text-neutral-100 max-sm:py-0"
      >
        <div
          className="flex mb-16 max-sm:mb-4 flex-col max-w-[423px] max-sm:max-w-full"
        >
          <div
            className="mb-24 max-md:mb-12 max-sm:mb-4 flex items-center gap-[4.5px]"
          >
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
              >О компании</span
            >
          </div>
          <h2
            className="leading-[125%] text-[48px] tracking-[-3%] max-sm:text-[28px] max-sm:text-center"
          >
            Почему выбирают именно нас
          </h2>
        </div>
        <div
          className="flex flex-col gap-4 w-[680px] max-sm:hidden text-neutral-100/80"
        >
          <p className="leading-[150%] text-[24px] align-middle tracking-[-3%]">
            «ДИОНИС» — многопрофильная строительная компания, объединяющая
            экспертов в сфере технического надзора, проектирования и
            строительства.
          </p>
          <p
            className="leading-[150%] text-[24px] align-middle tracking-[-3%] max-md:hidden"
          >
            Мы не просто проверяем качество — мы создаём его на всех этапах: от
            проектной документации до сдачи объекта «под ключ»
          </p>
        </div>
      </div>
      <div
        className="flex justify-between max-lg:mt-10 max-lg:pb-8 gap-4 max-sm:flex-wrap max-sm:flex-col pb-16"
      >
        <div
          className="p-8 bg-neutral-100 rounded-[2rem] max-sm:p-6 flex max-lg:items-center flex-col max-lg:justify-center max-lg:p-6"
        >
          <p
            className="text-[2.5rem] max-sm:text-[1.5rem] max-sm:mb-2 mb-4 leading-none tracking-[-3%] align-middle font-medium"
          >
            1000+ объектов
          </p>
          <p className="text-md tracking-[-3%] align-middle">
            Успешно проверили по ГОСТ и СНиП
          </p>
        </div>
        <div
          className="p-8 bg-neutral-100 rounded-[2rem] max-sm:p-6 flex max-lg:items-center flex-col max-lg:justify-center max-lg:p-6"
        >
          <p
            className="text-[2.5rem] mb-4 leading-none tracking-[-3%] align-middle font-medium max-sm:text-[1.5rem] max-sm:mb-2 max-lg:flex max-lg:justify-between items-center"
          >
            Состоим в СРО
          </p>
          <p className="text-md tracking-[-3%] align-middle">
            Имеем допуски НОСТРОЙ и НОПРИЗ
          </p>
        </div>
        <div
          className="p-8 bg-neutral-100 rounded-[2rem] max-sm:p-6 flex max-lg:items-center flex-col max-lg:justify-center max-lg:p-6"
        >
          <p
            className="text-[2.5rem] mb-4 leading-none tracking-[-3%] align-middle font-medium max-sm:text-[1.5rem] max-sm:mb-2 max-lg:flex max-lg:justify-between items-center"
          >
            20+ лет опыта
          </p>
          <p className="text-md tracking-[-3%] align-middle">
            В строительстве и контроле качества
          </p>
        </div>
      </div>
    </section>
    <section
      className="bg-neutral-200 px-8 z-20 py-16 max-sm:py-2 w-full rounded-2xl relative translate-y-[825px] mt-[-16px] max-sm:translate-y-[640px]"
    >
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
            className="uppercase text-text-dark-secondary font-bold max-sm:text-[0.7rem] max-sm:p-1"
            >Услуги</span
          >
        </div>
        <h2
          className="font-semibold leading-[125%] text-5xl tracking-[-3%] mb-10"
        >
          С чем мы можем вам помочь
        </h2>
        <div
          className="flex justify-end flex-col priemka h-[40.4375rem] w-full rounded-2xl text-neutral-100 p-8 mb-10"
        >
          <h3
            className="text-[2.5rem] font-medium leading-none tracking-[-3%] mb-3"
          >
            Приемка квартир
          </h3>
          <p
            className="tracking-[-3%] align-middle text-xl leading-[135%] font-medium mb-9 text-neutral-100/80"
          >
            Осмотр с помощью проф-оборудования, фото и видео-фиксация дефектов и
            оформление акта по СП, ГОСТ, ПУЭ.
          </p>
          <ButtonDetails
            to="/apartment-inspection"
            variant="secondary"
            class="w-full max-w-[18.3rem]"
          />
        </div>
      </div>
      <div
        class="grid grid-cols-3 justify-items-center gap-8 max-[1328px]:grid-cols-2 max-[1328px]:justify-items-stretch max-[744px]:gap-[0.625rem]"
      >
        <CardService v-for="card in cards" :key="card.id" :card="card" />
      </div>
    </section>
    <section
      className="bg-blue-600 px-8 py-16 max-sm:py-2 max-sm:h-[510px] h-[730px] w-full relative translate-y-[830px] max-sm:translate-y-[650px] mt-[-16px] z-30 rounded-2xl"
    >
      <div>
        <div
          className="mb-6 max-md:mb-3 max-sm:mb-2 flex items-center gap-[4.5px]"
        >
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
            >Отзывы</span
          >
        </div>
      </div>
      <div>
        <SliderReviews />
      </div>
    </section>
  </main>
</template>

<script setup>
import heroImage from '@/assets/images/img.jpg'
import servicesData from '@/data/services.json'
import { ref } from 'vue'
import ButtonDetails from '../components/ButtonDetails.vue'
import SliderReviews from '../components/SliderReviews.vue'
import CardService from '../components/CardService.vue'
const cards = ref(servicesData)
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

/* Media queries для 744px */
@media screen and (max-width: 744px) {
  /* Hero секция */
  section:first-of-type {
    height: 52.625rem !important;
    padding-bottom: 4rem !important;
  }
  
  section:first-of-type > div {
    margin-top: 474px !important;
    padding-left: 1.25rem !important;
    padding-right: 2rem !important;
  }
  
  section:first-of-type h1 {
    font-size: 5rem !important;
    line-height: 0.95 !important;
    letter-spacing: -3.17px !important;
  }
  
  section:first-of-type p {
    font-size: 1.5rem !important;
    line-height: 1.5 !important;
    letter-spacing: -0.71px !important;
    margin-bottom: 2rem !important;
  }
  
  /* Секция "О компании" */
  section:nth-of-type(2) {
    padding-top: 2rem !important;
    padding-left: 1.25rem !important;
    padding-right: 1.25rem !important;
    gap: 4rem;
  }
  
  section:nth-of-type(2) > div:first-child {
    flex-direction: column !important;
    gap: 1.625rem !important;
  }
  
  section:nth-of-type(2) > div:first-child > div:first-child {
    max-width: 100% !important;
    margin-bottom: 0 !important;
  }
  
  section:nth-of-type(2) > div:first-child > div:first-child > div:first-child {
    margin-bottom: 3rem !important;
  }
  
  section:nth-of-type(2) > div:first-child > div:first-child h2 {
    text-align: left !important;
    max-width: 420px;
  }
  
  section:nth-of-type(2) > div:first-child > div:last-child {
    display: flex !important;
    width: 100% !important;
    margin-left: 0 !important;
    margin-top: 0 !important;
  }
  
  section:nth-of-type(2) > div:first-child > div:last-child p {
    font-size: 1.5rem !important;
    line-height: 1.5 !important;
    letter-spacing: -0.71px !important;
  }
  
  section:nth-of-type(2) > div:first-child > div:last-child p:last-child {
    display: block !important;
  }
  
  /* Карточки статистики */
  section:nth-of-type(2) > div:last-child {
    flex-direction: column !important;
    gap: 1rem !important;
    padding-bottom: 0 !important;
  }
  
  section:nth-of-type(2) > div:last-child > div {
    padding: 2.1875rem 2rem !important;
  }
  
  section:nth-of-type(2) > div:last-child > div p:first-child {
    font-size: 2.5rem !important;
    margin-bottom: 1rem !important;
  }
  
  section:nth-of-type(2) > div:last-child > div p:last-child {
    font-size: 1.25rem !important;
  }
}

@media screen and (max-width: 640px) {
  section:first-of-type > div {
    margin-left: 1rem !important;
    margin-right: 1rem !important;
  }
  
  section:nth-of-type(2) {
    padding-left: 0 !important;
    padding-right: 0 !important;
  }
  
  section:nth-of-type(2) > div:first-child {
    padding-left: 0 !important;
    padding-right: 0 !important;
  }
}
</style>
