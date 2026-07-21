# BRIEF — Pasang Cluster Artikel LMB ke Situs Ini

**Halo agen. Berkas ini adalah perintah kerja Anda. Baca sampai habis, lalu kerjakan.**

Kalau Anda dipanggil dengan kalimat seperti *"pasang artikel LMB ke situs ini"* atau
*"baca artikel-lmb/BRIEF.md"*, inilah tugasnya.

---

## Tugas

Menerbitkan **11 artikel** tentang LMB (Lubang Masuk Burung) dan sirip rumah burung walet
ke situs di repo ini, memakai bahan yang sudah tersedia lengkap di folder `artikel-lmb/`.

Isi artikel **sudah jadi dan sudah diverifikasi**. Anda tidak perlu menulis ulang, meringkas,
memperbaiki gaya bahasa, atau mengarang isi baru. Tugas Anda adalah **mengadaptasi dan memasang**.

---

## Yang WAJIB dilakukan sebelum menyentuh apa pun

1. **Baca `artikel-lmb/README.md`** — spesifikasi lengkap: konvensi, aturan gambar,
   masalah yang sudah diketahui. Jangan lewati.
2. **Baca `artikel-lmb/manifest.json`** — data 11 artikel: judul, slug, meta description,
   focus keyword, halaman sumber buku, peta gambar, rantai tautan.
3. **Pelajari dulu bagaimana situs ini menyusun artikel yang sudah ada.** Buka 1–2 artikel
   existing, lihat strukturnya, lalu **ikuti pola itu**. Jangan memaksakan struktur dari
   situs asal. Bundle ini sengaja dibuat netral supaya bisa menyesuaikan.

---

## Urutan kerja

### 1. Kenali situs tujuan
Tentukan dulu: ini WordPress, situs statis HTML, atau SSG (Astro/Next/Hugo)?
Jawabannya menentukan bentuk keluaran:

| Jenis situs | Bentuk keluaran |
|---|---|
| WordPress | Fragmen HTML ditempel ke editor, atau diimpor lewat WP-CLI |
| Statis HTML | Fragmen dibungkus boilerplate tema situs ini |
| Astro / Next / Hugo | Konversi fragmen ke `.md`/`.mdx` + frontmatter sesuai skema koleksi situs ini |

### 2. Salin gambar
Salin `artikel-lmb/images/` (22 berkas) ke folder aset situs ini. Catat base path-nya —
itu nilai untuk token `{{IMG}}`.

### 3. Ganti SEMUA token
Fragmen di `articles/` memakai token untuk tiap hal yang terikat situs:

| Token | Isi dengan |
|---|---|
| `{{IMG}}` | Base path folder gambar, tanpa slash di akhir |
| `{{CTA_URL}}` | Halaman layanan/konsultasi situs ini (tujuan konversi) |
| `{{CTA_BANNER}}` | Gambar banner CTA milik situs ini |
| `{{CTA_ALT}}` | Teks alt banner CTA |
| `{{URL:slug}}` | URL artikel lain cluster ini di situs ini |

**Banner CTA tidak disertakan** di bundle (milik situs asal). Kalau situs ini belum punya,
**hapus seluruh blok `<div class="bw-banner">`** — jangan tinggalkan token kosong.

### 4. Bungkus dan pasang
Ikuti pola artikel existing situs ini. Pastikan canonical, Open Graph, dan JSON-LD
memakai **domain situs ini**, bukan domain asal.

### 5. Daftarkan ke halaman daftar/blog
Artikel yang tidak tertaut dari mana pun praktis tidak ditemukan pengunjung, meski URL-nya
hidup. Ini pernah terjadi di situs asal — jangan diulang.

### 6. Verifikasi (jangan dilewati)
Jalankan checklist di bagian bawah berkas ini.

---

## Aturan keras — jangan dilanggar

1. **JANGAN memformalkan bahasanya.** Artikel menyapa pembaca "Pak Bos" dengan ragam lisan
   (*nggak, banget, bikin, ngaruh*). Ini pilihan sadar pemilik, bukan kelalaian.

2. **JANGAN mengubah angka teknis.** 50–70 cm, jarak 50 m, dua tweeter pada LMB siku,
   kayu meranti/mahoni — semua dari buku sumber. Jangan mengarang, jangan "mengoreksi".

3. **JANGAN menghapus baris atribusi** `<p class="bw-source">`. Tiap artikel punya nomor
   halaman buku sendiri. Wajib ada, wajib benar.

4. **JANGAN menautkan gambar ke Google Drive.** Google memblokir hotlink, link mati kalau
   file dipindah, dan tidak terindeks. Gambar harus jadi berkas di dalam repo.

5. **JANGAN percaya nama berkas gambar — lihat isinya.** Saat bundle ini dibuat, berkas
   bernama *"lubang naga"* ternyata thumbnail marketing berlogo, dan *"LMB siku tampak atas"*
   isinya tidak sesuai namanya. Dua-duanya nyaris terpasang di artikel teknis.

6. **JANGAN memutus rantai "Baca juga".** Polanya melingkar 01→02→…→11→01. Kalau ada artikel
   yang tidak jadi dipublikasikan, alihkan tautannya ke artikel berikutnya yang ada.

7. **`width` dan `height` gambar wajib persis sama dengan dimensi berkas** (daftar di
   `manifest.json`). Ini mencegah pergeseran layout saat gambar termuat.

---

## Yang belum selesai (jangan dianggap bug)

- **Artikel 02, 06, 10 belum punya diagram.** Featured image ketiganya memakai foto LMB yang
  sama, jadi thumbnail terlihat kembar di halaman daftar. Gambar yang dibutuhkan tercatat di
  field `gambar_kurang` pada `manifest.json`. Pemilik akan mencarinya manual — **jangan
  mengarang gambar pengganti atau memakai stock photo.**
- **Artikel 04** bagian "LMB Lubang Naga" belum punya diagram.
- **Diagram tweeter tertulis "Twitter magnet"** — typo dari "Tweeter" di berkas sumbernya.

---

## Checklist sebelum melapor selesai

- [ ] Tidak ada string `{{` tersisa di berkas hasil
- [ ] Semua gambar melayani sebagai `image/*` — **periksa `content-type`, bukan cuma status 200.**
      Situs dengan catch-all bisa mengembalikan 200 berisi homepage untuk berkas yang tidak ada
      (*soft 404*), sehingga gambar hilang terlihat seperti berhasil.
- [ ] `width`/`height` tiap gambar cocok dengan dimensi berkas
- [ ] Semua anchor Daftar Isi punya heading tujuan
- [ ] Rantai "Baca juga" utuh, tidak ada link mati
- [ ] Baris `bw-source` ada di tiap artikel dengan nomor halaman yang benar
- [ ] Canonical / OG / JSON-LD memakai domain situs ini
- [ ] Ke-11 artikel tertaut dari halaman daftar/blog
- [ ] **Buka minimal satu artikel di browser sungguhan** dan pastikan gambarnya benar-benar
      termuat — jangan hanya mengandalkan pemeriksaan berkas

---

## Cara melapor

Sebutkan: berapa artikel terpasang, di URL apa, gambar mana yang masih kurang, dan apa yang
Anda ubah dari bundle. **Kalau ada langkah yang gagal atau dilewati, katakan terus terang** —
jangan laporkan selesai kalau belum diverifikasi.

Untuk perubahan sebesar ini, **jangan push langsung ke `main`**. Buat branch, lalu ajukan PR
supaya pemilik bisa meninjau 11 artikel sebelum tayang.

---

## Sumber

Seluruh isi dari **Buku Sukses Budidaya Walet** (Markaswalet), halaman 254–272.
Diagram dari dokumentasi R&D internal Markaswalet.
Bundle dibuat 17 Juli 2026, awalnya untuk budidayawalet.net.
