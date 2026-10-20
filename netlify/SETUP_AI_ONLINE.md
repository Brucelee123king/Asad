# Online AI Helper setup (optional - Offline mode works without this)

1. Get a free API key: open https://aistudio.google.com/apikey and create a key (Gemini). Free plan has daily limits.
2. In Netlify: Site settings > Environment variables > add  GEMINI_API_KEY = (your key).  Do not share this key.
3. Put the file netlify/functions/ask.js in your site project (same folder structure) and deploy.
   Note: Netlify "drag and drop" may not deploy functions. If it does not, deploy through GitHub or the Netlify CLI (netlify deploy --prod).
4. In the app: open AI Helper > gear icon > enter
   https://YOUR-SITE.netlify.app/.netlify/functions/ask   > Save. Then choose Online.
5. On the website itself you can leave the address empty.
Notes: AI answers can be wrong - check before the exam. Free plan limits may stop answers for the day.
