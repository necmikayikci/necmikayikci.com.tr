// Sayfadaki tüm metinler. Bileşenler yalnızca görünümden sorumlu.
import { downloads } from './config';

export type Icon =
  | 'moon' | 'dot' | 'code' | 'car' | 'case' | 'store' | 'lock' | 'mail' | 'bell'
  | 'wifi' | 'target' | 'down' | 'gift' | 'help';

export const meta = {
  title: 'Necmi Kayıkcı — Yazılım Geliştirici',
  description:
    'Necmi Kayıkcı — web, mobil ve masaüstü için sade uygulamalar geliştiren yazılım geliştirici. Vakit ve Zikir uygulamaları ücretsiz.',
};

export const nav = [
  { href: '#uygulamalar', label: 'Uygulamalar' },
  { href: '#projeler', label: 'Projeler' },
  { href: '#hakkimda', label: 'Hakkımda' },
  { href: '#destek', label: 'Destek' },
];

export const hero = {
  hello: 'Merhaba, ben Necmi Kayıkcı',
  titleBefore: 'Hayatı kolaylaştıran',
  titleAccent: 'sade',
  titleAfter: 'uygulamalar yapıyorum',
  lead: 'Web, mobil ve masaüstü için yazılım geliştiriyorum. Kendi ihtiyacımdan doğan uygulamaları herkes için ücretsiz paylaşıyorum.',
  primary: { href: '#uygulamalar', label: 'Uygulamaları indir' },
  secondary: { href: '#iletisim', label: 'İletişime geç' },
  facts: ['Ücretsiz', 'Reklamsız', 'Hesap gerektirmez'],
  chips: [
    { icon: 'lock' as Icon, text: 'Verileriniz cihazınızda kalır' },
    { icon: 'bell' as Icon, text: 'Sade ve gürültüsüz' },
  ],
};

export interface App {
  id: 'vakit' | 'zikir';
  name: string;
  icon: Icon;
  tags: string[];
  desc: string;
  features: string[];
  download: { href: string; label: string; file: string; size: string };
  secondary?: { label: string };
  install: string[];
  installNote?: string;
  releases: { version: string; items: string[] }[];
  sha256: string;
  verifyHint: string;
  image: { src: string; width: number; height: number; kind: 'mac' | 'phone' };
  floats: { icon: Icon; text: string }[];
}

export const apps: App[] = [
  {
    id: 'vakit',
    name: 'Vakit',
    icon: 'moon',
    tags: ['v2.1', 'macOS 14+', 'Apple Silicon + Intel'],
    desc: 'Menü çubuğunda bir sonraki namaz vaktine kalan süreyi gösteren, gürültüsüz bir macOS uygulaması.',
    features: [
      'Diyanet vakitleri; internet yoksa vakitler cihazda hesaplanır',
      'İmsakiye: hafta, ay ve Ramazan tabloları',
      'Ramazan modu: iftara ve sahura geri sayım',
      'Vakit bildirimleri, ezan sesi ve sessiz saatler',
    ],
    download: { href: downloads.vakit, label: 'macOS için indir', file: 'Vakit-2.1.dmg', size: '2,5 MB' },
    install: [
      '**Vakit-2.1.dmg** dosyasını açın ve **Vakit**\'i **Uygulamalar** klasörüne sürükleyin.',
      'Vakit\'i açın. macOS "doğrulanamadı" uyarısı verirse **Tamam**\'a basın.',
      '**Sistem Ayarları → Gizlilik ve Güvenlik**\'e gidin, **Yine de Aç** düğmesine basın ve onaylayın.',
      'Konum izni isterse verin; vakitler bulunduğunuz yere göre hesaplanır. İsterseniz şehri elle de seçebilirsiniz.',
    ],
    installNote:
      'Bu uyarı, uygulama Apple\'ın ücretli geliştirici imzasıyla imzalanmadığı için çıkar; bir kez onaylamanız yeterlidir.',
    releases: [
      {
        version: '2.1',
        items: [
          'İmsakiye penceresi: hafta, ay ve Ramazan tabloları',
          'Ramazan modu: "İftara" ve "Sahurun bitmesine" sayaçları, Kadir Gecesi notu',
          'Ezan sesi: bildirim sesi, yumuşak zil ya da kendi ses dosyanız; ses düzeyi ve sessiz saatler',
        ],
      },
    ],
    sha256: 'e632f2f708ccd5ce08f5325c3468ffcf89f7508effb4e09415a0f261d7e10182',
    verifyHint: 'İndirdiğiniz dosyanın değiştirilmediğini Terminal\'de kontrol edebilirsiniz:',
    image: { src: '/img/vakit.png', width: 656, height: 972, kind: 'mac' },
    floats: [
      { icon: 'wifi', text: 'İnternetsiz çalışır' },
      { icon: 'bell', text: 'Vakit bildirimi' },
    ],
  },
  {
    id: 'zikir',
    name: 'Zikir',
    icon: 'dot',
    tags: ['v1.0', 'Android 7+'],
    desc: 'Zikirlerinizi sayın, günlük hedef belirleyin, sure okumalarınızı takip edin.',
    features: [
      'Dokun-say zikir sayacı ve günlük hedef',
      'Sure takibi ve okuma ilerlemesi',
      'İstatistikler ve geçmiş',
      'Hatırlatma bildirimleri; verileriniz yalnızca cihazınızda',
    ],
    download: { href: downloads.zikir, label: 'APK indir', file: 'Zikir-1.0.apk', size: '63,4 MB' },
    secondary: { label: 'Google Play · yakında' },
    install: [
      'APK\'yı telefonunuzdan indirin ve indirilenlerden açın.',
      '"Bu kaynaktan uygulama yüklenmesine izin ver" sorulursa tarayıcınız için **izin verin**.',
      '**Yükle**\'ye basın. Google Play Protect uyarı gösterirse **Daha fazla ayrıntı → Yine de yükle**\'yi seçin.',
      'Hatırlatmalar için bildirim iznini verin.',
    ],
    releases: [
      { version: '1.0', items: ['İlk sürüm: zikir sayacı, günlük hedef, sure takibi, istatistikler ve hatırlatmalar'] },
    ],
    sha256: 'f897e44ee854a3f73afe676706f2637c3f0aff8f609b3b88b9be5b1026fc298b',
    verifyHint: 'Bilgisayarda Terminal ile kontrol edebilirsiniz:',
    image: { src: '/img/zikir.png', width: 706, height: 1600, kind: 'phone' },
    floats: [{ icon: 'target', text: 'Günlük hedef' }],
  },
];

export const projects = [
  {
    id: 'arac-radar', icon: 'car' as Icon, name: 'Araç Radar', state: 'Kapalı beta',
    desc: 'İkinci el araç ilanlarını analiz edip emsallerle karşılaştıran, adil fiyat tahmini çıkaran platform.',
    tech: ['Web', 'Tarayıcı eklentisi', 'Yapay zekâ'],
  },
  {
    id: 'plugmesh', icon: 'store' as Icon, name: 'PlugMesh', state: 'Shopify',
    desc: 'Shopify mağazaları için entegrasyon uygulaması.',
    tech: ['Web', 'E-ticaret'],
  },
  {
    id: 'careerpilot', icon: 'case' as Icon, name: 'CareerPilot AI', state: 'Geliştiriliyor',
    desc: 'CV ile iş ilanlarını eşleştiren, başvuru sürecine yardım eden yapay zekâ asistanı.',
    tech: ['.NET', 'React', 'Yapay zekâ'],
  },
];

export const about = {
  title: ['Fikirden yayına,', 'uçtan uca.'],
  paragraphs: [
    'Bir ürünün tamamında çalışıyorum: mimari, backend, arayüz, mobil, yayın ve bakım.',
    'En sevdiğim iş, gerçek bir ihtiyaçtan doğan küçük bir aracı sade ve uzun ömürlü hale getirmek. Vakit ve Zikir de böyle doğdu.',
  ],
  stack: ['.NET / C#', 'React', 'Next.js', 'Astro', 'TypeScript', 'React Native', 'Swift', 'SwiftUI', 'PostgreSQL', 'Docker', 'LLM entegrasyonu'],
};

export const faq: { app: string; items: { q: string; a: string }[] }[] = [
  {
    app: 'Vakit',
    items: [
      { q: '"Vakit doğrulanamadı" uyarısı çıkıyor', a: 'Uygulama Apple\'ın ücretli geliştirici imzasıyla imzalanmadığı için macOS bu uyarıyı gösterir. **Tamam**\'a basın, ardından **Sistem Ayarları → Gizlilik ve Güvenlik**\'e gidip **Yine de Aç**\'ı seçin. Bunu bir kez yapmanız yeterlidir.' },
      { q: 'Vakitler yanlış şehre göre görünüyor', a: 'Ayarlar\'dan şehri elle seçin ya da Konum Servisleri\'nde Vakit\'e izin verildiğinden emin olun.' },
      { q: 'Bilgisayar açıldığında Vakit kendiliğinden başlamıyor', a: 'Vakit\'i **Uygulamalar** klasörüne taşıyın ve Ayarlar\'dan "Oturum açıldığında başlat" seçeneğini açın.' },
      { q: 'Bildirim gelmiyor', a: '**Sistem Ayarları → Bildirimler → Vakit** bölümünden bildirimlere izin verin. Vakit ayarlarında ilgili vaktin zilinin açık olduğunu kontrol edin.' },
    ],
  },
  {
    app: 'Zikir',
    items: [
      { q: 'APK yüklenmiyor', a: 'Telefonunuz dosyayı açtığınız uygulamaya (ör. Chrome ya da Dosyalar) "bilinmeyen uygulamaları yükleme" izni vermenizi isteyecek. İzni verip tekrar deneyin. Google Play Protect uyarısında **Daha fazla ayrıntı → Yine de yükle**\'yi seçin.' },
      { q: 'Hatırlatmalar zamanında gelmiyor', a: 'Bildirim iznini verin. Bazı telefonlarda pil tasarrufu uygulamaları kapatır: **Ayarlar → Uygulamalar → Zikir → Pil**\'den "Kısıtlanmamış"ı seçin.' },
      { q: 'Sureler açılmıyor', a: 'Sure metinleri internetten indirilir. İnternet bağlantınızı kontrol edip tekrar deneyin.' },
    ],
  },
];

/** Metinlerde yalnızca **kalın** ve [metin](adres) desteklenir. Kaynak bizim; önce kaçış yapılır. */
export function inline(text: string): string {
  return text
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>')
    .replace(/\[(.+?)\]\((.+?)\)/g, '<a href="$2">$1</a>');
}
