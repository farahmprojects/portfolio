import streamlit as st
from data import SKILLS
from data import TIMELINE
import pandas as pd


st.title("🛠️")
st.title("Skills")
st.subheader("Here are my skills and their level out of 100:")


for skill, level in SKILLS.items(): 
    st.progress(level / 100, text=f"{skill}: {level}/100") #afficher la progress bar

    
bar_chart=pd.DataFrame({ #construire la bar chart 
         "skill": list(SKILLS.keys()),
         "level": list(SKILLS.values()),})

st.divider()
st.subheader("Take a look at the bar chart below that illustrates my level in each skill:")
st.bar_chart(bar_chart, x="skill", y="level", color="#A65336") #afficher la bar chart