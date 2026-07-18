#!/usr/bin/env bash
# Jalankan dari dalam folder repo BudidayaWalet.net
sed -i 's#<meta name="robots" content="noindex, nofollow">#<meta name="robots" content="follow, index, max-snippet:-1, max-video-preview:-1, max-image-preview:large">#g' *.html
n=$(grep -lE 'content="noindex, nofollow"' *.html 2>/dev/null | wc -l)
echo "Selesai. Sisa halaman noindex: $n (harus 0)."
