"""Render thumbnail.html → thumbnail.png at exactly 1280×720 via Playwright."""
import os
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
HTML = HERE / "thumbnail.html"
OUT = HERE / "thumbnail.png"

assert HTML.exists(), f"missing {HTML}"

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    context = browser.new_context(
        viewport={"width": 1280, "height": 720},
        device_scale_factor=1,
    )
    page = context.new_page()
    file_url = HTML.as_uri()
    page.goto(file_url, wait_until="networkidle")
    # Give web-fonts a moment to settle even after networkidle
    page.wait_for_timeout(800)
    page.screenshot(
        path=str(OUT),
        full_page=False,
        clip={"x": 0, "y": 0, "width": 1280, "height": 720},
        omit_background=False,
        type="png",
    )
    browser.close()

print(f"OK -> {OUT}")
print(f"size: {OUT.stat().st_size} bytes")
