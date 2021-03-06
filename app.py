import streamlit as st
from PIL import Image

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

#####################
# Header 
st.write('''
# Md Sumon Hossain, Ph.D.
##### *Resume* 
''')

image = Image.open('n.png')
st.image(image, width=150)

st.markdown('## Summary', unsafe_allow_html=True)
st.info('''
- Self-learner and a team player. Willing to learn and adapting new tools and technologies.
- Experienced Educator and Researcher with almost ten years of experience in mathematics and a passion for delivering insights based on modeling. 
- Strong verbal and written communication skills as demonstrated by extensive participation as invited speaker at `6` conferences as well as publishing 15 research articles.
- Well track record in scholarly research.
''')
##  Experienced Educator and Researcher with almost ten years of experience in data-oriented environment and a passion for delivering insights based on predictive modeling. 
## - Strong verbal and written communication skills as demonstrated by extensive participation as invited speaker at `10` conferences as well as publishing 149 research articles.
## - Strong track record in scholarly research .
#####################
# Navigation

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #16A2CB;">
  <a class="navbar-brand" href="https://youtube.com/dataprofessor" target="_blank">Md Sumon Hossain</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#experience">Experience</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#tools">Tools</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#social-media">Social Media</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

#####################
# Custom function for printing text
def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

def txt3(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  
def txt4(a, b, c):
  col1, col2, col3 = st.columns([1.5,2,2])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)

#####################
st.markdown('''
## Education
''')

txt('**Doctor of Philosophy** (Mathematics), *University of Groningen*, Netherlands',
'2018-2022')
st.markdown('''
- Thesis entitled `Reduced realizations and model reduction for switched linear systems`.
''')
## - Received Royal Golden Jubilee Ph.D. Scholarship of `2.152 million THB` covering tuition and stipend.
txt('**Masters of Philosophy** (Mathematics), *BUET*, Bangladesh',
'2014-2017')
st.markdown('''
- Graduated with First Class Honors.
''')

#####################
# st.markdown('''
# ## Experience
# ''')
# st.markdown('''
# - Managing a Center of `10` professors, researchers and students to ensure KPIs are strategically achieved namely to publish at least `20+` research publications annually. 
# - Actively took part in the talent hiring process as well as help employees to plan and develop their career path.
# - Set budget and handle procurement in order to facilitate education and research activities. Secured `> 10 million THB` budget.
# - Set and reflect on OKR on an annual basis to ensure productivity strategically matches the organization's direction.
# ''')

# txt('**Associate Professor**, Faculty of Medical Technology, Mahidol University, Thailand',
# '2012-2021')
# txt('**Assistant Professor**, Faculty of Medical Technology, Mahidol University, Thailand',
# '2009-2012')
# txt('**Lecturer**, Faculty of Medical Technology, Mahidol University, Thailand',
# '2006-2009')
# st.markdown('''
# - Provided mentorship and supervision to junior faculty, researchers, Ph.D./M.Sc./B.Sc. students. Mentored `3` Post-doctoral fellows, supervised `13` Ph.D. students, supervised `8` M.Sc. students, supervised `13` B.Sc. students and hosted `6` visiting students from U.S., Sweden and India.
# - Wrote and applied for research grants. Served as Principal Investigator for research grants that have been awarded `12.5 million THB` and `1.117 million SEK` in research funding from Thai and Swedish grant agencies.
# - Conducted research by applying machine learning to computational drug discovery and ensuring that research output exceeds `20+` articles per year.
# - Taught `10+` undergraduate/graduate classes on Bioinformatics, Data Mining, Scientific Research and Presentation, Research Methodology, Graduate Seminar, Programming for Health Data Science, etc.
# - Peer reviewed `100+` research articles for leading scientific journals.
# ''')

# txt('**Co-Chair**, International Conference on Pharmaceutical Bioinformatics at Pattaya, Thailand',
# '2016')
# st.markdown('''
# - Oversee all aspects of the conference preparations from conception to launch. This include inviting keynote and plenary speakers, create advertisement flyers, create abstract book, etc.
# - Conference attracted `200+` participants from `40+` countries from university and industry sector.
# - Chaired keynote session, technical workshop and some of the parallel sessions.
# ''')

# txt('**Content Creator**, [Data Professor YouTube Channel](https://youtube.com/dataprofessor/)',
# '2019-Present')
# st.markdown('''
# - `100,000+` subscribers on YouTube
# - Created `261` educational videos on data science, machine learning and bioinformatics as well as hosted several podcast episodes with data scientists.
# - Created `3` sponsored videos for Notion, Gradio and Classpert.
# ''')

# txt('**Content Creator**, [Coding Professor YouTube Channel](https://youtube.com/codingprofessor/)',
# '2019-Present')
# st.markdown('''
# - `3,200+` subscribers on YouTube
# - Created `38` educational videos on Python and R programming.
# ''')

# txt('**Technical Writer**, [Data Professor Blog](https://data-professor.medium.com/) on Medium.com',
# '2019-Present')
# st.markdown('''
# - `4,100+` subscribers on Medium
# - Written `68` technical blogs on data science, machine learning and bioinformatics.
# ''')

#####################
# st.markdown('''
# ## Tools
# ''')
# txt4('ABCpred', 'A web server for the discovery of acetyl- and butyryl-cholinesterase inhibitors', 'http://codes.bio/abcpred/')
# txt4('AutoWeka', 'An automated data mining software based on Weka', 'http://www.mt.mahidol.ac.th/autoweka/')
# txt4('ACPred', 'A computational tool for the prediction and analysis of anticancer peptides','http://codes.bio/acpred/')
# txt4('BioCurator', 'A web server for curating ChEMBL bioactivity data', 'http://codes.bio/biocurator/')
# txt4('CryoProtect', 'A web server for classifying antifreeze proteins from non-antifreeze proteins','http://codes.bio/cryoprotect/')
# txt4('ERpred', 'A web server for the prediction of subtype-specific estrogen receptor antagonists', 'http://codes.bio/erpred')
# txt4('HCVpred', 'A web server for predicting the bioactivity of Hepatitis C virus NS5B inhibitors', 'http://codes.bio/hemopred/')


#####################
st.markdown('''
## Skills
''')
txt3('Programming', '`Python`, `MatLab`, `Linux`, `JavaScript`')
txt3('Data processing/wrangling', '`SQL`, `pandas`, `numpy`')
txt3('Data visualization', '`matplotlib`, `seaborn`, `plotly`, `ggplot2`')
txt3('Machine Learning', '`scikit-learn`')
txt3('Deep Learning', '`TensorFlow`')
txt3('Web development', '`Flask`, `HTML`, `CSS`')
txt3('Model deployment', '`streamlit`, `Docker`, `Kubernates`, `Heroku`, `AWS`, `GitHub`')
## txt3('Model deployment', '`streamlit`, `gradio`, `R Shiny`, `Heroku`, `AWS`, `Digital Ocean`')

#####################
st.markdown('''
## Social Media
''')
txt2('LinkedIn', 'https://www.linkedin.com/in/md-sumon-hossain-197152ba/')
## txt2('Twitter', 'https://twitter.com/thedataprof')
txt2('GitHub', 'https://github.com/sumonhn22/')
# txt2('', 'https://github.com/chaninlab/')
# txt2('', 'https://github.com/dataprofessor')
txt2('ORCID', 'https://orcid.org/my-orcid?orcid=0000-0002-6357-2300')
## txt2('Scopus', 'http://www.scopus.com/authid/detail.url?authorId=12039071300')
txt2('Google Scholar', 'https://scholar.google.com/citations?user=1TflLNcAAAAJ&hl=en')
txt2('ResearchGate', 'https://www.researchgate.net/profile/M-Sumon-Hossain')

