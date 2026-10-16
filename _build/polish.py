"""Apply small, repeatable content and accessibility fixes to generated pages."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
CSS = '''
/* Keyboard navigation and motion preferences */
.skip-link{position:fixed;top:8px;left:8px;z-index:100;padding:10px 16px;background:var(--card);color:var(--fg);border:2px solid currentColor;transform:translateY(-160%)}
.skip-link:focus{transform:translateY(0)}
a:focus-visible{outline:3px solid currentColor;outline-offset:4px}
main:focus{outline:none}
[id]{scroll-margin-top:80px}
@media(prefers-reduced-motion:reduce){html{scroll-behavior:auto}}
'''

def correct_text(text):
    text = text.replace('CDC/NIOSH-funded', 'federally funded')
    text = text.replace('shorter tours', 'smaller average optimality gap')
    text = text.replace('smaller average gap', 'smaller average optimality gap')
    text = re.sub(r'A new fairness design cut (?:the )?night-shift imbalance (?:between physicians )?by about half\.',
                  'The model balances night-shift assignments alongside coverage and individual preferences.', text)
    text = text.replace('Fairer nights: a new fairness design cut the imbalance in night shifts between physicians by about half, with no loss in coverage.',
                        'Fairer nights: the model balances night-shift assignments between physicians while maintaining coverage.')
    return text

def polish():
    for path in sorted(ROOT.glob('*.html')) + sorted((ROOT / 'projects').glob('*.html')):
        text = correct_text(path.read_text(encoding='utf-8'))
        if '/* Keyboard navigation and motion preferences */' not in text:
            text = text.replace('</style>', CSS + '</style>', 1)
        if '<main' not in text:
            text = text.replace('</header>', '</header>\n<main id="main-content" tabindex="-1">', 1)
            text = text.replace('<footer>', '</main>\n<footer>', 1)
        if 'class="skip-link"' not in text:
            text = text.replace('<body>', '<body>\n<a class="skip-link" href="#main-content">Skip to content</a>', 1)
        text = text.replace('class=on>', 'class="on" aria-current="page">')
        path.write_text(text, encoding='utf-8')

if __name__ == '__main__':
    polish()
