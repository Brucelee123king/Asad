"""Rebuild the original PDF exactly: every page is a 632x900 pt full-page JPEG.
Usage: python3 rebuild_exact.py [output.pdf]   (needs: pip install reportlab)
Page images live in ./pages/p-000.jpg ... p-300.jpg (keep this folder with the script).
"""
import glob, os, sys
from reportlab.pdfgen import canvas

W, H = 632, 900
here = os.path.dirname(os.path.abspath(__file__))
out = sys.argv[1] if len(sys.argv) > 1 else os.path.join(here, "rebuilt.pdf")
images = sorted(glob.glob(os.path.join(here, "pages", "p-*.jpg")))
c = canvas.Canvas(out, pagesize=(W, H))
for img in images:
    c.drawImage(img, 0, 0, width=W, height=H)
    c.showPage()
c.save()
print(f"Wrote {out} with {len(images)} pages")
