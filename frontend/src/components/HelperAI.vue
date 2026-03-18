<script setup>
import { ref, nextTick } from 'vue'
import axios from 'axios'
import { ArrowUp } from 'lucide-vue-next'

const isChatOpen = ref(false)
const newMessage = ref('')
const messages = ref([{ type: 'bot', text: 'Здравствуйте! 💬 Можете узнать стоимость приемки, список документов или уточнить, как мы работаем — просто напишите вопрос.' }])
const chatMessages = ref(null)
const isLoading = ref(false) // Новое состояние для загрузки

const toggleChat = () => {
  isChatOpen.value = !isChatOpen.value
}

const sendMessage = async () => {
  if (!newMessage.value.trim()) return
  const userMessage = newMessage.value
  messages.value.push({ type: 'user', text: userMessage })
  newMessage.value = ''
  isLoading.value = true // Включаем индикатор загрузки
  await nextTick()
  chatMessages.value.scrollTop = chatMessages.value.scrollHeight

  try {
    const response = await axios.post('/chat', { message: userMessage }, {
      headers: { 'Content-Type': 'application/json' }
    })
    const botAnswer = response.data.answer
    messages.value.push({ type: 'bot', text: botAnswer })
  } catch (error) {
    console.error('Ошибка отправки сообщения:', error)
    messages.value.push({ type: 'bot', text: 'Произошла ошибка при отправке сообщения.' })
  } finally {
    isLoading.value = false // Выключаем индикатор загрузки
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
      <svg width="130" height="132" viewBox="0 0 130 132" fill="none" xmlns="http://www.w3.org/2000/svg">
<g filter="url(#filter0_dd_639_1678)">
<rect x="34" y="34" width="64" height="64" rx="18" fill="#4F7BFF"/>
<rect x="34" y="34" width="64" height="64" rx="18" fill="white" fill-opacity="0.15"/>
<path fill-rule="evenodd" clip-rule="evenodd" d="M76.3333 75.334V70.6673C76.3333 70.0485 76.0875 69.455 75.6499 69.0174C75.2123 68.5798 74.6188 68.334 74 68.334H72.6667C72.4015 68.334 72.1471 68.4393 71.9596 68.6269C71.772 68.8144 71.6667 69.0688 71.6667 69.334V76.6673C71.6667 77.2193 72.1147 77.6673 72.6667 77.6673H74C74.6188 77.6673 75.2123 77.4215 75.6499 76.9839C76.0875 76.5463 76.3333 75.9528 76.3333 75.334ZM55.3333 77.6673L56.7187 77.666C56.9745 77.6527 57.2155 77.5416 57.3919 77.3558C57.5683 77.17 57.6667 76.9235 57.6667 76.6673V69.334C57.6667 69.0688 57.5613 68.8144 57.3738 68.6269C57.1862 68.4393 56.9319 68.334 56.6667 68.334H55.3333C54.7145 68.334 54.121 68.5798 53.6834 69.0174C53.2458 69.455 53 70.0485 53 70.6673V75.334C53 76.6233 54.0453 77.6673 55.3333 77.6673Z" fill="white"/>
<path fill-rule="evenodd" clip-rule="evenodd" d="M55 71.3333V62C55 61.7348 54.8946 61.4804 54.7071 61.2929C54.5196 61.1054 54.2652 61 54 61C53.7348 61 53.4804 61.1054 53.2929 61.2929C53.1054 61.4804 53 61.7348 53 62V71.3333C53 71.5985 53.1054 71.8529 53.2929 72.0404C53.4804 72.228 53.7348 72.3333 54 72.3333C54.2652 72.3333 54.5196 72.228 54.7071 72.0404C54.8946 71.8529 55 71.5985 55 71.3333Z" fill="white"/>
<path d="M54.0001 63.0007C55.2887 63.0007 56.3334 61.956 56.3334 60.6673C56.3334 59.3787 55.2887 58.334 54.0001 58.334C52.7114 58.334 51.6667 59.3787 51.6667 60.6673C51.6667 61.956 52.7114 63.0007 54.0001 63.0007Z" fill="white"/>
<path fill-rule="evenodd" clip-rule="evenodd" d="M80.3334 54.0003C80.3334 53.3817 80.0881 52.7883 79.6494 52.351C79.433 52.1341 79.176 51.962 78.8929 51.8446C78.6099 51.7272 78.3065 51.6669 78.0001 51.667H68.6667C68.0481 51.667 67.4547 51.9123 67.0174 52.351C66.8005 52.5674 66.6284 52.8244 66.511 53.1075C66.3936 53.3905 66.3333 53.6939 66.3334 54.0003V58.8897C66.3334 60.1777 67.3787 61.223 68.6667 61.223H69.5854L71.5147 63.1523C71.6076 63.2453 71.7179 63.319 71.8393 63.3693C71.9606 63.4196 72.0907 63.4454 72.2221 63.4454C72.3535 63.4454 72.4835 63.4196 72.6049 63.3693C72.7263 63.319 72.8365 63.2453 72.9294 63.1523L74.8587 61.223H78.0001C78.6189 61.223 79.2124 60.9772 79.65 60.5396C80.0876 60.102 80.3334 59.5085 80.3334 58.8897V54.0003ZM73.6667 78.0003V67.3337C73.6667 66.7148 73.4209 66.1213 72.9833 65.6837C72.5457 65.2462 71.9523 65.0003 71.3334 65.0003H58.0001C57.3812 65.0003 56.7878 65.2462 56.3502 65.6837C55.9126 66.1213 55.6667 66.7148 55.6667 67.3337V78.0003C55.6667 79.2897 56.7121 80.3337 58.0001 80.3337H71.3334C71.9523 80.3337 72.5457 80.0878 72.9833 79.6502C73.4209 79.2127 73.6667 78.6192 73.6667 78.0003ZM60.6281 74.6603C61.1581 75.1913 61.7877 75.6125 62.4807 75.8999C63.1737 76.1873 63.9165 76.3352 64.6667 76.3352C65.417 76.3352 66.1598 76.1873 66.8528 75.8999C67.5458 75.6125 68.1754 75.1913 68.7054 74.6603C68.7982 74.5675 68.8718 74.4574 68.9221 74.3361C68.9723 74.2149 68.9981 74.0849 68.9981 73.9537C68.9981 73.8224 68.9723 73.6925 68.9221 73.5712C68.8718 73.45 68.7982 73.3398 68.7054 73.247C68.6126 73.1542 68.5024 73.0806 68.3812 73.0304C68.2599 72.9801 68.13 72.9543 67.9987 72.9543C67.8675 72.9543 67.7376 72.9801 67.6163 73.0304C67.4951 73.0806 67.3849 73.1542 67.2921 73.247C66.5954 73.9425 65.6512 74.3331 64.6667 74.3331C63.6823 74.3331 62.7381 73.9425 62.0414 73.247C61.9486 73.1542 61.8384 73.0806 61.7172 73.0304C61.5959 72.9801 61.466 72.9543 61.3347 72.9543C61.2035 72.9543 61.0736 72.9801 60.9523 73.0304C60.8311 73.0806 60.7209 73.1542 60.6281 73.247C60.5353 73.3398 60.4617 73.45 60.4114 73.5712C60.3612 73.6925 60.3354 73.8224 60.3354 73.9537C60.3354 74.0849 60.3612 74.2149 60.4114 74.3361C60.4617 74.4574 60.5353 74.5675 60.6281 74.6603ZM61.3334 68.667C61.687 68.667 62.0262 68.8075 62.2762 69.0575C62.5263 69.3076 62.6667 69.6467 62.6667 70.0003C62.6667 70.354 62.5263 70.6931 62.2762 70.9431C62.0262 71.1932 61.687 71.3337 61.3334 71.3337C60.9798 71.3337 60.6407 71.1932 60.3906 70.9431C60.1406 70.6931 60.0001 70.354 60.0001 70.0003C60.0001 69.6467 60.1406 69.3076 60.3906 69.0575C60.6407 68.8075 60.9798 68.667 61.3334 68.667ZM68.0001 68.667C68.3537 68.667 68.6928 68.8075 68.9429 69.0575C69.1929 69.3076 69.3334 69.6467 69.3334 70.0003C69.3334 70.354 69.1929 70.6931 68.9429 70.9431C68.6928 71.1932 68.3537 71.3337 68.0001 71.3337C67.6465 71.3337 67.3073 71.1932 67.0573 70.9431C66.8072 70.6931 66.6667 70.354 66.6667 70.0003C66.6667 69.6467 66.8072 69.3076 67.0573 69.0575C67.3073 68.8075 67.6465 68.667 68.0001 68.667Z" fill="white"/>
</g>
<defs>
<filter id="filter0_dd_639_1678" x="0" y="0" width="132" height="132" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB">
<feFlood flood-opacity="0" result="BackgroundImageFix"/>
<feColorMatrix in="SourceAlpha" type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 0" result="hardAlpha"/>
<feOffset/>
<feGaussianBlur stdDeviation="17"/>
<feComposite in2="hardAlpha" operator="out"/>
<feColorMatrix type="matrix" values="0 0 0 0 0.384615 0 0 0 0 0.484215 0 0 0 0 1 0 0 0 0.5 0"/>
<feBlend mode="normal" in2="BackgroundImageFix" result="effect1_dropShadow_639_1678"/>
<feColorMatrix in="SourceAlpha" type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 0" result="hardAlpha"/>
<feOffset/>
<feGaussianBlur stdDeviation="6.5"/>
<feComposite in2="hardAlpha" operator="out"/>
<feColorMatrix type="matrix" values="0 0 0 0 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0.1 0"/>
<feBlend mode="normal" in2="effect1_dropShadow_639_1678" result="effect2_dropShadow_639_1678"/>
<feBlend mode="normal" in="SourceGraphic" in2="effect2_dropShadow_639_1678" result="shape"/>
</filter>
</defs>
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
<path fill-rule="evenodd" clip-rule="evenodd" d="M15.3333 7.99992C15.1932 8 15.0567 7.95599 14.9431 7.87412C14.8295 7.79225 14.7444 7.67669 14.7001 7.54381L14.3497 6.49202C14.2164 6.0946 13.9051 5.78164 13.5067 5.64916L12.4547 5.29797C12.3222 5.25351 12.2071 5.16857 12.1255 5.05515C12.0439 4.94172 12 4.80553 12 4.66583C12 4.52612 12.0439 4.38995 12.1255 4.27652C12.2071 4.16309 12.3222 4.07815 12.4547 4.03368L13.5067 3.68249C13.9043 3.54913 14.2173 3.23795 14.3497 2.83964L14.7011 1.78784C14.7455 1.6554 14.8305 1.54027 14.9439 1.45871C15.0573 1.37713 15.1936 1.33325 15.3333 1.33325C15.4731 1.33325 15.6093 1.37713 15.7228 1.45871C15.8361 1.54027 15.9212 1.6554 15.9656 1.78784L16.3169 2.83964C16.3824 3.03588 16.4927 3.21419 16.6389 3.36047C16.7853 3.50676 16.9636 3.617 17.16 3.68249L18.212 4.03368C18.3444 4.07815 18.4596 4.16309 18.5412 4.27652C18.6228 4.38995 18.6667 4.52612 18.6667 4.66583C18.6667 4.80553 18.6228 4.94172 18.5412 5.05515C18.4596 5.16857 18.3444 5.25351 18.212 5.29797L17.16 5.64916C16.7624 5.78253 16.4493 6.09371 16.3169 6.49202L15.9656 7.54381C15.9215 7.67654 15.8365 7.792 15.7231 7.87385C15.6096 7.9557 15.4732 7.99981 15.3333 7.99992Z" fill="#4F6CFF"/>
<path fill-rule="evenodd" clip-rule="evenodd" d="M8.00033 17.3334C7.8021 17.3335 7.60953 17.2673 7.45325 17.1454C7.29695 17.0234 7.18594 16.8527 7.13783 16.6603L6.83217 15.4327C6.55257 14.3189 5.68297 13.4491 4.56931 13.1695L3.34191 12.8637C3.14925 12.816 2.9781 12.7051 2.85578 12.5488C2.73346 12.3924 2.66699 12.1996 2.66699 12.0011C2.66699 11.8025 2.73346 11.6097 2.85578 11.4534C2.9781 11.297 3.14925 11.1861 3.34191 11.1384L4.56931 10.8327C5.68297 10.5531 6.55257 9.68328 6.83217 8.56941L7.13783 7.3418C7.18555 7.14909 7.29642 6.97792 7.45274 6.85557C7.60906 6.73323 7.80183 6.66675 8.00033 6.66675C8.19882 6.66675 8.39159 6.73323 8.54791 6.85557C8.70423 6.97792 8.8151 7.14909 8.86282 7.3418L9.16849 8.56941C9.30519 9.11636 9.58794 9.61587 9.98653 10.0145C10.3851 10.4132 10.8845 10.696 11.4313 10.8327L12.6587 11.1384C12.8514 11.1861 13.0226 11.297 13.1449 11.4534C13.2672 11.6097 13.3337 11.8025 13.3337 12.0011C13.3337 12.1996 13.2672 12.3924 13.1449 12.5488C13.0226 12.7051 12.8514 12.816 12.6587 12.8637L11.4313 13.1695C10.8845 13.3062 10.3851 13.589 9.98653 13.9877C9.58794 14.3863 9.30519 14.8858 9.16849 15.4327L8.86282 16.6603C8.81471 16.8527 8.7037 17.0234 8.54741 17.1454C8.39113 17.2673 8.19855 17.3335 8.00033 17.3334Z" fill="#4F6CFF"/>
<path fill-rule="evenodd" clip-rule="evenodd" d="M18.0002 30.6668C17.783 30.6668 17.5717 30.596 17.3982 30.465C17.2247 30.3341 17.0986 30.1504 17.0389 29.9414L15.9549 26.1468C15.7215 25.3296 15.2837 24.5853 14.6827 23.9844C14.0817 23.3833 13.3375 22.9454 12.5203 22.7121L8.72559 21.6281C8.5168 21.5682 8.33315 21.4421 8.20242 21.2686C8.07168 21.0953 8.00098 20.884 8.00098 20.6668C8.00098 20.4496 8.07168 20.2382 8.20242 20.0649C8.33315 19.8914 8.5168 19.7653 8.72559 19.7054L12.5203 18.6214C13.3375 18.3881 14.0817 17.9502 14.6827 17.3492C15.2837 16.7482 15.7215 16.004 15.9549 15.1868L17.0389 11.3921C17.0987 11.1833 17.2249 10.9997 17.3983 10.8689C17.5718 10.7382 17.783 10.6675 18.0002 10.6675C18.2174 10.6675 18.4287 10.7382 18.6022 10.8689C18.7757 10.9997 18.9018 11.1833 18.9615 11.3921L20.0455 15.1868C20.279 16.004 20.7169 16.7482 21.3178 17.3492C21.9187 17.9502 22.663 18.3881 23.4802 18.6214L27.2749 19.7054C27.4837 19.7653 27.6674 19.8914 27.7981 20.0649C27.9289 20.2382 27.9995 20.4496 27.9995 20.6668C27.9995 20.884 27.9289 21.0953 27.7981 21.2686C27.6674 21.4421 27.4837 21.5682 27.2749 21.6281L23.4802 22.7121C22.663 22.9454 21.9187 23.3833 21.3178 23.9844C20.7169 24.5853 20.279 25.3296 20.0455 26.1468L18.9615 29.9414C18.9019 30.1504 18.7758 30.3341 18.6023 30.465C18.4289 30.596 18.2175 30.6668 18.0002 30.6668Z" fill="#4F6CFF"/>
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
          <div v-for="(msg, index) in messages" :key="index" :class="['message', msg.type]" class="mb-4 w-full ml-0 rounded-lg shadow-sm">
            <p class="text-[16px] font-normal leading-[150%] tracking-[-3%] text-text-dark-primary">
              {{ msg.text }}
            </p>
          </div>
          <!-- Индикатор загрузки -->
          <div v-if="isLoading" class="message bot mb-4 w-full ml-0 rounded-lg shadow-sm">
            <p class="text-[16px] font-normal leading-[150%] tracking-[-3%] text-text-dark-primary">
              <span class="loading-dots">...</span>
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
            :disabled="isLoading" 
          ></textarea>
          <button
            @click="sendMessage"
            id="chat-send"
            class="absolute bottom-5 right-5 flex items-center rounded-[8px] bg-gray-300 p-[6px] text-gray-600 hover:bg-blue-600"
            :disabled="isLoading"
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
  padding: 10px;
  border-radius: 10px;
}
.message.bot {
  background-color: #f0f0f0;
  padding: 10px;
  border-radius: 10px;
}
#chat-input {
  overflow-y: scroll;
}

/* Стили для анимации трех точек */
.loading-dots {
  display: inline-block;
  width: 24px;
  text-align: left;
}
.loading-dots::after {
  content: '...';
  display: inline-block;
  width: 24px;
  animation: dots 1.5s infinite;
}
@keyframes dots {
  0% { content: '.'; }
  33% { content: '..'; }
  66% { content: '...'; }
}
</style>