// Mirrors the page's localStorage into a JSON file in the Windows user-data folder,
// so history, accounts, bookmarks and settings survive updates and reinstalls.
const { ipcRenderer, contextBridge, webFrame } = require('electron');
try {
  const saved = ipcRenderer.sendSync('store:load') || {};
  Object.keys(saved).forEach((k) => { if (localStorage.getItem(k) === null) localStorage.setItem(k, saved[k]); });
  // push anything already in localStorage that the file does not have yet
  for (let i = 0; i < localStorage.length; i++) {
    const k = localStorage.key(i);
    if (!(k in saved)) ipcRenderer.send('store:set', k, localStorage.getItem(k));
  }
  contextBridge.exposeInMainWorld('__anStore', { set: (k, v) => ipcRenderer.send('store:set', String(k), v === null ? null : String(v)) });
  // the page runs in the main world, so the hook must be installed there
  webFrame.executeJavaScript(`(function () {
    var S = Storage.prototype, set = S.setItem, rem = S.removeItem, clr = S.clear;
    S.setItem = function (k, v) { set.call(this, k, v); if (this === window.localStorage) window.__anStore.set(k, v); };
    S.removeItem = function (k) { rem.call(this, k); if (this === window.localStorage) window.__anStore.set(k, null); };
    S.clear = function () { var ks = []; if (this === window.localStorage) for (var i = 0; i < this.length; i++) ks.push(this.key(i)); clr.call(this); ks.forEach(function (k) { window.__anStore.set(k, null); }); };
  })();`);
} catch (e) { console.error('storage bridge failed', e); }
