<script setup>
import { inject, onBeforeUnmount, onMounted, ref } from 'vue'
import { messengers } from '@/data/contacts'

const isModalOpen = ref(false)
const closeContactModal = inject('closeContactModal')

const availableMessengers = messengers.filter((messenger) => messenger.getUrl)

const openModal = () => {
  isModalOpen.value = true
}

const closeModal = () => {
  isModalOpen.value = false
  closeContactModal()
}

const openMessenger = (messenger) => {
  window.open(messenger.getUrl(), '_blank', 'noopener,noreferrer')
}

const onKeydown = (event) => {
  if (event.key === 'Escape' && isModalOpen.value) closeModal()
}

onMounted(() => document.addEventListener('keydown', onKeydown))
onBeforeUnmount(() => document.removeEventListener('keydown', onKeydown))

defineExpose({ openModal })
</script>

<template>
  <div
    v-if="isModalOpen"
    class="fixed inset-0 z-50 flex items-center justify-center bg-black/50"
    @click.self="closeModal"
  >
    <div
      class="relative w-full max-w-md rounded-[32px] bg-white p-8 shadow-xl max-sm:mx-4"
      role="dialog"
      aria-modal="true"
      aria-labelledby="contact-modal-title"
    >
      <button
        @click="closeModal"
        class="absolute right-4 top-4 rounded-full p-2 text-gray-400 transition-colors hover:bg-gray-100 hover:text-gray-600"
        aria-label="Закрыть"
      >
        <svg
          width="20"
          height="20"
          viewBox="0 0 24 24"
          fill="none"
          stroke="currentColor"
          stroke-width="2"
          stroke-linecap="round"
          stroke-linejoin="round"
        >
          <path d="m18 6-12 12"></path>
          <path d="m6 6 12 12"></path>
        </svg>
      </button>
      <div class="mb-8 pt-5">
        <h2
          id="contact-modal-title"
          class="text-[48px] leading-[125%] tracking-[-3%] max-sm:text-center max-sm:text-[28px]"
        >
          Связаться с нами
        </h2>
        <p
          class="align-middle text-[20px] font-normal leading-[150%] tracking-[-3%] text-neutral-600 max-sm:text-center max-sm:text-sm"
        >
          Напишите нам в удобный мессенджер — ответим в ближайшее время
        </p>
      </div>

      <div class="flex flex-col gap-3">
        <button
          v-for="messenger in availableMessengers"
          :key="messenger.id"
          @click="openMessenger(messenger)"
          class="flex w-full items-center gap-4 rounded-2xl border border-neutral-300 bg-neutral-100 px-5 py-4 text-left text-[20px] font-medium leading-none tracking-[-3%] text-text-dark-primary transition-colors duration-300 ease-out hover:bg-neutral-200 max-sm:text-[16px]"
        >
          <!-- Иконки: simple-icons (WhatsApp, Telegram), MAX — логотип с Wikimedia Commons -->
          <svg
            v-if="messenger.id === 'whatsapp'"
            class="size-10 shrink-0"
            viewBox="0 0 24 24"
            fill="#25D366"
            aria-hidden="true"
          >
            <path
              d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413Z"
            />
          </svg>
          <svg
            v-else-if="messenger.id === 'telegram'"
            class="size-10 shrink-0"
            viewBox="0 0 24 24"
            fill="#26A5E4"
            aria-hidden="true"
          >
            <path
              d="M11.944 0A12 12 0 0 0 0 12a12 12 0 0 0 12 12 12 12 0 0 0 12-12A12 12 0 0 0 12 0a12 12 0 0 0-.056 0zm4.962 7.224c.1-.002.321.023.465.14a.506.506 0 0 1 .171.325c.016.093.036.306.02.472-.18 1.898-.962 6.502-1.36 8.627-.168.9-.499 1.201-.82 1.23-.696.065-1.225-.46-1.9-.902-1.056-.693-1.653-1.124-2.678-1.8-1.185-.78-.417-1.21.258-1.91.177-.184 3.247-2.977 3.307-3.23.007-.032.014-.15-.056-.212s-.174-.041-.249-.024c-.106.024-1.793 1.14-5.061 3.345-.48.33-.913.49-1.302.48-.428-.008-1.252-.241-1.865-.44-.752-.245-1.349-.374-1.297-.789.027-.216.325-.437.893-.663 3.498-1.524 5.83-2.529 6.998-3.014 3.332-1.386 4.025-1.627 4.476-1.635z"
            />
          </svg>
          <svg
            v-else-if="messenger.id === 'max'"
            class="size-10 shrink-0"
            viewBox="0 0 24 24"
            aria-hidden="true"
          >
            <defs>
              <linearGradient
                id="max-icon-gradient"
                x1="0"
                y1="1"
                x2="1"
                y2="0"
              >
                <stop offset="0" stop-color="#44C8FF" />
                <stop offset="0.5" stop-color="#3B3FF0" />
                <stop offset="1" stop-color="#9B4FE0" />
              </linearGradient>
            </defs>
            <rect
              width="24"
              height="24"
              rx="6"
              fill="url(#max-icon-gradient)"
            />
            <path
              transform="translate(4.4 4.4) scale(0.37)"
              fill="#fff"
              fill-rule="evenodd"
              d="M21.47 41.88c-4.11 0-6.02-.6-9.34-3-2.1 2.7-8.75 4.81-9.04 1.2 0-2.71-.6-5-1.28-7.5C1 29.5.08 26.07.08 21.1.08 9.23 9.82.3 21.36.3c11.55 0 20.6 9.37 20.6 20.91a20.6 20.6 0 0 1-20.49 20.67m.17-31.32c-5.62-.29-10 3.6-10.97 9.7-.8 5.05.62 11.2 1.83 11.52.58.14 2.04-1.04 2.95-1.95a10.4 10.4 0 0 0 5.08 1.81 10.7 10.7 0 0 0 11.19-9.97 10.7 10.7 0 0 0-10.08-11.1Z"
            />
          </svg>
          <span>{{ messenger.title }}</span>
        </button>
      </div>
    </div>
  </div>
</template>
