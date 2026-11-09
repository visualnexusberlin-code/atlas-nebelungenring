"""Construye public/anillo/index.html: un único archivo sin peticiones a terceros.
Uso: python3 src/anillo/build.py   (desde la raíz del repositorio)"""
import base64, pathlib
H = pathlib.Path(__file__).resolve().parent
F = H / 'vendor' / 'fonts'
OUT = H.parents[1] / 'public' / 'anillo' / 'index.html'
b64 = lambda p: base64.b64encode(p.read_bytes()).decode()
def face(fam, file, w='400', st='normal', disp='swap'):
    return f'@font-face{{font-family:"{fam}";font-style:{st};font-weight:{w};font-display:{disp};src:url(data:font/woff2;base64,{b64(F/file)}) format("woff2")}}\n'
css = ''
for w, st in [('300','normal'),('400','normal'),('500','normal'),('400','italic'),('300','italic')]:
    css += face('Cormorant Garamond', f'cormorant-garamond-latin-{w}-{st}.woff2', w, st)
for w, st in [('400','normal'),('500','normal'),('400','italic')]:
    css += face('Instrument Sans', f'instrument-sans-latin-{w}-{st}.woff2', w, st)
for w in ('400','500'):
    css += face('IBM Plex Mono', f'ibm-plex-mono-latin-{w}-normal.woff2', w)
css += face('Noto Sans Runic', 'noto-sans-runic-runic-400-normal.woff2')
css += f'@font-face{{font-family:"Noto Music";font-weight:400;font-display:block;src:url(data:font/woff2;base64,{b64(H/"data"/"notomusic-sub.woff2")}) format("woff2")}}\n'
three = (H/'vendor'/'three.min.js').read_text(encoding='utf8').replace('</script', '<\\/script')
src = (H/'ring.src.html').read_text(encoding='utf8')
out = (src.replace('/*FONTS*/', css, 1).replace('/*THREE*/', three, 1)
          .replace('/*GEO*/', (H/'data'/'geo.json').read_text(), 1)
          .replace('/*PLATES*/', (H/'data'/'plates.json').read_text(), 1))
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(out, encoding='utf8')
print(f'{OUT} · {len(out)/1e6:.2f} MB')
