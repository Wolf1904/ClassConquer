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
st.set_page_config(page_title="eLibrary", page_icon=":books:", layout="wide")

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
    st.title('Welcome to LMS')
    st.write("Learning Management System")
    st.write('###')

    left_column, right_column = st.columns(2)
    with right_column:
        st.header('Why you should use?')
        st.write(
            '''
            - It help the students to integrate the technology into the curriculum, by increasing the technology literacy.
            - This e-library offers a variety of resources that can help you earn your degree, regardless of the subject or level you’re pursuing. This is through providing an environment conducive to learning, helpful librarians, and a variety of reference materials.
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
        webbrowser.open('www.google.com')
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
        - The eNotes of all subjects which are taught in 2nd and 3rd year
        - Notes from different colleges affilated to AKTU
        '''
    )

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Us!")
    st.write("##")

    contact_form = """
    <form action="https://formsubmit.co/el/xicoje" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
