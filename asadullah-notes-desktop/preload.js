// Mirrors the page's localStorage into a JSON file in the Windows user-data folder,
// so history, accounts, bookmarks and settings survive updates and reinstalls.
const { ipcRenderer } = require('electron');
try {
  const saved = ipcRenderer.sendSync('store:load') || {};
  Object.keys(saved).forEach((k) => { if (localStorage.getItem(k) === null) localStorage.setItem(k, saved[k]); });
  // push anything already in localStorage that the file does not have yet
  for (let i = 0; i < localStorage.length; i++) {
    const k = localStorage.key(i);
    if (!(k in saved)) ipcRenderer.send('store:set', k, localStorage.getItem(k));
  }
  const S = Storage.prototype, set = S.setItem, rem = S.removeItem, clr = S.clear;
  S.setItem = function (k, v) { set.call(this, k, v); if (this === localStorage) ipcRenderer.send('store:set', String(k), String(v)); };
  S.removeItem = function (k) { rem.call(this, k); if (this === localStorage) ipcRenderer.send('store:set', String(k), null); };
  S.clear = function () { if (this === localStorage) Object.keys(saved).forEach((k) => ipcRenderer.send('store:set', k, null)); clr.call(this); };
} catch (e) { console.error('storage bridge failed', e); }
