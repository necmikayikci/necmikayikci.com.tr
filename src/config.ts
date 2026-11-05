// Site ayarları. PUBLIC_* değerleri .env ya da Cloudflare build değişkenlerinden
// gelir; yoksa varsayılana düşer.

const MAIL = 'merhaba@necmikayikci.com.tr';

export const site = {
  name: 'Necmi Kayıkcı',
  url: 'https://necmikayikci.com.tr',
  mail: MAIL,
  mailto: (subject?: string) => `mailto:${MAIL}${subject ? `?subject=${encodeURIComponent(subject)}` : ''}`,
  github: 'https://github.com/necmikayikci',
  linkedin: 'https://www.linkedin.com/in/necmikayikci',
} as const;

// İndirme dosyaları Cloudflare R2'deki "files" bucket'ının apps/ klasöründe durur
// (Workers'ta dosya başına 25 MiB sınırı var, APK 63 MB). Bucket'a bağlı alan adı
// değişirse PUBLIC_FILES_URL ile ezilebilir.
const FILES = ((import.meta.env.PUBLIC_FILES_URL as string | undefined)?.trim() || 'https://download.necmikayikci.com.tr').replace(/\/$/, '');

export const downloads = {
  vakit: `${FILES}/apps/Vakit-2.1.dmg`,
  zikir: `${FILES}/apps/Zikir-1.0.apk`,
} as const;
