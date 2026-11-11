import streamlit as st
from data import TIMELINE
from data import LANGUAGES
from data import CERTIFICATIONS 


st.title("✎𓂃")
st.title("Education")


#3 tabs pour chauqe partie et pour chacune : afficher les images, l'année puis l'intitulé (descr)(dans des cards aussi)
tab1, tab2, tab3=st.tabs(["Formation", "Licenses and Certifications", "Languages"])
with tab1: 
    for formation in TIMELINE: 
        with st.container(border=True):
            col1, col2=st.columns([1, 5])
            with col1:
                st.image(formation["icone"], width=180)
            with col2: 
                st.write(f"**{formation['year']}** : {formation['descr']}")

with tab2: 
    for certif in CERTIFICATIONS: 
        with st.container(border=True):
            col1, col2=st.columns([1, 5])
            with col1:
                st.image(certif["icone"], width=180)
            with col2: 
                st.write(f"**{certif['year']}** : {certif['descr']}")

with tab3: 
    for language in LANGUAGES: 
        with st.container(border=True):
            col1, col2=st.columns([1, 5])
            with col1:
                st.image(language["icone"], width=180)
            with col2: 
                st.write(f"**{language['language']}** : {language['level']}")