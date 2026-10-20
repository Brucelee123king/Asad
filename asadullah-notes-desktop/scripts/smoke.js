// Launches the real Electron app (under xvfb on Linux), clicks through a quiz and reports JS errors.
const { app, BrowserWindow } = require('electron');
require('../main.js');
const errors = [];
app.disableHardwareAcceleration();
app.whenReady().then(async () => {
  await new Promise(r => setTimeout(r, 4000));
  const w = BrowserWindow.getAllWindows()[0];
  w.webContents.on('console-message', (e, lvl, msg) => { if (lvl >= 3) errors.push(msg); });
  const run = (c) => w.webContents.executeJavaScript(c);
  const res = {};
  res.title = await run('document.title');
  res.tests = await run('Object.keys(ALL).length');
  res.questions = await run('Object.values(ALL).reduce((n,a)=>n+a.length,0)');
  await run("document.getElementById('auth') && authGuest()");
  await run("openSec('o')"); await run("selectTest('1-50')");
  await run("document.getElementById('start-quiz-btn').click()");
  res.quizActive = await run('quizActive');
  await run('selectOption(0, 0); nextQuestion(); selectOption(1, quizData[1].correct)');
  await run('executeSubmitQuiz()');
  res.score = await run("document.getElementById('result-score-text').textContent");
  res.fa = await run("getComputedStyle(document.querySelector('.fa-solid')).fontFamily");
  res.fonts = await run("Promise.all([...document.fonts].map(f=>f.load().then(()=>f.family+':'+f.status,()=>f.family+':error'))).then(a=>[...new Set(a)])");
  res.tailwind = await run("getComputedStyle(document.querySelector('header')).position");
  res.external = await run("performance.getEntriesByType('resource').map(r=>r.name).filter(n=>!n.startsWith('app://'))");
  res.ls = await run("Object.keys(localStorage)");
  console.log('SMOKE', JSON.stringify(res), 'ERRORS', JSON.stringify(errors));
  await new Promise(r => setTimeout(r, 900)); app.quit();
});
