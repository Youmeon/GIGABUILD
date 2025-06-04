// Функция для получения пути к изображению
const getImageUrl = (imageName) => {
  try {
    return new URL(`../assets/images/${imageName}`, import.meta.url).href
  } catch (error) {
    console.error(`Ошибка загрузки изображения ${imageName}:`, error)
    return '' // Запасной путь или placeholder
  }
}

export default getImageUrl
