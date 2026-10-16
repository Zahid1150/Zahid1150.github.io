document.documentElement.classList.add('js');
const toggle = document.querySelector('.menu-toggle');
const nav = document.querySelector('#site-nav');
function closeMenu(returnFocus = false) {
  nav.classList.remove('open');
  toggle.setAttribute('aria-expanded', 'false');
  if (returnFocus) toggle.focus();
}
toggle.addEventListener('click', () => {
  const open = toggle.getAttribute('aria-expanded') !== 'true';
  toggle.setAttribute('aria-expanded', String(open));
  nav.classList.toggle('open', open);
});
document.addEventListener('click', event => {
  if (!event.target.closest('.site-header')) closeMenu();
});
document.addEventListener('keydown', event => {
  if (event.key === 'Escape' && toggle.getAttribute('aria-expanded') === 'true') closeMenu(true);
});
nav.addEventListener('click', event => { if (event.target.closest('a')) closeMenu(); });
matchMedia('(min-width:1201px)').addEventListener('change', () => closeMenu());
document.querySelectorAll('.gallery-filters button').forEach(button => {
  button.addEventListener('click', () => {
    document.querySelectorAll('.gallery-filters button').forEach(b => b.setAttribute('aria-pressed', String(b === button)));
    document.querySelectorAll('.gallery-item').forEach(item => {
      item.hidden = button.dataset.album !== 'all' && item.dataset.album !== button.dataset.album;
    });
  });
});
const dialog = document.querySelector('.photo-dialog');
if (dialog) {
  document.querySelectorAll('.photo-open').forEach(button => button.addEventListener('click', () => {
    const original = button.querySelector('img');
    const large = dialog.querySelector('img');
    large.src = original.src; large.alt = original.alt;
    dialog.querySelector('p').textContent = button.closest('figure').querySelector('figcaption').textContent;
    dialog.showModal();
  }));
  dialog.querySelector('.photo-close').addEventListener('click', () => dialog.close());
  dialog.addEventListener('click', event => { if (event.target === dialog) dialog.close(); });
}
