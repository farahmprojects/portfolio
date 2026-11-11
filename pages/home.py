import streamlit as st
from data import PROFILE, PROJECTS, SKILLS


st.title("⡞⠳⣄⣀⣠⠞⢷ ֹ۪")
st.title(f"Welcome! I'm {PROFILE['name']} ᯓ★")
st.subheader(f"⤷ {PROFILE["title"]}")
st.write(f"಄ {PROFILE["about"]}")
st.write(f"಄ {PROFILE['city']}")
st.write(f"಄ {PROFILE['email']}")


col1, col2=st.columns([1, 2])
with col1:
    st.write("಄ You can download my CV by hitting this button: ")
with col2:
    with open("assets/CV.pdf", "rb") as f: 
        st.download_button("Download my CV", f, file_name="CV.pdf") #ajout d'un bouton pour pouvoir télécharger mon CV


st.divider()


#trouver le plus gros niveau et retrouver le skill qui correspond
best_s=None
max=0
for skill, level in SKILLS.items():
    if level>max:
        max=level
        best_s=skill

#trois colonnes pour afficher les infos suivantes 
c1, c2, c3=st.columns(3)
with c1:
    st.metric(label="Number of Projects", value=len(PROJECTS))
with c2:
    st.metric(label="Number of Skills", value=len(SKILLS))
with c3:
    st.metric(label="Best Skill", value=best_s, delta=f"{max}/100")