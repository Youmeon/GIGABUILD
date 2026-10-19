// Пререндеринг: после `vite build` открывает каждую страницу в headless-браузере
// и сохраняет готовый HTML в dist, чтобы поисковики сразу видели текст страницы.
// Заодно генерирует sitemap.xml. Запускается из `npm run build`.

import fs from 'node:fs'
import path from 'node:path'
import { fileURLToPath } from 'node:url'
import puppeteer from 'puppeteer'
import { preview } from 'vite'

const SITE_URL = 'https://skdionis.ru'
const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..')
const dist = path.join(root, 'dist')

const services = JSON.parse(
  fs.readFileSync(path.join(root, 'src/data/detail_services.json'), 'utf8')
)

const pages = [
  '/',
  '/about',
  '/services',
  '/apartment-inspection',
  ...services.map((s) => `/services/${s.id}`),
]

// '/' -> index.html, '/about' -> about.html, '/services/1' -> services/1.html
const fileFor = (route) =>
  route === '/' ? 'index.html' : `${route.slice(1)}.html`

const server = await preview({
  root,
  logLevel: 'warn',
  preview: { port: 4179, strictPort: true },
})
const base = 'http://localhost:4179'
const browser = await puppeteer.launch({ args: ['--no-sandbox'] })

try {
  const page = await browser.newPage()
  await page.setViewport({ width: 1440, height: 900 })

  const render = async (route) => {
    await page.goto(base + route, { waitUntil: 'networkidle0' })
    await page.waitForSelector('#app main')
    const html = await page.evaluate(
      () => '<!doctype html>\n' + document.documentElement.outerHTML
    )
    console.log(`  ${route}  ->  ${await page.title()}`)
    // getImageUrl строит абсолютные адреса (new URL(..., import.meta.url)) — делаем их относительными
    return html.replaceAll(base, '')
  }

  // Сначала рендерим всё, потом пишем: иначе preview начнёт отдавать уже готовый index.html
  const results = []
  for (const route of pages) results.push([fileFor(route), await render(route)])
  results.push(['404.html', await render('/404')])

  for (const [file, html] of results) {
    const target = path.join(dist, file)
    fs.mkdirSync(path.dirname(target), { recursive: true })
    fs.writeFileSync(target, html)
  }
} finally {
  await browser.close()
  await new Promise((resolve) => server.httpServer.close(resolve))
}

const today = new Date().toISOString().slice(0, 10)
const sitemap = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
${pages.map((route) => `  <url><loc>${SITE_URL}${route}</loc><lastmod>${today}</lastmod></url>`).join('\n')}
</urlset>
`
fs.writeFileSync(path.join(dist, 'sitemap.xml'), sitemap)
console.log(`Пререндеринг готов: ${pages.length + 1} страниц, sitemap.xml`)
