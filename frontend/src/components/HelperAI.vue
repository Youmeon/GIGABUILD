<script setup>
import { ref, nextTick } from 'vue'
import axios from 'axios'
import { ArrowUp } from 'lucide-vue-next'

const isChatOpen = ref(false)
const newMessage = ref('')
const messages = ref([{ type: 'bot', text: 'Здравствуйте! 💬 Можете узнать стоимость приемки, список документов или уточнить, как мы работаем — просто напишите вопрос.' }])
const chatMessages = ref(null)

const toggleChat = () => {
  isChatOpen.value = !isChatOpen.value
}

const sendMessage = async () => {
  if (!newMessage.value.trim()) return
  const userMessage = newMessage.value
  messages.value.push({ type: 'user', text: userMessage })
  newMessage.value = ''
  await nextTick()
  chatMessages.value.scrollTop = chatMessages.value.scrollHeight

  try {
    const response = await axios.post('/chat', { message: userMessage }, {
      headers: { 'Content-Type': 'application/json' }
    })
    const botAnswer = response.data.answer
    messages.value.push({ type: 'bot', text: botAnswer })
    await nextTick()
    chatMessages.value.scrollTop = chatMessages.value.scrollHeight
  } catch (error) {
    console.error('Ошибка отправки сообщения:', error)
    messages.value.push({ type: 'bot', text: 'Произошла ошибка при отправке сообщения.' })
    await nextTick()
    chatMessages.value.scrollTop = chatMessages.value.scrollHeight
  }
}
</script>

<template>
  <div>
    <!-- Кнопка для открытия чата -->
    <div class="absolute bottom-[148px] right-[128px] z-[999]">
      <button
        v-if="!isChatOpen"
        @click="toggleChat"
        id="chat-toggle"
        class="fixed rounded-2xl"
      >
        <!-- SVG-кнопка, код из исходного компонента -->
        <svg width="130" height="132" viewBox="0 0 130 132" fill="none" xmlns="http://www.w3.org/2000/svg">
          <!-- ... (оставляем SVG без изменений) -->
        </svg>
      </button>
    </div>

    <!-- Модальное окно чата -->
    <div
      v-if="isChatOpen"
      @click="toggleChat"
      class="fixed inset-0 z-[1000] flex items-end justify-end bg-black/50 bg-none"
    >
      <div
        @click.stop
        class="fixed bottom-8 right-8 flex h-[512px] max-w-[1050px] flex-col shadow-xl max-sm:bottom-2 max-sm:right-0"
      >
        <!-- Заголовок -->
        <div class="mb-2 flex items-center justify-between rounded-b-[8px] rounded-t-[24px] bg-white p-4">
          <div class="flex items-center gap-[10px]">
            <svg width="32" height="32" viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg">
              <!-- ... (оставляем SVG без изменений) -->
            </svg>
            <span class="text-lg font-medium text-gray-800">Чат с AI-помощником</span>
          </div>
          <button
            @click="toggleChat"
            id="chat-close"
            class="text-gray-500 hover:text-gray-700"
          >
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="size-6">
              <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
        </div>
        <!-- Область сообщений -->
        <div
          id="chat-messages"
          ref="chatMessages"
          class="flex flex-1 flex-col overflow-y-auto rounded-t-[8px] bg-white p-6"
        >
          <div v-for="(msg, index) in messages" :key="index" :class="['message', msg.type]" class="mb-4 w-full rounded-lg shadow-sm">
            <p class="text-[16px] font-normal leading-[150%] tracking-[-3%] text-text-dark-primary">
              {{ msg.text }}
            </p>
          </div>
        </div>
        <!-- Поле ввода -->
        <div class="relative flex rounded-b-[24px] border-blue-500/20 bg-white px-3 pb-3">
          <textarea
            id="chat-input"
            v-model="newMessage"
            @keyup.enter="sendMessage"
            rows="2"
            placeholder="Напишите свой вопрос"
            class="h-[96px] flex-1 resize-none rounded-[24px] border bg-white p-3 shadow-xl focus:border-blue-300 focus:outline-none focus:ring"
          ></textarea>
          <button
            @click="sendMessage"
            id="chat-send"
            class="absolute bottom-5 right-5 flex items-center rounded-[8px] bg-gray-300 p-[6px] text-gray-600 hover:bg-gray-400"
          >
            <ArrowUp class="text-white" />
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.message.user {
  background-color: #e6f3ff;
  margin-left: 20%;
  padding: 10px;
  border-radius: 10px;
}
.message.bot {
  background-color: #f0f0f0;
  margin-right: 20%;
  padding: 10px;
  border-radius: 10px;
}
</style>