#!/usr/bin/env python3
"""Make a logo-library tile to spec.
Usage: make_tile.py SOURCE OUT_BASENAME
SOURCE: an https URL or local path to an .svg, .png, .jpg or .webp file.
OUT_BASENAME: kebab-case name without extension, e.g. etihad-airways.
Writes /home/claude/logo/out/logos/OUT.png (square, white ground, >=400px) and,
for SVG sources, /home/claude/logo/out/svg/OUT.svg. Refuses (exit 2) to write:
- raster sources whose logo, after trimming, is under 400px on its long side (no upscaling);
- a result that is blank or near-white (white-only logos): find a dark variant instead;
- a name that already exists in the library manifest or in out/logos.
Prints one JSON line with the result.
"""
import sys, os, io, json, csv, re, subprocess, urllib.request
from PIL import Image, ImageOps
ROOT='/home/claude/logo'
UA={'User-Agent':'ISOC-logo-library/1.0 (will.hardie@isoc.com)'}
def fail(msg): print(json.dumps({'ok':False,'error':msg})); sys.exit(2)
src,name=sys.argv[1],sys.argv[2]
if not re.fullmatch(r'[a-z0-9]+(-[a-z0-9]+)*',name): fail('name must be kebab-case')
taken={r['file'][:-4] for r in csv.DictReader(open(f'{ROOT}/manifest-new3.csv',encoding='utf-8-sig'))}
if name in taken or os.path.exists(f'{ROOT}/out/logos/{name}.png'): fail(f'name {name} already taken')
if src.startswith('http'):
    req=urllib.request.Request(src,headers=UA)
    data=urllib.request.urlopen(req,timeout=60).read()
else: data=open(src,'rb').read()
is_svg=src.lower().split('?')[0].endswith('.svg') or data[:1000].lstrip().startswith((b'<svg',b'<?xml')) and b'<svg' in data[:5000]
if is_svg:
    import cairosvg
    png=cairosvg.svg2png(bytestring=data,output_width=1600)
    im=Image.open(io.BytesIO(png)); vector=True
else:
    im=Image.open(io.BytesIO(data)); vector=False
im=im.convert('RGBA')
bg=Image.new('RGBA',im.size,(255,255,255,255)); bg.alpha_composite(im); im=bg.convert('RGB')
# trim near-white margins
inv=ImageOps.invert(im.convert('L')).point(lambda p:255 if p>12 else 0)
box=inv.getbbox()
if not box: fail('image is blank or white-only on white; find a dark or colour variant')
im=im.crop(box); w,h=im.size
if not vector and max(w,h)<400: fail(f'raster logo too small after trim ({w}x{h}); no upscaling allowed')
if vector:
    s=900/max(w,h); im=im.resize((round(w*s),round(h*s)),Image.LANCZOS); w,h=im.size
side=max(400,round(max(w,h)*1.12))
canvas=Image.new('RGB',(side,side),(255,255,255)); canvas.paste(im,((side-w)//2,(side-h)//2))
canvas.save(f'{ROOT}/out/logos/{name}.png',optimize=True)
if is_svg: open(f'{ROOT}/out/svg/{name}.svg','wb').write(data)
print(json.dumps({'ok':True,'png':f'out/logos/{name}.png','svg':is_svg,'size':side,'logo_px':[w,h]}))
