const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch({ args: ['--no-sandbox', '--disable-setuid-sandbox'] });
  const page = await browser.newPage();
  await page.goto('https://record.streamlit.app', { waitUntil: 'networkidle2' });
  await page.screenshot({ path: 'screenshot.png' });
  await browser.close();
})();
