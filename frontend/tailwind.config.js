// tailwind.config.js
import backgroundTokens from './src/styles/tokens/input/base/background.json' with { type: 'json' }
import globalTokens from './src/styles/tokens/input/base/global.json' with { type: 'json' }

// Helper function to extract $value from tokens
const extractValues = (tokens) => {
  const result = {}
  Object.keys(tokens).forEach((category) => {
    const categoryTokens = tokens[category]
    result[category] = {}
    Object.keys(categoryTokens).forEach((key) => {
      if (categoryTokens[key].$value) {
        result[category][key] = categoryTokens[key].$value
      } else {
        // Handle nested tokens (e.g., white-primary)
        result[category][key] = {}
        Object.keys(categoryTokens[key]).forEach((subKey) => {
          result[category][key][subKey] = categoryTokens[key][subKey].$value
        })
      }
    })
  })
  return result
}

// Extract values from token files
const globalColors = extractValues(globalTokens.color)
const backgroundColors = extractValues(backgroundTokens.background)

/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{vue,js,ts,jsx,tsx}'],
  theme: {
    container: {
      center: true,
      padding: '0 2rem',
    },
    extend: {
      colors: {
        // Map global.json colors
        neutral: globalColors.neutral,
        blue: globalColors.blue,
        brand: globalColors.brand,
        text: globalColors.text,
        star: globalColors.star,
        shadow: globalColors.shadow,
        // Map background.json colors
        background: backgroundColors,
      },
      // Map to specific Tailwind utilities
      backgroundColor: {
        neutral: backgroundColors.neutral,
        blue: backgroundColors.blue,
        'white-primary': backgroundColors['white-primary'],
        'white-secondary': backgroundColors['white-secondary'],
      },
      textColor: {
        text: globalColors.text,
      },
      fontSize: {
        h1: [
          '5rem',
          {
            fontWeight: 500,
            lineHeight: '1',
            letterSpacing: '-0.04em',
          },
        ],
        h2: [
          '3rem',
          {
            fontWeight: 600,
            lineHeight: '1',
            letterSpacing: '-0.03em',
          },
        ],
        h3: [
          '2.5rem',
          {
            fontWeight: 600,
            lineHeight: '1',
            letterSpacing: '-0.03em',
          },
        ],
        'btn-base': [
          '1.25rem',
          {
            fontWeight: 500,
            lineHeight: '1',
            letterSpacing: '-0.03em',
          },
        ],
        'btn-header': [
          '1rem',
          {
            fontWeight: 500,
            lineHeight: '1',
            letterSpacing: '-0.03em',
          },
        ],
        'txt-medium': [
          '1.25rem',
          {
            fontWeight: 500,
            lineHeight: '1.35',
            letterSpacing: '-0.03em',
          },
        ],
        'txt-normal': [
          '1.5rem',
          {
            fontWeight: 500,
            lineHeight: '1.5',
            letterSpacing: '-0.03em',
          },
        ],
      },
      fontFamily: {
        sans: ['Inter', 'sans-serif'],
      },
    },
  },
  plugins: [],
}
