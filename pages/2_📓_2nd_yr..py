import streamlit as st
from PIL import Image
import webbrowser


# ---PAGE_TITLE---
st.set_page_config(page_title="2nd yr.", page_icon="📖", layout="wide")

# Use local CSS
def local_CSS(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_CSS("style/style1.css")


# Using object notation
choice = st.sidebar.selectbox(
    "Choose Subject:",
    ("DS", "COA", "DSTL", "Maths IV", "Python", "Technical Communication", "Digital Electronics", "Human Values", "Computer System Security", "Microprocessor", "Operating Systems", "Automata", "Sensor Instrumentation", "Electronics Engg.")
)

if choice == "DS":
    img_DSA = Image.open("images/ds.jpg")

    left_column, right_column = st.columns((2, 1))
    with right_column:
        st.image(img_DSA)
    with left_column:
        st.header("Data Structure")
        st.subheader("Subject code: KCS301")

    st.write("---")
    st.subheader("Studocu:")
    link = st.button('*Click here...*', key = "1")
    if link:
        webbrowser.open('https://www.studocu.com/in/course/dr-apj-abdul-kalam-technical-university/data-structure/4904876')

    st.write("###")
    st.subheader("Topperworld:")
    link = st.button('*Click here...*', key = "2")
    if link:
        webbrowser.open('https://topperworld.in/aktu-b-tech-data-structure-notes/')
    
    st.write("###")
    st.subheader("AKTUtor:")
    link = st.button('*Click here...*', key = "3")
    if link:
        webbrowser.open('https://drive.google.com/file/d/1fVMePwWWZFtTTAEDExnXX6p-AfTbRtyo/view')
    st.write("###")
    st.subheader("source:")
    link = st.button('*Click here...*', key = "4")
    if link:
        webbrowser.open('link...')
    
    st.write("###")
    st.subheader("source:")
    link = st.button('*Click here...*', key = "5")
    if link:
        webbrowser.open('link...')

elif choice == "COA":
    img_COA = Image.open("images/coa.jpg")

    left_column, right_column = st.columns((2, 1))
    with right_column:
        st.image(img_COA)
    with left_column:
        st.header("Computer Organization and Architecture")
        st.subheader("Subject code: KCS302")
        
    st.write("---")
    st.subheader("source:")
    link = st.button('*Click here...*', key = "1")
    if link:
        webbrowser.open('link...')
    
    st.write("###")
    st.subheader("source:")
    link = st.button('*Click here...*', key = "2")
    if link:
        webbrowser.open('link...')
    
    st.write("###")
    st.subheader("source:")
    link = st.button('*Click here...*', key = "3")
    if link:
        webbrowser.open('link...')
    
    st.write("###")
    st.subheader("source:")
    link = st.button('*Click here...*', key = "4")
    if link:
        webbrowser.open('link...')
    
    st.write("###")
    st.subheader("source:")
    link = st.button('*Click here...*', key = "5")
    if link:
        webbrowser.open('link...')

elif choice == "DSTL":
    img_COA = Image.open("images/Dstl.jpg")

    left_column, right_column = st.columns((2, 1))
    with right_column:
        st.image(img_COA)
    with left_column:
        st.header("Data Structure and Theory of Logic")
        st.subheader("Subject code: KCS303")
        
    st.write("---")
    st.subheader("source:")
    link = st.button('*Click here...*', key = "1")
    if link:
        webbrowser.open('link...')
    
    st.write("###")
    st.subheader("source:")
    link = st.button('*Click here...*', key = "2")
    if link:
        webbrowser.open('link...')
    
    st.write("###")
    st.subheader("source:")
    link = st.button('*Click here...*', key = "3")
    if link:
        webbrowser.open('link...')
    
    st.write("###")
    st.subheader("source:")
    link = st.button('*Click here...*', key = "4")
    if link:
        webbrowser.open('link...')
    
    st.write("###")
    st.subheader("source:")
    link = st.button('*Click here...*', key = "5")
    if link:
        webbrowser.open('link...')

elif choice == "Maths IV":
    img_COA = Image.open("images/maths.jpg")

    left_column, right_column = st.columns((2, 1))
    with right_column:
        st.image(img_COA)
    with left_column:
        st.header("Engg. Mathematics IV")
        st.subheader("Subject code: KAS302")
        
    st.write("---")
    st.subheader("source:")
    link = st.button('*Click here...*', key = "1")
    if link:
        webbrowser.open('link...')
    
    st.write("###")
    st.subheader("source:")
    link = st.button('*Click here...*', key = "2")
    if link:
        webbrowser.open('link...')
    
    st.write("###")
    st.subheader("source:")
    link = st.button('*Click here...*', key = "3")
    if link:
        webbrowser.open('link...')
    
    st.write("###")
    st.subheader("source:")
    link = st.button('*Click here...*', key = "4")
    if link:
        webbrowser.open('link...')
    
    st.write("###")
    st.subheader("source:")
    link = st.button('*Click here...*', key = "5")
    if link:
        webbrowser.open('link...')

elif choice == "Python":
    img_COA = Image.open("images/py.png")

    left_column, right_column = st.columns((2, 1))
    with right_column:
        st.image(img_COA)
    with left_column:
        st.header("Python Programming")
        st.subheader("Subject code: KNC302")
        
    st.write("---")
    st.subheader("source:")
    link = st.button('*Click here...*', key = "1")
    if link:
        webbrowser.open('link...')
    
    st.write("###")
    st.subheader("source:")
    link = st.button('*Click here...*', key = "2")
    if link:
        webbrowser.open('link...')
    
    st.write("###")
    st.subheader("source:")
    link = st.button('*Click here...*', key = "3")
    if link:
        webbrowser.open('link...')
    
    st.write("###")
    st.subheader("source:")
    link = st.button('*Click here...*', key = "4")
    if link:
        webbrowser.open('link...')
    
    st.write("###")
    st.subheader("source:")
    link = st.button('*Click here...*', key = "5")
    if link:
        webbrowser.open('link...')

elif choice == "Technical Communication":
    img_COA = Image.open("images/TC.jpg")

    left_column, right_column = st.columns((2, 1))
    with right_column:
        st.image(img_COA)
    with left_column:
        st.header("Technical Commyunication")
        st.subheader("Subject code: KAS301")
        
    st.write("---")
    st.subheader("source:")
    link = st.button('*Click here...*', key = "1")
    if link:
        webbrowser.open('link...')
    
    st.write("###")
    st.subheader("source:")
    link = st.button('*Click here...*', key = "2")
    if link:
        webbrowser.open('link...')
    
    st.write("###")
    st.subheader("source:")
    link = st.button('*Click here...*', key = "3")
    if link:
        webbrowser.open('link...')
    
    st.write("###")
    st.subheader("source:")
    link = st.button('*Click here...*', key = "4")
    if link:
        webbrowser.open('link...')
    
    st.write("###")
    st.subheader("source:")
    link = st.button('*Click here...*', key = "5")
    if link:
        webbrowser.open('link...')

elif choice == "Digital Electronics":
    img_COA = Image.open("images/de.jpg")

    left_column, right_column = st.columns((2, 1))
    with right_column:
        st.image(img_COA)
    with left_column:
        st.header("Digital Electronics")
        st.subheader("Subject code: KOE039/039H")
        
    st.write("---")
    st.subheader("source:")
    link = st.button('*Click here...*', key = "1")
    if link:
        webbrowser.open('link...')
    
    st.write("###")
    st.subheader("source:")
    link = st.button('*Click here...*', key = "2")
    if link:
        webbrowser.open('link...')
    
    st.write("###")
    st.subheader("source:")
    link = st.button('*Click here...*', key = "3")
    if link:
        webbrowser.open('link...')
    
    st.write("###")
    st.subheader("source:")
    link = st.button('*Click here...*', key = "4")
    if link:
        webbrowser.open('link...')
    
    st.write("###")
    st.subheader("source:")
    link = st.button('*Click here...*', key = "5")
    if link:
        webbrowser.open('link...')

elif choice == "Human Values":
    img_COA = Image.open("images/hv.png")

    left_column, right_column = st.columns((2, 1))
    with right_column:
        st.image(img_COA)
    with left_column:
        st.header("Universal Human Value")
        st.subheader("Subject code: KVE301")
        
    st.write("---")
    st.subheader("source:")
    link = st.button('*Click here...*', key = "1")
    if link:
        webbrowser.open('link...')
    
    st.write("###")
    st.subheader("source:")
    link = st.button('*Click here...*', key = "2")
    if link:
        webbrowser.open('link...')
    
    st.write("###")
    st.subheader("source:")
    link = st.button('*Click here...*', key = "3")
    if link:
        webbrowser.open('link...')
    
    st.write("###")
    st.subheader("source:")
    link = st.button('*Click here...*', key = "4")
    if link:
        webbrowser.open('link...')
    
    st.write("###")
    st.subheader("source:")
    link = st.button('*Click here...*', key = "5")
    if link:
        webbrowser.open('link...')

elif choice == "Computer System Security":
    img_COA = Image.open("images/R.jpg")

    left_column, right_column = st.columns((2, 1))
    with right_column:
        st.image(img_COA)
    with left_column:
        st.header("Computer System Security")
        st.subheader("Subject code: KNC301")
        
    st.write("---")
    st.subheader("source:")
    link = st.button('*Click here...*', key = "1")
    if link:
        webbrowser.open('link...')
    
    st.write("###")
    st.subheader("source:")
    link = st.button('*Click here...*', key = "2")
    if link:
        webbrowser.open('link...')
    
    st.write("###")
    st.subheader("source:")
    link = st.button('*Click here...*', key = "3")
    if link:
        webbrowser.open('link...')
    
    st.write("###")
    st.subheader("source:")
    link = st.button('*Click here...*', key = "4")
    if link:
        webbrowser.open('link...')
    
    st.write("###")
    st.subheader("source:")
    link = st.button('*Click here...*', key = "5")
    if link:
        webbrowser.open('link...')

elif choice == "Microprocessor":
    img_COA = Image.open("images/mic.jpg")

    left_column, right_column = st.columns((2, 1))
    with right_column:
        st.image(img_COA)
    with left_column:
        st.header("Microprocessor")
        st.subheader("Subject code: KCS403")
        
    st.write("---")
    st.subheader("source:")
    link = st.button('*Click here...*', key = "1")
    if link:
        webbrowser.open('link...')
    
    st.write("###")
    st.subheader("source:")
    link = st.button('*Click here...*', key = "2")
    if link:
        webbrowser.open('link...')
    
    st.write("###")
    st.subheader("source:")
    link = st.button('*Click here...*', key = "3")
    if link:
        webbrowser.open('link...')
    
    st.write("###")
    st.subheader("source:")
    link = st.button('*Click here...*', key = "4")
    if link:
        webbrowser.open('link...')
    
    st.write("###")
    st.subheader("source:")
    link = st.button('*Click here...*', key = "5")
    if link:
        webbrowser.open('link...')

elif choice == "Operating Systems":
    img_COA = Image.open("images/os.jpg")

    left_column, right_column = st.columns((2, 1))
    with right_column:
        st.image(img_COA)
    with left_column:
        st.header("Operating Systems")
        st.subheader("Subject code: KCS401")
        
    st.write("---")
    st.subheader("source:")
    link = st.button('*Click here...*', key = "1")
    if link:
        webbrowser.open('link...')
    
    st.write("###")
    st.subheader("source:")
    link = st.button('*Click here...*', key = "2")
    if link:
        webbrowser.open('link...')
    
    st.write("###")
    st.subheader("source:")
    link = st.button('*Click here...*', key = "3")
    if link:
        webbrowser.open('link...')
    
    st.write("###")
    st.subheader("source:")
    link = st.button('*Click here...*', key = "4")
    if link:
        webbrowser.open('link...')
    
    st.write("###")
    st.subheader("source:")
    link = st.button('*Click here...*', key = "5")
    if link:
        webbrowser.open('link...')

elif choice == "Automata":
    img_COA = Image.open("images/aut.jpg")

    left_column, right_column = st.columns((2, 1))
    with right_column:
        st.image(img_COA)
    with left_column:
        st.header("Theory of Automata and Formal Languages")
        st.subheader("Subject code: KCS402")
        
    st.write("---")
    st.subheader("source:")
    link = st.button('*Click here...*', key = "1")
    if link:
        webbrowser.open('link...')
    
    st.write("###")
    st.subheader("source:")
    link = st.button('*Click here...*', key = "2")
    if link:
        webbrowser.open('link...')
    
    st.write("###")
    st.subheader("source:")
    link = st.button('*Click here...*', key = "3")
    if link:
        webbrowser.open('link...')
    
    st.write("###")
    st.subheader("source:")
    link = st.button('*Click here...*', key = "4")
    if link:
        webbrowser.open('link...')
    
    st.write("###")
    st.subheader("source:")
    link = st.button('*Click here...*', key = "5")
    if link:
        webbrowser.open('link...')

elif choice == "Sensor Instrumentation":
    img_COA = Image.open("images/si.jpg")

    left_column, right_column = st.columns((2, 1))
    with right_column:
        st.image(img_COA)
    with left_column:
        st.header("Sensor Instrumentation")
        st.subheader("Subject code: KOE034/034H")
        
    st.write("---")
    st.subheader("source:")
    link = st.button('*Click here...*', key = "1")
    if link:
        webbrowser.open('link...')
    
    st.write("###")
    st.subheader("source:")
    link = st.button('*Click here...*', key = "2")
    if link:
        webbrowser.open('link...')
    
    st.write("###")
    st.subheader("source:")
    link = st.button('*Click here...*', key = "3")
    if link:
        webbrowser.open('link...')
    
    st.write("###")
    st.subheader("source:")
    link = st.button('*Click here...*', key = "4")
    if link:
        webbrowser.open('link...')
    
    st.write("###")
    st.subheader("source:")
    link = st.button('*Click here...*', key = "5")
    if link:
        webbrowser.open('link...')

elif choice == "Electronics Engg.":
    img_COA = Image.open("images/ee.jpg")

    left_column, right_column = st.columns((2, 1))
    with right_column:
        st.image(img_COA)
    with left_column:
        st.header("Electronics Engg.")
        st.subheader("Subject code: KOE038/038H")
        
    st.write("---")
    st.subheader("source:")
    link = st.button('*Click here...*', key = "1")
    if link:
        webbrowser.open('link...')
    
    st.write("###")
    st.subheader("source:")
    link = st.button('*Click here...*', key = "2")
    if link:
        webbrowser.open('link...')
    
    st.write("###")
    st.subheader("source:")
    link = st.button('*Click here...*', key = "3")
    if link:
        webbrowser.open('link...')
    
    st.write("###")
    st.subheader("source:")
    link = st.button('*Click here...*', key = "4")
    if link:
        webbrowser.open('link...')
    
    st.write("###")
    st.subheader("source:")
    link = st.button('*Click here...*', key = "5")
    if link:
        webbrowser.open('link...')