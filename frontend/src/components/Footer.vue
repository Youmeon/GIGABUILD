<template>
  <footer
    :class="{
      'home-footer-stack translate-y-[830px] max-sm:translate-y-[650px]': isSpecialPage,
      'relative z-30 mt-[-30px] max-h-full w-full rounded-2xl rounded-b-none bg-blue-600 px-8 pb-[28px] pt-16 max-sm:py-2 max-[744px]:mt-[-16px] max-[744px]:rounded-t-none': true,
    }"
  >
    <div
      class="flex items-baseline justify-between max-[744px]:flex-col max-[744px]:items-start max-[744px]:gap-16"
    >
      <div
        class="flex max-w-[516px] flex-col gap-10 lg:mb-[50px] xl:mb-[215px] max-[744px]:max-w-full max-[744px]:gap-10 max-[744px]:items-start max-[744px]:text-left"
      >
        <h2
          class="text-5xl font-semibold leading-[125%] tracking-[-3%] text-neutral-100 max-sm:text-2xl max-[744px]:text-5xl max-[744px]:leading-normal max-[744px]:tracking-[-1.43px] max-[744px]:text-left"
        >
          Оставьте заявку<br />
          и мы свяжемся с вами в ближайшее время
        </h2>
        <button
          @click = "openRequestModal"
          class="max-w-[384px] rounded-2xl bg-neutral-800 transition-all duration-300 ease-out px-8 py-5 text-center align-middle text-[20px] font-medium leading-none tracking-[-3%] text-neutral-100 max-sm:text-[16px] hover:bg-neutral-700 max-[744px]:w-full max-[744px]:max-w-[448px] max-[744px]:py-5 max-[744px]:px-8 max-[744px]:text-[20px] max-[744px]:tracking-[-0.59px]"
        >
          Оставить заявку
        </button>
      </div>
      <div
        class="flex flex-col flex-nowrap gap-[10px] text-[48px] max-sm:text-2xl max-[744px]:gap-[5px] max-[744px]:items-start max-[744px]:w-full"
      >
        <a
          href="tel:+79144110611"
          class="footer-link footer-phone flex-nowrap text-nowrap font-semibold leading-[100%] tracking-[-3%] text-neutral-100 max-[744px]:text-5xl max-[744px]:leading-normal max-[744px]:tracking-[-1.43px] max-[744px]:pl-[3px] max-[744px]:pb-[3px] max-[744px]:font-semibold max-[744px]:border-b-0"
          >8 (914) 441-06-11</a
        >
        <a
          href="tel:+74212247365"
          class="footer-link footer-link--right footer-phone flex-nowrap text-nowrap font-semibold leading-[100%] tracking-[-3%] text-neutral-100 max-[744px]:text-5xl max-[744px]:leading-normal max-[744px]:tracking-[-1.43px] max-[744px]:pl-[3px] max-[744px]:pb-[3px] max-[744px]:ml-0 max-[744px]:font-semibold max-[744px]:border-b-0"
          >24-73-65</a
        >
      </div>
    </div>
    <div
      class="flex flex-wrap justify-between pb-4 text-[20px] text-neutral-100 max-sm:mt-4 max-sm:text-[12px] md:gap-[50px] xl:gap-[100px] max-[744px]:mt-[68px] max-[744px]:flex-row max-[744px]:justify-between max-[744px]:items-start"
    >
      <div class="flex w-full flex-wrap justify-between md:gap-3 max-[744px]:w-auto max-[744px]:flex-col max-[744px]:gap-[13px]">
        <div class="flex w-full items-center justify-between max-sm:gap-4 max-[744px]:w-auto max-[744px]:flex-col max-[744px]:items-start max-[744px]:gap-[13px]">
          <div class="flex-1 max-[744px]:flex-none">
            <router-link to="/" class="footer-link max-[744px]:text-[20px]">Главная</router-link>
          </div>
          <div class="flex-1 max-[744px]:flex-none">
            <router-link to="/apartment-inspection" class="footer-link max-[744px]:text-[20px]"
              >Приемка квартир</router-link
            >
          </div>
          <span class="flex-1 text-end max-[744px]:hidden"
            >г. Хабаровск, ул. Карла Маркса, 62А</span
          >
        </div>
        <div class="flex w-full items-center justify-between max-sm:gap-4 max-[744px]:w-auto max-[744px]:flex-col max-[744px]:items-start max-[744px]:gap-[13px]">
          <div class="flex-1 max-[744px]:flex-none">
            <router-link to="/about" class="footer-link max-[744px]:text-[20px]">О нас</router-link>
          </div>
          <div class="flex-1 max-[744px]:flex-none max-[744px]:mt-[3px]">
            <router-link to="/services" class="footer-link max-[744px]:text-[20px]">Услуги</router-link>
          </div>
          <span class="flex-1 text-end max-[744px]:hidden">пн-вс 08:00—19:00</span>
        </div>
      </div>
      
      <!-- Контакты для 744px справа -->
      <div class="hidden max-[744px]:flex max-[744px]:flex-col max-[744px]:gap-4 max-[744px]:w-[339px] max-[744px]:shrink-0">
        <span class="max-[744px]:text-[20px] max-[744px]:leading-[1.35] max-[744px]:tracking-[-0.59px] max-[744px]:text-right max-[744px]:font-medium">
          г. Хабаровск, ул. Карла Маркса, 62А
        </span>
        <span class="max-[744px]:text-[20px] max-[744px]:leading-[1.35] max-[744px]:tracking-[-0.59px] max-[744px]:text-right max-[744px]:font-medium max-[744px]:opacity-50">
          пн-вс 08:00—19:00
        </span>
      </div>
      
      <div
        class="flex w-full justify-between items-end max-sm:mt-4 max-sm:flex-col max-sm:items-center max-sm:gap-4 max-[744px]:mt-[24px] max-[744px]:flex-row max-[744px]:items-end max-[744px]:gap-4 max-[744px]:pt-1 max-[744px]:text-[16px] max-[744px]:leading-[1.45] max-[744px]:tracking-[-0.48px] max-[744px]:opacity-50"
      >
        <router-link to="/" class="flex-1 max-[744px]:flex max-[744px]:justify-start max-[744px]:self-end">
          <img
            src="../assets/images/logo-var2.svg"
            alt="logo"
            class="size-fit max-[744px]:w-[157px] max-[744px]:h-[28px]"
          />
        </router-link>
        <span class="flex-1 text-center max-[744px]:self-end">ООО "СК Дионис" © 2025</span>
        <router-link to="#" class="flex-1 text-end max-[744px]:self-end max-[744px]:text-right"
          >Политика конфиденциальности</router-link
        >
      </div>
    </div>
  </footer>
</template>

<script setup>
import { computed, inject } from 'vue'
import { useRoute } from 'vue-router'

const openRequestModal = inject('openRequestModal')

const route = useRoute()
const isSpecialPage = computed(() => {
  return route.path === '/' || route.path === '/apartment-inspection'
})
</script>

<style scoped>
.footer-link {
  position: relative;
  display: inline-block;
  text-decoration: none;
  padding-bottom: 2px;
  width: fit-content;
}

.footer-link::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  width: 0;
  height: 2px;
  background-color: currentColor;
  transition: width 0.3s ease;
}

.footer-link:hover::after {
  width: 100%;
}

.footer-link:not(:hover)::after {
  left: auto;
  right: 0;
  width: 0;
  transition: width 0.3s ease;
}

.footer-link--right {
  margin-left: auto;
}

/* Уменьшаем расстояние между баннером и footer для 825px-1023px */
@media screen and (min-width: 825px) and (max-width: 1023px) {
  footer {
    padding-top: 2rem !important;
  }
  
  footer > div:first-child > div:first-child {
    margin-bottom: 2rem !important;
  }
}

/* Плавный переход для номера телефона 745px-824px */
@media screen and (min-width: 745px) and (max-width: 824px) {
  footer > div:first-child {
    flex-direction: column !important;
    align-items: flex-start !important;
    gap: 4rem !important;
  }
  
  footer > div:first-child > div:first-child {
    margin-bottom: 0 !important;
  }
  
  footer > div:first-child > div:first-child button {
    width: 100% !important;
    max-width: 448px !important;
  }
  
  footer > div:first-child > div:last-child {
    align-items: flex-start !important;
  }
  
  footer > div:nth-child(2) {
    margin-top: 68px !important;
  }
  
  .footer-phone::after {
    display: none !important;
  }
  
  .footer-phone:hover::after {
    display: none !important;
  }
  
  .footer-link--right {
    margin-left: 0 !important;
  }
}

/* Убираем подчёркивание для телефонов на 744px */
@media screen and (max-width: 744px) {
  .footer-phone::after {
    display: none !important;
  }
  
  .footer-phone:hover::after {
    display: none !important;
  }
  
  /* Убираем margin-left: auto для второго телефона */
  .footer-link--right {
    margin-left: 0 !important;
  }
}

/* Синхронизация позиции футера с секцией отзывов на главной */
@media screen and (min-width: 641px) and (max-width: 744px) {
  footer.home-footer-stack {
    transform: translateY(800px) !important;
  }
}

@media screen and (max-width: 640px) {
  footer.home-footer-stack {
    transform: translateY(clamp(710px, calc(710px + (100vw - 375px) * 0.34), 800px)) !important;
  }
}
</style>
