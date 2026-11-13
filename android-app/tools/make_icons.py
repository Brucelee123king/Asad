#!/usr/bin/env python3
"""Legacy launcher PNGs (Android 7.x) drawn from the same geometry as res/drawable/ic_logo.xml (adaptive icon is a vector)."""
import os
from PIL import Image, ImageDraw
RES = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'app', 'src', 'main', 'res')
SIZES = {'mdpi': 48, 'hdpi': 72, 'xhdpi': 96, 'xxhdpi': 144, 'xxxhdpi': 192}
def bezier(p0, p1, p2, p3, n=24):
    out = []
    for i in range(n + 1):
        t = i / n; u = 1 - t
        out.append((u**3*p0[0] + 3*u*u*t*p1[0] + 3*u*t*t*p2[0] + t**3*p3[0], u**3*p0[1] + 3*u*u*t*p1[1] + 3*u*t*t*p2[1] + t**3*p3[1]))
    return out
def draw(size, round_):
    S = 4  # supersample
    n = size * S; k = n / 108.0
    img = Image.new('RGBA', (n, n), (0, 0, 0, 0)); d = ImageDraw.Draw(img)
    # background: indigo, light diagonal gradient
    bg = Image.new('RGBA', (n, n)); bd = ImageDraw.Draw(bg)
    for y in range(n):
        t = y / n
        bd.line([(0, y), (n, y)], fill=(int(0x4F * (0.85 + 0.15 * t)), int(0x46 * (0.85 + 0.15 * t)), int(0xE5 * (0.9 + 0.1 * t)), 255))
    mask = Image.new('L', (n, n), 0); md = ImageDraw.Draw(mask)
    if round_: md.ellipse([0, 0, n - 1, n - 1], fill=255)
    else: md.rounded_rectangle([0, 0, n - 1, n - 1], radius=int(n * 0.22), fill=255)
    img.paste(bg, (0, 0), mask)
    P = lambda pts: [(x * k, y * k) for x, y in pts]
    white, gold = (255, 255, 255, 255), (0xFB, 0xBF, 0x24, 255)
    d.polygon(P([(54, 30), (88, 45), (54, 60), (20, 45)]), fill=white)
    body = [(34, 55), (34, 70)] + bezier((34, 70), (34, 77), (74, 77), (74, 70)) + [(74, 55), (54, 64)]
    d.polygon(P(body), fill=white)
    d.rectangle([82.8 * k, 47 * k, 85.2 * k, 66 * k], fill=gold)
    d.ellipse([(84 - 3.2) * k, (66 - 0.2) * k, (84 + 3.2) * k, (66 + 6.2) * k], fill=gold)
    return img.resize((size, size), Image.LANCZOS)
for dens, px in SIZES.items():
    folder = os.path.join(RES, 'mipmap-' + dens); os.makedirs(folder, exist_ok=True)
    draw(px, False).save(os.path.join(folder, 'ic_launcher.png'), optimize=True)
    draw(px, True).save(os.path.join(folder, 'ic_launcher_round.png'), optimize=True)
print('ok')
