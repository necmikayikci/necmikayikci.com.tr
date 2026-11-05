#!/usr/bin/env python3
"""Metin sayfalarını (gizlilik, destek, 404) ortak üst/alt şablonla üretir.

Çalıştırma:  python3 scripts/sayfalar.py
İçeriği değiştirmek için bu dosyadaki PAGES sözlüğünü düzenleyin; HTML dosyaları
her çalıştırmada yeniden yazılır (elle düzenlemeyin).
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "site"
PROJ = "https://projeler.necmikayikci.com.tr"
HOME = "https://necmikayikci.com.tr"
MAIL = "merhaba@necmikayikci.com.tr"
UPDATED = "5 Kasım 2026"

SPRITE = """<svg width="0" height="0" style="position:absolute" aria-hidden="true">
    <symbol id="mark" viewBox="0 0 32 32"><path d="M13 4h15l-6 11H7z"/><path d="M10 17h15l-6 11H4z"/></symbol>
    <symbol id="i-bars" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M4 8h16M4 16h16"/></symbol>
    <symbol id="i-x" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M6 6l12 12M18 6 6 18"/></symbol>
  </svg>"""


def page(site: str, title: str, desc: str, canonical: str, body: str, noindex: bool = False) -> str:
    on_proj = site == "projeler"
    logo_href = HOME if on_proj else "/"
    if on_proj:
        links = [("/#vakit", "Vakit"), ("/#zikir", "Zikir"), ("/#diger", "Diğer projeler"), ("/destek/", "Destek")]
        cta = (HOME, "← Ana sayfa")
    else:
        links = [("/#uygulamalar", "Uygulamalar"), (PROJ, "Projeler"), ("/#hakkimda", "Hakkımda"), ("/#iletisim", "İletişim")]
        cta = (PROJ, "Uygulamaları indir")
    nav = "\n        ".join(f'<a href="{h}">{t}</a>' for h, t in links)
    mnav = "\n      ".join(f'<a href="{h}">{t} <span aria-hidden="true">→</span></a>' for h, t in links)
    foot_links = (
        f'<a href="{HOME}">Ana sayfa</a><a href="/destek/">Destek</a>'
        f'<a href="/vakit/gizlilik/">Vakit gizlilik</a><a href="/zikir/gizlilik/">Zikir gizlilik</a>'
        if on_proj else
        f'<a href="{PROJ}">Uygulamalar</a><a href="/#hakkimda">Hakkımda</a><a href="mailto:{MAIL}">İletişim</a>'
    )
    robots = '\n  <meta name="robots" content="noindex">' if noindex else ""
    return f"""<!DOCTYPE html>
<html lang="tr">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{desc}">{robots}
  <link rel="canonical" href="{canonical}">
  <meta name="theme-color" content="#fbf8f2">
  <link rel="icon" href="/favicon.svg" type="image/svg+xml">
  <link rel="icon" href="/favicon-32.png" sizes="32x32" type="image/png">
  <link rel="apple-touch-icon" href="/apple-touch-icon.png">
  <link rel="stylesheet" href="/assets/base.css">
</head>
<body>
  {SPRITE}
  <a class="skip" href="#icerik">İçeriğe geç</a>
  <header class="site-head">
    <div class="wrap">
      <a class="logo" href="{logo_href}" aria-label="Necmi Kayıkcı — ana sayfa"><svg aria-hidden="true"><use href="#mark"/></svg>Necmi Kayıkcı</a>
      <nav class="menu" aria-label="Ana menü">
        {nav}
      </nav>
      <div class="head-r">
        <a class="btn btn-ink btn-sm" href="{cta[0]}">{cta[1]}</a>
        <button class="menu-btn" type="button" aria-expanded="false" aria-controls="mobil-menu" aria-label="Menüyü aç">
          <svg class="bars" aria-hidden="true"><use href="#i-bars"/></svg><svg class="x" aria-hidden="true"><use href="#i-x"/></svg>
        </button>
      </div>
    </div>
    <nav id="mobil-menu" class="m-menu" aria-label="Mobil menü" hidden>
      {mnav}
      <a class="btn btn-ink" href="{cta[0]}">{cta[1]}</a>
    </nav>
  </header>

  <main id="icerik" class="doc">
{body}
  </main>

  <footer class="site-foot">
    <div class="wrap">
      <div class="end" style="padding-top:28px">
        <div class="end-bot" style="padding-top:0">
          <a class="logo" href="{logo_href}"><svg aria-hidden="true"><use href="#mark"/></svg>Necmi Kayıkcı</a>
          <nav aria-label="Alt menü">{foot_links}</nav>
          <span>© 2026</span>
        </div>
      </div>
    </div>
  </footer>
  <script src="/assets/site.js" defer></script>
</body>
</html>
"""


VAKIT_PRIVACY = f"""    <p class="crumb"><a href="/">Projeler</a> / <a href="/#vakit">Vakit</a> / Gizlilik</p>
    <h1>Vakit gizlilik politikası</h1>
    <p class="meta">Son güncelleme: {UPDATED} · Vakit 2.1 (macOS)</p>
    <p class="lead">Vakit hesap istemez, reklam göstermez ve kullanım verisi toplamaz. Geliştiriciye hiçbir veri gönderilmez.</p>

    <h2>Kısaca</h2>
    <table class="table">
      <tr><th>Veri</th><th>Ne için</th><th>Nereye gider</th></tr>
      <tr><td>Yaklaşık konum (enlem/boylam)</td><td>Bulunduğunuz yerin namaz vakitlerini almak</td><td>Aladhan API (api.aladhan.com)</td></tr>
      <tr><td>Konum → şehir adı</td><td>Panelde "İstanbul, Üsküdar" gibi yer adını göstermek</td><td>Apple'ın konum hizmetleri</td></tr>
      <tr><td>Ayarlar, vakit önbelleği, ses dosyanız</td><td>Uygulamanın çalışması</td><td>Yalnızca Mac'inizde</td></tr>
    </table>

    <h2>Konum</h2>
    <p>Vakit, izin verirseniz macOS Konum Servisleri'nden <strong>kilometre hassasiyetinde</strong> konumunuzu alır. Bunun yerine şehri elle de seçebilirsiniz.</p>
    <p>Namaz vakitlerini almak için konumunuz (virgülden sonra 4 basamağa yuvarlanmış enlem ve boylam), seçili hesaplama yöntemi ve saat diliminiz <strong>api.aladhan.com</strong> adresine gönderilir. Vakitler ay bazında bir kez çekilir ve Mac'inizde saklanır. İnternet yoksa vakitler doğrudan cihazınızda hesaplanır; bu durumda hiçbir istek gönderilmez.</p>
    <p>Konumun şehir/ilçe adına çevrilmesi ve elle şehir aramaları Apple'ın konum hizmetleri üzerinden yapılır.</p>

    <h2>Cihazınızda saklananlar</h2>
    <ul>
      <li>Ayarlarınız (macOS kullanıcı tercihleri)</li>
      <li>Vakit önbelleği: <code>~/Library/Application Support/Vakit/Cache</code></li>
      <li>Seçtiğiniz ezan sesi dosyası: <code>~/Library/Application Support/Vakit/Sounds</code></li>
    </ul>
    <p>Bildirimler Mac'inizde yerel olarak planlanır; dışarıya bir bildirim servisi kullanılmaz.</p>

    <h2>Toplanmayanlar</h2>
    <p>Analitik, çökme raporu, reklam kimliği, hesap ya da e-posta bilgisi toplanmaz. Uygulamada üçüncü taraf analiz veya reklam kütüphanesi yoktur.</p>

    <h2>Verilerinizi silmek</h2>
    <p>Vakit'i Uygulamalar klasöründen silin ve <code>~/Library/Application Support/Vakit</code> klasörünü kaldırın. Konum iznini <strong>Sistem Ayarları → Gizlilik ve Güvenlik → Konum Servisleri</strong>'nden istediğiniz zaman geri alabilirsiniz.</p>

    <h2>Üçüncü taraf hizmetler</h2>
    <ul>
      <li><a href="https://aladhan.com">Aladhan</a> — namaz vakitleri API'si. İstek sırasında IP adresinizi görür; kendi gizlilik koşulları geçerlidir.</li>
      <li><a href="https://www.apple.com/tr/legal/privacy/">Apple</a> — konum ve yer adı hizmetleri.</li>
    </ul>

    <h2>İletişim</h2>
    <p>Sorularınız için: <a href="mailto:{MAIL}?subject=Vakit%20gizlilik">{MAIL}</a></p>
"""

ZIKIR_PRIVACY = f"""    <p class="crumb"><a href="/">Projeler</a> / <a href="/#zikir">Zikir</a> / Gizlilik</p>
    <h1>Zikir gizlilik politikası</h1>
    <p class="meta">Son güncelleme: {UPDATED} · Zikir 1.0 (Android)</p>
    <p class="lead">Zikir hesap istemez, reklam göstermez ve kullanım verisi toplamaz. Zikir kayıtlarınız yalnızca telefonunuzda saklanır; geliştiriciye hiçbir veri gönderilmez.</p>

    <h2>Kısaca</h2>
    <table class="table">
      <tr><th>Veri</th><th>Nerede</th></tr>
      <tr><td>Zikir sayıları, hedefler, geçmiş, istatistikler</td><td>Yalnızca telefonunuzda</td></tr>
      <tr><td>Sure takibi ve okuma ilerlemesi</td><td>Yalnızca telefonunuzda</td></tr>
      <tr><td>Kur'an metni (sure içerikleri)</td><td>api.alquran.cloud adresinden indirilir</td></tr>
    </table>

    <h2>İnternet kullanımı</h2>
    <p>Uygulama, sureleri gösterebilmek için Kur'an metnini ve Türkçe mealini <strong>api.alquran.cloud</strong> adresinden indirir. Bu isteklerde sizinle ilgili bir bilgi gönderilmez; yalnızca istenen surenin numarası iletilir. Hizmet, her internet isteğinde olduğu gibi IP adresinizi görür.</p>

    <h2>İzinler</h2>
    <table class="table">
      <tr><th>İzin</th><th>Neden</th></tr>
      <tr><td>İnternet</td><td>Sure metinlerini indirmek</td></tr>
      <tr><td>Bildirim gönderme</td><td>Zikir ve okuma hatırlatmaları</td></tr>
      <tr><td>Tam zamanlı alarm</td><td>Hatırlatmaların seçtiğiniz saatte çalması</td></tr>
      <tr><td>Açılışta başlatma</td><td>Telefon yeniden başladığında hatırlatmaları yeniden kurmak</td></tr>
      <tr><td>Titreşim</td><td>Sayarken dokunsal geri bildirim</td></tr>
    </table>

    <h2>Toplanmayanlar</h2>
    <p>Analitik, çökme raporu, reklam kimliği, konum, rehber, hesap ya da e-posta bilgisi toplanmaz. Uygulamada üçüncü taraf analiz veya reklam kütüphanesi yoktur.</p>

    <h2>Verilerinizi silmek</h2>
    <p>Uygulamayı kaldırdığınızda tüm kayıtlarınız telefonunuzdan silinir. Kaldırmadan silmek için <strong>Ayarlar → Uygulamalar → Zikir → Depolama → Verileri temizle</strong> yolunu kullanabilirsiniz.</p>

    <h2>İletişim</h2>
    <p>Sorularınız için: <a href="mailto:{MAIL}?subject=Zikir%20gizlilik">{MAIL}</a></p>
"""

SUPPORT = f"""    <p class="crumb"><a href="/">Projeler</a> / Destek</p>
    <h1>Destek</h1>
    <p class="lead">Kurulumda takıldıysanız ya da bir hata bulduysanız aşağıya göz atın. Cevabı bulamazsanız bana yazın.</p>
    <p><a class="btn btn-green" href="mailto:{MAIL}?subject=Destek">{MAIL}</a></p>

    <h2 id="vakit" style="scroll-margin-top:16px">Vakit (macOS)</h2>
    <h3>"Vakit doğrulanamadı" uyarısı çıkıyor</h3>
    <p>Uygulama Apple'ın ücretli geliştirici imzasıyla imzalanmadığı için macOS bu uyarıyı gösterir. <strong>Tamam</strong>'a basın, ardından <strong>Sistem Ayarları → Gizlilik ve Güvenlik</strong>'e gidip <strong>Yine de Aç</strong>'ı seçin. Bunu bir kez yapmanız yeterlidir.</p>
    <h3>Vakitler yanlış şehre göre görünüyor</h3>
    <p>Ayarlar'dan şehri elle seçin ya da Konum Servisleri'nde Vakit'e izin verildiğinden emin olun.</p>
    <h3>Bilgisayar açıldığında Vakit kendiliğinden başlamıyor</h3>
    <p>Vakit'i <strong>Uygulamalar</strong> klasörüne taşıyın ve Ayarlar'dan "Oturum açıldığında başlat" seçeneğini açın.</p>
    <h3>Bildirim gelmiyor</h3>
    <p><strong>Sistem Ayarları → Bildirimler → Vakit</strong> bölümünden bildirimlere izin verin. Vakit ayarlarında ilgili vaktin zilinin açık olduğunu kontrol edin.</p>
    <h3>Sistem gereksinimi</h3>
    <p>macOS 14 (Sonoma) veya üstü. Apple Silicon ve Intel Mac'lerde çalışır.</p>

    <h2 id="zikir" style="scroll-margin-top:16px">Zikir (Android)</h2>
    <h3>APK yüklenmiyor</h3>
    <p>Telefonunuz dosyayı açtığınız uygulamaya (ör. Chrome ya da Dosyalar) "bilinmeyen uygulamaları yükleme" izni vermenizi isteyecek. İzni verip tekrar deneyin. Google Play Protect uyarısında <strong>Daha fazla ayrıntı → Yine de yükle</strong>'yi seçin.</p>
    <h3>Hatırlatmalar zamanında gelmiyor</h3>
    <p>Bildirim iznini verin. Bazı telefonlarda pil tasarrufu uygulamaları kapatır: <strong>Ayarlar → Uygulamalar → Zikir → Pil</strong>'den "Kısıtlanmamış"ı seçin.</p>
    <h3>Sureler açılmıyor</h3>
    <p>Sure metinleri internetten indirilir. İnternet bağlantınızı kontrol edip tekrar deneyin.</p>
    <h3>Sistem gereksinimi</h3>
    <p>Android 7.0 veya üstü.</p>

    <h2>İndirdiğim dosyayı nasıl doğrularım?</h2>
    <p>Her uygulamanın kartında "Dosyayı doğrula (SHA-256)" bölümü var. Terminal'de <code>shasum -a 256 dosya-adı</code> komutunun çıktısı oradaki değerle aynıysa dosya değiştirilmemiştir.</p>

    <h2>Hata bildirirken</h2>
    <p>Uygulama adını ve sürümünü, cihazınızı (ör. "MacBook Air M2, macOS 15" ya da "Samsung A54, Android 14") ve sorunu nasıl yaşadığınızı yazarsanız çok daha hızlı çözebilirim. Ekran görüntüsü de çok yardımcı olur.</p>
"""

NOT_FOUND = """    <p class="crumb">Hata 404</p>
    <h1>Bu sayfa bulunamadı.</h1>
    <p class="lead">Aradığınız sayfa taşınmış ya da hiç var olmamış olabilir.</p>
    <p style="display:flex;gap:10px;flex-wrap:wrap;margin-top:28px">{links}</p>
"""

PAGES = {
    ("projeler", "vakit/gizlilik/index.html"): ("Vakit gizlilik politikası — Necmi Kayıkcı",
        "Vakit macOS uygulamasının gizlilik politikası: hangi veriler, nerede ve neden kullanılır.",
        f"{PROJ}/vakit/gizlilik/", VAKIT_PRIVACY, False),
    ("projeler", "zikir/gizlilik/index.html"): ("Zikir gizlilik politikası — Necmi Kayıkcı",
        "Zikir Android uygulamasının gizlilik politikası: verileriniz yalnızca cihazınızda.",
        f"{PROJ}/zikir/gizlilik/", ZIKIR_PRIVACY, False),
    ("projeler", "destek/index.html"): ("Destek — Necmi Kayıkcı",
        "Vakit ve Zikir için kurulum yardımı, sık sorulan sorular ve iletişim.",
        f"{PROJ}/destek/", SUPPORT, False),
    ("projeler", "404.html"): ("Sayfa bulunamadı — Necmi Kayıkcı", "Sayfa bulunamadı.", f"{PROJ}/",
        NOT_FOUND.format(links='<a class="btn btn-green" href="/">Uygulamalara dön</a><a class="btn btn-line" href="' + HOME + '">Ana sayfa</a>'), True),
    ("necmikayikci.com.tr", "404.html"): ("Sayfa bulunamadı — Necmi Kayıkcı", "Sayfa bulunamadı.", f"{HOME}/",
        NOT_FOUND.format(links='<a class="btn btn-green" href="/">Ana sayfaya dön</a><a class="btn btn-line" href="' + PROJ + '">Uygulamalar</a>'), True),
}

for (site, rel), (title, desc, canonical, body, noindex) in PAGES.items():
    out = ROOT / site / rel
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(page(site, title, desc, canonical, body, noindex), encoding="utf-8")
    print("yazıldı:", out.relative_to(ROOT.parent))
