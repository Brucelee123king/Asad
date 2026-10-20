// Online AI Helper server. Keeps the API key secret (set GEMINI_API_KEY in Netlify > Site settings > Environment variables).
const MODEL = process.env.AI_MODEL || 'gemini-2.5-flash';
const CORS = {
  'Access-Control-Allow-Origin': '*',
  'Access-Control-Allow-Headers': 'Content-Type',
  'Access-Control-Allow-Methods': 'POST, OPTIONS',
  'Content-Type': 'application/json',
};
const reply = (code, obj) => ({ statusCode: code, headers: CORS, body: JSON.stringify(obj) });

exports.handler = async (event) => {
  if (event.httpMethod === 'OPTIONS') return { statusCode: 204, headers: CORS, body: '' };
  if (event.httpMethod !== 'POST') return reply(405, { error: 'POST only' });
  const key = process.env.GEMINI_API_KEY;
  if (!key) return reply(500, { error: 'Server has no GEMINI_API_KEY set.' });
  let b;
  try { b = JSON.parse(event.body || '{}'); } catch (e) { return reply(400, { error: 'Bad request' }); }
  if (!b || typeof b !== 'object') return reply(400, { error: 'Bad request' });
  const msgs = (Array.isArray(b.messages) ? b.messages : []).filter((m) => m && typeof m === 'object').slice(-8);
  while (msgs.length > 1 && msgs[0].role === 'model') msgs.shift();
  if (!msgs.length) return reply(400, { error: 'Empty question' });

  const contents = msgs.map((m) => ({
    role: m.role === 'model' ? 'model' : 'user',
    parts: [{ text: String(m.text || '').slice(0, 4000) }],
  }));
  const last = contents[contents.length - 1];
  const a = b.attachment;
  if (a && last.role === 'user') {
    if (a.data && !(/^(image\/(jpeg|png|webp)|application\/pdf)$/.test(a.mime || '') && a.data.length < 5.5e6))
      return reply(413, { error: 'Attachment not supported or too large (use JPG/PNG/WEBP/PDF under 4 MB).' });
    if (a.data)
      last.parts.push({ inline_data: { mime_type: a.mime, data: a.data } });
    else if (a.text) last.parts.push({ text: 'Attached file "' + String(a.name || '') + '":\n' + String(a.text).slice(0, 20000) });
  }
  const system =
    'You are a friendly exam-preparation tutor inside an MCQ practice app (Pakistan competitive exams: PMA, Forces Academy, Hakeem tests, general knowledge). ' +
    'Today is ' + String(b.date || '').slice(0, 10) + '. Use Google Search for current facts (office holders, recent events) and say when you are unsure. ' +
    'Answer in simple English unless the student writes in another language. Be correct first, then short and clear; use bullet points. ' +
    (b.context ? 'Current MCQ context: ' + String(b.context).slice(0, 2000) : '');

  try {
    const r = await fetch(
      'https://generativelanguage.googleapis.com/v1beta/models/' + MODEL + ':generateContent',
      {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', 'x-goog-api-key': key },
        body: JSON.stringify({
          system_instruction: { parts: [{ text: system }] },
          contents,
          tools: [{ google_search: {} }],
          generationConfig: { temperature: 0.4, maxOutputTokens: 4096 },
        }),
      }
    );
    const j = await r.json();
    if (!r.ok) return reply(502, { error: (j.error && j.error.message) || 'AI service error ' + r.status });
    const cand = (j.candidates || [])[0] || {};
    const why = (j.promptFeedback && j.promptFeedback.blockReason) || cand.finishReason || '';
    const text = ((cand.content && cand.content.parts) || []).map((p) => p.text || '').join('').trim();
    const chunks = (cand.groundingMetadata && cand.groundingMetadata.groundingChunks) || [];
    const sources = [...new Set(chunks.map((c) => c.web && c.web.title).filter(Boolean))];
    return reply(200, { reply: text || 'No answer (' + why + '). Try rephrasing.', sources });
  } catch (e) {
    return reply(502, { error: 'Could not reach the AI service.' });
  }
};
