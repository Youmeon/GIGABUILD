<template>
  <router-link
    :to="`/services/${card.id}`"
    class="group flex h-auto w-full flex-col justify-between overflow-hidden rounded-[32px] bg-white p-[12px] pt-[32px] transition-all duration-300 min-[1329px]:h-[506px] min-[1329px]:w-[448px] max-[744px]:gap-8"
  >
    <div class="px-5 max-[744px]:px-3">
      <div class="flex items-start justify-between">
        <div class="flex-1">
          <h4
            class="mb-4 text-[32px] font-medium leading-[125%] tracking-[-4%] text-[#262628] max-[744px]:text-[24px] max-[744px]:mb-3"
          >
            {{ card.title }}
          </h4>
          <p
            class="text-[20px] font-medium leading-[135%] tracking-[-3%] text-[#3b3b3c] max-[744px]:text-[16px]"
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
    <div class="mt-6 overflow-hidden rounded-[24px] max-[744px]:mt-0">
      <img
        :src="getImageUrl(card.image)"
        :alt="card.title"
        class="h-[245px] w-full object-cover transition-transform duration-300 group-hover:scale-105 max-[744px]:h-[180px]"
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
