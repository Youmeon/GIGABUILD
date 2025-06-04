<template>
  <footer
    :class="{
      'translate-y-[830px] max-sm:translate-y-[650px]': isSpecialPage,
      'relative z-30 mt-[-30px] max-h-full w-full rounded-2xl rounded-b-none bg-blue-600 px-8 pb-[28px] pt-16 max-sm:py-2': true,
    }"
  >
    <div
      class="flex items-baseline justify-between max-lg:flex-col max-lg:items-center max-lg:text-center"
    >
      <div
        class="flex max-w-[516px] flex-col gap-10 max-lg:mb-4 max-lg:items-center max-lg:justify-center max-lg:gap-2 lg:mb-[50px] xl:mb-[215px]"
      >
        <h2
          class="text-5xl font-semibold leading-[125%] tracking-[-3%] text-neutral-100 max-sm:text-2xl"
        >
          Оставьте заявку<br />
          и мы свяжемся с вами в ближайшее время
        </h2>
        <router-link
          to="#"
          class="max-w-[384px] rounded-2xl bg-neutral-800 px-8 py-5 text-center align-middle text-[20px] font-medium leading-none tracking-[-3%] text-neutral-100 max-lg:px-4 max-lg:py-3 max-sm:text-[16px]"
        >
          Оставить заявку
        </router-link>
      </div>
      <div
        class="flex flex-col flex-nowrap gap-[10px] text-[48px] max-lg:items-center max-sm:text-2xl"
      >
        <a
          href="tel:+79144110611"
          class="flex-nowrap text-nowrap font-semibold leading-[100%] tracking-[-3%] text-neutral-100"
          >8 (914) 441-06-11</a
        >
        <a
          href="tel:+74212247365"
          class="flex-nowrap text-nowrap text-end font-semibold leading-[100%] tracking-[-3%] text-neutral-100"
          >24-73-65</a
        >
      </div>
    </div>
    <div
      class="flex flex-wrap justify-between pb-4 text-[20px] text-neutral-100 max-sm:mt-4 max-sm:text-[12px] md:gap-[50px] xl:gap-[100px]"
    >
      <div class="flex w-full flex-wrap justify-between md:gap-3">
        <div class="flex w-full items-center justify-between max-sm:gap-4">
          <router-link to="/" class="flex-1">Главная</router-link>
          <router-link to="/about" class="lg:flex-1">О нас</router-link>
          <span class="flex-1 text-end"
            >г. Хабаровск, ул. Карла Маркса, 62А</span
          >
        </div>
        <div class="flex w-full items-center justify-between max-sm:gap-4">
          <router-link to="/apartment-inspection" class="flex-1"
            >Приемка квартир</router-link
          >
          <router-link to="/service" class="lg:flex-1">Услуги</router-link>
          <span class="flex-1 text-end">пн-вс 08:00—19:00</span>
        </div>
      </div>
      <div
        class="flex w-full justify-between max-sm:mt-4 max-sm:flex-col max-sm:items-center max-sm:gap-4"
      >
        <router-link to="/" class="flex-1">
          <img
            src="../assets/images/logo-var2.svg"
            alt="logo"
            class="size-fit"
          />
        </router-link>
        <span class="flex-1">ООО “СК Дионис” © 2025</span>
        <router-link to="#" class="flex-1 text-end"
          >Политика конфиденциальности</router-link
        >
      </div>
    </div>
  </footer>
</template>

<script setup>
import { computed } from 'vue'
import { useRoute } from 'vue-router'

const route = useRoute()
const isSpecialPage = computed(() => {
  return route.path === '/' || route.path === '/apartment-inspection'
})
</script>
