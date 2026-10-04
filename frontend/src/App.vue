<script setup>
import { provide, ref } from 'vue'
import Footer from './components/Footer.vue'
import ContactModal from './components/ContactModal.vue'
import Header from '/src/components/Header.vue'

const modalRef = ref(null)
const isModalOpen = ref(false)

const openContactModal = () => {
  modalRef.value?.openModal()
  isModalOpen.value = true
}

const closeContactModal = () => {
  isModalOpen.value = false
}

// Предоставляем функцию открытия модального окна и состояние всем дочерним компонентам
provide('openContactModal', openContactModal)
provide('isModalOpen', isModalOpen)
provide('closeContactModal', closeContactModal)
</script>

<template>
  <div class="bg-neutral-200">
    <Header />
    <div>
      <router-view />
    </div>
    <ContactModal ref="modalRef" />
    <Footer />
  </div>
</template>

<style scoped></style>
