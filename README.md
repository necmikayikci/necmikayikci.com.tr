# necmikayikci.com.tr

Tek sayfalık kişisel site (Astro, statik). Cloudflare Workers'ta (statik varlıklar) yayınlanır.

## Geliştirme

```bash
npm install
npm run dev        # http://localhost:4321
npm run build      # çıktı: dist/
npm run typecheck  # astro check
```

## Yapı

- `src/content.ts`: sayfadaki tüm metinler (uygulamalar, projeler, hakkımda, SSS). Metin değişiklikleri buradan.
- `src/config.ts`: e-posta, sosyal bağlantılar, indirme adresleri.
- `src/components/`: bölümler (Nav, Hero, Apps, Projects, About, Support, Footer).
- `src/pages/`: `index` (tek sayfa), `vakit/gizlilik`, `zikir/gizlilik`, `404`.
- `public/`: fontlar, görseller, `_headers`, `robots.txt`, `sitemap.xml`.
- `arsiv/`: önceki statik HTML sürümü (yayına girmez).

## Cloudflare Workers

Site, sunucu kodu olmayan bir Worker olarak yayınlanır; ayarlar `wrangler.jsonc` içinde
(`dist/` klasörü, bulunamayan sayfalar için `404.html`). `wrangler.jsonc` içindeki `name`,
paneldeki Worker adıyla aynı olmalı.

Worker → **Settings → Build** (Git bağlantısı):

| Ayar | Değer |
|---|---|
| Git repository | `necmikayikci/necmikayikci.com.tr`, dal `main` |
| Build command | `npm run build` |
| Deploy command | `npx wrangler deploy` |

Elle yayın (Git olmadan): `npx wrangler login`, ardından `npm run deploy`.

Alan adı: Worker → **Settings → Domains & Routes → Add → Custom domain** → `necmikayikci.com.tr`
(ve `www.`). Alan adının DNS'i Cloudflare'de olmalı.

## İndirme dosyaları (R2)

Workers'ta dosya başına 25 MiB sınırı olduğu için uygulama dosyaları repoda değil, Cloudflare R2'de durur:
`files` bucket'ı → `apps/` klasörü (`Vakit-2.1.dmg`, `Zikir-1.0.apk`). Bucket'a bağlı alan adı
`download.necmikayikci.com.tr`; adresler `https://download.necmikayikci.com.tr/apps/<dosya>`.
Alan adı değişirse build değişkeni `PUBLIC_FILES_URL` ile ezilebilir (bkz. `src/config.ts`).

Yeni sürümde: dosyayı R2'de `apps/` altına yükleyin, `src/config.ts` içindeki dosya adını ve
`src/content.ts` içindeki sürüm, boyut ve SHA-256 değerlerini güncelleyin (`shasum -a 256 dosya`).

`projeler.necmikayikci.com.tr` artık gerekmiyor. Eski bağlantılar için Cloudflare'de bir yönlendirme kuralı
(Rules → Redirect Rules) ekleyin: `projeler.necmikayikci.com.tr/*` → `https://necmikayikci.com.tr/#uygulamalar` (301).

## Yapılacaklar

- Fotoğraf: `public/img/necmi.jpg` ekleyip `Hero.astro` (.avatar) ve `About.astro` (.portrait) içindeki yorumlara göre `<img>` koyun.
- `merhaba@necmikayikci.com.tr` adresinin çalıştığını ve LinkedIn bağlantısını doğrulayın.
- `public/img/zikir.png` bir tasarım taslağı; gerçek ekran görüntüsüyle değiştirin.
