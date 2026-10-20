const { app, BrowserWindow, ipcMain, protocol, net, shell, Menu } = require('electron');
const path = require('path');
const fs = require('fs');
const { pathToFileURL } = require('url');

protocol.registerSchemesAsPrivileged([
  { scheme: 'app', privileges: { standard: true, secure: true, supportFetchAPI: true } }
]);

const SRC = path.join(__dirname, 'src');
let storeFile;
let store = {};
let writeTimer = null;

function loadStore() {
  storeFile = path.join(app.getPath('userData'), 'user-data.json');
  try {
    store = JSON.parse(fs.readFileSync(storeFile, 'utf8')) || {};
  } catch (e) {
    // missing or corrupted: keep a copy of a corrupted file and start clean
    try { if (fs.existsSync(storeFile)) fs.renameSync(storeFile, storeFile + '.corrupt-' + Date.now()); } catch (_) {}
    store = {};
  }
}
function flushStore() {
  clearTimeout(writeTimer); writeTimer = null;
  try {
    const tmp = storeFile + '.tmp';
    fs.writeFileSync(tmp, JSON.stringify(store));
    fs.renameSync(tmp, storeFile);
  } catch (e) { console.error('save failed', e); }
}

ipcMain.on('store:load', (e) => { e.returnValue = store; });
ipcMain.on('store:set', (e, k, v) => {
  if (typeof k !== 'string') return;
  if (v === null) delete store[k]; else store[k] = String(v);
  if (!writeTimer) writeTimer = setTimeout(flushStore, 400);
});

ipcMain.on('win:fullscreen', (e) => {
  const w = BrowserWindow.fromWebContents(e.sender);
  if (w) w.setFullScreen(!w.isFullScreen());
});

function createWindow() {
  const win = new BrowserWindow({
    width: 1280, height: 840, minWidth: 900, minHeight: 600,
    title: 'Asadullah Notes', backgroundColor: '#f8fafc', show: false,
    icon: path.join(__dirname, 'build', 'icon.ico'),
    webPreferences: {
      preload: path.join(__dirname, 'preload.js'),
      nodeIntegration: false, contextIsolation: true, sandbox: false, webSecurity: true
    }
  });
  Menu.setApplicationMenu(null);
  win.once('ready-to-show', () => win.show());
  // F11 toggles full screen (the menu bar is hidden, so there is no built-in shortcut)
  win.webContents.on('before-input-event', (e, input) => {
    if (input.type === 'keyDown' && input.key === 'F11') { e.preventDefault(); win.setFullScreen(!win.isFullScreen()); }
  });
  const sendFs = () => { if (!win.isDestroyed()) win.webContents.send('win:fs', win.isFullScreen()); };
  win.on('enter-full-screen', sendFs); win.on('leave-full-screen', sendFs);
  win.webContents.on('will-navigate', (e, url) => { if (!url.startsWith('app://')) e.preventDefault(); });
  win.webContents.setWindowOpenHandler(({ url }) => {
    if (/^https:\/\//.test(url)) shell.openExternal(url);
    return { action: 'deny' };
  });
  win.loadURL('app://local/index.html');
}

const gotLock = app.requestSingleInstanceLock();
if (!gotLock) app.quit();
else app.whenReady().then(() => {
  loadStore();
  protocol.handle('app', (req) => {
    const rel = decodeURIComponent(new URL(req.url).pathname).replace(/^\/+/, '') || 'index.html';
    const file = path.normalize(path.join(SRC, rel));
    if (!file.startsWith(SRC + path.sep)) return new Response('Forbidden', { status: 403 });
    return net.fetch(pathToFileURL(file).toString());
  });
  createWindow();
  app.on('activate', () => { if (!BrowserWindow.getAllWindows().length) createWindow(); });
});
app.on('second-instance', () => { const w = BrowserWindow.getAllWindows()[0]; if (w) { if (w.isMinimized()) w.restore(); w.focus(); } });
app.on('before-quit', () => { if (writeTimer) flushStore(); });
app.on('window-all-closed', () => app.quit());
