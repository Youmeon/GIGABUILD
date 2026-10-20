// Номер не хранится в коде и не выводится на странице открытым текстом:
// так его не соберут парсеры, которые ищут телефоны в HTML/JS для спам-обзвона.
// Ссылка на мессенджер собирается только в момент клика.
// Номер записан задом наперёд (+7 965 673-29-99).
const ENCODED_PHONE = '99923765697'

const decodePhone = () => ENCODED_PHONE.split('').reverse().join('')

// Ссылка на профиль компании в MAX.
// В MAX нет ссылок по номеру телефона, поэтому ссылка скопирована из приложения.
// Если строку очистить, кнопка MAX на сайте не показывается.
const MAX_URL = 'https://max.ru/u/f9LHodD0cOJDhCICgIigylc8Sz35xrmtoLLmIWzlXGYM4gtn6odq3rj4t1E'

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
    getUrl: MAX_URL ? () => MAX_URL : null,
  },
]
