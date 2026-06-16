<script setup>
import { provide, ref } from 'vue'
import Footer from './components/Footer.vue'
import RequestModal from './components/RequestModal.vue'
import Header from '/src/components/Header.vue'

const modalRef = ref(null)
const isModalOpen = ref(false)

const openRequestModal = () => {
  modalRef.value?.openModal()
  isModalOpen.value = true
}

const closeRequestModal = () => {
  isModalOpen.value = false
}

// Предоставляем функцию открытия модального окна и состояние всем дочерним компонентам
provide('openRequestModal', openRequestModal)
provide('isModalOpen', isModalOpen)
provide('closeRequestModal', closeRequestModal)
</script>

<template>
  <div class="bg-neutral-200">
    <Header />
    <div>
      <router-view />
    </div>
    <RequestModal ref="modalRef" />
    <HelperAI />
    <Footer />
  </div>
</template>

<style scoped></style>
