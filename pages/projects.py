import streamlit as st
from data import PROJECTS


st.title("๋࣭ ⭑✮💻₊ ⊹")
st.title("Projects")


#fonction qui retourne la liste triée de tous les tags présents dans les projets
#utilisation de "set" pour éviter les doublons
def all_tags(projects):
    tags=set()
    for project in projects:
        for tag in project["tags"]:
            tags.add(tag)
    return sorted(tags)

#fonction qui retourne la liste des projets qui ont au moins un des tags choisis par le visiteur
def filter_projects(projects, chosen):
    if chosen==[]: 
        return projects 
    else:
        projects_w_tags=[]
        for project in projects:
            for tag in project["tags"]:
                if tag in chosen:
                    projects_w_tags.append(project)
                    break
    return projects_w_tags 


#choix du tag par le visiteur 
chosen=st.multiselect("Filter by tag", options=all_tags(PROJECTS))

#choix de l'ordre d'affichage des projets selon l'année du projet
ordered=st.selectbox("Sort by year", ["Most recent first", "Oldest first"])

#on applique la fonction filter_projects sur PROJECTS et on trie le résultat selon l'année du projet
filtered=filter_projects(PROJECTS, chosen)
filtered=sorted(filtered, key=lambda p: p["year"],
                  reverse=(ordered=="Most recent first"))

#écris le nombre de projets trouvés avec la fonction filtre appliquée 
st.write(f"{len(filtered)} project(s) found")

#affichage des projets sur deux colonnes
col=st.columns(2)
for i, project in enumerate(filtered):
    with col[i % 2]:
        with st.container(border=True):
            st.subheader(project["title"])
            st.write(project["description"])
            st.write(", ".join(project["tags"]))
            st.caption(project["year"])
            st.link_button("See the code", project["link"])