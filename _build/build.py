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
    return f'<div class="pub"><div class="t">{E(title)}</div><div>{authors} ({year}). {venue}.</div>{badges(links)}</div>'


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


if __name__ == "__main__":
    main()
