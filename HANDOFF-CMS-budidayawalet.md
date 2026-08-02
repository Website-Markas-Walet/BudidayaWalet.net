# Respons Session: BudidayaWalet.net → CMS Terpusat

> Balasan atas Brief Standar. Arsitektur final diterima: CMS di `cms.markaswalet.id`
> (Next.js + Supabase, Vercel), media di Cloudflare R2 (`cdn.markaswalet.id`), scope **aditif**
> (CMS generate/commit KONTEN ke repo; navbar/menu/footer & URL tidak diubah).
> Legenda: ✅ terverifikasi di repo/live · ⚠️ masalah · ❓ butuh keputusan/fakta manusia.
> Repo: `Website-Markas-Walet/BudidayaWalet.net`, branch **main**.

---

## ⛔ BLOCKER #1 — Mekanisme deploy (butuh konfirmasi manusia)

Yang bisa saya buktikan dari luar:
- Live **di belakang Cloudflare** ✅ (`Server: cloudflare`, `CF-RAY: …-SIN` = Singapore, `cf-cache-status: DYNAMIC`).
- `cf-cache-status: DYNAMIC` → origin tampak **server yang di-proxy**, bukan cache statik khas Cloudflare Pages (ini inferensi, bukan bukti).
- Di repo **TIDAK ADA** config deploy apa pun ✅: tak ada `.github/workflows/`, `CNAME`, `netlify.toml`, `vercel.json`, `.nojekyll`.
- ⚠️ **KEANEHAN ROUTING PENTING:** live menyajikan **URL tanpa `.html`**.
  `/walet-untuk-batuk` → **200**, tapi `/walet-untuk-batuk.html` → **308 redirect** ke versi tanpa ekstensi.
  Padahal file di repo bernama `*.html` dan link internal memakai `*.html`. Artinya **ADA lapisan rewrite**
  (aturan Cloudflare / server origin) antara repo dan live. Repo ≠ live secara 1:1.

**❓ Hanya Anda yang tahu (wajib dijawab — tanpa ini tombol "Publish" tak punya target):**
1. Persis bagaimana repo → live? (Cloudflare Pages? server pull dari Git? upload manual? lainnya)
2. Branch produksi (kemungkinan `main`, konfirmasi).
3. Cloudflare akun **#1 atau #2**? Ada **Deploy Hook**?
4. Siapa/apa yang membuat URL jadi tanpa `.html`? (penentu URL kanonik untuk link yang di-generate CMS)

---

## ⛔ BLOCKER #2 — Akses tulis untuk CMS (butuh setup manusia)

Ini repo **GitHub**, jadi jalur commit CMS = mekanisme GitHub.
- Rekomendasi: **GitHub App** (scope minimal, bisa dicabut) atau **deploy key** khusus repo ini.
- ❓ Anda yang buat & pasang. **Jangan kirim token di chat** — cukup beri tahu mekanismenya.

---

## 3. Chrome jadi template ✅ (bisa saya kerjakan)

- Header dominan **316/373** file identik; footer dominan **303/373** identik → jadikan **kanonik**.
- ⚠️ Tapi ada **drift**: **8 varian header**, **~19 varian footer** (di-export beda waktu; bukti drift lain:
  meta generator campur **WordPress 5.8.2 & 6.0.1**; logo campur `2021/06/...` vs `2022/07/cropped-cropped-cropped-...`).
- Variabel per-halaman di chrome (harus jadi slot, bukan hard-code): footer `<form action>` (= URL halaman) & `wpforms[post_id]`.
- ⚠️ Widget melayang (tombol WA/telepon/CS) ada **di chrome** dan gambarnya **hotlink blogspot** (lihat §7).
- **Siap saya hasilkan:** `_layout.html` = 1 header+footer kanonik dengan penanda `<!-- CONTENT -->`. Tinggal minta.

## 4. Pola URL ✅

| Tipe | Pola di repo | URL live |
|---|---|---|
| Artikel | `/{slug}.html` (flat di root) | `/{slug}` (tanpa `.html`; `.html`→308) |
| Kota — cuci | `/cuci-sarang-walet-{kota}.html` | idem tanpa `.html` |
| Kota — konsultan | `/konsultan-walet-{kota}.html` | idem |
| Kota — sarang | `/sarang-walet-{kota}.html` | idem |
| Halaman seksi | folder + `index.html` | `/{seksi}/` (trailing slash) |

Keanehan: (a) `.html`→extensionless **308** di setiap link internal repo (hop redirect); (b) `sarang-walet`
dobel makna — jasa (`/sarang-walet-{kota}`) **dan** seksi (`/sarang-walet/`); (c) folder seksi:
`cuci-sarang-walet/`, `konsultan-walet/`, `sarang-walet/`, `blog/`, `our-products/`, `tentang-kami/`,
`kontak-kami/`, `category/`, `author/`, `comments/`, `feed/`.

## 5. Config situs ✅

- **Analytics:** GTM `GTM-M47PB95` · AdSense `ca-pub-2869782316576155` · TikTok pixel · FB domain-verify `crz2k4kkl4bjmau6f0y7gwfg96o20w`.
- **Brand:** warna `#278575` (teal, link/aksen) & `#051145` (navy, heading/teks); font **Poppins** (body) + **Playfair Display** (heading).
- **Logo kanonik:** `/wp-content/uploads/2021/06/cropped-logo-budidayawalet-*.png` (abaikan varian `2022/07/cropped-cropped-cropped-...`).
- **Favicon:** `/wp-content/uploads/2021/06/cropped-favicon-*.png`.
- **Kontak:** WA **0852 3535 0662 (Fairuz)** = `wa.me/6285235350662`.
- **Menu ekosistem:** header menaut ke **parfumwalet.com** (cross-link jaringan → kandidat kontrol pusat).

## 6. Ekspor konten terstruktur ✅

- **Model artikel — 12 slot variabel:** `title`, `slug`, `meta description`, `canonical`, `robots`,
  blok OG (title/desc/url/image), Twitter Card, **JSON-LD BreadcrumbList**, `shortlink /?p=ID`, 2× oembed,
  `<h1 entry-title>`, thumbnail, body `entry-content`. (+ footer form action & post_id).
- **Dataset kota:** **103 kota unik**, tapi **BUKAN grid rapi** — cuci **102**, konsultan **101**, sarang **103**.
  → butuh flag keanggotaan per-jasa, bukan asumsi 103×3. Daftar 103 kota **siap saya kirim** (cocokkan dgn master ~103 dari sarangwalet).
- ⚠️ Body penuh sampah class Google Docs (`c0 c1 c7…`) → perlu dibersihkan saat ekspor.

## 7. Inventaris media

- **Lokal ter-track: 215 gambar** ✅ (folder `2020/10`, `2021/06`, `2021/07`, `2026/07`, `elementor`).
- ⚠️ **Soft-404: 180 URL unik `/wp-content/uploads/2022/…`** dirujuk **77 file** tapi **tak ada di repo**
  (server balas HTML+HTTP 200 = soft-404). → putuskan: cari file asli atau ganti.
- ⚠️ **Hotlink untuk rehome ke R2 — 19 URL blogspot unik:** 4 ikon UI (WA/telepon/CS di widget melayang chrome,
  **prioritas tinggi** — tombol WA tiap halaman bergantung link blogspot yang rapuh) + ~15 foto `sarang-walet-*` + 1 lain.
- ⚠️ **Mixed content:** 26 rujukan absolut `http://budidayawalet.net` (jadikan `https`).
- Tak ada host gambar eksternal lain.

## 8. Stabilitas URL / redirect ✅

- Slug **tidak diubah** (scope aditif). Halaman baru dari CMS: **emit link internal tanpa `.html`** agar sama
  dengan URL kanonik live (hindari hop 308). Jika kelak normalisasi link lama, siapkan peta **301**.

---

## Catatan kebersihan repo
- ⚠️ Ada `./.claude/worktrees/…` di disk (untracked, 0 file ter-track git) — salinan situs sisa worktree.
  Tak masuk repo, tapi sebaiknya dibersihkan lokal agar tak mengacau grep/scan.

## Ringkas untuk orkestrator
> Deploy ❓ (di balik Cloudflare-SIN, origin tak diketahui, **0 config di repo**, live pakai **URL tanpa .html** via rewrite — 4 pertanyaan di Blocker #1). Akses tulis = GitHub App/deploy key (Anda setup). Chrome **mayoritas konvergen** (316/373 header) tapi masih **8 varian** → kanonik siap diekstrak. Kota **103 (grid tak rata 102/101/103)**. Media: 215 lokal, **180 soft-404 (2022)**, **19 hotlink blogspot** (4 ikon chrome prioritas) untuk rehome R2, 26 mixed-content http. **Koreksi addendum:** budidaya JUGA punya hotlink blogspot (bukan hanya soft-404).
