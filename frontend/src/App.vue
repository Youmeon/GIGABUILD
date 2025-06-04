<script setup>
import { provide, ref } from 'vue'
import Footer from './components/Footer.vue'
import HelperAI from './components/HelperAI.vue'
import RequestModal from './components/RequestModal.vue'
import Header from '/src/components/Header.vue'

const modalRef = ref(null)

const openRequestModal = () => {
  modalRef.value?.openModal()
}

// Предоставляем функцию открытия модального окна всем дочерним компонентам
provide('openRequestModal', openRequestModal)
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
