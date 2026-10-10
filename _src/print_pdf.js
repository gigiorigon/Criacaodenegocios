// Imprime o HTML combinado dos anexos em PDF com o Chromium do Playwright.
const path = require('path');
const { chromium } = require(process.env.PLAYWRIGHT_PATH || 'playwright');
(async () => {
  const root = path.resolve(__dirname, '..');
  const src = process.argv[2] || path.join(root, '_src', '_anexos_pdf.html');
  const b = await chromium.launch();
  const p = await b.newPage();
  await p.goto('file://' + src);
  await p.pdf({
    path: path.join(root, 'assets', 'Anexos_Giovani_Rigon_ADM0150.pdf'),
    format: 'A4', printBackground: true,
    margin: { top: '18mm', bottom: '18mm', left: '16mm', right: '16mm' },
    displayHeaderFooter: true, headerTemplate: '<span></span>',
    footerTemplate: '<div style="font-size:8px;width:100%;text-align:center;color:#777">Giovani Machado Rigon · 16/0070686 · Anexos · <span class="pageNumber"></span>/<span class="totalPages"></span></div>',
  });
  await b.close();
})();
