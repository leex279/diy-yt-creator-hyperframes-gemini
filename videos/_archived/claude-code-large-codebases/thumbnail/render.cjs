/**
 * render.cjs — Puppeteer renderer for claude-code-large-codebases thumbnails.
 * Usage: node videos/claude-code-large-codebases/thumbnail/render.cjs
 *
 * Renders variant-01.html through variant-10.html at 1280x720, then
 * contact-sheet.html at 1280x auto-height. PNGs land in the same directory.
 */

'use strict';

const path = require('path');
const fs = require('fs');

// Resolve puppeteer — try local node_modules first, then global
let puppeteer;
try {
  puppeteer = require(path.resolve(__dirname, '../../../node_modules/puppeteer'));
} catch (_) {
  try {
    puppeteer = require('puppeteer');
  } catch (e) {
    console.error('puppeteer not found. Run: npm install puppeteer (or pnpm add puppeteer)');
    process.exit(1);
  }
}

const THUMB_DIR = __dirname;
const VARIANTS = Array.from({ length: 15 }, (_, i) => `variant-${String(i + 1).padStart(2, '0')}`);

async function renderVariants(browser) {
  for (const name of VARIANTS) {
    const htmlPath = path.join(THUMB_DIR, `${name}.html`);
    const pngPath  = path.join(THUMB_DIR, `${name}.png`);

    if (!fs.existsSync(htmlPath)) {
      console.warn(`  SKIP ${name}.html — file not found`);
      continue;
    }

    const page = await browser.newPage();
    await page.setViewport({ width: 1280, height: 720, deviceScaleFactor: 1 });
    await page.goto(`file://${htmlPath}`, { waitUntil: 'networkidle0', timeout: 30000 });

    // Wait for web fonts (Google Fonts via @import) — poll until a known font is loaded
    await page.evaluate(() => document.fonts.ready);

    // Clip to the .thumb element (1280x720)
    const thumbEl = await page.$('.thumb');
    if (thumbEl) {
      await thumbEl.screenshot({ path: pngPath, type: 'png' });
    } else {
      await page.screenshot({ path: pngPath, clip: { x: 0, y: 0, width: 1280, height: 720 } });
    }

    await page.close();
    const size = Math.round(fs.statSync(pngPath).size / 1024);
    console.log(`  [OK] ${name}.png  (${size} KB)`);
  }
}

async function renderContactSheet(browser) {
  const htmlPath = path.join(THUMB_DIR, 'contact-sheet.html');
  const pngPath  = path.join(THUMB_DIR, 'contact-sheet.png');

  const page = await browser.newPage();
  // Width matches body width (1280px); height auto
  await page.setViewport({ width: 1280, height: 900, deviceScaleFactor: 1 });
  await page.goto(`file://${htmlPath}`, { waitUntil: 'networkidle0', timeout: 30000 });
  await page.evaluate(() => document.fonts.ready);

  // Full-page screenshot so we capture the whole grid however tall it is
  await page.screenshot({ path: pngPath, fullPage: true });
  await page.close();
  const size = Math.round(fs.statSync(pngPath).size / 1024);
  console.log(`  [OK] contact-sheet.png  (${size} KB)`);
}

(async () => {
  console.log('Launching Puppeteer...');
  const browser = await puppeteer.launch({
    headless: true,
    executablePath: 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
    args: ['--no-sandbox', '--disable-setuid-sandbox', '--font-render-hinting=none'],
  });

  console.log('\nRendering variants:');
  await renderVariants(browser);

  console.log('\nRendering contact sheet:');
  await renderContactSheet(browser);

  await browser.close();
  console.log('\nDone. Check videos/claude-code-large-codebases/thumbnail/ for PNGs.');
})();
