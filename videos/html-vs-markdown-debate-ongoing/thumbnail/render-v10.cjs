/**
 * Render variant-10.html → variant-10.png at 1280×720.
 * Headless Chrome via puppeteer.
 */
const puppeteer = require('puppeteer');
const path = require('path');
const fs = require('fs');

(async () => {
  const dir = __dirname;
  const html = path.join(dir, 'variant-10.html');
  const out = path.join(dir, 'variant-10.png');
  if (!fs.existsSync(html)) { console.error('missing', html); process.exit(1); }

  // Use system Chrome (puppeteer-core has no bundled browser)
  const chromePaths = [
    'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
    'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe'
  ];
  const executablePath = chromePaths.find(p => fs.existsSync(p));
  if (!executablePath) { console.error('Chrome not found'); process.exit(1); }
  const browser = await puppeteer.launch({
    executablePath,
    headless: 'new',
    args: ['--no-sandbox', '--disable-setuid-sandbox']
  });
  const page = await browser.newPage();
  await page.setViewport({ width: 1280, height: 720, deviceScaleFactor: 1 });
  await page.goto('file:///' + html.replace(/\\/g, '/'), { waitUntil: 'networkidle0', timeout: 30000 });
  await page.evaluateHandle('document.fonts.ready');
  await new Promise(r => setTimeout(r, 1500));

  const el = await page.$('.thumb');
  if (el) {
    await el.screenshot({ path: out });
  } else {
    await page.screenshot({ path: out, clip: { x: 0, y: 0, width: 1280, height: 720 } });
  }
  console.log('wrote', out);
  await browser.close();
})();
