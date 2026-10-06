const $ = (s) => document.querySelector(s);
const esc = (s) => String(s).replace(/[&<>"']/g, (c) => ({ '&':'&amp;', '<':'&lt;', '>':'&gt;', '"':'&quot;', "'":'&#39;' }[c]));
const readSet = (key) => new Set(JSON.parse(localStorage.getItem(key) || '[]'));
const state = { items: [], notes: [], activeNote: null, category: 'all', view: 'library', query: '', selected: null, mode: 'code', challenge: false, saved: readSet('pyroom-saved'), done: readSet('pyroom-done') };
const problemBriefs = {
  'problems/03_two_sum.py': { id:'1', name:'Two Sum', difficulty:'Easy', tags:'Array · Hash table', description:'Given an integer array and a target, return the indices of two distinct values that add up to the target. Assume exactly one answer exists.', example:'nums = [2, 7, 11, 15], target = 9  →  [0, 1]', url:'https://leetcode.com/problems/two-sum/' },
  'problems/01_reverse_string.py': { id:'344', name:'Reverse String · practice version', difficulty:'Easy', tags:'String · Two pointers', description:'Reverse the characters in a string. This repository demonstrates slicing and a loop; LeetCode’s original version asks you to reverse a character array in place.', example:'s = ["h", "e", "l", "l", "o"]  →  ["o", "l", "l", "e", "h"]', url:'https://leetcode.com/problems/reverse-string/' },
  'problems/02_palindrome.py': { id:'125', name:'Valid Palindrome · practice version', difficulty:'Easy', tags:'String · Two pointers', description:'Check whether a phrase reads the same forward and backward after lowercasing and removing non-alphanumeric characters. This file currently removes spaces only, so it is a simpler adaptation.', example:'"A man, a plan, a canal: Panama"  →  true', url:'https://leetcode.com/problems/valid-palindrome/' },
  'problems/06_single_number.py': { id:'136', name:'Single Number', difficulty:'Easy', tags:'Array · Bit manipulation', description:'In an integer array where every value appears twice except one, find the value that appears once. Aim for linear time and constant extra space.', example:'[4, 1, 2, 1, 2]  →  4', url:'https://leetcode.com/problems/single-number/' },
  'problems/088_merge_sorted_array.py': { id:'88', name:'Merge Sorted Array', difficulty:'Easy', tags:'Array · Two pointers', description:'Merge two sorted arrays into the first array, which has enough trailing space for both. Keep the result sorted and modify the first array in place.', example:'[1, 2, 3, 0, 0, 0], [2, 5, 6]  →  [1, 2, 2, 3, 5, 6]', url:'https://leetcode.com/problems/merge-sorted-array/' },
  'problems/08_best_time_to_buy_sell_stock.py': { id:'121', name:'Best Time to Buy and Sell Stock', difficulty:'Easy', tags:'Array · Dynamic programming', description:'Given daily stock prices, choose one day to buy and a later day to sell. Return the greatest possible profit; return zero if no profitable trade exists.', example:'[7, 1, 5, 3, 6, 4]  →  5', url:'https://leetcode.com/problems/best-time-to-buy-and-sell-stock/' },
  'problems/09_mejority_elements.py': { id:'169', name:'Majority Element', difficulty:'Easy', tags:'Array · Counting', description:'Find the value that occurs more than half the time in an array. The problem guarantees that such a value exists.', example:'[3, 2, 3]  →  3', url:'https://leetcode.com/problems/majority-element/' },
  'problems/11_container_with_most_water.py': { id:'11', name:'Container With Most Water', difficulty:'Medium', tags:'Array · Two pointers · Greedy', description:'Choose two vertical lines that, together with the x-axis, hold the greatest amount of water. The container area is limited by the shorter line and the distance between them.', example:'height = [1,8,6,2,5,4,8,3,7]  →  49', url:'https://leetcode.com/problems/container-with-most-water/' },
  'problems/15_3_sum.py': { id:'15', name:'3Sum', difficulty:'Medium', tags:'Array · Two pointers · Sorting', description:'Find all unique triplets in the array whose values sum to zero. Do not include duplicate triplets in the result.', example:'[-1, 0, 1, 2, -1, -4]  →  [[-1, -1, 2], [-1, 0, 1]]', url:'https://leetcode.com/problems/3sum/' },
  'problems/18_4_sum.py': { id:'18', name:'4Sum', difficulty:'Medium', tags:'Array · Two pointers · Sorting', description:'Find all unique groups of four values whose sum equals the target. The answer must not contain duplicate quadruplets.', example:'[1, 0, -1, 0, -2, 2], target = 0  →  [[-2, -1, 1, 2], [-2, 0, 0, 2], …]', url:'https://leetcode.com/problems/4sum/' },
  'problems/53_maximum_subarray.py': { id:'53', name:'Maximum Subarray', difficulty:'Medium', tags:'Array · Dynamic programming', description:'Find the contiguous subarray with the largest sum and return that sum. The subarray must contain at least one value.', example:'[-2, 1, -3, 4, -1, 2, 1, -5, 4]  →  6', url:'https://leetcode.com/problems/maximum-subarray/' },
  'problems/75_sort_colors.py': { id:'75', name:'Sort Colors', difficulty:'Medium', tags:'Array · Two pointers · Sorting', description:'Sort an array containing only 0, 1, and 2 in place so equal colors are together and ordered as red, white, blue (0, 1, 2). Try the one-pass, constant-space approach.', example:'[2, 0, 2, 1, 1, 0]  →  [0, 0, 1, 1, 2, 2]', url:'https://leetcode.com/problems/sort-colors/' },
  'problems/010_pow_x.py': { id:'50', name:'Pow(x, n)', difficulty:'Medium', tags:'Math · Recursion', description:'Implement exponentiation to compute x raised to the integer power n. Account for negative powers and large exponents.', example:'x = 2.0, n = 10  →  1024.0', url:'https://leetcode.com/problems/powx-n/' },
  'problems/2965_find_missing_and_repeated_values.py': { id:'2965', name:'Find Missing and Repeated Values', difficulty:'Easy', tags:'Array · Hash table · Matrix', description:'An n × n grid should contain every integer from 1 through n² once, but one value appears twice and another is missing. Return [repeated, missing].', example:'[[1, 3], [2, 2]]  →  [2, 4]', url:'https://leetcode.com/problems/find-missing-and-repeated-values/' },
  'problems/04_frequency_count.py': { difficulty:'Practice', tags:'String · Hash table', description:'Count how often each non-space character appears in the input text. This is a repository practice exercise.', example:'"hello"  →  {"h": 1, "e": 1, "l": 2, "o": 1}' },
  'problems/05_find_max.py': { difficulty:'Practice', tags:'Array · Iteration', description:'Find the largest value in a list without calling Python’s built-in max() function.', example:'[10, 4, 25, 7, 18]  →  25' },
  'problems/07_fizzbuzz.py': { id:'412', name:'Fizz Buzz · practice version', difficulty:'Easy', tags:'Math · String', description:'For each number in a range, print Fizz for multiples of 3, Buzz for multiples of 5, and FizzBuzz for multiples of both. This file uses 1 through 20.', example:'1, 2, Fizz, 4, Buzz, …, FizzBuzz', url:'https://leetcode.com/problems/fizz-buzz/' }
};
const notesKey = (path) => `pyroom-note:${path}`;
const labelFor = (key) => state.items.find(x => x.category === key)?.categoryLabel || key;
function persist() { localStorage.setItem('pyroom-saved', JSON.stringify([...state.saved])); localStorage.setItem('pyroom-done', JSON.stringify([...state.done])); }
function resetLessonScroll() { const list = $('#lesson-list'); list.scrollTop = 0; list.scrollLeft = 0; }
function setText(sel, value) { const el = $(sel); if (el) el.textContent = value; }
function stats() {
  const n = state.items.length, d = state.done.size;
  setText('#total-count', n); setText('#saved-count', state.saved.size); setText('#stat-files', n);
  setText('#stat-total', n); setText('#stat-done', d); setText('#stat-categories', new Set(state.items.map(x => x.category)).size);
  setText('#welcome-done', d); setText('#rail-done', d); setText('#rail-total', n);
  const bar = $('#progress-bar'); if (bar) bar.style.width = `${n ? Math.min(100, d / n * 100) : 0}%`;
  const railBar = $('#rail-progress-bar'); if (railBar) railBar.style.width = `${n ? Math.min(100, d / n * 100) : 0}%`;
}
function nav() {
  const cats = [...new Set(state.items.map(x => x.category))];
  $('#category-nav').innerHTML = cats.map(c => {
    const lessons = state.items.filter(x => x.category === c);
    const complete = lessons.filter(x => state.done.has(x.path)).length;
    return `<button class="category-link ${state.category === c ? 'active' : ''}" data-category="${esc(c)}" aria-pressed="${state.category === c}"><i class="cat-dot"></i>${esc(labelFor(c))}<span class="nav-count" title="${complete} of ${lessons.length} explored">${complete}/${lessons.length}</span></button>`;
  }).join('');
  $('#category-nav').querySelectorAll('[data-category]').forEach(b => b.onclick = () => {
    state.view = 'library'; state.category = b.dataset.category; state.query = ''; $('#search').value = '';
    const first = state.items.find(item => item.category === state.category);
    if (first) openFile(first.path); else render();
    resetLessonScroll();
  });
}
function renderNotesNav() {
  const host = $('#notes-nav');
  if (!host) return;
  host.innerHTML = state.notes.length ? state.notes.map(note => `<button class="note-link ${state.activeNote?.name === note.name ? 'active' : ''}" data-note="${esc(note.name)}" title="${esc(note.title)}"><span class="pdf-icon">PDF</span><span class="note-link-title">${esc(note.title)}</span></button>`).join('') : '<div class="notes-empty">No PDFs in notes/ yet</div>';
  host.querySelectorAll('[data-note]').forEach(button => button.onclick = () => openNote(button.dataset.note));
}
function updateNav() {
  document.querySelectorAll('.nav-item').forEach(b => b.classList.toggle('active', b.dataset.view === state.view));
  document.querySelectorAll('.category-link').forEach(b => b.classList.toggle('active', state.view !== 'notes' && b.dataset.category === state.category));
  $('#crumb').textContent = state.view === 'notes' ? (state.activeNote?.title || 'PDF NOTES').toUpperCase() : state.view === 'saved' ? 'BOOKMARKS' : state.category === 'all' ? 'ALL LESSONS' : labelFor(state.category).toUpperCase();
  $('#docs-kicker').textContent = state.view === 'notes' ? 'YOUR STUDY MATERIALS · PDF READER' : state.selected ? `${state.selected.categoryLabel.toUpperCase()} · YOUR PERSONAL NOTES` : 'PYTHON PRACTICE · YOUR PERSONAL NOTES';
}
function filtered() { return state.items.filter(x => (state.view !== 'saved' || state.saved.has(x.path)) && (state.category === 'all' || x.category === state.category) && (!state.query || `${x.title} ${x.categoryLabel} ${x.path}`.toLowerCase().includes(state.query.toLowerCase()))); }
function render() {
  nav(); renderNotesNav(); stats(); updateNav(); const items = filtered();
  $('#result-count').textContent = items.length ? `· ${items.length}` : '';
  $('#lesson-list').innerHTML = items.length ? items.map(x => `<article class="lesson-row ${state.selected?.path === x.path ? 'selected' : ''}" data-path="${esc(x.path)}" role="button" tabindex="0" aria-current="${state.selected?.path === x.path ? 'page' : 'false'}"><div class="file-icon">${x.category === 'problems' ? '{}' : x.category === 'projects' ? '↗' : x.category === 'oop' ? '◈' : x.category === 'numpy' ? 'np' : x.category === 'pandas' ? 'pd' : 'py'}</div><div class="lesson-copy"><div class="lesson-title">${esc(x.title)}</div><div class="lesson-meta">${esc(x.categoryLabel)}<i class="meta-dot"></i>${esc(x.path.split('/').at(-1))}</div></div><div class="lesson-trailing">${state.done.has(x.path) ? '<span class="done-mark" aria-label="Explored">✓</span>' : ''}<button class="bookmark-btn ${state.saved.has(x.path) ? 'saved' : ''}" data-save="${esc(x.path)}" title="${state.saved.has(x.path) ? 'Remove bookmark' : 'Bookmark lesson'}" aria-label="${state.saved.has(x.path) ? 'Remove bookmark' : 'Bookmark lesson'}">${state.saved.has(x.path) ? '★' : '☆'}</button><span class="row-arrow" aria-hidden="true">›</span></div></article>`).join('') : `<div class="empty-state">${state.view === 'saved' ? 'No bookmarks yet. Tap ☆ on a file to save it.' : 'No files match that search.'}</div>`;
  $('#lesson-list').querySelectorAll('.lesson-row').forEach(row => {
    row.onclick = e => { if (!e.target.closest('[data-save]')) openFile(row.dataset.path); };
    row.onkeydown = e => { if ((e.key === 'Enter' || e.key === ' ') && !e.target.closest('[data-save]')) { e.preventDefault(); openFile(row.dataset.path); } };
  });
  $('#lesson-list').querySelectorAll('[data-save]').forEach(btn => btn.onclick = e => { e.stopPropagation(); toggleSaved(btn.dataset.save); render(); });
}
function openNote(name) {
  const note = state.notes.find(item => item.name === name);
  if (!note) return;
  state.view = 'notes'; state.activeNote = note;
  render();
  const panel = $('#detail-panel');
  panel.classList.add('has-selection', 'pdf-detail');
  document.querySelector('.docs-layout').classList.remove('problem-layout');
  $('#outline-panel').hidden = true;
  $('#problem-panel').hidden = true;
  const src = `/api/notes/${encodeURIComponent(note.name)}#view=FitH`;
  const encodedName = encodeURIComponent(note.name);
  panel.innerHTML = `<div class="pdf-reader-head"><div><div class="detail-tag">STUDY NOTES <span class="tag-separator">/</span> PDF DOCUMENT</div><h1 class="pdf-title">${esc(note.title)}</h1><div class="pdf-meta">${(note.size / 1024 / 1024).toFixed(1)} MB · Opens in your browser’s PDF reader</div></div><div class="pdf-actions"><a class="action-btn" href="/api/notes/${encodedName}" download="${esc(note.name)}">Download</a><a class="action-btn" href="${src}" target="_blank" rel="noopener noreferrer">Open in new tab ↗</a></div></div><div class="pdf-reader-hint"><span>↕</span> Use the reader toolbar to search text, change zoom, move between pages, or print.</div><iframe class="pdf-frame" src="${src}" title="PDF reader: ${esc(note.title)}"></iframe>`;
}
function toggleSaved(path) { state.saved.has(path) ? state.saved.delete(path) : state.saved.add(path); persist(); }
function tokenized(source) {
  const pattern = /(#[^\n]*|'''[\s\S]*?'''|"""[\s\S]*?"""|'(?:\\.|[^'\\])*'|"(?:\\.|[^"\\])*"|\b(?:False|None|True|and|as|assert|async|await|break|class|continue|def|del|elif|else|except|finally|for|from|global|if|import|in|is|lambda|nonlocal|not|or|pass|raise|return|try|while|with|yield)\b|\b\d+(?:\.\d+)?\b|\b[A-Za-z_]\w*(?=\s*\())/g;
  let html = '', last = 0, match;
  while ((match = pattern.exec(source))) {
    html += esc(source.slice(last, match.index)); const t = match[0];
    const cls = t.startsWith('#') ? 'tok-comment' : /^["']/.test(t) ? 'tok-string' : /^\d/.test(t) ? 'tok-number' : /^(False|None|True|and|as|assert|async|await|break|class|continue|def|del|elif|else|except|finally|for|from|global|if|import|in|is|lambda|nonlocal|not|or|pass|raise|return|try|while|with|yield)$/.test(t) ? 'tok-keyword' : 'tok-function';
    html += `<span class="${cls}">${esc(t)}</span>`; last = pattern.lastIndex;
  }
  return html + esc(source.slice(last));
}
function learningPrompt(item, code) {
  if (item.category === 'problems') return `Before reading the solution, explain the input, expected output, and a simple approach. Then trace one example by hand. What is the time complexity?`;
  if (item.category === 'oop') return `In your own words: what is the class responsible for, what does each object remember, and which method changes or uses that state?`;
  if (item.category === 'data-structures') return `Recall the shape of this data structure. Which operations are useful here, and what would happen with an empty collection or a duplicate value?`;
  if (item.category === 'functions') return `Identify the inputs, returned value, and any side effects. Can you predict the output for a tiny example without running the code?`;
  if (item.category === 'projects') return `Describe the user flow from input to output. What validation or error case would you add next?`;
  if (item.category === 'experiments') return `What is this experiment trying to learn? Predict what it prints or changes before you run it.`;
  return `Summarize “${item.title}” in one sentence. What does the example teach, and what changes if you use a different value?`;
}
function challengeFor(item) {
  if (item.category !== 'problems') return `Make a small change to <b>${esc(item.title)}</b>: add a test case, handle an edge case, or explain why the current approach works.`;
  return `Try solving <b>${esc(item.title)}</b> from a blank file first. Write down your approach, test a normal case and an edge case, then compare with the repository solution.`;
}
function openFile(path) {
  const item = state.items.find(x => x.path === path); if (!item) return;
  state.activeNote = null;
  state.selected = item; state.mode = 'code'; state.challenge = false; render();
  const panel = $('#detail-panel'), brief = problemBriefs[path], layout = document.querySelector('.docs-layout');
  panel.classList.remove('pdf-detail');
  panel.classList.add('has-selection'); layout.classList.toggle('problem-layout', Boolean(brief));
  $('#outline-panel').hidden = Boolean(brief);
  $('#problem-panel').hidden = !brief;
  panel.innerHTML = '<div class="empty-detail"><div class="empty-orbit">…</div><h3>Opening your file</h3></div>';
  fetch('/api/source/' + encodeURIComponent(path)).then(r => r.text()).then(code => {
    if (state.selected?.path !== path) return;
    showDetail(item, code);
  }).catch(() => { panel.innerHTML = '<div class="empty-detail"><h3>Couldn’t open this file</h3><p>Make sure you started the local Python server.</p></div>'; });
}
function showDetail(item, code) {
  const panel = $('#detail-panel'); const lines = code.split('\n');
  const brief = problemBriefs[item.path];
  const savedSize = Math.max(12, Math.min(22, Number(localStorage.getItem('pyroom-code-size') || 15)));
  const first = code.split('\n').find(l => l.trim().startsWith('#'))?.replace(/^\s*#\s*/, '') || 'A Python practice file from your library.';
  const note = localStorage.getItem(notesKey(item.path)) || '';
  const modeContent = state.mode === 'code' ? `<div class="study-note"><span class="note-icon">✦</span><div><b>Quick idea</b><br>${esc(first)}. Read once, then explain it without looking.</div></div><div class="code-toolbar" id="source-section"><span>🐍 PYTHON SOURCE · ${lines.length} LINES</span><div class="code-controls"><button class="try-first-btn" id="hide-solution">${state.challenge ? 'Show solution' : '🙈 Try first'}</button><div class="size-control" aria-label="Code font size"><button id="font-down" title="Smaller code">−</button><span id="font-size-label">${savedSize}px</span><button id="font-up" title="Larger code">+</button></div></div></div>${state.challenge ? `<div class="challenge-cover"><div class="challenge-emoji">🧠</div><b>First, solve it yourself.</b><p>${challengeFor(item)}</p><button class="action-btn" id="reveal-code">I’m ready to compare →</button></div>` : `<div class="code-scroll"><div class="code-content" style="font-size:${savedSize}px"><div class="line-numbers">${lines.map((_, i) => i + 1).join('\n')}</div><pre>${tokenized(code)}</pre></div></div>`}` : state.mode === 'recall' ? `<div class="recall-card"><div class="recall-head"><span>✍️</span><div><b>Active recall</b><small>Close the code and retrieve it from memory.</small></div></div><p class="recall-question">${esc(learningPrompt(item, code))}</p><textarea id="recall-note" placeholder="Write what you remember…">${esc(note)}</textarea><div class="recall-foot"><span id="note-status">${note ? 'Saved on this device' : 'Your note saves automatically'}</span><button class="action-btn" id="show-hint">Show a hint</button></div><div class="hint-box" id="hint-box" hidden>${esc(first)}</div></div>` : `<div class="practice-card"><div class="practice-label">YOUR MINI CHALLENGE</div><div class="challenge-big">${item.category === 'problems' ? 'Solve it before you peek.' : 'Make the idea yours.'}</div><p>${challengeFor(item)}</p><div class="practice-steps"><div><i>1</i><span>Try it in your editor</span></div><div><i>2</i><span>Test one edge case</span></div><div><i>3</i><span>Explain the solution</span></div></div><button class="action-btn wide-btn" id="practice-peek">Open the repository code →</button></div>`;
  panel.innerHTML = `<div class="detail-head"><div class="detail-tag">${esc(item.categoryLabel)} <span class="tag-separator">/</span> ${brief ? `LEETCODE PROBLEM${brief.id ? ` #${esc(brief.id)}` : ''}` : 'PYTHON STUDY GUIDE'}</div><div class="detail-title-row"><h1 class="detail-title">${esc(item.title)}</h1><div class="detail-actions"><button class="action-btn" id="copy-btn">▣ Copy</button><button class="action-btn" id="save-detail">${state.saved.has(item.path) ? '★ Saved' : '☆ Save'}</button></div></div><div class="detail-path">${esc(item.path)}</div></div><div class="study-tabs" id="study-tools"><button class="study-tab ${state.mode === 'code' ? 'active' : ''}" data-mode="code">Code</button><button class="study-tab ${state.mode === 'recall' ? 'active' : ''}" data-mode="recall">Revise</button><button class="study-tab ${state.mode === 'practice' ? 'active' : ''}" data-mode="practice">Practice</button></div>${modeContent}<button class="mark-done ${state.done.has(item.path) ? 'completed' : ''}" id="done-btn">${state.done.has(item.path) ? '✓  Explored — click to undo' : '○  Mark as explored'}</button>`;
  if (brief) {
    const side = $('#problem-panel');
    side.innerHTML = `<div class="problem-card-head"><span class="lc-mark">LC</span><div><div class="problem-kicker">${brief.id ? `LEETCODE · #${esc(brief.id)}` : 'PYTHON PRACTICE'}</div><h3>${esc(brief.name || item.title)}</h3></div></div><div class="difficulty-badge ${brief.difficulty.toLowerCase()}">${esc(brief.difficulty)}</div><div class="problem-tags">${esc(brief.tags)}</div><div class="problem-divider"></div><div class="problem-section-title">PROBLEM</div><p class="problem-description">${esc(brief.description)}</p><div class="example-label">EXAMPLE</div><pre class="problem-example">${esc(brief.example)}</pre><div class="problem-tip"><span>💡</span><p><b>Before you code</b><br>Write down your approach and think of one edge case.</p></div>${brief.url ? `<a class="leetcode-link" href="${esc(brief.url)}" target="_blank" rel="noopener noreferrer">Open official LeetCode problem ↗</a>` : '<div class="practice-only">Repository exercise · no LeetCode link</div>'}`;
  }
  panel.querySelectorAll('[data-mode]').forEach(b => b.onclick = () => { state.mode = b.dataset.mode; showDetail(item, code); });
  $('#copy-btn').onclick = async () => { await navigator.clipboard.writeText(code); $('#copy-btn').textContent = '✓ Copied!'; setTimeout(() => { if ($('#copy-btn')) $('#copy-btn').textContent = '▣ Copy'; }, 1400); };
  $('#save-detail').onclick = () => { toggleSaved(item.path); render(); showDetail(item, code); };
  $('#done-btn').onclick = () => { state.done.has(item.path) ? state.done.delete(item.path) : state.done.add(item.path); persist(); render(); showDetail(item, code); };
  if ($('#reveal-code')) $('#reveal-code').onclick = () => { state.challenge = false; showDetail(item, code); };
  if ($('#hide-solution')) $('#hide-solution').onclick = () => { state.challenge = !state.challenge; showDetail(item, code); };
  const resizeCode = (delta) => { const next = Math.max(12, Math.min(22, savedSize + delta)); localStorage.setItem('pyroom-code-size', next); showDetail(item, code); };
  if ($('#font-down')) $('#font-down').onclick = () => resizeCode(-1);
  if ($('#font-up')) $('#font-up').onclick = () => resizeCode(1);
  if ($('#practice-peek')) $('#practice-peek').onclick = () => { state.mode = 'code'; state.challenge = false; showDetail(item, code); };
  if ($('#recall-note')) $('#recall-note').oninput = e => { localStorage.setItem(notesKey(item.path), e.target.value); $('#note-status').textContent = 'Saved on this device ✓'; };
  if ($('#show-hint')) $('#show-hint').onclick = () => { $('#hint-box').hidden = !$('#hint-box').hidden; $('#show-hint').textContent = $('#hint-box').hidden ? 'Show a hint' : 'Hide hint'; };
}
document.querySelectorAll('.nav-item').forEach(b => b.onclick = () => {
  state.activeNote = null;
  state.view = b.dataset.view; state.category = 'all'; state.query = ''; $('#search').value = '';
  const first = filtered()[0];
  if (first) openFile(first.path); else { state.selected = null; render(); }
  resetLessonScroll();
});
function applyTheme(theme) {
  document.documentElement.setAttribute('data-theme', theme);
  localStorage.setItem('pyroom-theme', theme);
  const toggle = $('#theme-toggle');
  if (toggle) toggle.setAttribute('aria-pressed', theme === 'dark' ? 'true' : 'false');
}
(function initTheme() {
  const stored = localStorage.getItem('pyroom-theme');
  const theme = stored || (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
  applyTheme(theme);
})();
$('#theme-toggle').onclick = () => {
  const next = document.documentElement.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
  applyTheme(next);
};
$('#search').addEventListener('input', e => { state.query = e.target.value; render(); resetLessonScroll(); });
window.addEventListener('keydown', e => { if ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === 'k') { e.preventDefault(); $('#search').focus(); } if (e.key === 'Escape') $('#search').blur(); });
$('#search').addEventListener('keydown', e => { if (e.key === 'Escape') e.target.value = ''; });
(async () => {
  try {
    const [filesResponse, notesResponse] = await Promise.all([fetch('/api/files'), fetch('/api/notes')]);
    state.items = await filesResponse.json();
    state.notes = await notesResponse.json();
    nav(); renderNotesNav(); render();
  } catch { $('#lesson-list').innerHTML = '<div class="empty-state">Start the app with <code>python3 app.py</code> to load your files.</div>'; }
})();
