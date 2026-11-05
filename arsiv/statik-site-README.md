# necmikayikci.com.tr

İki statik site, derleme adımı yok.

| Klasör | Alan adı |
|---|---|
| `site/necmikayikci.com.tr/` | necmikayikci.com.tr |
| `site/projeler/` | projeler.necmikayikci.com.tr |

## Yerelde açmak

```bash
python3 -m http.server 8010 --directory site/necmikayikci.com.tr
python3 -m http.server 8011 --directory site/projeler
```

Her site kendi kökünden sunulmalı (`/assets/...` yolları köke göre).

## Ortak dosyalar

`assets/base.css`, `assets/site.js` ve `assets/fonts/` iki sitede de aynı. Birini değiştirince diğerine kopyalayın.

Gizlilik, destek ve 404 sayfaları `scripts/sayfalar.py` ile üretilir; içeriği orada düzenleyip `python3 scripts/sayfalar.py` çalıştırın.

## Yayına almadan önce

- `site/projeler/dosyalar/Zikir-1.0.apk` 63 MB. Cloudflare Pages tek dosyada 25 MiB sınırı koyar; APK'yı GitHub Releases'a yükleyip `projeler/index.html` içindeki indirme bağlantısını değiştirin.
- Yeni sürümde dosya boyutunu ve SHA-256 değerini (`shasum -a 256 dosya`) sayfada güncelleyin.
- Fotoğraf eklemek için `index.html` içindeki "Fotoğraf eklemek için" yorumlarına bakın.
