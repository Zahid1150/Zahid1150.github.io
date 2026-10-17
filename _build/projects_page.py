"""Generate _site/pages/projects.html from the individual project pages.

Every project is shown in full on one page, in the same format: context line,
problem, methods, findings, figures, methods & tools, and documents.
Edit a project's text in _site/pages/projects/<slug>.html and rebuild.
"""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / '_site/pages/projects'

GROUPS = [
    ('Graduate research', 'Studies from my M.S. research at the University of Tennessee Space Institute, published or presented at conferences.',
     ['learning-tsp', 'bullwhip-simulation', 'perishable-inventory-rl', 'injection-molding-scheduling']),
    ('Course and industry projects', 'Applied projects from graduate courses at Clemson and the University of Tennessee, and an industry collaboration.',
     ['ed-admission-prediction', 'mdp-physician-allocation', 'fresenius-downtime', 'bike-demand-forecasting',
      'network-interdiction', 'lagrangian-relaxation', 'facility-location-branch-and-bound', 'ludo-dqn']),
]


def parse(slug):
    t = (SRC / f'{slug}.html').read_text(encoding='utf-8')
    title = re.search(r'<h1>(.*?)</h1>', t, re.S).group(1)
    role = re.search(r'<p class="role"[^>]*>(.*?)</p>', t, re.S).group(1)
    body = t.split('<div class="wrap doc">', 1)[1].rsplit('</div>', 1)[0]
    body = body.replace('../', '')
    body = re.sub(r'<h2>(.*?)</h2>', r'<h3 class="pj-h">\1</h3>', body)
    # collect consecutive figures into one grid
    body = re.sub(r'((?:<figure>.*?</figure>\s*)+)', lambda m: '<div class="pj-figs">' + m.group(1) + '</div>', body, flags=re.S)
    return title, role, body


def build():
    out = ['<div class="band slim"><div class="wrap"><h1>Research &amp; Projects</h1>'
           '<p class="role">Optimization, machine learning, and simulation for operational decisions.</p></div></div>',
           '<div class="wrap pj-page">',
           '<section class="pj-lead"><div class="pj-lead-img"><img src="images/sched_overview.png" alt="Healthcare workforce scheduling model"></div>'
           '<div><p class="eyebrow">Doctoral research · Clemson · Ongoing</p><h2>Healthcare Workforce Planning and Scheduling</h2>'
           '<p>Preference-based and fatigue-aware optimization informed by clinician interviews, surveys, and operational requirements. '
           'Synthetic scheduling benchmarks met an average of 84–87% of weighted preference categories while satisfying all hard staffing rules.</p>'
           '<a class="text-link" href="research.html">Read about my doctoral research →</a></div></section>']
    jump = []
    secs = []
    for name, intro, slugs in GROUPS:
        arts = []
        for s in slugs:
            title, role, body = parse(s)
            jump.append(f'<a href="#{s}">{title}</a>')
            arts.append(f'<article class="pj" id="{s}"><p class="eyebrow">{role}</p><h2>{title}</h2>{body}</article>')
        secs.append(f'<section class="pj-group"><h2 class="pj-group-title">{name}</h2><p class="pj-group-intro">{intro}</p>{"".join(arts)}</section>')
    out.append('<nav class="pj-jump" aria-label="Projects on this page">' + ''.join(jump) + '</nav>')
    out += secs
    out.append('<p class="pj-foot">For citations and presentation details, see <a href="publications.html">Publications</a>.</p></div>')
    (ROOT / '_site/pages/projects.html').write_text('\n'.join(out), encoding='utf-8')


if __name__ == '__main__':
    build()
