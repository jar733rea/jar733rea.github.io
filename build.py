from pathlib import Path
from html import escape
import json, shutil
root=Path(__file__).parent
out=root/'dist'; out.mkdir(exist_ok=True)
projects=json.loads((root/'projects.json').read_text())
nav=[('index','About'),('bio','Bio'),('publications','Publications'),('activities','Activities'),('contact','Contact')]
def link(slug,label): return f'<a href="{slug}.html">{label}</a>'
def graphic():
 return '''<svg viewBox="0 0 600 480" role="img" aria-labelledby="landscape-title"><title id="landscape-title">Conceptual landscape connecting slopes, levees, and coastal water; illustration, not research data</title><defs><pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse"><path d="M40 0H0V40" fill="none" stroke="#ffffff" stroke-opacity=".09"/></pattern></defs><rect width="600" height="480" fill="#133f43"/><rect width="600" height="480" fill="url(#grid)"/><circle cx="440" cy="98" r="45" fill="#d6c89e"/><path d="M0 300L170 125 335 300 460 230 600 310V480H0Z" fill="#426f69"/><path d="M0 345L170 172 335 345 460 275 600 355" fill="none" stroke="#d4cba9" stroke-width="2"/><path d="M0 380L170 215 335 380 460 318 600 390" fill="none" stroke="#9cb7a3"/><path d="M0 415L170 260 335 415 460 360 600 430" fill="none" stroke="#9cb7a3"/><path d="M315 350Q390 330 460 350T600 350V480H315Z" fill="#71b7b3" fill-opacity=".7"/><path d="M330 380Q405 360 475 380T620 380M330 410Q405 390 475 410T620 410M330 440Q405 420 475 440T620 440" fill="none" stroke="#d1e2d7"/><path d="M135 170L180 220" stroke="#e5d5aa" stroke-width="2"/><text x="35" y="450" fill="#d5e1d9" font-family="sans-serif" font-size="12" letter-spacing="3">GROUND / WATER / RISK</text></svg>'''
cards=''.join(f'<article class="project" id="{["slopes","levees","coasts"][i]}"><span class="number">0{i+1} / {escape(p["field"])}</span><h2>{escape(p["title"])}</h2><p>{escape(p["description"])}</p><span class="status">Research theme · publication status pending</span></article>' for i,p in enumerate(projects))
pages={
 'index':('Welcome','''<div class="profile-layout"><section class="biography"><h1>Welcome</h1><p>I am a graduate researcher in <strong>geotechnical engineering and natural hazards</strong> at Rutgers University. My research interests connect earthquake engineering, probabilistic risk, and coastal processes.</p><p>I study questions involving seismic slope displacement under subduction earthquakes, probabilistic seismic–flood levee risk, and coastal sediment and hydrodynamic modeling.</p><p>My work focuses on understanding the interaction between ground, water, and natural hazards, with an interest in uncertainty and infrastructure resilience.</p><p><a href="cv.html">Curriculum vitae</a></p><h2>Research interests</h2><ul class="research-list"><li><a href="research.html#slopes">Geotechnical earthquake engineering and ground deformation</a></li><li><a href="research.html#levees">Natural hazards, probabilistic risk, and infrastructure resilience</a></li><li><a href="research.html#slopes">AI and data-driven methods for geotechnical engineering and natural hazards</a></li></ul><h2>Activities</h2><p>Research presentations, academic activities, and publication updates will be added as details are confirmed.</p><p><a href="activities.html">View activities</a></p></section><aside class="profile-sidebar" aria-label="Profile and contact"><img class="profile-portrait" src="assets/juan-headshot.png" alt="Portrait of Juan Rea-Avila" width="1122" height="1402"><p class="sidebar-email">juan.rea@rutgers.edu</p><div class="profile-links"><a href="https://github.com/jar733rea">GitHub ↗</a></div></aside></div>'''),
'research':('ResearchsSS',f'<p class="eyebrow">RESEARCH</p><h1>Ground, water<br><em>and uncertainty.</em></h1><p class="intro">Three connected research themes in geotechnical engineering and natural hazards.</p><div class="projects">{cards}</div><p class="note">These descriptions summarize research topics supplied by Juan. They do not report findings or imply that a paper has been published, submitted, or accepted.</p>'),
'publications':('Publications','''<p class="eyebrow">SCHOLARSHIP</p><h1>Publications</h1><div class="panel"><h2>Bibliography forthcoming</h2><p>Verified citations and publication links will be added here.</p><p>Submitted manuscripts and unpublished work will be listed separately with their status clearly identified.</p></div>'''),
'cv':('Curriculum vitae','''<p class="eyebrow">BACKGROUND</p><h1>Curriculum vitae</h1><div class="panel"><h2>CV coming soon</h2><p>The full academic CV will be available here after review.</p><a class="button" href="assets/Juan-Rea-Avila-CV-placeholder.txt" download>Download CV placeholder ↓</a><p class="note">Plain-text placeholder only; this is not a complete CV.</p></div>'''),
'activities':('Activities','''<p class="eyebrow">ACADEMIC COMMUNITY</p><h1>Activities</h1><div class="panel"><h2>Updates forthcoming</h2><p>Conference presentations, teaching, professional service, and outreach will be added as details are confirmed.</p></div>'''),
'contact':('Contact','''<p class="eyebrow">LET’S CONNECT</p><h1>Contact</h1><p class="intro">For research conversations and academic inquiries.</p><div class="panel"><h2>Juan Rea-Avila</h2><p>Graduate researcher<br>Geotechnical engineering & natural hazards<br>Rutgers University</p><a class="contact" href="mailto:juan.rea@rutgers.edu">juan.rea@rutgers.edu ↗</a></div>''')}
pages['bio'] = ('Bio', (root/'content/bio.html').read_text())
# Page content is kept in editable HTML fragments under content/.
for name in ('research', 'publications', 'activities', 'cv', 'contact'):
 pages[name] = (pages[name][0], (root/'content'/f'{name}.html').read_text())
title, home = pages['index']
home = home.replace('My work focuses on understanding the interaction between ground, water, and natural hazards, with an interest in uncertainty and infrastructure resilience.', 'I am pursuing an M.S. in Civil &amp; Environmental Engineering at Rutgers University (expected 2027), where I serve as a Graduate Assistant at the Center for Advanced Infrastructure and Transportation (CAIT). I earned my B.S. in Civil Engineering from the University of Cuenca, Ecuador, in 2023.')
home = home.replace('Research presentations, academic activities, and publication updates will be added as details are confirmed.', 'Two coauthored contributions have been accepted for presentation at the ASCE2027 Experience, on post-earthquake levee flood risk and stabilized coastal sediments. Three manuscripts are in preparation.')
home = home.replace('<a href="https://github.com/jar733rea">GitHub ↗</a>', '<a href="https://scholar.google.com/citations?user=ccj87rIAAAAJ">Google Scholar ↗</a><a href="https://www.linkedin.com/in/juan-rea-avila/">LinkedIn ↗</a><a href="https://github.com/jar733rea">GitHub ↗</a>')
# The About biography is written in third person.
start = home.index('<p>I am a graduate researcher')
end = home.index('<p><a href="cv.html">', start)
home = home[:start] + '<p><a href="bio.html">Juan Rea-Avila</a> is a graduate assistant at <a href="https://www.rutgers.edu/">Rutgers University</a>, pursuing an M.S. in the <a href="https://cee.rutgers.edu/">Department of Civil and Environmental Engineering</a>. He works under the supervision of <a href="https://soe.rutgers.edu/staff-directory/tyler-oathes-phd">Tyler Oathes, Ph.D.</a>, and conducts research through the <a href="https://cait.rutgers.edu/">Center for Advanced Infrastructure and Transportation</a>.</p><p>His research combines numerical modeling, probabilistic analysis, and artificial intelligence to study earthquake-induced ground deformation and infrastructure risk. Current work focuses on seismic slope displacement and the effects of earthquake damage on levee flood risk, with the aim of supporting more resilient infrastructure. This website presents his <a href="research.html">research</a>, <a href="publications.html">publications and manuscripts</a>, and <a href="activities.html">academic activities</a>. For collaboration or academic inquiries, please <a href="contact.html">get in touch</a>.</p>' + home[end:]
# Accessible logo links for professional profiles.
profiles = [
 ('googlescholar', 'Google Scholar', 'https://scholar.google.com/citations?user=ccj87rIAAAAJ'),
 ('linkedin', 'LinkedIn', 'https://www.linkedin.com/in/juan-rea-avila/'),
 ('github', 'GitHub', 'https://github.com/jar733rea'),
 ('researchgate', 'ResearchGate', 'https://www.researchgate.net/profile/Juan-Rea-Avila-2'),
 ('orcid', 'ORCID', 'https://orcid.org/0009-0004-2973-7310'),
]
icons = '<div class="profile-links" aria-label="Professional profiles">'
for filename, label, url in profiles:
 svg = (root/'assets'/f'{filename}.svg').read_text()
 svg = svg.replace('<svg ', '<svg aria-hidden="true" focusable="false" ', 1)
 icons += f'<a href="{url}" aria-label="{label}" title="{label}">{svg}</a>'
icons += '</div>'
pages['contact'] = (pages['contact'][0], pages['contact'][1].replace('{{PROFILE_LOGOS}}', icons))
a = home.index('<div class="profile-links">')
b = home.index('</div>', a) + len('</div>')
home = home[:a] + icons + home[b:]
home = home.replace('href="cv.html"', 'href="assets/Juan-Rea-Avila-CV.pdf"')
home = home.replace('>Curriculum vitae</a>', '>Curriculum vitae</a><br><a href="assets/juan-headshot.png" download="Juan-Rea-Avila-headshot.png">High-resolution photo</a>')
# Five most recent dated activities, newest first.
featured = '<section class="featured-activities"><h2>Recent activities</h2><div class="featured-cards"><article class="activity-entry"><p><strong class="activity-date">October 15, 2026:</strong> <a href="activities.html">Selected as Geotechnical Research Subcommittee Representative</a>, NSF NHERI Graduate Student Council.</p></article><article class="activity-entry"><p><strong class="activity-date">October 6, 2026:</strong> <a href="activities.html">CAIT sediment-placement modeling poster</a>, ASBPA National Coastal Conference, Atlantic City, New Jersey.</p></article><article class="activity-entry"><p><strong class="activity-date">August 11–13, 2026:</strong> <a href="activities.html">NHERI SPARC 2026 participant and travel award recipient</a>, Texas Advanced Computing Center, Austin, Texas.</p></article><article class="activity-entry"><p><strong class="activity-date">July 13–17, 2026:</strong> <a href="activities.html">13NCEE participant</a>, Portland, Oregon; Vilas and Ingrid Mujumdar Registration Grant recipient.</p></article><article class="activity-entry"><p><strong class="activity-date">June 3, 2026:</strong> <a href="activities.html">Selected as a member of the Embankments, Dams, and Slopes Technical Committee</a>, ASCE Geo-Institute.</p></article></div><p><a href="activities.html">View all activities</a></p></section>'
activity_start = home.index('<h2>Activities</h2>')
activity_end = home.index('</section>', activity_start)
home = home[:activity_start] + featured + home[activity_end:]
import re
home = re.sub(r'<a href="research\.html(?:#[^"]*)?">(.*?)</a>', r'\1', home)
pages['index'] = (title, home)
# Share the About profile sidebar across the main pages.
sidebar_start = home.index('<aside class="profile-sidebar"')
sidebar_end = home.index('</aside>', sidebar_start) + len('</aside>')
sidebar = home[sidebar_start:sidebar_end]
for name in ('bio', 'research', 'publications', 'activities', 'contact'):
 page_title, content = pages[name]
 # Contact already includes professional profiles in the shared sidebar.
 if name == 'contact':
  content = content.replace('<h2>Professional profiles</h2>', '').replace(icons, '')
 if name in ('activities', 'publications'):
  pages[name] = (page_title, '<div class="activities-layout"><section class="page-content">' + content + '</section></div>')
 else:
  pages[name] = (page_title, '<div class="profile-layout"><section class="page-content">' + content + '</section>' + sidebar + '</div>')
for slug,(title,body) in pages.items():
 navigation = ''
 for page, label in nav:
  current = ' aria-current="page"' if page == slug else ''
  if page == 'index':
   navigation += f'<a class="home-link" href="index.html" aria-label="Home" title="Home"{current}><svg aria-hidden="true" viewBox="0 0 24 24" width="18" height="18" fill="currentColor"><path d="M12 3 1 12h3v9h6v-6h4v6h6v-9h3L12 3Z"/></svg></a>'
  else:
   destination = 'assets/Juan-Rea-Avila-CV.pdf' if page == 'cv' else f'{page}.html'
   navigation += f'<a href="{destination}"{current}>{label}</a>' 
 (out/f'{slug}.html').write_text(f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="description" content="Juan Rea-Avila — graduate researcher in geotechnical engineering and natural hazards at Rutgers University."><meta name="theme-color" content="#CC0033"><link rel="icon" type="image/svg+xml" href="assets/favicon.svg?v=2"><title>{escape(title)} | Juan Rea-Avila</title><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Source+Sans+3:ital,wght@0,400;0,600;0,700;1,400;1,700&display=swap" rel="stylesheet"><link rel="stylesheet" href="style.css?v=20261021-12"></head><body><a class="skip" href="#main">Skip to content</a><header><nav aria-label="Main navigation">{navigation}</nav></header><main id="main">{body}</main><footer><span>© 2026 Juan Rea-Avila. All rights reserved.</span><span class="footer-disclaimer">Views expressed on my personal website are my own.</span></footer></body></html>''')
shutil.copy(root/'style.css',out/'style.css')
(out/'assets').mkdir(exist_ok=True)
for asset in ('asbpa-2026-presentation.jpeg', 'asbpa-2026-poster.png'):
 shutil.copy(root/'assets'/asset, out/'assets'/asset)
shutil.copy(root/'assets/sparc-2026-participants.jpeg', out/'assets/sparc-2026-participants.jpeg')
shutil.copy(root/'assets/rutgers-logo.svg', out/'assets/rutgers-logo.svg')
shutil.copy(root/'assets/juan-headshot.png', out/'assets/juan-headshot.png')
shutil.copy(root/'assets/Juan-Rea-Avila-CV.pdf', out/'assets/Juan-Rea-Avila-CV.pdf')
(out/'.nojekyll').touch()
(out/'404.html').write_text('<!doctype html><html lang="en"><meta charset="utf-8"><title>Page not found</title><h1>Page not found</h1><a href="index.html">Return to Juan Rea-Avila’s website</a></html>')
print(f'Built {len(pages)} pages in {out}')

shutil.copy(root/'assets/vanguardia-graduation-2022.jpg', out/'assets/vanguardia-graduation-2022.jpg')

shutil.copy(root/'assets/favicon.svg', out/'assets/favicon.svg')
