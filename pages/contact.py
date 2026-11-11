import streamlit as st
import datetime
import os
import csv


st.title("˗ˏˋ ꒰ ✉︎ ꒱ ˎˊ˗")
st.title("Contact me")


#fonction pour check si les infos entrées sont correctes selon certaines conditions
def check(name, email, message):
    problems=[]
    if not name.strip():
        problems.append("You did not provide a name.")
    if "@" not in email: #besoin de faire un elif pour le mail car sinon ça bug (déjà testé avec deux if)
        problems.append("The email you entered is not valid, @ is missing.")
    elif "." not in email.split("@")[1]:
        problems.append("The email you entered is not valid, domain is missing.")
    if len(message) < 10:
        problems.append("Your message is too short, it must be at least 10 characters long.")
    return problems

#fonction pour sauvegarder les messages reçus dans le fichier messages.csv
def save(name, email, message):
    date=datetime.datetime.now()
    if os.path.exists("messages.csv")==True: #le cas où le fichier existe déjà
        with open("messages.csv", "a") as f:
            writer=csv.writer(f) #crée un objet writer afin de pouvoir utiliser les fonctions de csv 
            writer.writerow([date, name, email, message]) #alors on écrit la ligne avec les infos
    else : #le cas où le fichier n'existe pas 
        with open("messages.csv", "a") as f:
            writer=csv.writer(f) #crée un objet writer afin de pouvoir utiliser les fonctions de csv 
            writer.writerow(["Date", "Name", "Email", "Message"])#si le fichier n'existe pas encore, on écrit l'entête
            writer.writerow([date, name, email, message]) #puis on écrit le ligne avec les infos 


with st.form("contact"):
    name=st.text_input("Your name")
    email=st.text_input("Your email")
    message=st.text_area("Your message")
    sent=st.form_submit_button("Send") #vrai seulement sur le run qui suit le click

#vérif des messages reçus et affichage des messages d'erreur ou de succès si problems est vide
if sent:
    problems=check(name, email, message)
    if problems==[]:
        #st.success("Your message has been sent successfully! Thank you.")
        save(name, email, message)
        st.toast("Your message has been sent successfully! Thank you.")
        st.snow()
    else:
        #st.error("We're sorry but your message could not be sent, please fix the following problem(s):")
        with st.expander("We're sorry but your message could not be sent, please fix the following problem(s):"):
            for problem in problems:
                st.write(f"- {problem}")


#Réponses à la question: 
#on ouvre le fichier avce le mode "a" et pas "w" car : 
#le mode "a" ajoute les nouvelles lignes / infos à la fin du fichier sans supprimer celles qui étaient là avant
#alors que le mode "w" écrase à chaque ouverture ce qui était déjà présent avant
#le mode "a" est donc le plus adapté au prijet car on souhaite sauvegarder les messages dans le fichiers "messages.csv"