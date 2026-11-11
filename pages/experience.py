import streamlit as st
from data import JOBS


st.title("( ◡̀_◡́)ᕤ")
st.title("Experience")


#afficher les jobs comme pour projects, dans des cards
for job in JOBS:
    with st.container(border=True):
        col1, col2 = st.columns([1, 4])
        with col1:
            st.markdown(
                f"<div style='font-size:50px; text-align:center;'>{job['icone']}</div>", unsafe_allow_html=True)
        with col2:
            st.subheader(job["position"])
            st.markdown(f"**{job['company']}**")
            st.caption(f"📍 {job['location']} | 📅 {job['year']}")
            st.write(f"*{job['contract']}*")