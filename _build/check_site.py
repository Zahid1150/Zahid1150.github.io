"""Check local links, navigation, landmarks, and editable content before deployment."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urljoin, urlsplit, unquote
import json
root=Path(__file__).resolve().parent.parent
class Page(HTMLParser):
    def __init__(self):
        super().__init__();self.ids=[];self.refs=[];self.mains=0;self.h1s=0
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if 'id' in a:self.ids.append(a['id'])
        if tag=='main':self.mains+=1
        if tag=='h1':self.h1s+=1
        for k in ('href','src'):
            if k in a:self.refs.append(a[k])
pages={}
for p in list(root.glob('*.html'))+list((root/'projects').glob('*.html')):
    parser=Page();parser.feed(p.read_text(encoding='utf-8'));pages[p.relative_to(root).as_posix()]=parser
errors=[]
for name,p in pages.items():
    if p.mains!=1 or p.h1s!=1:errors.append(f'{name}: expected one main and h1')
    if len(set(p.ids))!=len(p.ids):errors.append(f'{name}: duplicate IDs')
    for ref in p.refs:
        u=urlsplit(urljoin('https://local.test/'+name,ref))
        if u.netloc!='local.test':continue
        target=unquote(u.path.lstrip('/'))
        if not (root/target).is_file():errors.append(f'{name}: missing file {ref}')
        elif u.fragment and target in pages and unquote(u.fragment) not in pages[target].ids:errors.append(f'{name}: missing anchor {ref}')
for p in (root/'content').glob('*.json'):json.loads(p.read_text(encoding='utf-8'))
if errors:raise SystemExit('\n'.join(errors))
print(f'PASS: {len(pages)} pages, local files, anchors, unique IDs, headings, and JSON content.')
