<template>
  <router-link
    :to="`/services/${card.id}`"
    class="group flex h-[506px] w-[448px] shrink-0 flex-col gap-8 overflow-hidden rounded-[32px] bg-white p-[12px] pt-[32px] transition-all duration-300"
  >
    <div class="ml-5 mr-[72px]">
      <div class="flex items-start justify-between gap-6">
        <div class="flex flex-1 flex-col gap-6">
          <h4
            class="text-[32px] font-medium leading-[125%] tracking-[-1.27px] text-[#262628]"
          >
            {{ card.title }}
          </h4>
          <p
            class="text-[20px] font-medium leading-[135%] tracking-[-0.59px] text-[#3b3b3c]"
          >
            {{ card.description }}
          </p>
        </div>
        <div
          class="flex h-9 w-9 shrink-0 items-center justify-center rounded-full bg-neutral-800 text-white opacity-0 transition-opacity duration-300 group-hover:opacity-100"
        >
          <svg
            width="24"
            height="24"
            viewBox="0 0 24 24"
            fill="none"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              d="M3.80005 20.2L19 5"
              stroke="currentColor"
              stroke-width="2.5"
            />
            <path d="M19 21V5H3" stroke="currentColor" stroke-width="2.5" />
          </svg>
        </div>
      </div>
    </div>
    <div class="overflow-hidden rounded-[24px]">
      <img
        :src="getImageUrl(card.image)"
        :alt="card.title"
        class="h-[245px] w-full object-cover transition-transform duration-300 group-hover:scale-105"
      />
    </div>
  </router-link>
</template>

<script setup>
import getImageUrl from '../utils/getImageURL'

defineProps({
  card: {
    type: Object,
    required: true,
  },
})
</script>
