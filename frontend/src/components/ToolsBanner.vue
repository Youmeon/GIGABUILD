<template>
  <div class="tools-banner">
    <div class="tools-banner__text-container">
      <div class="tools-banner__header">
        <div class="tools-banner__label">
          <div class="tools-banner__circle"></div>
          <p class="tools-banner__label-text">ОБОРУДОВАНИЕ</p>
        </div>
        <h2 class="tools-banner__title">Используемые инструменты</h2>
      </div>
      
      <p class="tools-banner__description">
        Наши специалисты приезжают со своим набором поверенных и сертифицированных инструментов — всё откалибровано и соответствует стандартам, чтобы вы получили объективную и надёжную оценку
      </p>
    </div>
    
    <div class="tools-banner__gallery" :style="{ backgroundImage: `url(${currentToolImage})` }">
      <div class="tools-banner__gallery-overlay">
        <div class="tools-banner__controls">
          <h3 class="tools-banner__tool-name">{{ currentTool.title }}</h3>
          
          <div class="tools-banner__nav">
            <button
              @click="prevTool"
              class="tools-banner__nav-btn"
              aria-label="Предыдущий инструмент"
            >
              <ArrowLeft class="tools-banner__nav-icon" />
            </button>
            
            <button
              @click="nextTool"
              class="tools-banner__nav-btn"
              aria-label="Следующий инструмент"
            >
              <ArrowRight class="tools-banner__nav-icon" />
            </button>
          </div>
        </div>
        
        <div class="tools-banner__progress">
          <div 
            class="tools-banner__progress-bar"
            :style="{ width: progressWidth }"
          ></div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { ArrowLeft, ArrowRight } from 'lucide-vue-next'
import getImageUrl from '../utils/getImageURL'

const props = defineProps({
  tools: {
    type: Array,
    required: true,
  },
})

const currentIndex = ref(0)

const currentTool = computed(() => props.tools[currentIndex.value] || props.tools[0])

const currentToolImage = computed(() => {
  return getImageUrl(currentTool.value.image)
})

const progressWidth = computed(() => {
  const progress = ((currentIndex.value + 1) / props.tools.length) * 100
  return `${progress}%`
})

const nextTool = () => {
  currentIndex.value = (currentIndex.value + 1) % props.tools.length
}

const prevTool = () => {
  currentIndex.value = currentIndex.value === 0 
    ? props.tools.length - 1 
    : currentIndex.value - 1
}
</script>

<style scoped>
.tools-banner {
  display: flex;
  align-items: flex-start;
  gap: 16px;
  width: 100%;
}

.tools-banner__text-container {
  width: 448px;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: 178px;
  flex-shrink: 0;
}

.tools-banner__header {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: 24px;
  width: 100%;
}

.tools-banner__label {
  display: flex;
  align-items: center;
  gap: 8px;
}

.tools-banner__circle {
  width: 6px;
  height: 6px;
  flex-shrink: 0;
  background-color: #3d59eb;
  border-radius: 50%;
}

.tools-banner__label-text {
  color: #3b3b3c;
  font-size: 14px;
  font-weight: 700;
  line-height: 1.1;
  letter-spacing: -0.55px;
  text-transform: uppercase;
}

.tools-banner__title {
  color: #262628;
  font-size: 48px;
  font-weight: 600;
  line-height: 1.25;
  letter-spacing: -1.43px;
  text-align: left;
  width: 100%;
}

.tools-banner__description {
  color: #3b3b3c;
  font-size: 20px;
  font-weight: 400;
  line-height: 1.5;
  letter-spacing: -0.59px;
  text-align: left;
  max-width: 380px;
}

.tools-banner__gallery {
  max-width: 1280px;
  flex-grow: 1;
  background-position: top left;
  background-size: cover;
  background-repeat: no-repeat;
  padding-top: 352px;
  border-radius: 32px;
  min-height: 500px;
  transition: background-image 0.5s ease-in-out;
}

.tools-banner__gallery-overlay {
  display: flex;
  flex-direction: column;
  gap: 22px;
  background: linear-gradient(0deg, rgba(2, 2, 3, 0) 0%, rgba(2, 2, 3, 0.7) 75%);
  padding: 99px 32px 26px 34px;
  border-radius: 32px;
}

.tools-banner__controls {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
}

.tools-banner__tool-name {
  color: #fff;
  font-size: 40px;
  font-weight: 500;
  line-height: normal;
  letter-spacing: -1.19px;
  text-align: left;
  margin: -8px 0 0 -2px;
}

.tools-banner__nav {
  display: flex;
  align-items: flex-start;
  gap: 8px;
}

.tools-banner__nav-btn {
  width: 62px;
  height: 40px;
  flex-shrink: 0;
  background-color: #fafafc;
  padding: 8px 19px;
  border-radius: 12px;
  border: none;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.2s ease;
}

.tools-banner__nav-btn:hover {
  background-color: #eef0f9;
}

.tools-banner__nav-icon {
  width: 24px;
  height: 24px;
  color: #262628;
}

.tools-banner__progress {
  background-color: rgba(255, 255, 255, 0.2);
  border-radius: 999px;
  height: 4px;
  overflow: hidden;
}

.tools-banner__progress-bar {
  height: 100%;
  background-color: #fafafc;
  border-radius: 999px;
  transition: width 0.3s ease;
}

/* Responsive */
@media (max-width: 1162px) {
  .tools-banner {
    flex-direction: column;
    align-items: center;
    gap: 92px;
  }
  
  .tools-banner__text-container {
    width: 100%;
    max-width: 448px;
    align-items: center;
  }
  
  .tools-banner__title,
  .tools-banner__description {
    text-align: center;
  }
  
  .tools-banner__gallery {
    width: 100%;
  }
}

@media (max-width: 632px) {
  .tools-banner__controls {
    flex-direction: column;
    align-items: center;
    gap: 14px;
  }
  
  .tools-banner__tool-name {
    margin: 0;
    text-align: center;
  }
  
  .tools-banner__gallery-overlay {
    padding: 99px 16px 26px 16px;
  }
}

@media (max-width: 576px) {
  .tools-banner__text-container {
    gap: 80px;
  }
  
  .tools-banner__title {
    font-size: 32px;
  }
  
  .tools-banner__description {
    font-size: 18px;
  }
  
  .tools-banner__tool-name {
    font-size: 28px;
  }
}
</style>
