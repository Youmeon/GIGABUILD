// Функция для получения пути к изображению
const getImageUrl = (imageName) => {
  try {
    // Проверяем, содержит ли путь подпапку
    if (imageName.includes('/')) {
      return new URL(`../assets/images/${imageName}`, import.meta.url).href
    }
    // Если это изображение из banner-acceptance-of-apartments
    if (imageName.startsWith('acceptance-of-apartments-banner-')) {
      return new URL(`../assets/images/banner-acceptance-of-apartments/${imageName}`, import.meta.url).href
    }
    return new URL(`../assets/images/${imageName}`, import.meta.url).href
  } catch (error) {
    console.error(`Ошибка загрузки изображения ${imageName}:`, error)
    return '' // Запасной путь или placeholder
  }
}

export default getImageUrl
