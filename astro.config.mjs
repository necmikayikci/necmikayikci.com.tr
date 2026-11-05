// @ts-check
import { defineConfig } from 'astro/config';

// necmikayikci.com.tr — tek sayfalık kişisel site + uygulama gizlilik sayfaları.
// Cloudflare Pages: derleme komutu `npm run build`, çıktı klasörü `dist`.
export default defineConfig({
  site: 'https://necmikayikci.com.tr',
  build: { inlineStylesheets: 'auto' },
});
