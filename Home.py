import requests
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu




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
    st.title('Welcome to Project: eLibrary!')
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
    <form action="https://formsubmit.co/rachit190403@gmail.com" method="POST">
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