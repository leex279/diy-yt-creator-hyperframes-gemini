/**
 * Screenshot capture for dario-amodei-ai-writes-all-code
 * Takes screenshots at key timeline moments via the HyperFrames studio
 */
const puppeteer = require('puppeteer');
const path = require('path');
const fs = require('fs');

const STUDIO_URL = 'http://localhost:3011';
const SCREENSHOTS_DIR = path.join(__dirname, '..', 'screenshots');
const SLUG = 'dario-amodei-ai-writes-all-code';

async function sleep(ms) {
  return new Promise(r => setTimeout(r, ms));
}

async function main() {
  fs.mkdirSync(SCREENSHOTS_DIR, { recursive: true });

  const browser = await puppeteer.launch({
    headless: true,
    args: ['--no-sandbox', '--disable-setuid-sandbox', '--disable-gpu']
  });

  const page = await browser.newPage();
  await page.setViewport({ width: 1400, height: 900 });

  console.log('Navigating to studio...');
  await page.goto(STUDIO_URL, { waitUntil: 'networkidle2', timeout: 30000 });
  await sleep(3000);

  // Screenshot 1: Studio overview (shows composition loaded)
  const shot1 = path.join(SCREENSHOTS_DIR, `${SLUG}-studio-overview.png`);
  await page.screenshot({ path: shot1, fullPage: false });
  console.log('Shot 1: studio overview ->', shot1);

  // Try to find canvas/preview iframe
  const frames = page.frames();
  console.log('Frames found:', frames.length);

  // Screenshot 2: Full page to see composition name in sidebar
  const shot2 = path.join(SCREENSHOTS_DIR, `${SLUG}-composition-loaded.png`);
  await page.screenshot({ path: shot2, fullPage: true });
  console.log('Shot 2: composition loaded ->', shot2);

  // Look for the preview canvas area
  const canvasSelector = 'canvas, iframe, [data-composition-id]';
  try {
    await page.waitForSelector(canvasSelector, { timeout: 5000 });
    const el = await page.$(canvasSelector);
    if (el) {
      const shot3 = path.join(SCREENSHOTS_DIR, `${SLUG}-canvas-element.png`);
      await el.screenshot({ path: shot3 });
      console.log('Shot 3: canvas element ->', shot3);
    }
  } catch (e) {
    console.log('Canvas selector not found:', e.message);
  }

  // Check page title and content
  const title = await page.title();
  console.log('Page title:', title);

  const bodyText = await page.evaluate(() => document.body.innerText.slice(0, 500));
  console.log('Body text preview:', bodyText);

  await browser.close();
  console.log('Done.');
}

main().catch(err => {
  console.error('Screenshot script failed:', err);
  process.exit(1);
});
