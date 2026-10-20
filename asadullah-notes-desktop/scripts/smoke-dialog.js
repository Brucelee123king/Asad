// Checks the styled "Leave this test?" dialog (back button + All Tests) in the real app and saves screenshots.
const { app, BrowserWindow } = require('electron');
require('../main.js');
const fs = require('fs');
app.disableHardwareAcceleration();
app.whenReady().then(async () => {
  await new Promise(r => setTimeout(r, 4000));
  const w = BrowserWindow.getAllWindows()[0];
  const errors = []; w.webContents.on('console-message', (e, l, m) => { if (l >= 3) errors.push(m); });
  const run = c => w.webContents.executeJavaScript(c);
  const wait = ms => new Promise(r => setTimeout(r, ms));
  const res = {};
  await run("authGuest()"); await run("openSec('o')"); await run("selectTest('1-50')");
  await run("document.getElementById('start-quiz-btn').click()"); await wait(500);
  const shown = () => run("!document.getElementById('modal-an-confirm').classList.contains('hidden')");
  await run("document.getElementById('backBtn').click()"); await wait(400);
  res.backShowsModal = await shown(); res.native = 'none'; await wait(2500);
  fs.writeFileSync(process.env.OUT + '/dialog-light.png', (await w.webContents.capturePage()).toPNG());
  await run("document.getElementById('anc-cancel').click()"); await wait(200);
  res.afterStay = { modalHidden: !(await shown()), quizActive: await run('quizActive') };
  await run("document.documentElement.classList.add('dark')");
  await run("showSelect()"); await wait(2500);
  res.allTestsShowsModal = await shown();
  fs.writeFileSync(process.env.OUT + '/dialog-dark.png', (await w.webContents.capturePage()).toPNG());
  await run("document.getElementById('anc-ok').click()"); await wait(400);
  res.afterLeave = { quizActive: await run('quizActive'), selectVisible: await run("!document.getElementById('view-select').classList.contains('hidden')") };
  console.log('DIALOG', JSON.stringify(res), 'ERRORS', JSON.stringify(errors)); app.quit();
});
