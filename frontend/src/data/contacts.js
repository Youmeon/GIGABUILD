// Номер не хранится в коде и не выводится на странице открытым текстом:
// так его не соберут парсеры, которые ищут телефоны в HTML/JS для спам-обзвона.
// Ссылка на мессенджер собирается только в момент клика.
// Номер записан задом наперёд (+7 965 673-29-99).
const ENCODED_PHONE = '99923765697'

const decodePhone = () => ENCODED_PHONE.split('').reverse().join('')

export const messengers = [
  {
    id: 'whatsapp',
    title: 'WhatsApp',
    getUrl: () => `https://wa.me/${decodePhone()}`,
  },
  {
    id: 'telegram',
    title: 'Telegram',
    // Работает, если в настройках Telegram разрешено находить аккаунт по номеру
    getUrl: () => `https://t.me/+${decodePhone()}`,
  },
  {
    id: 'max',
    title: 'MAX',
    // В MAX нет ссылок по номеру телефона — нужна ссылка на профиль/чат.
    // Пока здесь null, кнопка не показывается.
    getUrl: null,
  },
]
