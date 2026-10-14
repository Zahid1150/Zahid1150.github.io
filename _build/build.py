#!/usr/bin/env python3
"""Builds the static site. Run from the repository root:  python3 _build/build.py
All site content lives in this file. Every claim must trace to the master CV,
a presented abstract or poster, or text Zahid supplied."""
import os, html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
E = html.escape

SCHOLAR = "https://scholar.google.com/citations?user=Gf1KtKsAAAAJ&hl=en"
LINKEDIN = "https://www.linkedin.com/in/md-zahidul-islam-9a0a68129/"
GITHUB = "https://github.com/Zahid1150"
EMAIL = "mdzahii@clemson.edu"

CSS = """
:root{--bg:#ffffff;--fg:#1f2328;--muted:#5f6b76;--line:#e6e8eb;--accent:#0b5c86;--soft:#f5f7f9}
@media (prefers-color-scheme:dark){:root{--bg:#111418;--fg:#e6e8eb;--muted:#9aa5b1;--line:#2a3038;--accent:#6cb6e0;--soft:#181c21}}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--fg);font:17px/1.65 "Source Sans 3",system-ui,-apple-system,"Segoe UI",sans-serif}
a{color:var(--accent);text-decoration:none}
a:hover{text-decoration:underline}
.wrap{max-width:840px;margin:0 auto;padding:0 20px}
header.site{border-bottom:1px solid var(--line)}
header.site .wrap{display:flex;align-items:center;gap:22px;height:60px;overflow-x:auto}
header.site .name{font-weight:600;color:var(--fg);margin-right:auto;white-space:nowrap}
header.site nav a{color:var(--muted);white-space:nowrap;font-size:.95rem}
header.site nav a.on,header.site nav a:hover{color:var(--fg);text-decoration:none}
header.site nav{display:flex;gap:20px}
main{padding:40px 0 64px}
h1{font-size:2rem;line-height:1.2;margin:0 0 6px;font-weight:600}
h2{font-size:1.3rem;margin:48px 0 14px;font-weight:600;padding-bottom:6px;border-bottom:1px solid var(--line)}
h3{font-size:1.08rem;margin:0 0 4px;font-weight:600}
p{margin:0 0 14px}
.muted{color:var(--muted)}
.small{font-size:.92rem}
.hero{display:grid;grid-template-columns:150px 1fr;gap:32px;align-items:start}
.hero img{width:150px;height:150px;object-fit:cover;border-radius:6px}
.role{color:var(--muted);margin:0 0 16px}
.links{display:flex;flex-wrap:wrap;gap:6px 18px;margin-top:6px;font-size:.95rem}
.list{list-style:none;padding:0;margin:0}
.list>li{padding:14px 0;border-bottom:1px solid var(--line)}
.list>li:last-child{border-bottom:0}
.meta{color:var(--muted);font-size:.9rem}
.more{display:inline-block;margin-top:10px;font-size:.95rem}
.pub{padding:10px 0}
.pub .t{font-weight:600}
.badges{display:flex;flex-wrap:wrap;gap:8px;margin-top:6px}
.badge{font-size:.82rem;border:1px solid var(--line);border-radius:4px;padding:1px 8px;color:var(--muted)}
a.badge{color:var(--accent);border-color:var(--accent)}
a.badge:hover{text-decoration:none;background:var(--soft)}
.news td{padding:6px 16px 6px 0;vertical-align:top}
.news td:first-child{color:var(--muted);white-space:nowrap;font-size:.92rem}
.crumb{font-size:.92rem;margin-bottom:18px}
figure{margin:24px 0;padding:14px;border:1px solid var(--line);border-radius:6px;background:#fff}
figure img{display:block;max-width:100%;max-height:520px;margin:0 auto}
figcaption{color:#5f6b76;font-size:.88rem;margin-top:10px;text-align:center}
.facts{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin:18px 0 6px}
.facts div{background:var(--soft);border-radius:6px;padding:12px 14px}
.facts b{display:block;font-size:1.25rem}
.facts span{color:var(--muted);font-size:.88rem}
.note{background:var(--soft);border-left:3px solid var(--accent);padding:10px 14px;font-size:.93rem;color:var(--muted);margin:18px 0}
ul.tight{padding-left:20px;margin:0 0 14px}
ul.tight li{margin-bottom:6px}
footer{border-top:1px solid var(--line);padding:24px 0 40px;color:var(--muted);font-size:.9rem}
@media (max-width:640px){.hero{grid-template-columns:1fr;gap:18px}.hero img{width:120px;height:120px}.facts{grid-template-columns:1fr}h1{font-size:1.7rem}}
"""

NAV = [("index.html", "About"), ("research.html", "Research"), ("projects.html", "Projects"),
       ("publications.html", "Publications"), ("Zahid_Islam_Academic_CV.pdf", "CV")]


def page(path, title, body, active, desc="Md Zahidul Islam, Ph.D. candidate in Industrial Engineering (Operations Research), Clemson University."):
    depth = path.count("/")
    up = "../" * depth
    nav = "".join(f'<a href="{up}{h}"{" class=on" if h == active else ""}>{t}</a>' for h, t in NAV)
    out = f"""<!doctype html>
<html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{E(title)}</title>
<meta name="description" content="{E(desc)}">
<link rel="icon" href="{up}images/photo.jpg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Source+Sans+3:wght@400;600&display=swap" rel="stylesheet">
<style>{CSS}</style>
</head><body>
<header class="site"><div class="wrap"><a class="name" href="{up}index.html">Md Zahidul Islam</a><nav>{nav}</nav></div></header>
<main><div class="wrap">
{body.replace('{up}', up)}
</div></main>
<footer><div class="wrap">Md Zahidul Islam · Department of Industrial Engineering, Clemson University · <a href="mailto:{EMAIL}">{EMAIL}</a></div></footer>
</body></html>
"""
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    open(full, "w").write(out)


def badges(links):
    return '<div class="badges">' + "".join(
        f'<a class="badge" href="{E(u)}" target="_blank" rel="noopener">{E(l)}</a>' for l, u in links) + "</div>" if links else ""


# ---------------------------------------------------------------- publications
PUBS = [
    ("journal", 2024, "A scalable and adaptable supervised learning approach for solving the traveling salesman problems",
     "Lyu, Z., <b>Islam, M. Z.</b>, &amp; Yu, A. J.", "<i>IEEE Transactions on Intelligent Transportation Systems</i>, 25(11), 17092–17104",
     "https://doi.org/10.1109/TITS.2024.3410691"),
    ("conf", 2022, "An agent-based simulation model to mitigate the bullwhip effect via information sharing and risk pooling",
     "<b>Islam, M. Z.</b>, Roozeboom, N., Gunderson, P., Li, X., &amp; Yu, A. J.", "<i>2022 Winter Simulation Conference (WSC)</i>, 1636–1647. IEEE",
     "https://doi.org/10.1109/WSC57314.2022.10015288"),
    ("journal", 2021, "Stature estimation from handprint measurements: An application to the medicolegal investigation",
     "Asadujjaman, M., Hossain, M. G., Rana, M. S., &amp; <b>Islam, M. Z.</b>", "<i>Egyptian Journal of Forensic Sciences</i>, 11(1), 1–13",
     "https://doi.org/10.1186/s41935-020-00215-1"),
    ("conf", 2021, "An improved network design of an open-loop reverse supply chain",
     "Kabir, M. R., Kamal, M. S., &amp; <b>Islam, M. Z.</b>", "<i>2021 International Conference on Automation, Control and Mechatronics for Industry 4.0 (ACMI)</i>, 1–6. IEEE",
     "https://doi.org/10.1109/ACMI53878.2021.9528280"),
    ("conf", 2021, "Design and re-engineering of an automated solar lawn mower",
     "Rahul, J. K., Chakraborty, S., Khayer, N., Hriday, A. R., Mia, M. L., <b>Islam, M. Z.</b>, &amp; Ahmed, T.",
     "<i>2021 International Conference on Automation, Control and Mechatronics for Industry 4.0 (ACMI)</i>. IEEE", None),
    ("conf", 2021, "Sex identification from hand measurements using machine learning",
     "<b>Islam, M. Z.</b>, Supto, M. R., Asadujjaman, M., &amp; Chakrabortty, R. K.",
     "<i>2021 International Conference on Computing, Communication, and Intelligent Systems (ICCCIS)</i>, 536–540. IEEE",
     "https://doi.org/10.1109/ICCCIS51004.2021.9397222"),
    ("conf", 2020, "Time befitting supply chain for the future of Bangladesh apparel industry by aligning Industry 4.0",
     "Fahim, M. R. I., Chyon, F. A., Suman, M. N. H., &amp; <b>Islam, M. Z.</b>",
     "<i>International Conference on Mechanical, Industrial and Energy Engineering (ICMIEE20)</i>, Khulna, Bangladesh", None),
    ("journal", 2016, "Cost-effective decisions on service rate at a customer care centre with a multi-server queuing model",
     "Nahar, K., <b>Islam, M. Z.</b>, &amp; Islam, M. M.", "<i>Journal of Modern Science and Technology</i>, 4(1), 144–153", None),
]

TALKS = [
    ("Nov 2026", "Emergency department physician scheduling with heterogeneous individual preferences",
     "INFORMS Annual Meeting, San Francisco, CA", "Accepted talk"),
    ("Oct 2026", "Preferences, alignment, fatigue, and burnout: A cross-sectional shift-schedule survey of emergency department nurses and attending physicians",
     "Prisma Health Education and Research Institute Research Showcase", "Accepted poster"),
    ("Oct 2026", "Shift preference alignment, workload, and fatigue in emergency medicine clinicians (with C. Norton, first author)",
     "Prisma Health Education and Research Institute Research Showcase", "Accepted poster"),
    ("May 2026", "Multi-site physician scheduling incorporating work-related fatigue and individual preferences",
     "IISE Annual Conference &amp; Expo, Arlington, TX", "Talk"),
    ("Feb 2026", "Fatigue-aware multi-site rostering model for emergency department physicians with fairness and well-being constraints",
     "Healthcare Systems Process Improvement Conference, Atlanta, GA", "Talk"),
    ("Nov 2025", "The impact of emergency department shift scheduling on clinician fatigue and well-being: A qualitative study",
     "Prisma Health Education and Research Institute Showcase, Columbia, SC", "Poster"),
    ("May 2023", "Deep reinforcement learning for inventory optimization of perishable products with a quantity discount",
     "IISE Annual Conference &amp; Expo, New Orleans, LA", "Talk"),
    ("May 2023", "Unrelated parallel machine scheduling problem for plastic injection molding (with A. Owens and A. J. Yu)",
     "IISE Annual Conference &amp; Expo, New Orleans, LA", "Talk"),
]


def pub_html(p):
    kind, year, title, authors, venue, doi = p
    links = [("DOI", doi)] if doi else []
    return f'<div class="pub"><div class="t">{E(title)}</div><div class="a">{authors} ({year}). {venue}.</div>{badges(links)}</div>'


# ---------------------------------------------------------------- projects
# fields: slug, title, label, line (one-sentence summary), facts [(value,label)], overview, approach[], results[], note, tools, figure (src, caption), docs [(label,url)]
PROJECTS = [
    dict(slug="bullwhip-simulation", title="Agent-Based Simulation of the Bullwhip Effect",
         label="Research · UT Space Institute · Winter Simulation Conference 2022",
         line="AnyLogic simulation showing how information sharing and risk pooling reduce order amplification in a multi-stage supply chain.",
         facts=[("46.3%", "lower order-to-demand variance at the factory"), ("49.3%", "lower variance at the wholesaler"), ("WSC 2022", "peer-reviewed proceedings")],
         overview="Small changes in customer demand grow into large swings in orders as they move up a supply chain (the bullwhip effect). This study tested two strategies for damping those swings.",
         approach=["Built an agent-based supply chain simulation in AnyLogic.",
                   "Compared information sharing, risk pooling, and the two combined."],
         results=["With both strategies combined, simulated order-to-demand variance fell by 46.3% at the factory and 49.3% at the wholesaler."],
         tools="AnyLogic, agent-based simulation", docs=[("Paper (DOI)", "https://doi.org/10.1109/WSC57314.2022.10015288")]),
    dict(slug="learning-tsp", title="Learning-Based Optimization for the Traveling Salesman Problem",
         label="Research · UT Space Institute · IEEE Transactions on Intelligent Transportation Systems, 2024",
         line="Co-authored a supervised-learning approach that guides exact and heuristic solvers on large routing problems.",
         facts=[("28%", "shorter tours than a graph pointer-network baseline"), ("59%", "less runtime on 1,000-node instances"), ("IEEE T-ITS", "journal article")],
         overview="Large traveling salesman problems are slow to solve exactly. This work trains a model to predict which parts of a high-quality tour are likely, then uses those predictions to guide solution methods.",
         approach=["Supervised learning predicts structural components of high-quality solutions.",
                   "The predictions are integrated with exact and heuristic solution methods."],
         results=["Published benchmarks showed 28% shorter tours with 59% less runtime than a graph pointer-network baseline on 1,000-node instances."],
         note="Collaborative work; I am the second author.",
         tools="Supervised learning, combinatorial optimization", docs=[("Paper (DOI)", "https://doi.org/10.1109/TITS.2024.3410691")]),
    dict(slug="perishable-inventory-rl", title="Deep Reinforcement Learning for Perishable Inventory",
         label="Research · UT Space Institute · IISE Annual Conference 2023",
         line="Reinforcement-learning ordering policies for perishable products with stochastic demand, deterioration, and quantity discounts.",
         overview="Perishable products lose value over time, so ordering too much creates waste and ordering too little creates shortages. Quantity discounts add a further trade-off.",
         approach=["Developed reinforcement-learning policies for a perishable inventory system with stochastic demand, product deterioration, and quantity discounts."],
         results=["Presented at the IISE Annual Conference & Expo, New Orleans, May 2023."],
         tools="Deep reinforcement learning, Python"),
    dict(slug="injection-molding-scheduling", title="Production Scheduling for Plastic Injection Molding",
         label="Research · UT Space Institute · IISE Annual Conference 2023",
         line="Mixed-integer model for scheduling jobs on parallel molding machines under resource limits, using a manufacturer's data.",
         overview="A plastics manufacturer needed to assign jobs to parallel injection-molding machines that differ in capability, while respecting shared resource limits.",
         approach=["Collaborated on a resource-constrained, unrelated parallel-machine scheduling formulation (mixed-integer linear program).",
                   "Solved it with Gurobi using data from the manufacturer."],
         results=["Presented at the IISE Annual Conference & Expo, New Orleans, May 2023 (with A. Owens and A. J. Yu)."],
         tools="MILP, Gurobi"),
    dict(slug="ed-admission-prediction", title="Predicting Emergency Department Admissions",
         label="Graduate class project · Applied Data Science, Clemson University, Spring 2025",
         line="Compared five classifiers on 347,360 emergency department visits using structured data and chief-complaint text.",
         facts=[("347,360", "visits in the analysis dataset"), ("550", "features (50 structured + 500 text)"), ("0.863", "best ROC-AUC (CatBoost)")],
         overview="Knowing early which emergency department patients will be admitted helps hospitals plan beds and staff. This project predicted admission versus discharge from triage-time information in the MIMIC-IV-ED research database.",
         approach=["Joined the ED stay, triage, and patient tables and cleaned 425,011 initial visits down to 347,360.",
                   "Combined 50 structured predictors with 500 TF-IDF features from chief-complaint text.",
                   "Compared logistic regression, random forest, XGBoost, CatBoost, and LightGBM on an 80/20 stratified split with three-fold cross-validated grid search.",
                   "Evaluated ROC-AUC, precision, recall, F1, confusion matrices, threshold behavior, and feature importance."],
         results=["CatBoost reached the best ROC-AUC (0.863), compared with 0.853 for logistic regression."],
         note="Course-project results on a retrospective, single-institution dataset; not externally validated or used clinically.",
         tools="Python, pandas, scikit-learn, XGBoost, CatBoost, LightGBM",
         figure=("images/ed_roc.jpg", "ROC curves for the five tuned models, from the project report."),
         docs=[("Project report (PDF)", "docs/ED_Admission_Prediction_Report.pdf")]),
    dict(slug="bike-demand-forecasting", title="Bike-Sharing Demand Forecasting",
         label="Graduate class project · team project with A. Hines",
         line="Forecast hourly bike rentals in Seoul with neural networks, an LSTM, XGBoost, and random forest.",
         facts=[("≈0.96", "test R² for the tuned neural network"), ("0.91", "test R² before tuning"), ("4", "model families compared")],
         overview="Bike-sharing systems need to know how many bikes will be rented each hour. This project forecast hourly demand in Seoul from weather, time of day, season, holidays, and whether the system was operating.",
         approach=["Compared an artificial neural network, a PyTorch LSTM on sliding-window sequences, XGBoost, and random forest.",
                   "Tuned the neural network with Ray Tune, XGBoost with staged grid search, and random forest with GridSearchCV.",
                   "Used correlation and feature-importance analysis to identify what drives demand."],
         results=["Tuning raised the neural network's test R² from 0.91 to about 0.96."],
         note="Team project; results reflect the team's work.",
         tools="Python, PyTorch, Ray Tune, XGBoost, scikit-learn",
         figure=("images/bike_fit.jpg", "Predicted versus actual hourly demand on the test set."),
         docs=[("Final presentation (PDF)", "docs/Bike_Sharing_Forecasting_Presentation.pdf")]),
    dict(slug="mdp-physician-allocation", title="Dynamic Physician Allocation with Markov Decision Processes",
         label="Graduate class project · Clemson University",
         line="When should a physician switch between critical and mild-patient queues? Solved as a Markov decision process four ways.",
         facts=[("336", "states"), ("9", "actions"), ("4", "solution methods compared")],
         overview="An emergency department must decide, as patients arrive, how to divide physicians between critical and mild-patient queues. Waiting is costlier for critical patients, but mild patients also accumulate.",
         approach=["Modeled the problem as a discounted Markov decision process, uniformizing a continuous-time queueing model with class-specific arrival rates, service rates, holding costs, and congestion penalties.",
                   "Solved a 336-state, 9-action instance by value iteration, policy iteration, modified policy iteration, and a Gurobi dual linear program."],
         results=["Compared the methods on runtime, iteration counts, value functions, and policy agreement."],
         tools="Python, dynamic programming, Gurobi"),
    dict(slug="network-interdiction", title="Network Interdiction for Wildlife Trafficking",
         label="Graduate class project · IE 8700, Clemson University, Fall 2023",
         line="Which routes should enforcement block to make trafficking of poached tiger parts as hard as possible?",
         facts=[("29", "nodes"), ("68", "edges"), ("2", "model variants")],
         overview="Poached tiger parts move through local transportation networks before reaching international markets. This project asked which links enforcement should block, under a limited budget, to lengthen traffickers' best route or raise their chance of detection.",
         approach=["Formulated bilevel shortest-path interdiction models with a travel-distance variant and a detection-probability variant.",
                   "Converted them to single-level models with dualization and a logarithmic transformation, and solved them in Gurobi.",
                   "Built a synthetic case study based on the geography of Bandhavgarh Tiger Reserve in Python with NetworkX and Matplotlib."],
         results=["Compared which routes were blocked and the resulting objective values across interdiction budgets."],
         note="An illustrative case study, not observed trafficking data.",
         tools="Python, NetworkX, Matplotlib, Gurobi",
         figure=("images/interdiction.jpg", "Case-study network; blocked arcs shown in red."),
         docs=[("Project report (PDF)", "docs/Network_Interdiction_Report.pdf")]),
    dict(slug="facility-location-branch-and-bound", title="Facility Location with a Custom Branch-and-Bound",
         label="Graduate class project · MATH 8120, Clemson University, Fall 2024",
         line="Built a branch-and-bound solver from scratch and benchmarked it against an integer solver and the LP relaxation.",
         overview="The uncapacitated facility location problem decides which facilities to open and how to assign customers to them. The goal of the project was to implement and study the branch-and-bound algorithm itself.",
         approach=["Implemented the integer model, its LP relaxation, and a custom branch-and-bound routine in MATLAB with Gurobi.",
                   "Included fractional-variable branching, variable fixing, incumbent comparison, and node counting."],
         results=["Benchmarked five random instances from 10 to 50 facilities, comparing objective values, runtimes, and nodes visited."],
         note="A study in algorithm design and benchmarking, not a claim of beating a commercial solver.",
         tools="MATLAB, Gurobi"),
    dict(slug="lagrangian-relaxation", title="Lagrangian Relaxation with Subgradient Updates",
         label="Graduate class project · team project",
         line="Relaxed hard resource constraints and tuned a subgradient method to get bounds and feasible schedules.",
         overview="Some scheduling models are hard because of constraints that link time periods through shared resources. Lagrangian relaxation moves those constraints into the objective with penalty multipliers, making the rest of the problem easier.",
         approach=["Relaxed time-indexed resource constraints with nonnegative multipliers.",
                   "Updated the multipliers with a subgradient method and decreasing step size over 200 iterations, tracking bounds and recovered feasible solutions."],
         results=["Showed how step size affects convergence: some settings failed to converge, others slowed progress or produced feasible solutions less often.",
                  "Benchmarked against the original formulation and an LP-relaxation bound."],
         note="Team project with J. Wu and M. Ren.",
         tools="Lagrangian relaxation, subgradient optimization",
         docs=[("Project report (PDF)", "docs/Lagrangian_Relaxation_Report.pdf")]),
    dict(slug="fresenius-downtime", title="Reducing Production Downtime at Fresenius Medical Care",
         label="Team project with Fresenius Medical Care",
         line="Analyzed equipment effectiveness on automated production lines and proposed a failure-reporting system.",
         overview="Automated production lines for dialysis products (Bibag) had low overall equipment effectiveness (OEE). The team looked for where the losses came from.",
         approach=["Analyzed four months of company-provided production data.",
                   "Split OEE into availability, performance, and quality, and attributed breakdowns to failure modes."],
         results=["Proposed an integrated failure-reporting system, standardized data entry, a supporting database, and standard operating procedures."],
         note="International team project. Improvement figures on the poster are projections under stated assumptions, not realized results.",
         tools="Production data analysis, OEE, process improvement",
         figure=("images/fresenius_poster.jpg", "Team poster."),
         docs=[("Poster (PDF)", "docs/Fresenius_Downtime_Poster.pdf")]),
    dict(slug="ludo-dqn", title="Deep Q-Network Agent for the Board Game Ludo",
         label="Team project · University of Tennessee, Knoxville",
         line="Trained a reinforcement-learning agent to play Ludo and tested how design choices affect it.",
         overview="Ludo mixes chance (dice) with strategy, which makes it a useful test for reinforcement learning.",
         approach=["Adapted a Ludo environment and a Deep Q-Network agent with epsilon-greedy exploration, experience replay, and local and target networks.",
                   "Compared processed and raw state representations, action-selection designs, reward shaping, network depth, learning rate, and discount factor."],
         results=["Reward and architecture changes improved some aspects of performance, but overall agent performance fell short of expectations."],
         note="Team project with S. N. B. Tushar and A. Muhury; I led the agent and execution modules.",
         tools="Python, deep Q-learning",
         docs=[("Project report (PDF)", "docs/Ludo_DQN_Report.pdf")]),
]


def project_page(p):
    facts = ""
    if p.get("facts"):
        facts = '<div class="facts">' + "".join(f"<div><b>{E(v)}</b><span>{E(l)}</span></div>" for v, l in p["facts"]) + "</div>"
    fig = ""
    if p.get("figure"):
        src, cap = p["figure"]
        fig = f'<figure><img src="{{up}}{src}" alt="{E(cap)}"><figcaption>{E(cap)}</figcaption></figure>'
    docs = ""
    if p.get("docs"):
        docs = "<h2>Documents</h2>" + badges([(l, (u if u.startswith("http") else "{up}" + u)) for l, u in p["docs"]])
    note = f'<div class="note">{E(p["note"])}</div>' if p.get("note") else ""
    body = f"""<div class="crumb"><a href="{{up}}projects.html">← All projects</a></div>
<h1>{E(p['title'])}</h1>
<p class="muted">{E(p['label'])}</p>
{facts}
<h2>Problem</h2><p>{E(p['overview'])}</p>
<h2>What I did</h2><ul class="tight">{''.join(f'<li>{E(x)}</li>' for x in p['approach'])}</ul>
<h2>Results</h2><ul class="tight">{''.join(f'<li>{E(x)}</li>' for x in p['results'])}</ul>
{note}
{fig}
<p class="small muted"><b>Tools:</b> {E(p['tools'])}</p>
{docs}"""
    page(f"projects/{p['slug']}.html", f"{p['title']} | Md Zahidul Islam", body, "projects.html", p["line"])


def project_item(p):
    return f"""<li><h3><a href="{{up}}projects/{p['slug']}.html">{E(p['title'])}</a></h3>
<div class="meta">{E(p['label'])}</div><div>{E(p['line'])}</div></li>"""


# ---------------------------------------------------------------- research page
RESEARCH = """<h1>Research</h1>
<p>My doctoral research asks how emergency department schedules can be built to meet staffing needs while protecting clinicians from fatigue and burnout. It combines optimization models with evidence collected from the clinicians themselves through interviews, surveys, and wearable-device data.</p>
<div class="note">This work is part of a CDC/NIOSH-funded, multi-institution project with Prisma Health, Clemson University, Wake Forest University School of Medicine, and the University of Central Florida. Advisor: Dr. Kevin M. Taaffe.</div>

<h2 id="scheduling">Optimization models for physician scheduling</h2>
<p>Emergency physicians in a multi-hospital system rotate across sites, work nights and weekends, and have individual preferences. I build models that produce schedules meeting every hard staffing rule while balancing fatigue, fairness, and those preferences.</p>
<ul class="tight">
<li>Turned clinician and hospital requirements into multi-site scheduling models (mixed-integer and constraint programming) covering staffing levels, eligibility, credentials, rest, fatigue, fairness, and individual preferences.</li>
<li>Implemented the models in Python with Gurobi and Google OR-Tools and compared solution approaches for large instances on a high-performance computing cluster.</li>
<li>Built a bi-objective model that trades clinician fatigue against schedule quality and fairness for physicians rotating across multiple hospitals over a 90-day planning horizon. Fatigue is scored with a shift fatigue index based on chronotype misalignment, shift end time, and shift length.</li>
<li>With Dr. Kevin Taaffe and Dr. Hervé Kerivin: a model in which each physician distributes 100 points across preference categories (nights, weekends, protected days, work blocks, shift types, and others); the points become physician-specific weights in the objective.</li>
</ul>
<p><b>Result so far:</b> on synthetic benchmarks with 25 to 75 physicians, schedules met an average of 84–87% of each physician's weighted preference categories while satisfying all hard staffing rules.</p>
<p class="small muted">Presented at the Healthcare Systems Process Improvement Conference (Feb 2026) and the IISE Annual Conference (May 2026); accepted talk at the INFORMS Annual Meeting (Nov 2026).</p>

<h2 id="interviews">Interview study: how schedules shape fatigue</h2>
<figure><img src="{up}images/interview_poster.jpg" alt="Interview study poster"><figcaption>Poster, Prisma Health Research Showcase, November 2025.</figcaption></figure>
<p>Semi-structured interviews with 13 physicians and 18 nurses at three Prisma Health emergency departments explored how shift length, timing, distribution, and flexibility affect fatigue, burnout, and well-being. Transcripts were coded with codebooks developed by the team, with interrater reliability assessed on a dual-coded subset.</p>
<ul class="tight">
<li>Both groups linked fatigue to unpredictable shifts, high workload, and insufficient recovery.</li>
<li>Nurses tended to prefer 12-hour shifts for fewer workdays but reported fatigue after long stretches; physicians tended to prefer 9–10-hour shifts and rotations that fit their body clock.</li>
<li>The findings informed the survey questions and the scheduling models.</li>
</ul>
<div class="badges"><a class="badge" href="{up}docs/Interview_Study_Poster_2025.pdf" target="_blank" rel="noopener">Poster (PDF)</a><span class="badge">Manuscript in preparation</span></div>

<h2 id="survey">Survey study: preferences, schedule fit, and burnout</h2>
<figure><img src="{up}images/survey_poster.jpg" alt="Survey study poster"><figcaption>Poster accepted for the Prisma Health Research Showcase, October 2026.</figcaption></figure>
<p>A survey of 103 nurses and 57 attending physicians at seven Prisma Health emergency departments (March–May 2026) compared scheduling preferences, recovery needs, and the link between schedule fit and burnout.</p>
<ul class="tight">
<li>Nurses most often preferred 12-hour shifts; physicians most often preferred 9-hour shifts.</li>
<li>76% of clinicians preferred shifts longer than the point at which they begin to feel tired.</li>
<li>Clinicians reported needing more time off after more consecutive shifts and after night shifts.</li>
<li>Schedules that better matched clinicians' preferences were associated with lower burnout and fatigue, after accounting for profession, age, and work hours.</li>
</ul>
<div class="badges"><a class="badge" href="{up}docs/Survey_Study_Poster_2026.pdf" target="_blank" rel="noopener">Poster (PDF)</a><span class="badge">Manuscript in preparation</span></div>

<h2 id="llm">Large language models for qualitative analysis</h2>
<p>With S. V. Abrol, V. Prabhu, and K. M. Taaffe, I am evaluating how well large language models perform inductive thematic analysis of healthcare interviews. Using 18 emergency department nurse interviews and a human-developed codebook of 47 codes, we compare Claude Sonnet and Opus at medium and high reasoning-effort settings on conceptual alignment, code coverage, coding specificity, and higher-order interpretation.</p>
<ul class="tight">
<li>Preliminary results: the four model configurations together captured 93.6% of the human codes, and the best single configuration captured 83.0%.</li>
<li>Larger models generally covered more codes, but the models struggled with higher-order themes about schedule satisfaction and alignment.</li>
<li>My role: reviewing and refining human–model code mappings, evaluating prompting approaches, designing the inter-rater reliability assessment, and computing agreement statistics.</li>
</ul>
<div class="badges"><span class="badge">Ongoing · manuscript in preparation</span></div>

<h2 id="earlier">Earlier research</h2>
<p>At the University of Tennessee Space Institute (2021–2022) I worked on supply chain simulation, learning-based routing, perishable inventory, and production scheduling. See the <a href="{up}projects.html">projects page</a>.</p>
"""

# ---------------------------------------------------------------- home page
HOME = f"""<div class="hero">
<img src="{{up}}images/photo.jpg" alt="Md Zahidul Islam">
<div>
<h1>Md Zahidul Islam</h1>
<p class="role">Ph.D. Candidate, Industrial Engineering (Operations Research)<br>Clemson University</p>
<p>I build optimization, simulation, and machine-learning models that turn operational requirements and data into decisions. My doctoral research designs emergency physician schedules for a multi-hospital health system that meet staffing rules while accounting for fatigue, fairness, and individual preferences.</p>
<div class="links">
<a href="{{up}}Zahid_Islam_Resume.pdf">Resume</a>
<a href="{{up}}Zahid_Islam_Academic_CV.pdf">Academic CV</a>
<a href="{SCHOLAR}">Google Scholar</a>
<a href="{LINKEDIN}">LinkedIn</a>
<a href="{GITHUB}">GitHub</a>
<a href="mailto:{EMAIL}">{EMAIL}</a>
</div>
</div></div>

<h2>Research interests</h2>
<p>Healthcare operations and workforce scheduling · mixed-integer and constraint programming · simulation · machine learning for operations · supply chains.</p>
<p class="small muted">Expected Ph.D.: December 2027. Seeking 2027 internships in operations research and data science.</p>

<h2>News</h2>
<table class="news">
<tr><td>Nov 2026</td><td>Talk accepted at the INFORMS Annual Meeting on physician scheduling with individual preferences.</td></tr>
<tr><td>Oct 2026</td><td>Survey study poster accepted at the Prisma Health Research Showcase.</td></tr>
<tr><td>May 2026</td><td>Presented multi-site physician scheduling at the IISE Annual Conference.</td></tr>
<tr><td>2026</td><td>Clemson INFORMS student chapter received the INFORMS Magna Cum Laude award, during my term as president.</td></tr>
</table>

<h2>Current research</h2>
<ul class="list">
<li><h3><a href="{{up}}research.html#scheduling">Optimization models for physician scheduling</a></h3><div>Multi-site schedules balancing coverage, fatigue, fairness, and preferences.</div></li>
<li><h3><a href="{{up}}research.html#interviews">Interview study: how schedules shape fatigue</a></h3><div>31 clinicians at three emergency departments.</div></li>
<li><h3><a href="{{up}}research.html#survey">Survey study: preferences, schedule fit, and burnout</a></h3><div>160 clinicians at seven emergency departments.</div></li>
<li><h3><a href="{{up}}research.html#llm">Large language models for qualitative analysis</a></h3><div>How well do LLMs reproduce human thematic coding?</div></li>
</ul>
<a class="more" href="{{up}}research.html">Research details →</a>

<h2>Selected projects</h2>
<ul class="list">{''.join(project_item(p) for p in PROJECTS if p['slug'] in ('learning-tsp','bullwhip-simulation','ed-admission-prediction','bike-demand-forecasting','network-interdiction'))}</ul>
<a class="more" href="{{up}}projects.html">All projects →</a>

<h2>Selected publications</h2>
{''.join(pub_html(p) for p in PUBS[:2])}
<a class="more" href="{{up}}publications.html">All publications and talks →</a>

<h2>Teaching and service</h2>
<ul class="tight">
<li>Lecturer and Assistant Professor, Industrial &amp; Production Engineering, RUET, Bangladesh (2019–2021): Probability and Statistics, Operations Management, Industrial Simulation.</li>
<li>Lecturer, Ahsanullah University of Science and Technology, Bangladesh (2017–2018).</li>
<li>Graduate Teaching Assistant, Clemson University and University of Tennessee (2022–2024).</li>
<li>President, Clemson University INFORMS Student Chapter (2025–2026); co-host of the <i>Optimality Gap</i> podcast.</li>
<li>Undergraduate research mentor for twelve students across five disciplines, Clemson Creative Inquiry (2025–present).</li>
<li>Peer reviewer: <i>Journal of Big Data</i>, <i>Scientific Reports</i>, <i>BMC Medical Imaging</i>.</li>
</ul>

<h2>Education</h2>
<ul class="tight">
<li><b>Ph.D., Industrial Engineering</b> (Operations Research), Clemson University, expected Dec 2027. GPA 3.90/4.00.</li>
<li><b>M.S., Industrial Engineering</b>, University of Tennessee, Knoxville, 2023. GPA 4.00/4.00.</li>
<li><b>B.Sc., Industrial &amp; Production Engineering</b>, Rajshahi University of Engineering &amp; Technology, 2016. First in class; University Gold Medal and Prime Minister Gold Medal.</li>
</ul>
"""


def main():
    page("index.html", "Md Zahidul Islam | Operations Research & Data Science", HOME, "index.html")
    page("research.html", "Research | Md Zahidul Islam", RESEARCH, "research.html")
    groups = [("Research projects", [p for p in PROJECTS if p["label"].startswith("Research")]),
              ("Graduate and industry projects", [p for p in PROJECTS if not p["label"].startswith("Research")])]
    body = "<h1>Projects</h1><p class=\"muted\">Click a project for details, figures, and documents. Current doctoral work is on the <a href=\"{up}research.html\">research page</a>.</p>"
    for name, ps in groups:
        body += f"<h2>{name}</h2><ul class=\"list\">{''.join(project_item(p) for p in ps)}</ul>"
    page("projects.html", "Projects | Md Zahidul Islam", body, "projects.html")
    for p in PROJECTS:
        project_page(p)
    pubs = "<h1>Publications</h1><p class=\"muted\">Citation counts on <a href=\"" + SCHOLAR + "\">Google Scholar</a>.</p>"
    pubs += "<h2>Journal articles</h2>" + "".join(pub_html(p) for p in PUBS if p[0] == "journal")
    pubs += "<h2>Conference proceedings</h2>" + "".join(pub_html(p) for p in PUBS if p[0] == "conf")
    pubs += "<h2>Talks and posters</h2><table class=\"news\">" + "".join(
        f"<tr><td>{d}</td><td><b>{E(t)}</b><br><span class=\"muted\">{v} · {k}</span></td></tr>" for d, t, v, k in TALKS) + "</table>"
    page("publications.html", "Publications | Md Zahidul Islam", pubs, "publications.html")



# ================================================================ v3 design (overrides above)
CSS = """
:root{--bg:#f5f6fa;--card:#fff;--fg:#1b2133;--muted:#5d6577;--line:#e3e6ee;--navy:#16213e;--purple:#522d80;--orange:#e8590c;--orange-soft:#fff1e8;--chip:#eef0f7}
@media (prefers-color-scheme:dark){:root{--bg:#0f1320;--card:#171c2c;--fg:#e8eaf2;--muted:#a2a9bb;--line:#272e44;--orange:#ff8a4c;--orange-soft:#2a1c14;--chip:#202741}}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;background:var(--bg);color:var(--fg);font:16.5px/1.65 Inter,system-ui,-apple-system,"Segoe UI",sans-serif}
a{color:var(--orange);text-decoration:none}
a:hover{text-decoration:underline}
h1,h2,h3{font-family:"Plus Jakarta Sans",Inter,sans-serif;line-height:1.2;letter-spacing:-.01em}
.wrap{max-width:1080px;margin:0 auto;padding:0 20px}
header.site{position:sticky;top:0;z-index:10;background:color-mix(in srgb,var(--navy) 94%,transparent);backdrop-filter:blur(6px)}
header.site .wrap{display:flex;align-items:center;gap:22px;height:58px;overflow-x:auto}
header.site .name{font-family:"Plus Jakarta Sans",sans-serif;font-weight:700;color:#fff;margin-right:auto;white-space:nowrap}
header.site nav{display:flex;gap:22px}
header.site nav a{color:#c7cbe0;font-size:.93rem;font-weight:500;white-space:nowrap}
header.site nav a.on,header.site nav a:hover{color:#fff;text-decoration:none}
.band{background:linear-gradient(120deg,var(--navy) 0%,#2b2a5e 55%,var(--purple) 100%);color:#fff;padding:56px 0 60px}
.band.slim{padding:40px 0 48px}
.band h1{font-size:clamp(2rem,4.6vw,2.9rem);margin:0 0 8px}
.band .role{color:#d9dcf0;font-size:1.08rem;margin:0 0 16px}
.band p{color:#e9eaf6;max-width:640px}
.band a{color:#fff}
.hero{display:grid;grid-template-columns:190px 1fr;gap:40px;align-items:center}
.hero img{width:190px;height:190px;border-radius:50%;object-fit:cover;border:4px solid rgba(255,255,255,.85);box-shadow:0 10px 30px rgba(0,0,0,.3)}
.btns{display:flex;flex-wrap:wrap;gap:10px;margin-top:22px}
.btn{display:inline-block;padding:9px 18px;border-radius:8px;font-weight:600;font-size:.92rem;border:1px solid rgba(255,255,255,.4);color:#fff}
.btn:hover{text-decoration:none;background:rgba(255,255,255,.1)}
.btn.primary{background:var(--orange);border-color:var(--orange)}
.btn.primary:hover{filter:brightness(1.08);background:var(--orange)}
.stats{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;margin-top:-56px;position:relative}
.stat{background:var(--card);border-radius:12px;padding:18px 20px;box-shadow:0 6px 20px rgba(22,33,62,.08);border:1px solid var(--line)}
.stat b{display:block;font-family:"Plus Jakarta Sans",sans-serif;font-size:1.7rem;color:var(--purple)}
@media (prefers-color-scheme:dark){.stat b{color:#b79cf0}}
.stat span{color:var(--muted);font-size:.88rem}
section{padding:56px 0 8px}
section h2{font-size:1.75rem;margin:0 0 6px}
.lede{color:var(--muted);margin:0 0 24px;max-width:700px}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(310px,1fr));gap:20px}
.grid.two{grid-template-columns:repeat(auto-fill,minmax(440px,1fr))}
.card{background:var(--card);border:1px solid var(--line);border-radius:12px;overflow:hidden;display:flex;flex-direction:column;color:var(--fg);transition:transform .15s,box-shadow .15s}
a.card:hover{text-decoration:none;transform:translateY(-3px);box-shadow:0 12px 28px rgba(22,33,62,.12)}
.thumb{height:170px;background:#fff;display:flex;align-items:center;justify-content:center;border-bottom:1px solid var(--line);overflow:hidden;padding:10px}
.thumb img{max-width:100%;max-height:150px;object-fit:contain}
.thumb.art{background:linear-gradient(135deg,#f3f0fa,#fdf1ea)}
@media (prefers-color-scheme:dark){.thumb.art{background:linear-gradient(135deg,#221d36,#2a1d17)}}
.thumb svg{width:70%;height:120px}
.thumb .s{stroke:var(--purple);fill:none;stroke-width:2.2}
.thumb .f{fill:var(--orange)}
.thumb .m{fill:#c9bfdc}
.thumb .ms{stroke:#c9bfdc;fill:none;stroke-width:2}
.cbody{padding:18px 20px 20px;display:flex;flex-direction:column;flex:1}
.tag{align-self:flex-start;font-size:.72rem;font-weight:700;letter-spacing:.04em;text-transform:uppercase;color:var(--purple);background:var(--chip);padding:3px 9px;border-radius:999px}
@media (prefers-color-scheme:dark){.tag{color:#c9b5f5}}
.card h3{font-size:1.12rem;margin:10px 0 6px}
.card p{margin:0;color:var(--muted);font-size:.94rem}
.go{margin-top:auto;padding-top:14px;color:var(--orange);font-weight:600;font-size:.9rem}
.pubs{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:6px 24px}
.pub{padding:14px 0;border-bottom:1px solid var(--line)}
.pub:last-child{border-bottom:0}
.pub .t{font-weight:600}
.pub .a{color:var(--muted);font-size:.93rem}
.badges{display:flex;flex-wrap:wrap;gap:8px;margin-top:8px}
.badge{font-size:.8rem;font-weight:600;border:1px solid var(--line);border-radius:999px;padding:3px 11px;color:var(--muted)}
a.badge{color:var(--orange);border-color:var(--orange)}
a.badge:hover{text-decoration:none;background:var(--orange-soft)}
.cols{display:grid;grid-template-columns:1fr 1fr;gap:20px}
.panel{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:22px 24px}
.panel h3{margin:0 0 10px;font-size:1.15rem}
.panel ul{padding-left:18px;margin:0}
.panel li{margin-bottom:8px}
.news{width:100%;border-collapse:collapse}
.news td{padding:9px 14px 9px 0;vertical-align:top;border-bottom:1px solid var(--line)}
.news tr:last-child td{border-bottom:0}
.news td:first-child{color:var(--purple);font-weight:600;white-space:nowrap;font-size:.9rem;width:96px}
@media (prefers-color-scheme:dark){.news td:first-child{color:#c9b5f5}}
.doc>*{max-width:860px}
.doc h2{font-size:1.35rem;margin:36px 0 10px}
.doc ul{padding-left:20px}
.doc li{margin-bottom:6px}
.crumb a{color:#d9dcf0;font-size:.92rem}
.facts{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin:-36px 0 8px;position:relative}
figure{margin:26px 0;padding:14px;border:1px solid var(--line);border-radius:12px;background:#fff}
figure img{display:block;max-width:100%;max-height:560px;margin:0 auto}
figcaption{color:#5d6577;font-size:.88rem;margin-top:10px;text-align:center}
.note{background:var(--orange-soft);border-left:3px solid var(--orange);padding:10px 14px;border-radius:0 8px 8px 0;font-size:.93rem;margin:18px 0}
.small{font-size:.92rem}.muted{color:var(--muted)}
footer{margin-top:64px;background:var(--navy);color:#c7cbe0;padding:28px 0;font-size:.9rem}
footer a{color:#fff}
@media (max-width:760px){.hero{grid-template-columns:1fr;gap:20px}.hero img{width:130px;height:130px}.stats{grid-template-columns:repeat(2,1fr)}.cols,.grid.two{grid-template-columns:1fr}.facts{grid-template-columns:1fr}}
"""

ART = {
 "network": '<svg viewBox="0 0 200 100"><g class="ms"><path d="M30 70 L70 30 L120 55 L170 25 M70 30 L100 85 L120 55 M30 70 L100 85"/></g><g class="f"><circle cx="30" cy="70" r="7"/><circle cx="70" cy="30" r="7"/><circle cx="120" cy="55" r="7"/><circle cx="170" cy="25" r="7"/><circle cx="100" cy="85" r="7"/></g></svg>',
 "tour": '<svg viewBox="0 0 200 100"><path class="s" d="M25 60 L55 20 L105 15 L160 30 L180 70 L130 88 L70 85 Z"/><g class="f"><circle cx="25" cy="60" r="5"/><circle cx="55" cy="20" r="5"/><circle cx="105" cy="15" r="5"/><circle cx="160" cy="30" r="5"/><circle cx="180" cy="70" r="5"/><circle cx="130" cy="88" r="5"/><circle cx="70" cy="85" r="5"/></g></svg>',
 "stock": '<svg viewBox="0 0 200 100"><path class="s" d="M15 25 L55 75 L55 25 L95 75 L95 25 L135 75 L135 25 L175 75"/><line class="ms" x1="10" y1="80" x2="190" y2="80"/><g class="f"><rect x="160" y="10" width="26" height="10" rx="2"/></g></svg>',
 "gantt": '<svg viewBox="0 0 200 100"><g class="m"><rect x="20" y="18" width="50" height="14" rx="3"/><rect x="90" y="43" width="60" height="14" rx="3"/><rect x="40" y="68" width="40" height="14" rx="3"/></g><g class="f"><rect x="75" y="18" width="70" height="14" rx="3"/><rect x="20" y="43" width="60" height="14" rx="3"/><rect x="90" y="68" width="80" height="14" rx="3"/></g></svg>',
 "states": '<svg viewBox="0 0 200 100"><g class="ms"><circle cx="45" cy="50" r="24"/><circle cx="155" cy="50" r="24"/></g><path class="s" d="M70 40 Q100 15 130 40 M130 60 Q100 85 70 60"/><g class="f"><circle cx="45" cy="50" r="7"/><circle cx="155" cy="50" r="7"/></g></svg>',
 "facility": '<svg viewBox="0 0 200 100"><g class="ms"><path d="M100 50 L40 20 M100 50 L40 80 M100 50 L60 50 M160 30 L185 15 M160 30 L185 50"/></g><g class="m"><circle cx="40" cy="20" r="6"/><circle cx="40" cy="80" r="6"/><circle cx="60" cy="50" r="6"/><circle cx="185" cy="15" r="6"/><circle cx="185" cy="50" r="6"/></g><g class="f"><rect x="90" y="40" width="20" height="20" rx="3"/><rect x="150" y="20" width="20" height="20" rx="3"/></g></svg>',
 "converge": '<svg viewBox="0 0 200 100"><path class="s" d="M10 85 Q40 20 60 60 T100 40 T140 45 T190 42"/><line class="ms" stroke-dasharray="5 4" x1="10" y1="40" x2="190" y2="40"/><circle class="f" cx="190" cy="42" r="5"/></svg>',
 "dice": '<svg viewBox="0 0 200 100"><rect class="s" x="40" y="20" width="56" height="56" rx="10"/><rect class="s" x="110" y="30" width="56" height="56" rx="10"/><g class="f"><circle cx="56" cy="36" r="5"/><circle cx="68" cy="48" r="5"/><circle cx="80" cy="60" r="5"/><circle cx="126" cy="46" r="5"/><circle cx="150" cy="46" r="5"/><circle cx="126" cy="70" r="5"/><circle cx="150" cy="70" r="5"/></g></svg>',
 "schedule": '<svg viewBox="0 0 200 100"><g class="m"><rect x="20" y="15" width="30" height="18" rx="3"/><rect x="100" y="15" width="30" height="18" rx="3"/><rect x="60" y="41" width="30" height="18" rx="3"/><rect x="140" y="41" width="30" height="18" rx="3"/><rect x="20" y="67" width="30" height="18" rx="3"/><rect x="140" y="67" width="30" height="18" rx="3"/></g><g class="f"><rect x="60" y="15" width="30" height="18" rx="3"/><rect x="140" y="15" width="30" height="18" rx="3"/><rect x="20" y="41" width="30" height="18" rx="3"/><rect x="100" y="41" width="30" height="18" rx="3"/><rect x="60" y="67" width="30" height="18" rx="3"/><rect x="100" y="67" width="30" height="18" rx="3"/></g></svg>',
 "llm": '<svg viewBox="0 0 200 100"><rect class="s" x="18" y="18" width="70" height="64" rx="8"/><g class="m"><rect x="30" y="32" width="46" height="6"/><rect x="30" y="46" width="36" height="6"/><rect x="30" y="60" width="42" height="6"/></g><path class="s" d="M98 50 L120 50"/><g class="f"><rect x="130" y="24" width="52" height="14" rx="7"/><rect x="130" y="43" width="42" height="14" rx="7"/><rect x="130" y="62" width="48" height="14" rx="7"/></g></svg>',
}
THUMB = {"bullwhip-simulation":"network","learning-tsp":"tour","perishable-inventory-rl":"stock","injection-molding-scheduling":"gantt",
 "mdp-physician-allocation":"states","facility-location-branch-and-bound":"facility","lagrangian-relaxation":"converge","ludo-dqn":"dice"}


def thumb_html(p):
    if p.get("figure"):
        return f'<div class="thumb"><img src="{{up}}{p["figure"][0]}" alt="" loading="lazy"></div>'
    return f'<div class="thumb art" aria-hidden="true">{ART[THUMB[p["slug"]]]}</div>'


SHORT = {"learning-tsp": "IEEE T-ITS 2024", "bullwhip-simulation": "WSC 2022", "perishable-inventory-rl": "IISE 2023", "injection-molding-scheduling": "IISE 2023"}


def short_label(p):
    if p["slug"] in SHORT:
        return SHORT[p["slug"]]
    l = p["label"]
    return l.split(" · ")[0] if not l.startswith("Research") else l.split(" · ")[-1]


def project_item(p):
    return f"""<a class="card" href="{{up}}projects/{p['slug']}.html">{thumb_html(p)}<div class="cbody">
<span class="tag">{E(short_label(p))}</span><h3>{E(p['title'])}</h3><p>{E(p['line'])}</p><span class="go">Details →</span></div></a>"""


def page(path, title, body, active, desc="Md Zahidul Islam, Ph.D. candidate in Industrial Engineering (Operations Research), Clemson University."):
    up = "../" * path.count("/")
    nav = "".join(f'<a href="{up}{h}"{" class=on" if h == active else ""}>{t}</a>' for h, t in NAV)
    out = f"""<!doctype html>
<html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{E(title)}</title>
<meta name="description" content="{E(desc)}">
<link rel="icon" href="{up}images/photo.jpg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Plus+Jakarta+Sans:wght@600;700&display=swap" rel="stylesheet">
<style>{CSS}</style>
</head><body>
<header class="site"><div class="wrap"><a class="name" href="{up}index.html">Md Zahidul Islam</a><nav>{nav}</nav></div></header>
{body.replace('{up}', up)}
<footer><div class="wrap">Md Zahidul Islam · Department of Industrial Engineering, Clemson University · <a href="mailto:{EMAIL}">{EMAIL}</a></div></footer>
</body></html>
"""
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    open(full, "w").write(out)


def band(title, sub, crumb=""):
    c = f'<div class="crumb">{crumb}</div>' if crumb else ""
    return f'<div class="band slim"><div class="wrap">{c}<h1>{E(title)}</h1><p class="role" style="margin:0">{sub}</p></div></div>'


def project_page(p):
    facts = ""
    if p.get("facts"):
        facts = '<div class="facts">' + "".join(f'<div class="stat"><b>{E(v)}</b><span>{E(l)}</span></div>' for v, l in p["facts"]) + "</div>"
    fig = ""
    if p.get("figure"):
        src, cap = p["figure"]
        fig = f'<figure><img src="{{up}}{src}" alt="{E(cap)}"><figcaption>{E(cap)}</figcaption></figure>'
    docs = ""
    if p.get("docs"):
        docs = "<h2>Documents</h2>" + badges([(l, (u if u.startswith("http") else "{up}" + u)) for l, u in p["docs"]])
    note = f'<div class="note">{E(p["note"])}</div>' if p.get("note") else ""
    body = band(p["title"], E(p["label"]), '<a href="{up}projects.html">← All projects</a>') + f"""
<div class="wrap doc">{facts}
<h2>Problem</h2><p>{E(p['overview'])}</p>
<h2>What I did</h2><ul>{''.join(f'<li>{E(x)}</li>' for x in p['approach'])}</ul>
<h2>Results</h2><ul>{''.join(f'<li>{E(x)}</li>' for x in p['results'])}</ul>
{note}{fig}
<p class="small muted"><b>Tools:</b> {E(p['tools'])}</p>
{docs}</div>"""
    page(f"projects/{p['slug']}.html", f"{p['title']} | Md Zahidul Islam", body, "projects.html", p["line"])


def rcard(anchor, tag, title, text, img=None, art=None):
    th = f'<div class="thumb"><img src="{{up}}{img}" alt="" loading="lazy"></div>' if img else f'<div class="thumb art" aria-hidden="true">{ART[art]}</div>'
    return f'<a class="card" href="{{up}}research.html#{anchor}">{th}<div class="cbody"><span class="tag">{tag}</span><h3>{title}</h3><p>{text}</p><span class="go">Read more →</span></div></a>'


RCARDS = "".join([
    rcard("scheduling", "Optimization", "Physician scheduling models", "Multi-site schedules that meet every staffing rule while balancing fatigue, fairness, and individual preferences.", art="schedule"),
    rcard("interviews", "Qualitative study", "How schedules shape fatigue", "Interviews with 31 nurses and physicians at three emergency departments.", img="images/interview_poster.jpg"),
    rcard("survey", "Survey study", "Preferences, schedule fit, and burnout", "Survey of 160 clinicians at seven emergency departments.", img="images/survey_poster.jpg"),
    rcard("llm", "Large language models", "LLMs for thematic analysis", "How well do large language models reproduce human coding of healthcare interviews?", art="llm"),
])

SELECTED = ['ed-admission-prediction', 'bike-demand-forecasting', 'network-interdiction', 'learning-tsp', 'bullwhip-simulation', 'fresenius-downtime']

HOME = f"""<div class="band"><div class="wrap"><div class="hero">
<img src="{{up}}images/photo.jpg" alt="Md Zahidul Islam">
<div>
<h1>Md Zahidul Islam</h1>
<p class="role">Ph.D. Candidate, Industrial Engineering (Operations Research) · Clemson University</p>
<p>I build optimization, simulation, and machine-learning models that turn operational requirements and data into decisions. My doctoral research designs emergency physician schedules for a multi-hospital health system that meet staffing rules while accounting for fatigue, fairness, and individual preferences.</p>
<div class="btns">
<a class="btn primary" href="{{up}}Zahid_Islam_Resume.pdf">Resume</a>
<a class="btn primary" href="{{up}}Zahid_Islam_Academic_CV.pdf">Academic CV</a>
<a class="btn" href="{SCHOLAR}">Google Scholar</a>
<a class="btn" href="{LINKEDIN}">LinkedIn</a>
<a class="btn" href="{GITHUB}">GitHub</a>
<a class="btn" href="mailto:{EMAIL}">Email</a>
</div></div></div></div></div>

<div class="wrap">
<div class="stats">
<div class="stat"><b>8</b><span>peer-reviewed publications</span></div>
<div class="stat"><b>3.90</b><span>Ph.D. GPA, Clemson University</span></div>
<div class="stat"><b>12</b><span>undergraduate researchers mentored</span></div>
<div class="stat"><b>Dec 2027</b><span>expected Ph.D.; seeking 2027 internships</span></div>
</div>

<section><h2>Research</h2>
<p class="lede">Scheduling emergency department clinicians so that hospitals stay covered and clinicians stay rested. Part of a CDC/NIOSH-funded, multi-institution project with Prisma Health.</p>
<div class="grid two">{RCARDS}</div></section>

<section><h2>Selected projects</h2>
<p class="lede">Research and graduate projects in optimization, simulation, and machine learning. Open a project for methods, results, figures, and documents.</p>
<div class="grid">{''.join(project_item(p) for p in PROJECTS if p['slug'] in SELECTED)}</div>
<p style="margin-top:18px"><a href="{{up}}projects.html"><b>All 12 projects →</b></a></p></section>

<section><h2>Publications</h2>
<p class="lede">Eight peer-reviewed publications. <a href="{{up}}publications.html">Full list with talks and posters →</a></p>
<div class="pubs">{''.join(pub_html(p) for p in PUBS[:4])}</div></section>

<section><h2>News</h2>
<div class="panel"><table class="news">
<tr><td>Nov 2026</td><td>Talk accepted at the INFORMS Annual Meeting on physician scheduling with individual preferences.</td></tr>
<tr><td>Oct 2026</td><td>Survey study poster accepted at the Prisma Health Research Showcase.</td></tr>
<tr><td>May 2026</td><td>Presented multi-site physician scheduling at the IISE Annual Conference.</td></tr>
<tr><td>2026</td><td>Clemson INFORMS student chapter received the INFORMS Magna Cum Laude award during my term as president.</td></tr>
</table></div></section>

<section><h2>Teaching, service, and education</h2>
<div class="cols">
<div class="panel"><h3>Teaching and service</h3><ul>
<li>Lecturer and Assistant Professor, Industrial &amp; Production Engineering, RUET, Bangladesh (2019–2021): Probability and Statistics, Operations Management, Industrial Simulation.</li>
<li>Lecturer, Ahsanullah University of Science and Technology, Bangladesh (2017–2018).</li>
<li>Graduate Teaching Assistant, Clemson University and University of Tennessee (2022–2024).</li>
<li>President, Clemson University INFORMS Student Chapter (2025–2026); co-host of the <i>Optimality Gap</i> podcast.</li>
<li>Mentor to twelve undergraduate researchers across five disciplines, Clemson Creative Inquiry.</li>
<li>Peer reviewer: <i>Journal of Big Data</i>, <i>Scientific Reports</i>, <i>BMC Medical Imaging</i>.</li>
</ul></div>
<div class="panel"><h3>Education</h3><ul>
<li><b>Ph.D., Industrial Engineering</b> (Operations Research), Clemson University, expected Dec 2027. GPA 3.90/4.00. Advisor: Dr. Kevin M. Taaffe.</li>
<li><b>M.S., Industrial Engineering</b>, University of Tennessee, Knoxville, 2023. GPA 4.00/4.00.</li>
<li><b>B.Sc., Industrial &amp; Production Engineering</b>, Rajshahi University of Engineering &amp; Technology, 2016. First in class.</li>
</ul>
<h3 style="margin-top:18px">Honors</h3><ul>
<li>Dr. Lloyd W. Crawford Fellowship, UT Space Institute (2021)</li>
<li>University Gold Medal, RUET (2019); Prime Minister Gold Medal, Bangladesh (2018)</li>
</ul></div>
</div></section>
</div>
"""


def main():
    page("index.html", "Md Zahidul Islam | Operations Research & Data Science", HOME, "index.html")
    rb = RESEARCH.replace("<h1>Research</h1>\n", "", 1)
    page("research.html", "Research | Md Zahidul Islam",
         band("Research", "Emergency department scheduling, clinician fatigue, and well-being") + f'<div class="wrap doc">{rb}</div>', "research.html")
    groups = [("Research projects", [p for p in PROJECTS if p["label"].startswith("Research")]),
              ("Graduate and industry projects", [p for p in PROJECTS if not p["label"].startswith("Research")])]
    body = band("Projects", 'Open a project for methods, results, figures, and documents. Current doctoral work is on the <a href="{up}research.html">research page</a>.') + '<div class="wrap">'
    for name, ps in groups:
        body += f'<section><h2>{name}</h2><div class="grid">{"".join(project_item(p) for p in ps)}</div></section>'
    page("projects.html", "Projects | Md Zahidul Islam", body + "</div>", "projects.html")
    for p in PROJECTS:
        project_page(p)
    pubs = band("Publications", f'Eight peer-reviewed publications · <a href="{SCHOLAR}">Google Scholar</a>') + '<div class="wrap">'
    pubs += '<section><h2>Journal articles</h2><div class="pubs">' + "".join(pub_html(p) for p in PUBS if p[0] == "journal") + "</div></section>"
    pubs += '<section><h2>Conference proceedings</h2><div class="pubs">' + "".join(pub_html(p) for p in PUBS if p[0] == "conf") + "</div></section>"
    pubs += '<section><h2>Talks and posters</h2><div class="panel"><table class="news">' + "".join(
        f'<tr><td>{d}</td><td><b>{E(t)}</b><br><span class="muted">{v} · {k}</span></td></tr>' for d, t, v, k in TALKS) + "</table></div></section></div>"
    page("publications.html", "Publications | Md Zahidul Islam", pubs, "publications.html")



# ================================================================ v4 content (overrides above)
CSS += """
.skills{display:flex;flex-wrap:wrap;gap:6px;margin-top:12px}
.sk{font-size:.76rem;font-weight:500;color:var(--fg);background:var(--chip);border-radius:6px;padding:2px 8px}
.card p.long{color:var(--fg);opacity:.86}
.skillgrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:16px}
.skillgrid .panel h3{font-size:1.02rem;margin-bottom:10px}
.intro{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:22px 26px;margin-bottom:22px}
.intro p:last-child{margin-bottom:0}
.figs{display:grid;grid-template-columns:1fr 1fr;gap:14px}
.figs figure{margin:14px 0}
.doc h3{font-size:1.12rem;margin:26px 0 8px}
@media (max-width:760px){.figs{grid-template-columns:1fr}}
"""


def skills_html(items):
    return '<div class="skills">' + "".join(f'<span class="sk">{E(x)}</span>' for x in items) + "</div>"


BLURB = {
 "bullwhip-simulation": "Built an agent-based supply chain simulation in AnyLogic to test two ways of damping the bullwhip effect. Combining information sharing with risk pooling reduced simulated order-to-demand variance by 46.3% at the factory and 49.3% at the wholesaler.",
 "learning-tsp": "Co-authored a supervised-learning method that predicts parts of a high-quality tour and feeds those predictions to exact and heuristic solvers. Published benchmarks showed 28% shorter tours with 59% less runtime than a graph pointer-network baseline on 1,000-node instances.",
 "perishable-inventory-rl": "Developed reinforcement-learning ordering policies for perishable products whose value decays over time, under random demand and quantity discounts that reward ordering more. Presented at the IISE Annual Conference in 2023.",
 "injection-molding-scheduling": "Collaborated on a mixed-integer model that assigns jobs to injection-molding machines with different capabilities under shared resource limits, solved in Gurobi with a plastics manufacturer's data. Presented at the IISE Annual Conference in 2023.",
 "ed-admission-prediction": "Predicted admission versus discharge for 347,360 emergency department visits by combining 50 structured triage variables with 500 text features from chief complaints. Compared five classifiers with cross-validated tuning; CatBoost reached the best ROC-AUC (0.863).",
 "bike-demand-forecasting": "Forecast hourly bike rentals in Seoul from weather, time, season, and holiday features, comparing a neural network, an LSTM, XGBoost, and random forest. Hyperparameter tuning raised the neural network's test R² from 0.91 to about 0.96.",
 "mdp-physician-allocation": "Modeled how to split physicians between critical and mild-patient queues as a Markov decision process built from a queueing model. Solved a 336-state instance with value iteration, policy iteration, modified policy iteration, and linear programming, and compared the results.",
 "network-interdiction": "Built bilevel optimization models that choose which routes to block, under a budget, to disrupt trafficking of poached tiger parts. Reformulated them to single-level models and compared blocked routes across budgets on a case study based on Bandhavgarh Tiger Reserve.",
 "facility-location-branch-and-bound": "Implemented a branch-and-bound algorithm from scratch for the uncapacitated facility location problem in MATLAB with Gurobi, and benchmarked it against the integer solver and LP relaxation on instances with 10 to 50 facilities.",
 "lagrangian-relaxation": "Relaxed hard resource constraints in a scheduling model with Lagrange multipliers and updated them with a subgradient method over 200 iterations. Studied how the step size affects convergence, bounds, and how often feasible schedules are recovered.",
 "fresenius-downtime": "Analyzed four months of production data from automated dialysis-product lines, breaking equipment effectiveness into availability, performance, and quality losses by failure mode. Proposed a failure-reporting system, a supporting database, and standard operating procedures.",
 "ludo-dqn": "Trained a Deep Q-Network agent to play Ludo and tested how state representation, reward shaping, network depth, and learning parameters affect it. Some changes helped, but overall performance fell short of expectations.",
}
SKILLS = {
 "bullwhip-simulation": ["Agent-Based Simulation", "AnyLogic", "Supply Chain Analysis", "Scenario Analysis"],
 "learning-tsp": ["Supervised Learning", "Combinatorial Optimization", "Routing", "Heuristics"],
 "perishable-inventory-rl": ["Deep Reinforcement Learning", "Inventory Optimization", "Stochastic Modeling", "Python"],
 "injection-molding-scheduling": ["Mixed-Integer Linear Programming", "Production Scheduling", "Gurobi"],
 "ed-admission-prediction": ["Python", "pandas", "scikit-learn", "Gradient Boosting", "Text Features (TF-IDF)", "Cross-Validation", "Healthcare Data"],
 "bike-demand-forecasting": ["Time-Series Forecasting", "PyTorch", "LSTM", "XGBoost", "Hyperparameter Tuning", "Ray Tune"],
 "mdp-physician-allocation": ["Markov Decision Processes", "Dynamic Programming", "Queueing Theory", "Linear Programming", "Gurobi"],
 "network-interdiction": ["Bilevel Optimization", "Duality", "Network Models", "Gurobi", "NetworkX"],
 "facility-location-branch-and-bound": ["Branch and Bound", "Integer Programming", "LP Relaxation", "MATLAB", "Gurobi"],
 "lagrangian-relaxation": ["Lagrangian Relaxation", "Subgradient Optimization", "Integer Programming"],
 "fresenius-downtime": ["Production Data Analysis", "OEE", "Process Improvement", "Failure-Mode Analysis"],
 "ludo-dqn": ["Deep Q-Learning", "Reinforcement Learning", "Python"],
}


def project_item(p):
    return f"""<a class="card" href="{{up}}projects/{p['slug']}.html">{thumb_html(p)}<div class="cbody">
<span class="tag">{E(short_label(p))}</span><h3>{E(p['title'])}</h3><p class="long">{E(BLURB[p['slug']])}</p>{skills_html(SKILLS[p['slug']])}<span class="go">Details →</span></div></a>"""


_old_project_page = project_page


def project_page(p):
    _old_project_page(p)
    f = os.path.join(ROOT, "projects", p["slug"] + ".html")
    t = open(f).read()
    tools = f'<p class="small muted"><b>Tools:</b> {E(p["tools"])}</p>'
    assert tools in t
    t = t.replace(tools, tools + "<h2>Skills</h2>" + skills_html(SKILLS[p["slug"]]), 1)
    open(f, "w").write(t)


RESEARCH_INTRO = """<p>My research develops data-driven, fatigue-aware, and preference-based optimization models for healthcare workforce scheduling, with a focus on emergency department physicians and nurses. I combine operations research, mathematical optimization, statistical analysis, and human-factors research to understand how shift schedules affect clinicians' fatigue, sleep, recovery, burnout, and well-being, and to build schedules that account for them.</p>
<p>The work is part of a CDC/NIOSH-funded, multi-institution project with Prisma Health, Clemson University, Wake Forest University School of Medicine, and the University of Central Florida. I bring together evidence from clinician interviews, surveys, historical work schedules, wearable sleep monitoring, and physiological measurements, and use it to design scheduling approaches that meet clinical staffing requirements while balancing individual preferences, fairness, and fatigue-related risk, in support of clinician well-being, patient safety, and efficient operations.</p>"""

RESEARCH = f"""<div class="intro">{RESEARCH_INTRO}<p class="small muted">Advisor: Dr. Kevin M. Taaffe, Clemson University.</p></div>

<h2 id="scheduling">Optimization models for emergency physician scheduling</h2>
<p>Prisma Health's emergency physicians rotate among seven emergency department locations. Every schedule has to keep each department staffed around the clock while respecting credentials, rest rules, and leave, and it also shapes how tired physicians get, how fairly nights and weekends are shared, and how well each person's life fits around work. I am working on two connected scheduling problems.</p>
<figure style="max-width:520px"><img src="{{up}}images/multi_hospital.jpg" alt="Illustration of one physician working across several hospitals"><figcaption>Physicians in a hospital network work at several sites, often far from home.</figcaption></figure>

<h3 id="preferences">1. Scheduling with individually weighted preferences</h3>
<p>With Dr. Kevin Taaffe and Dr. Hervé Kerivin, and in partnership with Prisma Health, I am building a mixed-integer model in which physicians say not only what they prefer but how much each preference matters to them. Each physician distributes a fixed budget of points across scheduling features such as night shifts, weekend shifts, protected days off, work blocks and recovery after them, shift type, early and late shifts, runs of the same shift type, and paired weekends. More points on a feature means that feature matters more, and the points become physician-specific weights in the objective.</p>
<ul>
<li>Hard constraints enforce shift coverage, availability, workload targets, overtime limits, one shift per day, minimum rest, and no backward shift rotations.</li>
<li>Violations are measured two ways: whether an undesired event happened, and how far a count (for example, nights in a month) exceeds the physician's preferred limit.</li>
<li>On synthetic benchmarks with 25 to 75 physicians, schedules met an average of 84–87% of each physician's weighted preference categories while satisfying all hard staffing rules.</li>
</ul>
<p class="small muted">Accepted talk, INFORMS Annual Meeting, November 2026 · manuscript in preparation.</p>
{{skills1}}

<h3 id="fatigue">2. Fatigue-aware multi-site rostering</h3>
<p>This model builds three-month schedules for physicians across a multi-hospital network with the explicit goal of reducing fatigue. Fatigue is scored with a Shift Fatigue Index that combines how well a shift matches the physician's chronotype (body clock), when the shift ends, and how long it is. The model minimizes total fatigue alongside penalties for unfair sharing of night, weekend, and distant-hospital shifts, departures from shift-bundling or spreading preferences, and over- or under-time.</p>
<ul>
<li>Hard rules guarantee coverage, at most one shift per day, vacation and request-off days, protected rest after nights, and no night shifts at distant hospitals.</li>
<li>The interview study shaped the model: themes such as batching versus spreading shifts, recovery after nights, fair sharing of undesirable shifts, and chronotype fit became constraints and penalties.</li>
<li>On synthetic instances built to reflect real operations (including a case with 80 physicians across four nearby departments), the model produced feasible rosters that met coverage while lowering total fatigue, extending recovery after nights, shortening long runs of workdays, and sharing night, weekend, and distant shifts more evenly.</li>
<li>I implemented the models in Python with Gurobi and Google OR-Tools and ran large instances on a high-performance computing cluster. A bi-objective version makes the trade-off between fatigue and schedule quality explicit, giving decision-makers a range of options rather than a single schedule.</li>
<li>I have presented this work to emergency physicians for feedback. Data collection on sleep and fatigue is ongoing and will be used to calibrate the fatigue measure.</li>
</ul>
<div class="figs">
<figure><img src="{{up}}images/roster_heatmap.jpg" alt="Roster heatmap for 20 physicians over 30 days"><figcaption>Roster for 20 of 80 physicians over 30 days, colored by shift type (synthetic instance).</figcaption></figure>
<figure><img src="{{up}}images/schedule_fatigue.jpg" alt="Schedules and fatigue scores over time for five physicians"><figcaption>Schedules and fatigue scores over a month for five physicians (synthetic instance).</figcaption></figure>
</div>
<p class="small muted">Presented at the Healthcare Systems Process Improvement Conference (Feb 2026) and the IISE Annual Conference (May 2026).</p>
{{skills2}}

<h2 id="interviews">Interview study: how schedules shape fatigue</h2>
<p>To ground the models in clinicians' experience, I led a qualitative study with 13 physicians and 18 nurses (including seven leaders) at three Prisma Health emergency departments. I co-designed the interview guide, conducted 30-minute semi-structured interviews on ideal schedules, recovery, nights and weekends, flexibility, and what a "fatigue-optimized" schedule would look like, and coded transcripts with codebooks the team developed (6 nurse categories with 40+ codes; 16 physician categories with 150+ sub-codes), checking interrater reliability on a dual-coded subset.</p>
<ul>
<li>Both groups linked fatigue to unpredictable shifts, high workload, and insufficient recovery, and saw control, consistency, and recovery time as essential.</li>
<li>Nurses tended to prefer 12-hour shifts for fewer workdays but reported fatigue after long stretches; physicians tended to prefer 9–10-hour shifts and rotations aligned with their body clock.</li>
<li>The findings informed the survey questions and the scheduling models.</li>
</ul>
<figure style="max-width:620px"><img src="{{up}}images/interview_poster.jpg" alt="Interview study poster"><figcaption>Poster, Prisma Health Research Showcase, November 2025.</figcaption></figure>
<div class="badges"><a class="badge" href="{{up}}docs/Interview_Study_Poster_2025.pdf" target="_blank" rel="noopener">Poster (PDF)</a><span class="badge">Manuscript in preparation</span></div>
{{skills3}}

<h2 id="survey">Survey study: preferences, schedule fit, and burnout</h2>
<p>I led a cross-sectional survey of 103 nurses and 57 attending physicians at seven Prisma Health general, pediatric, and psychiatric emergency departments (March–May 2026). It measured preferred shift length, block length, and night shifts and the reasons behind them; when fatigue sets in during a shift; time off needed to recover; how well clinicians' recent schedules matched their preferences; burnout; physical, mental, and emotional fatigue; sleep; and chronotype.</p>
<ul>
<li>Nurses most often preferred 12-hour shifts (67%); physicians most often preferred 9-hour shifts (49%).</li>
<li>76% of clinicians preferred shifts that last beyond the point at which they begin to feel tired (a median of 2 hours longer).</li>
<li>Clinicians reported needing more time off after more consecutive shifts and after night shifts.</li>
<li>Schedules that better matched clinicians' preferences were associated with lower burnout and fatigue after adjusting for profession, age, and work hours; associations with burnout and emotional fatigue held after also adjusting for sleep, chronotype, and shift types.</li>
</ul>
<figure style="max-width:720px"><img src="{{up}}images/survey_poster.jpg" alt="Survey study poster"><figcaption>Poster accepted for the Prisma Health Research Showcase, October 2026.</figcaption></figure>
<div class="badges"><a class="badge" href="{{up}}docs/Survey_Study_Poster_2026.pdf" target="_blank" rel="noopener">Poster (PDF)</a><span class="badge">Manuscript in preparation</span></div>
{{skills4}}

<h2 id="llm">Large language models for qualitative analysis</h2>
<p>With S. V. Abrol, V. Prabhu, and K. M. Taaffe, I am evaluating how well large language models can perform inductive thematic analysis of healthcare interviews. Using the 18 nurse interviews and a human-developed reference codebook of 47 codes, we compare Claude Sonnet and Opus at medium and high reasoning-effort settings on conceptual alignment, code coverage, coding specificity, and whether the models reproduce higher-order human interpretations.</p>
<ul>
<li>Preliminary results: the four model configurations together captured 93.6% of the human codes, and the best single configuration captured 83.0%.</li>
<li>Larger models generally covered more codes, but the models struggled with higher-order themes about schedule satisfaction and alignment.</li>
<li>My role: reviewing and refining human–model code mappings, evaluating prompting and analysis approaches, designing the inter-rater reliability assessment, computing agreement statistics, and contributing to validation and the manuscript.</li>
</ul>
<div class="badges"><span class="badge">Ongoing · manuscript in preparation</span></div>
{{skills5}}

<h2 id="earlier">Earlier research</h2>
<p>At the University of Tennessee Space Institute (2021–2022) I worked on supply chain simulation, learning-based routing, perishable inventory, and production scheduling. See the <a href="{{up}}projects.html">projects page</a>.</p>
"""
RSK = {
 "skills1": ["Mixed-Integer Linear Programming", "Preference Modeling", "Multi-Criteria Optimization", "Gurobi", "Python", "Workforce Scheduling"],
 "skills2": ["Mixed-Integer Linear Programming", "Constraint Programming (CP-SAT)", "Multi-Objective Optimization", "Fatigue Modeling", "Gurobi", "Google OR-Tools", "HPC / SLURM"],
 "skills3": ["Qualitative Research", "Interview Design", "Thematic Analysis", "Inter-Rater Reliability", "Stakeholder Engagement"],
 "skills4": ["Survey Design", "Regression Analysis", "Hypothesis Testing", "Statistical Analysis", "Data Visualization"],
 "skills5": ["Large Language Models", "Prompt Design", "Inter-Rater Agreement", "Qualitative Coding", "Evaluation Design"],
}
for k, v in RSK.items():
    RESEARCH = RESEARCH.replace("{" + k + "}", skills_html(v))


def rcard(anchor, tag, title, text, sk, img=None, art=None):
    th = f'<div class="thumb"><img src="{{up}}{img}" alt="" loading="lazy"></div>' if img else f'<div class="thumb art" aria-hidden="true">{ART[art]}</div>'
    return f'<a class="card" href="{{up}}research.html#{anchor}">{th}<div class="cbody"><span class="tag">{tag}</span><h3>{title}</h3><p class="long">{text}</p>{skills_html(sk)}<span class="go">Read more →</span></div></a>'


RCARDS = "".join([
    rcard("preferences", "Optimization", "Physician scheduling with weighted preferences",
          "A mixed-integer model in which each physician distributes a budget of points across scheduling features, so the schedule reflects both what they prefer and how much it matters. Schedules met 84–87% of weighted preferences on synthetic 25–75-physician benchmarks while meeting all staffing rules.",
          RSK["skills1"][:4], img="images/multi_hospital.jpg"),
    rcard("fatigue", "Optimization", "Fatigue-aware multi-site rostering",
          "Three-month schedules across a hospital network that minimize a Shift Fatigue Index built from chronotype fit, shift end time, and shift length, while sharing nights, weekends, and distant shifts fairly. Presented at HSPI and IISE 2026.",
          RSK["skills2"][:4], img="images/roster_heatmap.jpg"),
    rcard("interviews", "Qualitative study", "How schedules shape clinician fatigue",
          "Semi-structured interviews with 13 physicians and 18 nurses at three emergency departments, coded into team-built codebooks. The themes became constraints and penalties in the scheduling models.",
          RSK["skills3"][:4], img="images/interview_poster.jpg"),
    rcard("survey", "Survey study", "Preferences, schedule fit, and burnout",
          "A survey of 160 nurses and physicians at seven emergency departments. Clinicians whose schedules better matched their preferences reported lower burnout and fatigue.",
          RSK["skills4"][:4], img="images/survey_poster.jpg"),
    rcard("llm", "Large language models", "LLMs for thematic analysis",
          "Testing whether large language models can reproduce human coding of nurse interviews. Four model configurations together recovered 93.6% of a 47-code human codebook, but missed higher-order themes.",
          RSK["skills5"][:4], art="llm"),
])

SKILL_GROUPS = [
 ("Optimization", ["Mixed-Integer Linear Programming", "Constraint Programming (CP-SAT)", "Multi-Objective Optimization", "Lagrangian Relaxation", "Branch and Bound", "Bilevel Optimization", "Dynamic Programming", "Markov Decision Processes", "Queueing Theory", "Workforce Scheduling"]),
 ("Machine learning and statistics", ["Supervised Learning", "Gradient Boosting (XGBoost, CatBoost, LightGBM)", "Neural Networks and LSTM", "Time-Series Forecasting", "Deep Reinforcement Learning", "Text Features (TF-IDF)", "Regression Analysis", "Hypothesis Testing", "Design of Experiments"]),
 ("Simulation", ["Agent-Based Simulation", "Discrete-Event Simulation", "AnyLogic", "Arena"]),
 ("Human-centered research", ["Survey Design", "Semi-Structured Interviews", "Thematic Analysis", "Inter-Rater Reliability", "Wearable and Physiological Data", "LLM Evaluation"]),
 ("Software and tools", ["Python", "NumPy", "pandas", "scikit-learn", "PyTorch", "TensorFlow", "Gurobi", "Google OR-Tools", "CPLEX", "MATLAB", "R", "SQL", "Git", "SLURM / HPC"]),
]
SKILLS_SECTION = '<section><h2>Skills</h2><p class="lede">Methods and tools used across my research and projects.</p><div class="skillgrid">' + "".join(
    f'<div class="panel"><h3>{n}</h3>{skills_html(v)}</div>' for n, v in SKILL_GROUPS) + "</div></section>"

import re as _re
HOME = _re.sub(r'<div class="stats">.*?</div>\n</div>\n', '', HOME, count=1, flags=_re.S)
HOME = _re.sub(r'(<section><h2>Research</h2>).*?(</section>)',
               lambda m: m.group(1) + '<div class="intro" style="margin-top:6px">' + RESEARCH_INTRO + '</div><div class="grid">' + RCARDS + '</div>' + m.group(2),
               HOME, count=1, flags=_re.S)
HOME = HOME.replace('<section><h2>Publications</h2>', SKILLS_SECTION + '<section><h2>Publications</h2>', 1)


HOME = _re.sub(r'(<section><h2>Selected projects</h2>.*?<div class="grid">).*?(</div>\n<p style)',
               lambda m: m.group(1) + "".join(project_item(p) for p in PROJECTS if p["slug"] in SELECTED) + m.group(2),
               HOME, count=1, flags=_re.S)


# ================================================================ v5: experience page
NAV = [("index.html", "About"), ("research.html", "Research"), ("experience.html", "Experience"), ("projects.html", "Projects"),
       ("publications.html", "Publications"), ("Zahid_Islam_Academic_CV.pdf", "CV")]
CSS += """
.tl{position:relative;padding-left:26px;border-left:2px solid var(--line);margin-left:6px}
.job{position:relative;margin-bottom:22px}
.job:before{content:"";position:absolute;left:-34px;top:24px;width:12px;height:12px;border-radius:50%;background:var(--orange);border:3px solid var(--bg)}
.job .head{display:flex;flex-wrap:wrap;justify-content:space-between;gap:4px 16px;align-items:baseline}
.job h3{margin:0;font-size:1.12rem}
.job .when{color:var(--purple);font-weight:600;font-size:.9rem;white-space:nowrap}
@media (prefers-color-scheme:dark){.job .when{color:#c9b5f5}}
.job .org{color:var(--muted);margin:2px 0 10px}
.job ul{padding-left:18px;margin:0}
.job li{margin-bottom:6px}
"""

JOBS = [
 ("Research", [
  ("Graduate Research Assistant", "Department of Industrial Engineering, Clemson University · Clemson, SC", "Jan 2025 – Present", [
    "Lead doctoral researcher on a CDC/NIOSH-funded, multi-institution scheduling project with Prisma Health, collaborating with faculty in industrial engineering, psychology, emergency medicine, and sleep science.",
    "Translated clinician and hospital requirements into multi-site workforce scheduling models (MILP and CP-SAT) covering staffing levels, eligibility, credentials, rest, fatigue, fairness, and individual preferences.",
    "Implemented the models in Python with Gurobi and Google OR-Tools and compared solution approaches for large instances on a high-performance computing cluster; schedules met an average of 84–87% of each physician's weighted preference categories across synthetic 25–75-physician benchmarks while satisfying all hard staffing rules.",
    "Formulated a bi-objective model trading clinician fatigue against schedule quality and fairness for physicians rotating across multiple hospitals over a 90-day planning horizon.",
    "Integrated work schedules, surveys, interviews, wearable-device, and physiological data into analysis-ready datasets, and turned the findings into model inputs, constraints, and evaluation measures.",
    "Coordinate multi-site data collection and supervise undergraduate research assistants; present results to clinical collaborators to inform scheduling recommendations."],
   ["Mixed-Integer Linear Programming", "CP-SAT", "Gurobi", "Google OR-Tools", "Python", "HPC", "Survey and Interview Research"], "research.html"),
  ("Graduate Research Assistant", "University of Tennessee Space Institute · Tullahoma, TN", "Aug 2021 – Jul 2022", [
    "Built an AnyLogic supply chain simulation (Winter Simulation Conference paper) in which combined information sharing and risk pooling reduced simulated order-to-demand variance by 46.3% at the factory and 49.3% at the wholesaler.",
    "Worked on a supervised-learning approach for the traveling salesman problem (IEEE Transactions on Intelligent Transportation Systems article).",
    "Developed reinforcement-learning ordering policies for perishable inventory with stochastic demand, deterioration, and quantity discounts (IISE Annual Conference presentation).",
    "Collaborated on a Gurobi production-scheduling model for parallel injection-molding machines using a plastics manufacturer's data (IISE Annual Conference presentation)."],
   ["Agent-Based Simulation", "AnyLogic", "Supervised Learning", "Reinforcement Learning", "MILP"], "projects.html"),
 ]),
 ("Teaching", [
  ("Lecturer and Assistant Professor", "Department of Industrial & Production Engineering, Rajshahi University of Engineering & Technology (RUET) · Bangladesh", "Feb 2019 – Aug 2021", [
    "Taught undergraduate courses in Probability and Statistics, Operations Management, Product Design, Control Theory and Automation, and Industrial Simulation, with associated laboratory courses.",
    "Advised undergraduate research and capstone projects in optimization, simulation, scheduling, manufacturing, and supply chain systems.",
    "Developed course materials, examinations, laboratory exercises, and applied modeling assignments."],
   ["Teaching", "Statistics", "Simulation", "Project Advising"], None),
  ("Lecturer", "Department of Mechanical and Production Engineering, Ahsanullah University of Science and Technology · Dhaka, Bangladesh", "Apr 2017 – Dec 2018", [
    "Taught Operations Management, Engineering Economy, Material Handling and Maintenance Management, Manufacturing Processes, Machine Tools and Machining, and Engineering Materials.",
    "Prepared lectures, assessments, laboratory activities, and applied engineering assignments."],
   ["Teaching", "Operations Management", "Engineering Economy"], None),
  ("Graduate Teaching Assistant", "Department of Industrial Engineering, Clemson University · Clemson, SC", "Aug 2023 – Dec 2024", [
    "Supported Systems Modeling, Quality Engineering, Supply Chain Design and Control, and Engineering Economic Analysis with grading, student consultation, laboratory activities, and problem-solving sessions."],
   ["Teaching Support"], None),
  ("Graduate Teaching Assistant", "Department of Industrial and Systems Engineering, University of Tennessee · Knoxville, TN", "Aug 2022 – Jul 2023", [
    "Supported Facilities Planning and Material Handling and Quality Control and Management with grading and student consultation."],
   ["Teaching Support"], None),
 ]),
 ("Industry", [
  ("Intern", "Energypack Engineering Limited · Dhaka, Bangladesh", "Jun 2015 – Jul 2015", [
    "Prepared a quality manual for transformer fabrication processes to support standardized manufacturing and quality-control procedures.",
    "Conducted facility layout planning for production areas."],
   ["Quality Management", "Facility Layout"], None),
 ]),
 ("Leadership and mentoring", [
  ("President", "Clemson University INFORMS Student Chapter", "Aug 2025 – Sep 2026", [
    "Led chapter programming, invited seminars, professional-development and outreach events, and coordination with faculty and university partners; co-host and producer of the Optimality Gap podcast.",
    "The chapter received the INFORMS Student Chapter Annual Award at the Magna Cum Laude level in 2026 during this term."],
   ["Leadership", "Event Organization", "Science Communication"], None),
  ("Vice President", "Clemson University INFORMS Student Chapter", "Aug 2024 – Jul 2025", [
    "Supported chapter programming, professional-development events, and outreach; co-host and producer of the Optimality Gap podcast.",
    "The chapter received the INFORMS Student Chapter Annual Award at the Magna Cum Laude level in 2025 during this term."],
   ["Leadership"], None),
  ("Undergraduate Research Mentor", "Clemson University Creative Inquiry", "Fall 2025 – Present", [
    "Mentor twelve undergraduates from industrial engineering, biological sciences, bioengineering, health science, and nursing in field data collection, data-quality checks, analysis, and research presentation."],
   ["Mentoring", "Research Supervision"], None),
 ]),
]


def job_html(j):
    title, org, when, bullets, sk, link = j
    more = f'<p style="margin:10px 0 0"><a href="{{up}}{link}"><b>Related work →</b></a></p>' if link else ""
    return f'<div class="job panel"><div class="head"><h3>{E(title)}</h3><span class="when">{E(when)}</span></div><div class="org">{E(org)}</div><ul>{"".join(f"<li>{E(b)}</li>" for b in bullets)}</ul>{skills_html(sk)}{more}</div>'


_main_v4 = main


def main():
    _main_v4()
    body = band("Experience", "Research, teaching, industry, and leadership") + '<div class="wrap">'
    for name, jobs in JOBS:
        body += f'<section><h2>{name}</h2><div class="tl">{"".join(job_html(j) for j in jobs)}</div></section>'
    page("experience.html", "Experience | Md Zahidul Islam", body + "</div>", "experience.html")

if __name__ == "__main__":
    main()
