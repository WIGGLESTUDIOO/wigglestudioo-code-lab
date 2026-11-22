# Can You Guess What This Code Draws?  -  WiggleStudioo
# Run:  pip install pillow numpy   then   python guess_the_code.py
# It saves 11 pictures (round01_circle.png ...) in the same folder.
# Note: the video shows short, simplified lines. This is the full runnable version.
import math, random
import numpy as np
from math import cos, sin, radians, pi, exp, log
from PIL import Image, ImageDraw

W = H = 600
cx, cy = W / 2, H / 2
BG = (12, 10, 30)

def canvas():
    img = Image.new("RGB", (W, H), BG)
    return img, ImageDraw.Draw(img)

def dot(d, x, y, r=3, color=(255, 170, 215)):
    d.ellipse((x - r, y - r, x + r, y + r), fill=color)

def save(img, n, name):
    img.save(f"round{n:02d}_{name}.png")
    print("saved", f"round{n:02d}_{name}.png")

# 1. circle
img, d = canvas()
for deg in range(360):
    x = cx + 200 * cos(radians(deg))
    y = cy + 200 * sin(radians(deg))
    dot(d, x, y)
save(img, 1, "circle")

# 2. spiral
img, d = canvas()
for i in range(900):
    r = i * 0.32
    a = i * 0.1
    dot(d, cx + r * cos(a), cy + r * sin(a), 2.5, (150, 220, 255))
save(img, 2, "spiral")

# 3. flower
img, d = canvas()
for deg in range(720):
    a = radians(deg)
    r = 230 * cos(6 * a)
    dot(d, cx + r * cos(a), cy + r * sin(a), 2.5, (255, 140, 200))
save(img, 3, "flower")

# 4. stars
img, d = canvas()
for i in range(300):
    x = random.uniform(0, W)
    y = random.uniform(0, H)
    size = random.uniform(1, 4)
    dot(d, x, y, size / 2 + .5, (255, 245, 220))
save(img, 4, "stars")

# 5. waves
img, d = canvas()
cols = [(90, 60, 200), (80, 100, 220), (70, 140, 230), (80, 180, 235), (110, 215, 240), (170, 240, 250)]
for k in range(6):
    for x in range(W):
        y = 250 + k * 45 + 20 * sin(x * .02 + k)
        d.line((x, y, x, H), fill=cols[k])
save(img, 5, "waves")

# 6. mandala
img, d = canvas()
def petal(angle, size, color):
    pts = []
    for t in range(0, 361, 10):
        u = radians(t)
        px, py = size * (1 + cos(u)) / 2, size * .22 * sin(u)
        pts.append((cx + px * cos(angle) - py * sin(angle), cy + px * sin(angle) + py * cos(angle)))
    d.polygon(pts, outline=color)
for ring in range(6, 0, -1):
    for k in range(12):
        angle = k * 2 * pi / 12 + ring * .13
        petal(angle, 60 + ring * 38, (255, 120 + ring * 20, 200))
save(img, 6, "mandala")

# 7. tree
img, d = canvas()
def branch(x, y, a, L, depth):
    if depth == 0:
        return
    x2 = x + L * cos(a)
    y2 = y - L * sin(a)
    d.line((x, y, x2, y2), fill=(120 + depth * 15, 255 - depth * 12, 170), width=max(1, depth))
    branch(x2, y2, a + .4, L * .75, depth - 1)
    branch(x2, y2, a - .4, L * .75, depth - 1)
branch(cx, H - 20, pi / 2, 120, 9)
save(img, 7, "tree")

# 8. snowflake
img, d = canvas()
def arm(x, y, a, length, depth):
    if depth == 0:
        return
    x2, y2 = x + length * cos(a), y + length * sin(a)
    d.line((x, y, x2, y2), fill=(190, 230, 255), width=2)
    mx, my = x + length * .55 * cos(a), y + length * .55 * sin(a)
    arm(mx, my, a + radians(60), length / 2.4, depth - 1)
    arm(mx, my, a - radians(60), length / 2.4, depth - 1)
    arm(x2, y2, a, length / 2.6, depth - 1)
for k in range(6):
    arm(cx, cy, radians(60 * k), 250, 4)
save(img, 8, "snowflake")

# 9. galaxy
n = 90000
r = np.random.exponential(.28, n)
arm_off = np.random.randint(0, 2, n) * pi
theta = 3.4 * np.log(1 + 3.2 * r) + arm_off + np.random.normal(0, .12, n)
x = r * np.cos(theta)
y = r * np.sin(theta) * .46
mix = np.exp(-5 * r)[:, None]
col = np.array([110, 150, 255]) * (1 - mix) + np.array([255, 215, 130]) * mix
acc = np.zeros((H, W, 3))
px = (cx + x * 300).astype(int)
py = (cy + y * 300).astype(int)
ok = (px >= 0) & (px < W) & (py >= 0) & (py < H)
np.add.at(acc, (py[ok], px[ok]), col[ok] * .6)
img = Image.fromarray(np.clip(acc + np.array(BG), 0, 255).astype(np.uint8))
save(img, 9, "galaxy")

# 10. lightning
img, d = canvas()
def bolt(p, q, depth, spread):
    if depth == 0:
        d.line((p[0], p[1], q[0], q[1]), fill=(220, 235, 255), width=2)
        return
    mid = ((p[0] + q[0]) / 2 + random.uniform(-spread, spread), (p[1] + q[1]) / 2 + random.uniform(-spread / 4, spread / 4))
    bolt(p, mid, depth - 1, spread / 2)
    bolt(mid, q, depth - 1, spread / 2)
bolt((cx, 20), (cx + 40, H - 20), 8, 160)
save(img, 10, "lightning")

# 11. aurora
yy, xx = np.mgrid[0:H, 0:W].astype(float)
im = np.zeros((H, W, 3)) + np.array(BG, float)
palette = [(60, 255, 170), (80, 230, 200), (120, 190, 255), (170, 140, 255), (230, 120, 220)]
for k in range(5):
    base = 150 + 26 * k + 44 * np.sin(xx / 80 + k)
    dd = (base - yy) / 170
    glow = np.exp(-dd * 2) * (dd > 0)
    im += glow[..., None] * np.array(palette[k]) * .55
img = Image.fromarray(np.clip(im, 0, 255).astype(np.uint8))
save(img, 11, "aurora")
