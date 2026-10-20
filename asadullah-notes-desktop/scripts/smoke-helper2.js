const { app, BrowserWindow } = require('electron');
require('../main.js'); const fs = require('fs');
app.disableHardwareAcceleration();
app.whenReady().then(async () => {
  await new Promise(r => setTimeout(r, 4000));
  const w = BrowserWindow.getAllWindows()[0], run = c => w.webContents.executeJavaScript(c), wait = ms => new Promise(r => setTimeout(r, ms));
  const errors = []; w.webContents.on('console-message', (e, l, m) => { if (l >= 3) errors.push(m); });
  const res = {};
  await run("authGuest()"); await wait(1200); await run("openSec('o')"); await run("selectTest('1-50')");
  await run("document.getElementById('start-quiz-btn').click()"); await wait(800);
  await run("document.getElementById('anHelpBtn').click()"); await wait(1200);
  res.chipsBeforeAnswer = await run("document.querySelectorAll('#anChips button').length");
  await run("document.getElementById('anTabOff').click()"); await wait(500);
  await run("selectOption(0, quizData[0].correct)"); await wait(800);
  res.chips = await run("[...document.querySelectorAll('#anChips button')].map(b=>b.textContent)");
  const labels = res.chips; res.out = {};
  for (let i = 0; i < labels.length; i++) { await run("document.querySelectorAll('#anChips button')[" + i + "].click()"); await wait(200);
    res.out[labels[i]] = (await run("document.querySelector('#anMsgs').lastElementChild.innerText")).slice(0, 90).replace(/\n/g, ' | '); }
  await wait(2000); fs.writeFileSync(process.env.OUT + '/helper-q.png', (await w.webContents.capturePage()).toPNG());
  await run("nextQuestion()"); await wait(500);
  res.chipsAfterNext = await run("document.querySelector('#anChips').innerText.slice(0,40)");
  console.log('H2', JSON.stringify(res, null, 1), 'ERRORS', JSON.stringify(errors)); app.quit();
});
