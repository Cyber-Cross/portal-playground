#!/usr/bin/env python3
"""Build Portal-Playground-offline.html: one self-contained file, no internet, no ES modules.

Three.js and cannon-es are inlined as classic scripts (wrapped in functions that return their
exports), so the game runs when opened straight from disk in any browser, including Safari.
"""
import pathlib, re, urllib.request
here = pathlib.Path(__file__).parent
libs = [
    ('THREE', 'three', 'https://unpkg.com/three@0.160.0/build/three.module.js'),
    ('CANNON', 'cannon-es', 'https://unpkg.com/cannon-es@0.20.0/dist/cannon-es.js'),
]

def wrap(code, var):
    m = re.search(r'^export \{([^}]*)\};?[ \t]*$', code, re.M)
    assert m and code.count('\nexport ') == 1, f'unexpected export layout in {var}'
    pairs = []
    for n in (x.strip() for x in m.group(1).split(',')):
        if not n: continue
        a, _, b = n.partition(' as ')
        pairs.append(f'{b.strip()}: {a.strip()}' if b else a.strip())
    body = code[:m.start()] + code[m.end():]
    return f'var {var} = (function () {{\n"use strict";\n{body}\nreturn {{ {", ".join(pairs)} }};\n}})();\n'

bundle = ''
for var, name, url in libs:
    cache = here / 'vendor' / (name + '.js')
    if not cache.exists():
        cache.parent.mkdir(exist_ok=True)
        cache.write_bytes(urllib.request.urlopen(url).read())
    bundle += wrap(cache.read_text(), var)

src = (here / 'index.html').read_text()
game = re.search(r'<script type="module">(.*?)</script>', src, re.S)
code = re.sub(r"^import \* as (THREE|CANNON) from '[^']+';\n", '', game.group(1), flags=re.M)
assert 'import ' not in code.split('\n', 5)[1], 'leftover import'
out = src[:game.start()] + '<script>\n' + bundle + '</script>\n<script>\n(function () {\n"use strict";\n' + code + '\n})();\n</script>' + src[game.end():]
out = re.sub(r'<script type="importmap">.*?</script>\n?', '', out, count=1, flags=re.S)
(here / 'Portal-Playground-offline.html').write_text(out)
print('built', len(out) // 1024, 'KB')
