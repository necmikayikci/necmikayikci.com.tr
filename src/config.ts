// Ortama bağlı ayarlar. Değerler .env (PUBLIC_*) ya da Cloudflare Pages ortam
// değişkenlerinden gelir; yoksa varsayılana düşer.

const MAIL = 'merhaba@necmikayikci.com.tr';

export const site = {
  name: 'Necmi Kayıkçı',
  url: 'https://necmikayikci.com.tr',
  mail: MAIL,
  mailto: (subject?: string) => `mailto:${MAIL}${subject ? `?subject=${encodeURIComponent(subject)}` : ''}`,
  github: 'https://github.com/necmikayikci',
  linkedin: 'https://www.linkedin.com/in/necmikayikci',
} as const;

// İndirme adresleri. Vakit dmg'si küçük (2,5 MB), site içinden sunulur.
// Zikir APK'sı 63 MB: Cloudflare Pages'in 25 MiB dosya sınırını aştığı için
// dışarıda (GitHub Releases / R2) barındırılır. Adres yoksa buton "yakında" olur.
export const downloads = {
  vakit: '/dosyalar/Vakit-2.1.dmg',
  zikir: (import.meta.env.PUBLIC_ZIKIR_APK_URL as string | undefined)?.trim() || '',
} as const;
