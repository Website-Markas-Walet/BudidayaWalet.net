# Cluster Artikel LMB & Sirip — Content Bundle

**Untuk agen AI: baca berkas ini sampai habis sebelum mengerjakan apa pun.**
Bundle ini berisi 11 artikel siap pasang beserta gambarnya. Semua keputusan editorial
sudah diambil dan dikunci di sini — ikuti, jangan diputuskan ulang.

Bundle ini **netral terhadap situs**. Tidak ada tema, menu, atau footer di dalamnya.
Isinya bisa dipasang ke situs mana pun (WordPress, HTML statis, SSG).

---

## 1. Isi bundle

```
artikel-lmb/
├── README.md          ← berkas ini
├── manifest.json      ← metadata mesin: 11 artikel, token, konvensi, dimensi gambar
├── articles/          ← 11 fragmen HTML (isi artikel saja, ~5 KB masing-masing)
├── images/            ← 22 gambar, sudah dioptimasi
└── assets/
    └── article.css    ← CSS untuk class bw-* yang dipakai fragmen
```

`manifest.json` adalah sumber kebenaran untuk judul, meta description, focus keyword,
slug, halaman sumber buku, peta gambar, dan rantai tautan. **Baca itu dulu.**

---

## 2. Cara pasang (3 langkah)

### Langkah 1 — Salin gambar
Salin isi `images/` ke folder aset situs tujuan. Catat base path-nya; itu jadi nilai `{{IMG}}`.

### Langkah 2 — Ganti SEMUA token
Fragmen di `articles/` memakai token untuk setiap hal yang terikat situs. **Wajib diganti semua** sebelum publikasi:

| Token | Ganti dengan | Contoh |
|---|---|---|
| `{{IMG}}` | Base path gambar, tanpa slash di akhir | `/wp-content/uploads/2026/07` |
| `{{CTA_URL}}` | Halaman layanan/konsultasi situs tujuan | `/layanan/` |
| `{{CTA_BANNER}}` | Gambar banner CTA milik situs tujuan | `/img/banner-konsultasi.png` |
| `{{CTA_ALT}}` | Teks alt banner CTA | `Konsultasi gedung walet bersama Markaswalet` |
| `{{URL:slug}}` | URL artikel lain di situs tujuan | `{{URL:jenis-jenis-lmb}}` → `/jenis-jenis-lmb.html` |

> **Banner CTA tidak disertakan** di bundle karena milik situs asal. Situs tujuan harus
> menyediakan bannernya sendiri. Kalau belum ada, hapus saja seluruh blok `<div class="bw-banner">`
> — jangan biarkan `{{CTA_BANNER}}` tidak terisi.

**Verifikasi:** setelah selesai, cari string `{{` di seluruh berkas hasil. Harus nol.

### Langkah 3 — Bungkus sesuai situs tujuan

**Kalau WordPress:** tempel fragmen ke editor (mode HTML/Custom HTML). Isi judul, slug,
meta description, dan focus keyword dari `manifest.json`. Upload featured image.
Muat `assets/article.css` lewat tema atau plugin Custom CSS.

**Kalau situs statis:** bungkus fragmen dengan boilerplate tema situs tujuan
(`<head>`, header, footer). Sisipkan isi `article.css` sebagai blok `<style>` di dalam
`entry-content`, atau muat sebagai berkas CSS terpisah. Jangan lupa canonical, Open Graph,
dan JSON-LD memakai domain situs tujuan.

---

## 3. Konvensi yang WAJIB dipertahankan

Ini keputusan yang sudah diambil. Jangan diubah tanpa persetujuan pemilik.

### Gaya bahasa
- **Menyapa pembaca "Pak Bos".** Santai, ragam lisan: *nggak, banget, bikin, ngaruh, disaranin.*
- **JANGAN diformalkan.** Ini pilihan sadar, bukan kelalaian.
- Judul bergaya pertanyaan/kejutan, sering diakhiri tanda seru.
- Intro 3–4 kalimat: hook masalah → kenapa penting → janji isi artikel.
- Penutup = rangkuman, bukan informasi baru.

### Isi
- **Semua klaim teknis berasal dari buku.** Angka seperti 50–70 cm, jarak 50 m, dua tweeter
  pada LMB siku, kayu meranti/mahoni — jangan mengarang angka baru, jangan "memperbaiki" angka.
- **Atribusi wajib.** Tiap artikel diakhiri `<p class="bw-source">` dengan nomor halaman
  spesifiknya. Jangan dihapus, jangan disamakan nomornya.
- **Framing konsultasi.** Tiap artikel punya bagian yang menunjukkan antar-subsistem saling
  mengunci (LMB ↔ cahaya ↔ ventilasi ↔ suara), sehingga perbaikan sepotong-sepotong berisiko.
  Ini yang mengarahkan pembaca ke CTA — jangan dipotong karena dianggap mengulang.

### Rantai "Baca juga"
Melingkar: **01 → 02 → … → 11 → 01**. Tiap artikel menautkan artikel berikutnya.
Kalau ada artikel yang tidak jadi dipublikasikan, **alihkan tautannya ke artikel berikutnya
yang ada** — jangan biarkan rantai putus atau menghasilkan link mati.

### Daftar Isi
Fragmen sudah memuat `<nav class="bw-toc">` manual, dan setiap anchor sudah cocok dengan
`id` heading tujuannya. **Kalau situs tujuan punya plugin TOC otomatis, hapus `<nav>` ini**
supaya tidak muncul dua daftar isi.

### Gambar
- **Featured:** 1280×720 (16:9). Diagram yang rasionya bukan 16:9 di-*fit* utuh di atas
  kanvas putih — **jangan di-crop paksa**, karena teks di dalam diagram bisa terpotong.
- **Inline:** lebar maksimal 1280, jaga rasio asli.
- **`width` dan `height` wajib persis sama dengan dimensi file** (daftarnya di `manifest.json`).
  Ini mencegah pergeseran layout saat gambar termuat. Kalau gambar diproses ulang,
  perbarui juga atribut di fragmen.
- Gambar inline pakai `loading="lazy"`; featured tidak.
- Caption diagram diakhiri `Sumber: Internal Markaswalet.`

---

## 4. Aturan gambar dari Google Drive

Gambar sumber ada di folder R&D Markaswalet di Drive. Kalau perlu menambah gambar:

1. **JANGAN menautkan langsung ke Drive.** Google memblokir hotlink, link mati kalau file
   dipindah, tidak terindeks sebagai gambar situs, dan lambat. **Selalu unduh jadi berkas
   di dalam repo.**
2. **Selalu lihat isi gambarnya sebelum dipakai — jangan percaya nama berkas.** Ini bukan
   saran teoretis: saat bundle ini dibuat, berkas bernama *"lubang naga"* ternyata thumbnail
   marketing berlogo, dan *"LMB siku tampak atas"* isinya tidak sesuai namanya. Dua-duanya
   nyaris terpasang di artikel teknis.
3. Berkas R&D sering bertipe **shortcut** Drive yang tidak bisa diunduh lewat API. Cara yang
   berhasil: pakai MCP Drive untuk **mencari** (murah, cuma metadata), lalu unduh lewat
   **HTTP langsung** ke `drive.google.com/uc?export=download&id=<ID>` (folder ter-share, jadi
   tidak membebani konteks).

---

## 5. Masalah yang sudah diketahui

- **Artikel 02, 06, 10 belum punya diagram.** Featured image ketiganya memakai foto LMB yang
  sama, jadi thumbnail terlihat kembar di halaman daftar artikel. Gambar yang dibutuhkan
  tercatat di field `gambar_kurang` pada `manifest.json`.
- **Artikel 04** bagian "LMB Lubang Naga" belum punya diagram.
- **Typo di diagram sumber:** diagram tweeter tertulis *"Twitter magnet"*, seharusnya *"Tweeter"*.
  Perbaiki di berkas sumber Drive kalau memungkinkan.
- **Byline "Rahma Aziz".** Kalau situs tujuan tidak punya halaman author untuknya, tampilkan
  sebagai teks biasa tanpa tautan — jangan bikin link mati.

---

## 6. Checklist sebelum publikasi

- [ ] Tidak ada string `{{` tersisa di berkas hasil
- [ ] Semua gambar yang dirujuk benar-benar ada, dan **melayani sebagai `image/*`** —
      periksa `content-type`, bukan cuma status 200. Situs yang punya *catch-all* bisa
      mengembalikan 200 berisi homepage untuk berkas yang tidak ada (*soft 404*).
- [ ] `width`/`height` tiap gambar cocok dengan dimensi file
- [ ] Semua anchor Daftar Isi punya heading tujuan
- [ ] Rantai "Baca juga" utuh, tidak ada link mati
- [ ] Baris `bw-source` ada di tiap artikel dengan nomor halaman yang benar
- [ ] Canonical, Open Graph, dan JSON-LD memakai domain situs tujuan
- [ ] Artikel tertaut dari halaman daftar/blog — **artikel yang tidak tertaut praktis tidak
      ditemukan pengunjung meski URL-nya hidup**
- [ ] Buka satu artikel di browser sungguhan dan pastikan gambarnya termuat

---

## 7. Sumber

Seluruh isi bersumber dari **Buku Sukses Budidaya Walet** (Markaswalet), halaman 254–272.
Diagram berasal dari folder dokumentasi R&D internal Markaswalet.
