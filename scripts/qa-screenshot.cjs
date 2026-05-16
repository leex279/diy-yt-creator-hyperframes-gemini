// Phase QA — capture each phase's mid-point as a PNG so a human can review every
// frame in one glance instead of scrubbing a render. Uses the local HTML directly
// (file://) for deterministic capture and seeks the GSAP timeline to specific
// time samples.
const puppeteer = require('puppeteer-core');
const path = require('path');

const CHROME = process.env.CHROME_PATH;
const OUT_DIR = process.env.OUT_DIR;
const PROJECT_DIR = process.env.PROJECT_DIR;

const SAMPLES = [
  { name: 'p9-pre-endcard',  t: 154.5 },
  { name: 'endcard-mid',     t: 158.5 },
  { name: 'endcard-final',   t: 160.7 }
];

(async () => {
  const browser = await puppeteer.launch({
    executablePath: CHROME,
    headless: 'new',
    args: ['--no-sandbox', '--disable-dev-shm-usage', '--enable-features=CanvasDrawElement'],
    defaultViewport: { width: 1080, height: 1920, deviceScaleFactor: 1 }
  });
  try {
    const page = await browser.newPage();
    const compUrl = process.env.STATIC_URL || 'http://localhost:8765/index.html';
    console.log('loading', compUrl);
    page.on('console', m => console.log('  page:', m.type(), m.text()));
    page.on('pageerror', e => console.log('  pageerror:', e.message));
    page.on('requestfailed', r => console.log('  req-failed:', r.url(), r.failure().errorText));
    await page.goto(compUrl, { waitUntil: 'networkidle2', timeout: 60000 });
    const diag = await page.evaluate(() => ({
      hasGsap: typeof gsap !== 'undefined',
      hasWindowTl: typeof window.__timelines !== 'undefined',
      mainKeys: window.__timelines ? Object.keys(window.__timelines) : []
    }));
    console.log('diagnostic:', JSON.stringify(diag));
    if (!diag.hasWindowTl || !diag.mainKeys.includes('main')) {
      throw new Error('timeline not registered: ' + JSON.stringify(diag));
    }
    for (const s of SAMPLES) {
      await page.evaluate((t) => {
        const tl = window.__timelines.main;
        tl.pause();
        tl.seek(t);
      }, s.t);
      await new Promise(r => setTimeout(r, 400));
      const out = path.join(OUT_DIR, `${s.name}.png`);
      await page.screenshot({ path: out, clip: { x: 0, y: 0, width: 1080, height: 1920 } });
      console.log('captured', out, 'at', s.t + 's');
    }
  } finally {
    await browser.close();
  }
})();
