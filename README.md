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
- `public/`: fontlar, görseller, `dosyalar/Vakit-2.1.dmg`, `_headers`, `robots.txt`, `sitemap.xml`.
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
| Build variables | `PUBLIC_ZIKIR_APK_URL` (aşağıya bakın) |

`PUBLIC_ZIKIR_APK_URL` derleme sırasında okunur: **Build → Variables and secrets** bölümüne girilmeli,
Worker'ın çalışma zamanı değişkenlerine değil. Değiştirdikten sonra yeniden deploy gerekir.

Elle yayın (Git olmadan): `npx wrangler login`, ardından `npm run deploy`.

Alan adı: Worker → **Settings → Domains & Routes → Add → Custom domain** → `necmikayikci.com.tr`
(ve `www.`). Alan adının DNS'i Cloudflare'de olmalı.

Cloudflare tek dosya için 25 MiB sınırı koyar. Zikir APK'si (63 MB) bu yüzden `public/` içinde değil:
GitHub Releases ya da Cloudflare R2'ye yükleyip adresini `PUBLIC_ZIKIR_APK_URL` olarak girin.
Değişken boşsa sitede "APK indir · yakında" pasif düğmesi görünür. APK dosyası şu an `arsiv/statik-site/projeler/dosyalar/Zikir-1.0.apk` konumunda.

`projeler.necmikayikci.com.tr` artık gerekmiyor. Eski bağlantılar için Cloudflare'de bir yönlendirme kuralı
(Rules → Redirect Rules) ekleyin: `projeler.necmikayikci.com.tr/*` → `https://necmikayikci.com.tr/#uygulamalar` (301).

## Yapılacaklar

- Fotoğraf: `public/img/necmi.jpg` ekleyip `Hero.astro` (.avatar) ve `About.astro` (.portrait) içindeki yorumlara göre `<img>` koyun.
- `merhaba@necmikayikci.com.tr` adresinin çalıştığını ve LinkedIn bağlantısını doğrulayın.
- `public/img/zikir.png` bir tasarım taslağı; gerçek ekran görüntüsüyle değiştirin.
- Yeni sürümde: `content.ts` içindeki sürüm, boyut ve SHA-256 değerlerini güncelleyin (`shasum -a 256 dosya`).
