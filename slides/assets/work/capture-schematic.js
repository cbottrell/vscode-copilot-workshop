const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({
    headless: true,
    executablePath: '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
  });
  const page = await browser.newPage({
    viewport: { width: 1600, height: 900 },
    deviceScaleFactor: 1,
    colorScheme: 'light',
  });
  await page.goto('file:///Users/cbottrell/Documents/Codex/2026-07-19/mak/work/whole-token-prediction-preview.html');
  await page.waitForSelector('#whole-token-prediction #whole-network-nodes circle');
  await page.locator('#whole-token-prediction').screenshot({
    path: '/Users/cbottrell/Documents/Codex/2026-07-19/mak/outputs/llm-next-token-schematic.png',
  });
  await browser.close();
})();
