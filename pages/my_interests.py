import streamlit as st
from data import INTERESTS


st.title("‧₊˚✿ My Interests ✿˚₊‧")


st.subheader("A little collection of the things I enjoy, the hobbies I explore and the subjects that inspire me.")
st.write("")


#afficher dans des cards comme pour projects 
for i in range(0, len(INTERESTS), 2):
    col1, col2 = st.columns(2)
    with col1:
        interest = INTERESTS[i]
        with st.container(border=True):
             st.markdown(f"<div style='text-align:center; font-size:45px;'>"f"{interest['icon']}</div>", unsafe_allow_html=True)
             st.markdown(f"<h3 style='text-align:center;'>{interest['title']}</h3>", unsafe_allow_html=True)
             st.markdown(f"<p style='text-align:center; min-height:75px;'>" f"{interest['description']}</p>", unsafe_allow_html=True)
    if i + 1 < len(INTERESTS):
        with col2:
            interest = INTERESTS[i + 1]
            with st.container(border=True):
                 st.markdown(f"<div style='text-align:center; font-size:45px;'>" f"{interest['icon']}</div>", unsafe_allow_html=True)
                 st.markdown(f"<h3 style='text-align:center;'>{interest['title']}</h3>", unsafe_allow_html=True)
                 st.markdown(f"<p style='text-align:center; min-height:75px;'>" f"{interest['description']}</p>", unsafe_allow_html=True)