# Add a book (PDF) to the app: developer handoff

Use this only for PDFs the app owner has the rights to distribute
(their own content, a licensed book, or public domain / openly licensed material).

Stack assumed: Firebase (Storage + Firestore) with a web/JS front end.
If the app is Flutter or native Android/iOS, use section 5.

---

## 1. Upload the files (Firebase Console, no code)

1. Firebase Console -> Build -> Storage.
2. Create folders `books/` and `books/covers/`.
3. Upload the PDF to `books/<book-id>.pdf` and the cover to `books/covers/<book-id>.jpg`.
   Example book id: `bk_mybook`.

## 2. Storage rules (only logged-in app users can read)

Firebase Console -> Storage -> Rules:

```
rules_version = '2';
service firebase.storage {
  match /b/{bucket}/o {
    match /books/{allPaths=**} {
      allow read: if request.auth != null;
      allow write: if false;   // upload only from the Console / admin
    }
  }
}
```

## 3. Book data

Find where the existing book (`bk_issb130`) is defined (search the repo for that id).
It is either hard-coded in the source or in a Firestore collection. Add one more entry
with the same shape. Suggested fields:

```js
{
  id: "bk_mybook",
  title: "My Book Title",
  subtitle: "120 pages",
  price: 0,                              // or the price in Rs
  coverPath: "books/covers/bk_mybook.jpg",
  pdfPath: "books/bk_mybook.pdf"
}
```

If the app unlocks books with a key, also add a document in the `catKeys`
collection with the same id (as `bk_issb130` has) and its key field.

## 4. Web code: "Read book" opens the PDF

```js
// Firebase v9+ modular SDK
import { getStorage, ref, getDownloadURL } from "firebase/storage";

export async function getBookUrl(pdfPath) {
  const storage = getStorage();
  return await getDownloadURL(ref(storage, pdfPath));
}
```

Simple viewer using pdf.js (add to the page):

```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.min.js"></script>
<div id="pager">
  <button id="prev">Prev</button>
  <span>Page <input id="pageNum" type="number" min="1" style="width:4em"> of <span id="pageCount"></span></span>
  <button id="next">Next</button>
</div>
<canvas id="pdfCanvas"></canvas>
```

```js
pdfjsLib.GlobalWorkerOptions.workerSrc =
  "https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.worker.min.js";

export async function openBook(bookId, pdfPath) {
  const url = await getBookUrl(pdfPath);
  const pdf = await pdfjsLib.getDocument(url).promise;
  const canvas = document.getElementById("pdfCanvas");
  const ctx = canvas.getContext("2d");
  const input = document.getElementById("pageNum");
  document.getElementById("pageCount").textContent = pdf.numPages;

  let current = Number(localStorage.getItem("lastPage_" + bookId)) || 1;

  async function render(n) {
    n = Math.min(Math.max(n, 1), pdf.numPages);
    current = n;
    const page = await pdf.getPage(n);
    const viewport = page.getViewport({ scale: 1.5 });
    canvas.width = viewport.width;
    canvas.height = viewport.height;
    await page.render({ canvasContext: ctx, viewport }).promise;
    input.value = n;
    localStorage.setItem("lastPage_" + bookId, n);
  }

  document.getElementById("prev").onclick = () => render(current - 1);
  document.getElementById("next").onclick = () => render(current + 1);
  input.onchange = () => render(Number(input.value));
  render(current);
}
```

Call `openBook(book.id, book.pdfPath)` from the "Read book" button.
Add a loading indicator and a "Retry" button around the `await` calls.

## 5. Flutter / native

- Flutter: `firebase_storage` for `getDownloadURL()`, plus `syncfusion_flutter_pdfviewer`
  (`SfPdfViewer.network(url)`) or `pdfx`.
- Android: Firebase Storage `getDownloadUrl()` plus a PDF viewer library.
- Cache the downloaded file so it is not re-downloaded every time.

## 6. Checklist

- [ ] PDF and cover uploaded to Storage
- [ ] Storage rules published
- [ ] Book entry added (code or Firestore)
- [ ] Key document added in `catKeys` if the app uses keys
- [ ] "Read book" opens the PDF, shows page X of N, remembers the last page
- [ ] Tested on a real phone
