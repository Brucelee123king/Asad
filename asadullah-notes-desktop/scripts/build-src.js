// Splits the original single-file app into src/index.html + src/data.js + src/app.js
// without changing any question data. Run: node scripts/build-src.js <original.html>
const fs = require('fs'), path = require('path');
const input = process.argv[2] || path.join(__dirname, '..', '..', 'original-backup', 'index-7.original.html');
const out = path.join(__dirname, '..', 'src');
const lines = fs.readFileSync(input, 'utf8').split('\n');
const iStart = lines.findIndex(l => l.includes('let quizData = [];')) - 1; // the opening <script> line
const iData0 = lines.findIndex(l => l.includes('const ALL = {'));
const iData1 = lines.findIndex(l => l.includes('const isExtra'));
if (iStart < 0 || iData0 < 0 || iData1 < 0) throw new Error('markers not found');
const head = lines.slice(0, iStart + 1);               // everything up to and incl. <script>
const pre = lines.slice(iStart + 1, iData0);           // let quizData, currentTestKey
const data = lines.slice(iData0, iData1 + 1);          // question databases + helpers
const rest = lines.slice(iData1 + 1);
fs.writeFileSync(path.join(out, 'data.js'), pre.concat(data).join('\n') + '\n');
// classic scripts share globals, so data.js must load before the app script
head[head.length - 1] = '<script src="data.js"></script>\n    <script>';
let html = head.concat(rest).join('\n');
html = html.replace(/<script async src="\/\.netlify[^>]*><\/script>/g, '');
fs.writeFileSync(path.join(out, 'index.html'), html);
console.log('wrote', out);
