const { app, BrowserWindow, ipcMain, protocol, net, shell, Menu, safeStorage } = require('electron');
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

// ---- AI helper (online tab): the key is stored encrypted in the user-data folder and never reaches the page ----
const AI_MODEL = 'claude-sonnet-5-5';
const AI_SYSTEM = 'You are the study helper inside Asadullah Notes, an MCQ practice app for Pakistani competitive and military-academy entry tests (PMA, Forces Academy, ISSB-style tests). Explain clearly and simply, step by step, and go deeper when the student asks for more detail. Answer in the language the student uses (English, Urdu, Hindi or Roman Urdu). For current affairs or office-holders, search the web and mention the date or source; say plainly when you are not sure. Keep answers focused.';
const keyFile = () => path.join(app.getPath('userData'), 'ai-key.bin');
function readKey() {
  try {
    const b = fs.readFileSync(keyFile());
    const t = b.slice(0, 1).toString(), body = b.slice(1);
    if (t === 'E') return safeStorage.decryptString(body);
    return body.toString('utf8');
  } catch (e) { return ''; }
}
function writeKey(k) {
  const enc = safeStorage.isEncryptionAvailable();
  fs.writeFileSync(keyFile(), Buffer.concat([Buffer.from(enc ? 'E' : 'P'), enc ? safeStorage.encryptString(k) : Buffer.from(k, 'utf8')]));
}
ipcMain.handle('ai:hasKey', () => !!readKey());
ipcMain.handle('ai:setKey', (e, k) => {
  k = String(k || '').trim();
  if (!/^sk-[A-Za-z0-9_\-]{20,}$/.test(k)) return { ok: false, error: 'That does not look like a valid API key.' };
  try { writeKey(k); return { ok: true }; } catch (err) { return { ok: false, error: 'Could not save the key.' }; }
});
ipcMain.handle('ai:clearKey', () => { try { fs.unlinkSync(keyFile()); } catch (e) {} return { ok: true }; });
const TEXT_TYPES = /^(text\/|application\/json)/;
function buildContent(msg) {
  const parts = [];
  let extra = '';
  (msg.attachments || []).slice(0, 5).forEach((a) => {
    const data = String(a.data || '');
    if (data.length > 14e6) return; // ~10 MB decoded
    if (/^image\/(png|jpeg|gif|webp)$/.test(a.type)) parts.push({ type: 'image', source: { type: 'base64', media_type: a.type, data } });
    else if (a.type === 'application/pdf') parts.push({ type: 'document', source: { type: 'base64', media_type: 'application/pdf', data } });
    else if (TEXT_TYPES.test(a.type) || /\.(txt|md|csv|json)$/i.test(a.name || '')) extra += '\n\n[File: ' + String(a.name).slice(0, 100) + ']\n' + Buffer.from(data, 'base64').toString('utf8').slice(0, 100000);
  });
  parts.push({ type: 'text', text: String(msg.text || '').slice(0, 20000) + extra });
  return parts;
}
async function callClaude(key, messages, withSearch) {
  const body = { model: AI_MODEL, max_tokens: 1800, system: AI_SYSTEM, messages };
  if (withSearch) body.tools = [{ type: 'web_search_20250305', name: 'web_search', max_uses: 5 }];
  const ctl = new AbortController(); const t = setTimeout(() => ctl.abort(), 90000);
  try {
    const r = await net.fetch('https://api.anthropic.com/v1/messages', { method: 'POST', signal: ctl.signal,
      headers: { 'content-type': 'application/json', 'x-api-key': key, 'anthropic-version': '2023-06-01' }, body: JSON.stringify(body) });
    return { status: r.status, json: await r.json().catch(() => ({})) };
  } finally { clearTimeout(t); }
}
ipcMain.handle('ai:chat', async (e, payload) => {
  const key = readKey();
  if (!key) return { ok: false, error: 'no-key' };
  try {
    const hist = Array.isArray(payload.messages) ? payload.messages.slice(-20) : [];
    const messages = hist.map((m, i) => ({ role: m.role === 'assistant' ? 'assistant' : 'user', content: m.role === 'assistant' ? String(m.text || '') : buildContent(i === hist.length - 1 ? m : { text: m.text }) }));
    let r = await callClaude(key, messages, true), searchNote = '';
    if (r.status === 400 && /web_search|tool/i.test(JSON.stringify(r.json))) { r = await callClaude(key, messages, false); searchNote = 'Web search is not enabled for this API key, so this answer comes from the model only.'; }
    if (r.status === 401) return { ok: false, error: 'Your API key was rejected. Please check it in Settings.' };
    if (r.status === 429) return { ok: false, error: 'Too many requests or no credit left on this key. Try again later.' };
    if (r.status < 200 || r.status >= 300) return { ok: false, error: (r.json && r.json.error && r.json.error.message) || ('The AI service returned an error (' + r.status + ').') };
    let text = ''; const sources = [];
    (r.json.content || []).forEach((b) => {
      if (b.type === 'text') { text += b.text; (b.citations || []).forEach((c) => { if (c.url && !sources.some((s) => s.url === c.url)) sources.push({ url: c.url, title: c.title || c.url }); }); }
    });
    return { ok: true, text: text.trim() || 'No answer was returned.', sources: sources.slice(0, 6), note: searchNote };
  } catch (err) {
    return { ok: false, error: err && err.name === 'AbortError' ? 'The request took too long. Please try again.' : 'Could not reach the AI service. Check your internet connection.' };
  }
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
