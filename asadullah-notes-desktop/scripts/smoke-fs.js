const { app, BrowserWindow } = require('electron');
require('../main.js'); const fs = require('fs');
app.disableHardwareAcceleration();
app.whenReady().then(async () => {
  await new Promise(r => setTimeout(r, 4000));
  const w = BrowserWindow.getAllWindows()[0], run = c => w.webContents.executeJavaScript(c), wait = ms => new Promise(r => setTimeout(r, ms));
  await run("authGuest()"); await wait(2500);
  const res = { btnVisible: await run("getComputedStyle(document.getElementById('fsBtn')).display"), before: w.isFullScreen() };
  fs.writeFileSync(process.env.OUT + '/fs-before.png', (await w.webContents.capturePage()).toPNG());
  await run("document.getElementById('fsBtn').click()"); await wait(2000);
  res.afterClick = w.isFullScreen(); res.icon = await run("document.getElementById('fsBtn').firstChild.className");
  w.webContents.sendInputEvent({ type: 'keyDown', keyCode: 'F11' }); await wait(1500);
  res.afterF11 = w.isFullScreen();
  console.log('FS', JSON.stringify(res)); app.quit();
});
