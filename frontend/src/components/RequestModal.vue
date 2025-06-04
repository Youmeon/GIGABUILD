<script setup>
import { reactive, ref } from 'vue'
import axios from 'axios'

const isModalOpen = ref(false)
const isSubmitting = ref(false)

const form = reactive({
  name: '',
  phone: '',
  email: '',
})

const errors = reactive({
  name: '',
  phone: '',
  email: '',
})

const openModal = () => {
  isModalOpen.value = true
}

const closeModal = () => {
  isModalOpen.value = false
  resetForm()
}

const resetForm = () => {
  form.name = ''
  form.phone = ''
  form.email = ''
  errors.name = ''
  errors.phone = ''
  errors.email = ''
}

const validateForm = () => {
  let isValid = true
  errors.name = ''
  errors.phone = ''
  errors.email = ''

  if (!form.name.trim()) {
    errors.name = 'Имя обязательно для заполнения'
    isValid = false
  }

  if (!form.phone.trim()) {
    errors.phone = 'Телефон обязателен для заполнения'
    isValid = false
  }

  if (form.email && !/\S+@\S+\.\S+/.test(form.email)) {
    errors.email = 'Введите корректный email'
    isValid = false
  }

  return isValid
}

const submitForm = async () => {
  if (!validateForm()) return

  isSubmitting.value = true

  try {
    const formData = new URLSearchParams()
    formData.append('name', form.name)
    formData.append('phone', form.phone)
    if (form.email) formData.append('email', form.email)

    const response = await axios.post('/api/send-form', formData, {
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded'
      }
    })

    if (response.data.success) {
      alert('Заявка успешно отправлена!')
      closeModal()
    } else {
      alert('Произошла ошибка при отправке заявки.')
    }
  } catch (error) {
    console.error('Ошибка отправки формы:', error)
    alert('Произошла ошибка при отправке заявки.')
  } finally {
    isSubmitting.value = false
  }
}

defineExpose({ openModal })
</script>

<template>
  <div
    v-if="isModalOpen"
    class="fixed inset-0 z-50 flex items-center justify-center bg-black/50"
    @click.self="closeModal"
  >
    <div class="relative w-full max-w-md rounded-[32px] bg-white p-8 shadow-xl max-sm:mx-4">
      <button
        @click="closeModal"
        class="absolute right-4 top-4 rounded-full p-2 text-gray-400 transition-colors hover:bg-gray-100 hover:text-gray-600"
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
        <h2 class="text-[48px] leading-[125%] tracking-[-3%] max-sm:text-center max-sm:text-[28px]">
          Оставьте заявку
        </h2>
        <p class="mb-6 align-middle text-[20px] font-normal leading-[150%] tracking-[-3%] text-neutral-600 max-sm:text-sm">
          и мы свяжемся с вами в ближайшее время
        </p>
      </div>
      <form @submit.prevent="submitForm" class="flex flex-col gap-3">
        <div>
          <label for="name" class="block text-sm font-medium text-text-dark-primary"></label>
          <input
            id="name"
            v-model="form.name"
            type="text"
            required
            class="w-full rounded-[14px] border border-neutral-500 bg-neutral-100 px-4 py-[20.5px] text-sm focus:border-blue-500 focus:outline-none focus:ring-1 focus:ring-blue-500"
            :class="{ 'border-red-500': errors.name }"
            placeholder="Ваше имя*"
          />
          <p v-if="errors.name" class="mt-1 text-xs text-red-500">{{ errors.name }}</p>
        </div>
        <div>
          <label for="phone" class="mb-1 block text-sm font-medium text-gray-700"></label>
          <input
            id="phone"
            v-model="form.phone"
            type="tel"
            required
            class="w-full rounded-[14px] border border-neutral-500 bg-neutral-100 px-4 py-[20.5px] text-sm focus:border-blue-500 focus:outline-none focus:ring-1 focus:ring-blue-500"
            :class="{ 'border-red-500': errors.phone }"
            placeholder="Ваш телефон*"
          />
          <p v-if="errors.phone" class="mt-1 text-xs text-red-500">{{ errors.phone }}</p>
        </div>
        <div class="mb-2">
          <label for="email" class="mb-1 block text-sm font-medium text-gray-700"></label>
          <input
            id="email"
            v-model="form.email"
            type="email"
            class="w-full rounded-[14px] border border-neutral-500 bg-neutral-100 px-4 py-[20.5px] text-sm focus:border-blue-500 focus:outline-none focus:ring-1 focus:ring-blue-500"
            :class="{ 'border-red-500': errors.email }"
            placeholder="Ваш e-mail"
          />
          <p v-if="errors.email" class="mt-1 text-xs text-red-500">{{ errors.email }}</p>
        </div>
        <button
          type="submit"
          :disabled="isSubmitting"
          class="max-w-[384px] rounded-2xl bg-blue-600 px-8 py-5 text-center align-middle text-[20px] font-medium leading-none tracking-[-3%] text-neutral-100 max-lg:px-4 max-lg:py-3 max-sm:text-[16px]"
        >
          <span v-if="!isSubmitting">Оставить заявку</span>
          <span v-else>Отправка...</span>
        </button>
        <p class="text-center text-xs text-gray-500">
          Нажимая кнопку «Отправить», вы соглашаетесь с
          <a href="#" class="text-blue-600 hover:underline">политикой конфиденциальности</a>
        </p>
      </form>
    </div>
  </div>
</template>