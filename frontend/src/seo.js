// Заголовок, описание, canonical и Open Graph для каждой страницы.
// Значения берутся из meta маршрута (src/router/index.js).

export const SITE_URL = 'https://skdionis.ru'
export const SITE_NAME = 'СК Дионис'

const DEFAULT_DESCRIPTION =
  'Приёмка квартир, строительный контроль, обследование зданий и строительные экспертизы в Хабаровске.'

const setMeta = (attr, key, content) => {
  let el = document.head.querySelector(`meta[${attr}="${key}"]`)
  if (!el) {
    el = document.createElement('meta')
    el.setAttribute(attr, key)
    document.head.appendChild(el)
  }
  el.setAttribute('content', content)
}

const setCanonical = (href) => {
  let el = document.head.querySelector('link[rel="canonical"]')
  if (!href) {
    el?.remove()
    return
  }
  if (!el) {
    el = document.createElement('link')
    el.setAttribute('rel', 'canonical')
    document.head.appendChild(el)
  }
  el.setAttribute('href', href)
}

export const applySeo = (route) => {
  const meta =
    typeof route.meta.seo === 'function'
      ? route.meta.seo(route)
      : route.meta.seo
  const title = meta?.title ? `${meta.title} — ${SITE_NAME}` : SITE_NAME
  const description = meta?.description || DEFAULT_DESCRIPTION
  const url =
    SITE_URL + (route.path === '/' ? '/' : route.path.replace(/\/$/, ''))

  document.title = title
  setMeta('name', 'description', description)
  setMeta('name', 'robots', meta?.noindex ? 'noindex' : 'index, follow')
  setMeta('property', 'og:title', title)
  setMeta('property', 'og:description', description)
  setMeta('property', 'og:url', url)
  setCanonical(meta?.noindex ? null : url)
}
