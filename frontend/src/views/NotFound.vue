<template>
  <main class="bg-neutral-200 text-text-dark-primary">
    <section
      class="mt-[176px] px-8 pb-[160px] max-md:mt-16 max-md:px-4 max-md:pb-20"
    >
      <h1
        class="mb-6 align-middle text-[80px] font-medium leading-[115%] tracking-[-4%] max-lg:text-[5rem] max-md:text-[2.5rem] max-sm:text-[2rem]"
      >
        Страница не найдена
      </h1>
      <p
        class="mb-10 text-[20px] leading-[150%] tracking-[-3%] text-neutral-600 max-sm:text-base"
      >
        Возможно, ссылка устарела или в адресе опечатка.
      </p>
      <ButtonDetails to="/" label="На главную" variant="primary" />
    </section>
  </main>
</template>

<script setup>
import ButtonDetails from '@/components/ButtonDetails.vue'
</script>
