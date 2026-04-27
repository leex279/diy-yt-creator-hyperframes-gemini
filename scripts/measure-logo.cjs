// One-off: measure the rendered #top-banner-logo from the live preview server.
const path = require("path");
const puppeteer = require(path.join(
  process.env.USERPROFILE || process.env.HOME,
  ".npm-global",
  "node_modules",
  "puppeteer-mcp-server",
  "node_modules",
  "puppeteer"
));

(async () => {
  const url =
    process.argv[2] ||
    "http://localhost:3002/api/projects/claude-connectors-everyday-life/preview";
  const chromePath = path.join(
    process.env.USERPROFILE || process.env.HOME,
    ".cache",
    "hyperframes",
    "chrome",
    "chrome-headless-shell",
    "win64-131.0.6778.85",
    "chrome-headless-shell-win64",
    "chrome-headless-shell.exe"
  );
  const browser = await puppeteer.launch({ headless: "shell", executablePath: chromePath });
  const page = await browser.newPage();
  await page.setViewport({ width: 1080, height: 1920, deviceScaleFactor: 1 });
  await page.goto(url, { waitUntil: "domcontentloaded", timeout: 20000 });
  // Wait for the iframe to spawn after the SPA boots and reads the hash route
  for (let i = 0; i < 30; i++) {
    await new Promise((r) => setTimeout(r, 500));
    const count = await page.evaluate(() => document.querySelectorAll("iframe").length);
    if (count > 0) break;
  }

  const frameInfo = await page.evaluate(() => {
    const iframes = Array.from(document.querySelectorAll("iframe"));
    return iframes.map((f) => ({ src: f.src, name: f.name, id: f.id }));
  });
  console.error("[frames]", JSON.stringify(frameInfo));

  // If we loaded the file:// composition directly, there's no iframe. Measure the page.
  if (frameInfo.length === 0) {
    await page.waitForSelector("#top-banner-logo", { timeout: 5000 });
    await new Promise((r) => setTimeout(r, 500));
    const result = await page.evaluate(() => {
      const logo = document.getElementById("top-banner-logo");
      const banner = document.getElementById("top-banner");
      const root = document.getElementById("root");
      const dump = (el) => {
        if (!el) return null;
        const r = el.getBoundingClientRect();
        const cs = getComputedStyle(el);
        return {
          rect: { x: r.x, y: r.y, w: r.width, h: r.height },
          computed: {
            width: cs.width, height: cs.height, display: cs.display,
            position: cs.position, left: cs.left, right: cs.right,
            margin: cs.margin, textAlign: cs.textAlign, maxWidth: cs.maxWidth,
          },
        };
      };
      return {
        root: dump(root),
        banner: dump(banner),
        logo: dump(logo),
        logoSrc: logo?.getAttribute("src"),
        logoSrcResolved: logo?.src,
        logoNatural: logo ? { w: logo.naturalWidth, h: logo.naturalHeight } : null,
        logoComplete: logo?.complete,
      };
    });
    console.log(JSON.stringify(result, null, 2));
    await browser.close();
    return;
  }

  // Pick the first iframe whose src includes our project id
  const targetFrame = page
    .frames()
    .find((f) => f.url().includes("claude-connectors-everyday-life") || f.url().includes("/preview"));
  if (!targetFrame) {
    console.error("No matching iframe found. Frames:", page.frames().map((f) => f.url()));
    process.exit(2);
  }
  console.error("[picked]", targetFrame.url());

  // Wait for logo to be in the iframe document
  await targetFrame.waitForSelector("#top-banner-logo", { timeout: 10000 });
  await new Promise((r) => setTimeout(r, 500));

  const result = await targetFrame.evaluate(() => {
    const root = document.getElementById("root");
    const banner = document.getElementById("top-banner");
    const logo = document.getElementById("top-banner-logo");
    const dump = (el) => {
      if (!el) return null;
      const r = el.getBoundingClientRect();
      const cs = getComputedStyle(el);
      return {
        rect: { x: r.x, y: r.y, w: r.width, h: r.height },
        computed: {
          width: cs.width,
          height: cs.height,
          display: cs.display,
          position: cs.position,
          left: cs.left,
          right: cs.right,
          margin: cs.margin,
          textAlign: cs.textAlign,
          maxWidth: cs.maxWidth,
        },
      };
    };
    return {
      root: dump(root),
      banner: dump(banner),
      logo: dump(logo),
      logoSrc: logo ? logo.getAttribute("src") : null,
      logoNatural: logo ? { w: logo.naturalWidth, h: logo.naturalHeight } : null,
      logoComplete: logo ? logo.complete : null,
    };
  });

  console.log(JSON.stringify(result, null, 2));
  await browser.close();
})().catch((e) => {
  console.error("ERR:", e.message);
  process.exit(1);
});
