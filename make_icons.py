"""
Generates icon-192.png and icon-512.png (square app icons for the PWA
manifest) from the TJC logo, padded onto a white square canvas.

Run once, or again if the logo changes:
    python make_icons.py
"""
import os
from PIL import Image

FOLDER = os.path.dirname(os.path.abspath(__file__))
LOGO = os.path.join(FOLDER, "Screenshot 2026-06-21 082454.png")

logo = Image.open(LOGO).convert("RGBA")


def make_icon(size, pad_ratio=0.12):
    canvas = Image.new("RGBA", (size, size), (255, 255, 255, 255))
    pad = int(size * pad_ratio)
    avail_w = size - pad * 2
    avail_h = size - pad * 2
    ratio = min(avail_w / logo.width, avail_h / logo.height)
    new_w = int(logo.width * ratio)
    new_h = int(logo.height * ratio)
    resized = logo.resize((new_w, new_h), Image.LANCZOS)
    x = (size - new_w) // 2
    y = (size - new_h) // 2
    canvas.paste(resized, (x, y), resized)
    return canvas.convert("RGB")


make_icon(192).save(os.path.join(FOLDER, "icon-192.png"))
make_icon(512).save(os.path.join(FOLDER, "icon-512.png"))
print("icons created")
