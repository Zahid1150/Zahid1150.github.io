"""Build the portfolio from editable content and retained research pages.

Run python _build/finalize.py. Uses only the Python standard library.
"""
from pathlib import Path
from html import escape as e
import json, re

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / 'content'

def read(name):
    return json.loads((DATA / name).read_text(encoding='utf-8'))

def link(href, label, cls='text-link'):
    return f'<a class="{cls}" href="{e(href, quote=True)}">{e(label)}</a>'

def page(name, title, description, body):
    depth = '../' if '/' in name else ''
    config = read('settings.json')
    cv_url = config['cv'] if config['cv'].startswith(('/', 'https://')) else depth + config['cv']
    links = ''.join(f'<a href="{depth}{e(x["url"])}"'+(' aria-current="page"' if x['url']==name else '')+f'>{e(x["label"])}</a>' for x in config['navigation'] if x.get('visible', True))
    html = f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(title)} | Md Zahidul Islam</title><meta name="description" content="{e(description, quote=True)}">
<link rel="canonical" href="https://zahid1150.github.io/{'' if name=='index.html' else name}">
<meta property="og:title" content="{e(title)} | Md Zahidul Islam"><meta property="og:description" content="{e(description, quote=True)}"><meta property="og:image" content="https://zahid1150.github.io/images/photo.jpg"><meta property="og:type" content="website">
<link rel="icon" href="{depth}images/photo.jpg"><link rel="stylesheet" href="{depth}assets/site.css">
<script src="{depth}assets/site.js" defer></script></head><body>
<a class="skip-link" href="#main-content">Skip to content</a>
<header class="site-header"><div class="nav-wrap"><a class="brand" href="{depth}index.html">Md Zahidul Islam<span>Operations Research & Data Science</span></a>
<button class="menu-toggle" type="button" aria-expanded="false" aria-controls="site-nav"><span aria-hidden="true">☰</span> Menu</button>
<nav id="site-nav" aria-label="Main navigation">{links}<a class="nav-cv" href="{e(cv_url)}">CV ↗</a></nav></div></header>
<main id="main-content" tabindex="-1">{body}</main>
<footer class="site-footer"><div class="wrap"><div><strong>Md Zahidul Islam</strong><p>Operations Research · Data Science<br>Clemson, South Carolina</p></div><div><a href="mailto:mdzahii@clemson.edu">mdzahii@clemson.edu</a><p><a href="https://github.com/Zahid1150">GitHub</a> · <a href="https://www.linkedin.com/in/md-zahidul-islam-9a0a68129/">LinkedIn</a> · <a href="https://scholar.google.com/citations?user=Gf1KtKsAAAAJ&amp;hl=en">Google Scholar</a></p><small>© 2026 Md Zahidul Islam</small></div></div></footer>
</body></html>'''
    path=ROOT/name
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(html, encoding='utf-8')

def heading(kicker, title, description):
    return f'<div class="page-heading wrap"><p class="eyebrow">{e(kicker)}</p><h1>{e(title)}</h1><p class="intro">{e(description)}</p></div>'

def home():
    data=read('home.json'); settings=read('settings.json'); awards=read('awards.json')['items']
    selected=''.join(f'<article class="work-card"><a href="{e(x["url"])}"><div class="work-image"><img src="{e(x["image"])}" alt="{e(x["alt"])}" loading="lazy" width="640" height="360"></div><div class="work-body"><p class="eyebrow">{e(x["category"])}</p><h3>{e(x["title"])}</h3><p>{e(x["description"])}</p><span class="text-link">Explore the work →</span></div></a></article>' for x in data['featured'])
    honors=''.join(f'<div class="honor"><span class="year">{e(x["year"])}</span><h3>{e(x["title"])}</h3><p>{e(x["organization"])}</p></div>' for x in awards if x.get('featured'))
    return f'''<div class="hero-band"><section class="home-hero wrap"><div class="hero-copy"><p class="eyebrow">Clemson University · Industrial Engineering</p><h1>{e(data['headline'])}</h1><p class="hero-role">Ph.D. Candidate in Operations Research</p><p class="hero-intro">{e(data['intro'])}</p><div class="hero-actions">{link('#selected-work','Explore my work','button primary')}{link(settings['resume'],'Download resume','button')}</div><p class="availability"><span aria-hidden="true"></span>{e(data['availability'])}</p><div class="social-links">{link(settings['cv'],'Academic CV')}{link('mailto:mdzahii@clemson.edu','Email')}{link('https://scholar.google.com/citations?user=Gf1KtKsAAAAJ&hl=en','Google Scholar')}</div></div><figure class="portrait"><img src="images/photo.jpg" alt="Md Zahidul Islam" width="600" height="720" fetchpriority="high"><figcaption>Md Zahidul Islam <span>Optimization · Analytics · Decision Support</span></figcaption></figure></section></div>
<section class="section tint" id="selected-work"><div class="wrap"><div class="section-title"><div><p class="eyebrow">From models to decisions</p><h2>Selected work</h2></div>{link('projects.html','Explore all projects →')}</div><div class="work-grid">{selected}</div></div></section>
<section class="section wrap"><div class="editorial"><div><p class="eyebrow">Technical focus</p><h2>Decisions shaped by people,<br>resources, and uncertainty.</h2></div><div><p>{e(data['interests'])}</p>{link('research.html','My doctoral research →')}<div class="topics"><span>Optimization & scheduling</span><span>Machine learning</span><span>Simulation & stochastic models</span></div></div></div></section>
<section class="section tint"><div class="wrap editorial"><div><p class="eyebrow">Experience & education</p><h2>Experience across models,<br>data, and operations.</h2><p>{e(data['background'])}</p>{link('experience.html','Explore my experience →')}</div><ol class="education-mini"><li><span>Expected 2027 · Clemson University</span><h3>Ph.D., Industrial Engineering</h3><p>Operations Research</p></li><li><span>2023 · University of Tennessee, Knoxville</span><h3>M.S., Industrial Engineering</h3></li><li><span>2016 · RUET</span><h3>B.Sc., Industrial & Production Engineering</h3></li></ol></div></section>
<section class="section wrap"><div class="section-title"><div><p class="eyebrow">Recognition</p><h2>Selected honors</h2></div>{link('experience.html#honors','All honors & awards →')}</div><div class="honors-grid">{honors}</div></section>
<section class="section community-band"><div class="wrap editorial"><div><p class="eyebrow">Beyond research</p><h2>Leadership, mentoring,<br>and community.</h2></div><div><p>{e(data['community'])}</p>{link('community.html','Community & service →','button')}</div></div></section>
<section class="section wrap gallery-teaser"><div><p class="eyebrow">Gallery</p><h2>People, places, and milestones.</h2><p>Research, teaching, and community activities across Clemson and Bangladesh.</p></div>{link('gallery.html','Visit the gallery →','button')}</section>
<section class="contact-section wrap"><h2>Let’s connect.</h2><p>{e(data['availability'])}</p>{link('mailto:mdzahii@clemson.edu','mdzahii@clemson.edu ↗','contact-link')}</section>'''

def community():
    content=heading('Leadership & involvement','Community & Service','Student leadership, mentoring, and professional service in Bangladesh and the United States.')
    content+='<div class="wrap community-content">'
    for group in read('service.json')['groups']:
        content+=f'<section class="section"><div class="section-title"><h2>{e(group["title"])}</h2></div><div class="service-list">'
        for x in group['items']:
            content+=f'<article class="service-item"><p class="year">{e(x["dates"])}</p><div><h3>{e(x["role"])}</h3><p class="organization">{e(x["organization"])}</p>'
            if x.get('description'):content+=f'<p>{e(x["description"])}</p>'
            content+='</div></article>'
        content+='</div></section>'
    return content+'</div>'

def gallery():
    items=read('gallery.json')['photos']
    body=heading('Moments & milestones','Gallery','A collection of research, teaching, conference, and community moments.')
    if not items:
        return body+'<section class="wrap gallery-empty"><span class="eyebrow">The collection is growing</span><h2>Photos coming soon.</h2><p>Albums will bring together moments from Clemson, RUET, and community life in Bangladesh.</p><a class="text-link" href="community.html">Explore community & service →</a></section>'
    albums=sorted(set(x['album'] for x in items))
    body+='<section class="wrap section"><div class="gallery-filters" role="group" aria-label="Filter photos by album"><button data-album="all" aria-pressed="true">All photos</button>'
    body+=''.join(f'<button data-album="{e(a)}" aria-pressed="false">{e(a)}</button>' for a in albums)+'</div><div class="gallery-grid">'
    for x in items:
        body+=f'<figure class="gallery-item" data-album="{e(x["album"])}"><button class="photo-open" type="button" aria-label="Enlarge: {e(x["caption"])}"><img src="{e(x["image"])}" alt="{e(x["alt"])}" loading="lazy"></button><figcaption><strong>{e(x["caption"])}</strong><span>{e(x["album"])} · {e(x.get("date", ""))}</span></figcaption></figure>'
    return body+'</div></section><dialog class="photo-dialog"><button class="photo-close" autofocus>Close ×</button><img alt=""><p></p></dialog>'

def build():
    for template in (ROOT/'_site/pages').glob('**/*.html'):
        name=template.relative_to(ROOT/'_site/pages').as_posix()
        body=template.read_text(encoding='utf-8')
        title={'research.html':'Research','projects.html':'Projects','publications.html':'Publications','experience.html':'Experience & Education'}.get(name)
        if not title:
            match=re.search(r'<h1[^>]*>(.*?)</h1>',body,re.S)
            title=re.sub('<[^>]+>','',match.group(1)) if match else 'Project'
        if name=='experience.html':
            body=body.replace('<h1>Experience</h1>', '<h1>Experience & Education</h1>')
            body=body.replace('Research, teaching, industry, and leadership','Research, teaching, industry, education, and recognition')
            body+='<section class="section wrap" id="education"><h2>Education</h2><div class="service-list">'
            for x in read('education.json')['items']:
                body+=f'<article class="service-item"><p class="year">{e(x["dates"])}</p><div><h3>{e(x["degree"])}</h3><p>{e(x["institution"])}</p><p>{e(x["detail"])}</p></div></article>'
            body+='</div></section><section class="section wrap" id="honors"><h2>Honors, Fellowships & Awards</h2><div class="service-list">'
            for x in read('awards.json')['items']:
                body+=f'<article class="service-item"><p class="year">{e(x["year"])}</p><div><h3>{e(x["title"])}</h3><p class="organization">{e(x["organization"])}</p><p>{e(x["description"])}</p></div></article>'
            body+='</div></section>'
        page(name,title,'Research and professional work of Md Zahidul Islam, Ph.D. candidate at Clemson University.',body)
    page('index.html','Operations Research & Data Science','Optimization, simulation, and machine learning for healthcare, supply chains, and operational decisions.',home())
    page('community.html','Community & Service','Leadership and service at RUET, Greater Khulna Association, and Clemson University.',community())
    page('gallery.html','Gallery','Research, teaching, conferences, and community moments from Clemson and Bangladesh.',gallery())
    paths=sorted(ROOT.glob('*.html'))+sorted((ROOT/'projects').glob('*.html'))
    urls=''.join(f'<url><loc>https://zahid1150.github.io/{p.relative_to(ROOT).as_posix()}</loc></url>' for p in paths)
    (ROOT/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+urls+'</urlset>',encoding='utf-8')
    (ROOT/'robots.txt').write_text('User-agent: *\nAllow: /\nSitemap: https://zahid1150.github.io/sitemap.xml\n',encoding='utf-8')
    print(f'Built {len(paths)} pages.')

if __name__=='__main__':build()
