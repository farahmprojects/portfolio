import streamlit as st
from data import PROFILE

st.set_page_config(
    page_title=PROFILE["name"],
    page_icon=":briefcase:",
    layout="wide"
)

pages = [
    st.Page("pages/home.py", title="About me", icon=":material/person:", default=True),
    st.Page("pages/education.py", title="Education", icon=":material/school:"),
    st.Page("pages/experience.py", title="Experience", icon=":material/work:"),
    st.Page("pages/projects.py", title="Projects", icon=":material/code:"),
    st.Page("pages/skills.py", title="Skills", icon=":material/bar_chart:"),
    st.Page("pages/my_interests.py", title="My interests", icon=":material/book:"),
    st.Page("pages/contact.py", title="Contact me", icon=":material/mail:")
]

#cache le menu de navigation par défaut
pg = st.navigation(pages, position="hidden")

with st.sidebar:
    st.markdown(f"### {PROFILE['name']} ⊹ ࣪ ˖")
    st.image("assets/photo.jpeg", width=260)
    #ajout profil GitHub
    st.markdown("## ಄ My Github Profile:\n""[⤷click hereˎˊ˗](https://github.com/farahmprojects)")
    #ajout profil LinkedIn
    st.markdown("## ಄ My LinkedIn Profile:\n""[⤷click hereˎˊ˗](https://www.linkedin.com/in/farah-moutaki-a05477421/)")


    st.divider()


    for page in pages:
        st.page_link(
            page,
            label=page.title,
            icon=page.icon
        )

#run the selected page
pg.run()