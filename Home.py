import requests
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
from streamlit.components.v1 import html
import webbrowser

# pureButton = '''<style>
#     a{
#         text-decoration: none;
#         color: white;
#         border: 2px solid rgb(170, 199, 199);
#         border-radius: 2px;
#         padding: 3px 6px 3px 6px;
#         background-color: black;
#     }
# </style>
#     <a href='http://www.google.com' target='_blank'>Submit</a>
# '''
# html(pureButton)



# ---PAGE_TITLE---
st.set_page_config(page_title="E-Learning Portal", page_icon=":books:", layout="wide")

# st.sidebar.title("Main Menu")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

# ---ASSETS---
lottie_ebooks = load_lottieurl("https://assets3.lottiefiles.com/private_files/lf30_fqygznk9.json")


# ---CONTENT---
with  st.container():
    st.subheader(
                '''
                "If we can put a man on the moon and sequence the human genome, we should be able to devise something close to a universal digital public library." — Peter Singer
                ''')
    st.title('Welcome to the Project')
    st.header("E-Learning Portal")
    st.write('###')

    left_column, right_column = st.columns(2)
    with right_column:
        st.header('Why you should use?')
        st.write(
            '''
            - It help the students to integrate the technology into the curriculum, by increasing the technology literacy.
            - This LMS offers a variety of resources that can help you earn good knowledge, regardless of the subject or level you’re pursuing. .
            ''')
    with left_column:
        st_lottie(lottie_ebooks, height=300, key="ebooks") #---ANIMATION---

st.write('---')
# ..............................................................................
import streamlit as st

# Using object notation
st.sidebar.markdown("### PYQ :")
add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Select","Semester 1","Semester 2","Semester 3","Semester 4","Semester 5","Semester 6","Semester 7","Semester 8")
)


if add_selectbox == "Semester 1":
        webbrowser.open('https://drive.google.com/drive/folders/1Ya_3tHGTwUz_XbUxUU4Qim1Ww-0Nck5I?usp=share_link')
if add_selectbox == "Semester 2":
        webbrowser.open('https://drive.google.com/drive/folders/18tm0pZsLSycC3ojvIO6FXjWvF4I7FNmb?usp=sharing')
if add_selectbox == "Semester 3":
        webbrowser.open('https://drive.google.com/drive/folders/1eMMpqlhUx9msLavZfssmfKjXsGBEfeu9?usp=sharing')
if add_selectbox == "Semester 4":
        webbrowser.open('https://drive.google.com/drive/folders/19-Rj6yaFuCxzMKl8Ig9gQMRYfVsJqwJn?usp=share_link')
if add_selectbox == "Semester 5":
        webbrowser.open('')
if add_selectbox == "Semester 6":
        webbrowser.open('...')
if add_selectbox == "Semester 7":
        webbrowser.open('...')
if add_selectbox == "Semester 8":
        webbrowser.open('...')
        















# ......................................................................
# ---IN THIS SITE---
with st.container():
    st.subheader('What will you find in this site?')
    st.write(
        '''
        You will find in this site:
        - The eNotes of all subjects which are taught in 2nd and 3rd year during B.Tech Program
        - Notes from different colleges affilated to AKTU
        '''
    )

# # ---- CONTACT ----
# with st.container():
#     st.write("---")
#     st.header("Get In Touch With Us!")
#     st.write("##")

#     contact_form = """
#     <form action="https://formsubmit.co/el/xicoje" method="POST">
#         <input type="hidden" name="_captcha" value="false">
#         <input type="text" name="name" placeholder="Your name" required>
#         <input type="email" name="email" placeholder="Your email" required>
#         <textarea name="message" placeholder="Your message here" required></textarea>
#         <button type="submit">Send</button>
#     </form>
#     """
#     left_column, right_column = st.columns(2)
#     with left_column:
#         st.markdown(contact_form, unsafe_allow_html=True)
#     with right_column:
#         st.empty()
import numpy as np
import pandas as pd

import sqlite3
conn = sqlite3.connect('student_feedback.db')
c = conn.cursor()
    

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS feedback(date_submitted DATE, Q1 TEXT, Q2 INTEGER, Q3 INTEGER, Q4 TEXT, Q5 TEXT, Q6 TEXT, Q7 TEXT, Q8 TEXT)')

def add_feedback(date_submitted, Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8):
    c.execute('INSERT INTO feedback (date_submitted,Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8) VALUES (?,?,?,?,?,?,?,?,?)',(date_submitted,Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8))
    conn.commit()

def main():
    st.write("---")
    st.write("*The Study Material Provided Is Not Ours And Belongs To Respective Owners.")
    st.write("---")

    st.title("Student Feedback")

    d = st.date_input("Today's date",None, None, None, None)
    
    question_1 = st.selectbox('What was your subject ?',('',"Maths IV", "COA", "DSTL", "DS", "Python", "Technical Communication", "Digital Electronics", "Human Values", "Computer System Security", "Microprocessor", "Operating Systems", "Automata", "Sensor Instrumentation", "Electronics Engg.","DBMS","Machine Learning","Soft Computing","Compiler Design","Data Analytics","software Engineering","Web Technology"))
    st.write('You selected:', question_1)
    
    question_2 = st.slider('What semester are you in?', 1,8)
    st.write('You selected:', question_2) 
    
    question_3 = st.slider('Overall, how happy are you with the Notes? (5 being very happy and 1 being very dissapointed)', 1,5,1)
    st.write('You selected:', question_3)

    question_4 = st.selectbox('Were the notes interactive?',('','Yes', 'No'))
    st.write('You selected:', question_4)

    question_5 = st.selectbox('Was the syllabus updated?',('','Yes', 'No'))
    st.write('You selected:', question_5)

    question_6 = st.selectbox('Are these notes worth sharing ?',('','Yes', 'No'))
    st.write('You selected:', question_6)

    question_7 = st.selectbox('Will you refer the same in future?',('','Yes', 'No'))
    st.write('You selected:', question_7)

    question_8 = st.text_input('What could have been better?', max_chars=50)

    if st.button("Submit feedback"):
        create_table()
        add_feedback(d, question_1, question_2, question_3, question_4, question_5, question_6, question_7, question_8)
        st.success("Feedback submitted")
main()