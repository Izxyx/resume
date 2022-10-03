# Libraries
from pathlib import Path
import streamlit as st
from PIL import Image


# Paths
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir/'styles'/'main.css'
resume_file = current_dir/'assets'/'CV_Victor_Hugo_Pérez_Barrios.pdf'
profile_pic = current_dir/"assets"/"profile-pic.png"


# Settings
PAGE_TITLE = 'Digital CV | Victor Hugo Pérez Barrios'
NAME = 'Victor Hugo Pérez Barrios'
DESCRIPTION = 'Junior Data Analyst'
EMAIL = 'dc.vhpb@gmail.com'
PHONE = '(044) 5513337258'
CITY = 'Miguel Hidalgo, CDMX'
SOCIAL_MEDIA = {
    'Linkedin': 'https://www.linkedin.com/in/arqhp/',
    'Github': 'https://github.com/Izxyx',
    'Instagram': 'https://www.instagram.com/arq_v/'
}
PROJECTS = {
    '► EDA retail store and machine learning modeling (Pandas, Seaborn, Plotly, Matplotlib, Scipy, Missingno Scikitlearn).': 'https://github.com/Izxyx/eda_retail_store/blob/master/eda_retail_store.ipynb',
    '► Retail store sales dashboard.': 'https://www.youtube.com/watch?v=PyoRdu-i0AQ&ab_channel=DilanxC',
    '► Predicting sales based on retail store features.': 'https://www.youtube.com/watch?v=PyoRdu-i0AQ&ab_channel=DilanxC',
    '► Forecasting sales based on store features.': 'https://www.youtube.com/watch?v=PyoRdu-i0AQ&ab_channel=DilanxC',
    '► Power BI dashboard.': 'https://www.youtube.com/watch?v=PyoRdu-i0AQ&ab_channel=DilanxC',
    '► Excel dashboard.': 'https://www.youtube.com/watch?v=PyoRdu-i0AQ&ab_channel=DilanxC',
    '► Example report retail stores insights.': 'https://www.youtube.com/watch?v=PyoRdu-i0AQ&ab_channel=DilanxC'
}


# Configuration
st.set_page_config(page_title=PAGE_TITLE,page_icon='random')


# Header
with open(css_file) as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
with open(resume_file,"rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# CV
col1, col2 = st.columns(2,gap='small')
with col1:
    st.image(profile_pic,width=300)

with col2:
    st.title(NAME)
    st.subheader(DESCRIPTION)
    st.download_button(
        label=' 📄 Download Resume',
        data=PDFbyte,
        file_name=resume_file.name,
        mime='application/octet-stream',
    )
    st.write('Mail:  ',EMAIL)
    st.write('Phone:  ',PHONE)
    st.write('Location:  ',CITY)


# Social Links
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")
st.write("---")

# Qualifications
st.write('\n')
st.subheader("Qulifications")
st.write("""
- ► 2 Years experience extracting insights from data.

- ► Strong hands on experience and knowledge in Python and Excel.

- ► Good understanding of statistical principles and their respective applications.
""")
st.write('\n') 
st.write("---")

#  Hard Skills
st.write('\n')
st.subheader("Hard Skills")
st.write("""
- ► Programming: Python (Scikit-learn, Pandas, TensorFlow, Keras), SQL

- ► Data Visulization: PowerBI, Tableu, Matplotlib, MS Excel, Matplotlib, Seaborn, Plotly

- ► Modeling: Regression, Decision Trees, Clustering, Classificaction, XGBoost, Catboost, Lightboost

- ► Databases: MySQL, MongoDB, Firebase
""")
st.write('\n') 
st.write("---")


# Experience 
st.write('\n')
st.subheader("Experience")

st.write("**Real State Data Analyst  |  Miniso S.A.P.I.**")
st.write("October 2021 - Present")
st.write("""
- ► Analyst in charge of inspection and planning for new mall stores opening, layout stores development, needs conciliation across different functional areas inside the company.

- ► Used PowerBI and SQL to redeﬁne and track KPIs surrounding architecture initiatives and supplied recommendations to boost earnings in stores.

- ► Built machine learning models, dashboards and maps to generate meaningful insights from  stores data.

- ► Compiled, studied, and inferred large amounts of data, modeling  information to find pattern in stores.

- ► Collaborated with financial team to oversee end-to-end process surrounding stores data.
""")
st.write('\n') 
st.write("---")

# Projects
st.write('\n')      
st.subheader("Projects")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")