import streamlit as st
from data import PROFILE, PROJECTS, SKILLS

st.title(f"Hi, I'm {PROFILE['name']}")
st.subheader(PROFILE["title"])
left, right = st.columns([1, 2])
with left:
    st.image("assets/photo.png", width=220)
with right:
    st.write(PROFILE["about"])
    st.write(PROFILE['city'])
    st.write(PROFILE['email'])
    with open("assets/CV.pdf", "rb") as f:
        st.download_button("Download my CV", f, file_name="CV.pdf")


st.divider()

best_s = None
max = 0
for skill, level in SKILLS.items():
    if level > max:
        max = level
        best_s = skill

c1, c2, c3 = st.columns(3)
with c1:
    st.metric(label="Number of Projects", value=len(PROJECTS))
with c2:
    st.metric(label="Number of Skills", value=len(SKILLS))
with c3:
    st.metric(label="Best Skill", value=best_s, delta=f"{max}/100")