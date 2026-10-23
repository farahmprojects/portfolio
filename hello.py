import streamlit as st

print("run")
st.title("Hello!")
name = st.text_input("What is your name?")
if name:
    st.write(f"Nice to meet you, {name}.")

age = st.slider("Your age", 15, 70, 20)
thirty = 30 - age
if age >= 30 :
    st.write("you're already 30 years old or more")
else :
    thirtyin = st.write(f"You will be 30 in {thirty} years")


#Réponse à la question 1): 3 "run" s'affichent car :
#Lorsque je lance le programme hello.py avec la commande suivante : streamlit run hello.py, un premier "run" s'affiche, ensuite lorsque j'entre mon prénom, 
#un deuxième "run" s'affiche et enfin quand j'entre un autre prénom, un troisième "run" s'affiche dans le terminal. 
#Cela s'explique de la façcon suivante : à chaque fois que l'utilisateur intéragit avec la page web, tout le programme run du début à la fin et la page est "redessinée".
#Ainsi, étant donné que la ligne : print("run") est placée tout au début du fichier, il y a un "run" qui s'affiche à chaque interaction. 
#Ce qui nous fait donc bien un total de 3 "run". 