# Aktifkan index 39 artikel: ubah noindex,nofollow -> follow,index
# Jalankan di folder repo BudidayaWalet.net:  python aktifkan-index.py
import glob
OLD = '<meta name="robots" content="noindex, nofollow">'
NEW = '<meta name="robots" content="follow, index, max-snippet:-1, max-video-preview:-1, max-image-preview:large">'
n = 0
for f in glob.glob('*.html'):
    s = open(f, encoding='utf-8', newline='').read()
    if OLD in s:
        open(f, 'w', encoding='utf-8', newline='').write(s.replace(OLD, NEW))
        n += 1
print("Selesai. %d file diubah dari noindex ke index." % n)
sisa = sum('content="noindex' in open(f, encoding='utf-8', errors='ignore').read() for f in glob.glob('*.html'))
print("Sisa halaman noindex:", sisa, "(harus 0)")
