<template>
  <component
    :is="componentTag"
    :to="to"
    :type="buttonType"
    class="btn-details relative inline-flex min-h-[60px] items-center justify-center gap-3 overflow-hidden rounded-2xl px-[11px] py-[18px] text-btn-base transition-colors duration-300"
    :class="variantClass"
    @click="onClick"
  >
    <span class="relative z-10">{{ label }}</span>

    <span class="btn-details__icon" aria-hidden="true">
      <svg
        width="24"
        height="24"
        viewBox="0 0 24 24"
        fill="none"
        xmlns="http://www.w3.org/2000/svg"
        class="btn-details__arrow btn-details__arrow--default"
      >
        <path d="M3.8 20.2L19 5" stroke="currentColor" stroke-width="2.5" />
        <path d="M19 21V5H3" stroke="currentColor" stroke-width="2.5" />
      </svg>

      <svg
        width="25"
        height="25"
        viewBox="0 0 25 25"
        fill="none"
        xmlns="http://www.w3.org/2000/svg"
        class="btn-details__arrow btn-details__arrow--hover"
      >
        <path d="M0.817666 12.3137H22.3137" stroke="white" stroke-width="2.5" />
        <path
          d="M11 23.6274L22.3137 12.3137L11 1"
          stroke="white"
          stroke-width="2.5"
        />
      </svg>

      <svg
        width="46"
        height="24"
        viewBox="0 0 46 24"
        fill="none"
        xmlns="http://www.w3.org/2000/svg"
        class="btn-details__arrow btn-details__arrow--active"
      >
        <path d="M1.68628 12.3137H43.3137" stroke="white" stroke-width="2.5" />
        <path
          d="M35 20.6274L43.3137 12.3137L35 4"
          stroke="white"
          stroke-width="2.5"
        />
      </svg>
    </span>
  </component>
</template>

<script setup>
import { computed } from 'vue'
import { RouterLink } from 'vue-router'

const props = defineProps({
  label: {
    type: String,
    default: 'Подробнее',
  },
  variant: {
    type: String,
    default: 'secondary',
    validator: (value) => ['primary', 'secondary'].includes(value),
  },
  to: {
    type: [String, Object],
    default: '',
  },
  type: {
    type: String,
    default: 'button',
  },
})

const emit = defineEmits(['click'])

const componentTag = computed(() => (props.to ? RouterLink : 'button'))

const buttonType = computed(() => (props.to ? undefined : props.type))

const variantClass = computed(() => {
  if (props.variant === 'secondary') {
    return 'bg-neutral-100 text-blue-600 hover:bg-blue-500 hover:text-white active:bg-blue-400 active:text-white'
  }

  return 'bg-blue-600 text-white hover:bg-blue-500 active:bg-blue-400'
})

const onClick = (event) => {
  emit('click', event)
}
</script>

<style scoped>
.btn-details__icon {
  position: relative;
  z-index: 10;
  width: 24px;
  height: 24px;
  display: block;
  flex-shrink: 0;
  overflow: visible;
}

.btn-details__arrow {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  transform-origin: center;
  opacity: 0;
  transition:
    transform 320ms cubic-bezier(0.22, 1, 0.36, 1),
    opacity 220ms ease;
  will-change: transform, opacity;
  pointer-events: none;
}

.btn-details__arrow--default {
  transform: translate(-50%, -50%);
  opacity: 1;
}

.btn-details__arrow--hover {
  transform: translate(calc(-50% - 16px), calc(-50% + 2px)) scale(0.86);
}

.btn-details__arrow--active {
  transform: translate(calc(-50% - 22px), calc(-50% + 1px)) scaleX(0.52);
  transform-origin: center;
}

.btn-details:hover .btn-details__arrow--default {
  transform: translate(calc(-50% + 16px), calc(-50% - 2px)) scale(0.86);
  opacity: 0;
}

.btn-details:hover .btn-details__arrow--hover {
  transform: translate(-50%, -50%) scale(1);
  opacity: 1;
}

.btn-details:focus-visible:not(:active) .btn-details__arrow--default {
  transform: translate(calc(-50% + 16px), calc(-50% - 2px)) scale(0.86);
  opacity: 0;
}

.btn-details:focus-visible:not(:active) .btn-details__arrow--hover {
  transform: translate(-50%, -50%) scale(1);
  opacity: 1;
}

.btn-details:active .btn-details__arrow--default {
  transform: translate(calc(-50% - 18px), -50%) scale(0.7);
  opacity: 0;
}

.btn-details:active .btn-details__arrow--hover {
  transform: translate(calc(-50% + 22px), -50%) scale(0.8);
  opacity: 0;
}

.btn-details:active .btn-details__arrow--active {
  transform: translate(calc(-50% + 22px), -50%) scaleX(1);
  opacity: 1;
}

@media (prefers-reduced-motion: reduce) {
  .btn-details,
  .btn-details__arrow {
    transition-duration: 0.01ms !important;
  }
}
</style>
