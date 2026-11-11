#!/usr/bin/env python3
"""Build the single-file Caffeinity Experience.

Inlines everything in assets/ into src/template.html as data: URIs and writes
  index.html      a standalone page (open it directly, or serve it with GitHub Pages)
  dist/page.html  the same page without the <html>/<head>/<body> wrapper, for hosts that add their own
"""
import base64, json, pathlib

root = pathlib.Path(__file__).resolve().parent
MIME = {'.webp': 'image/webp', '.png': 'image/png', '.jpg': 'image/jpeg', '.mp4': 'video/mp4'}
imgs, vids = {}, {}
for f in sorted((root / 'assets').iterdir()):
    mime = MIME.get(f.suffix)
    if not mime:
        continue
    uri = 'data:%s;base64,%s' % (mime, base64.b64encode(f.read_bytes()).decode())
    (vids if mime.startswith('video') else imgs)[f.stem] = uri

page = (root / 'src' / 'template.html').read_text()
page = page.replace('__IMAGES__', json.dumps(imgs)).replace('__VIDEOS__', json.dumps(vids))
(root / 'dist').mkdir(exist_ok=True)
(root / 'dist' / 'page.html').write_text(page)
(root / 'index.html').write_text(
    '<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
    '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
    '<style>body{margin:0}</style>\n</head>\n<body>\n' + page + '\n</body>\n</html>\n')
print('built index.html (%.1f MB) from %d images, %d clips' % (len(page) / 1e6, len(imgs), len(vids)))
