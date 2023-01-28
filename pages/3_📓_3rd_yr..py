import streamlit as st
from PIL import Image
import webbrowser


# ---PAGE_TITLE---
st.set_page_config(page_title="3rd yr.", page_icon="📖", layout="wide")

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style1.css")


# Using object notation
choice = st.sidebar.selectbox(
    "Choose Subject:",
    ("DS", "COA", "DSTL", "Maths IV", "Python", "Technical Communication", "Digital Electronics", "Human Values", "CSS", "Microprocessor", "Operating Systems", "Automata", "Sensor Instrumentation", "Electronics Engg.")
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

elif choice == "COA":
    img_COA = Image.open("images/OIP.jpg")

    left_column, right_column = st.columns((2, 1))
    with right_column:
        st.image(img_COA)
    with left_column:
        st.header("Computer Organization and Architecture")
        st.subheader("Subject code: KCS301")
        
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
        st.header("Data Structure")
        st.subheader("Subject code: KCS301")
        
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
        st.header("Data Structure")
        st.subheader("Subject code: KCS301")
        
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
        st.header("Data Structure")
        st.subheader("Subject code: KCS301")
        
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
        st.header("Data Structure")
        st.subheader("Subject code: KCS301")
        
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
        st.header("Data Structure")
        st.subheader("Subject code: KCS301")
        
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
        st.header("Data Structure")
        st.subheader("Subject code: KCS301")
        
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

elif choice == "CSS":
    img_COA = Image.open("images/R.jpg")

    left_column, right_column = st.columns((2, 1))
    with right_column:
        st.image(img_COA)
    with left_column:
        st.header("Data Structure")
        st.subheader("Subject code: KCS301")
        
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
        st.header("Data Structure")
        st.subheader("Subject code: KCS301")
        
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
        st.header("Data Structure")
        st.subheader("Subject code: KCS301")
        
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
        st.header("Data Structure")
        st.subheader("Subject code: KCS301")
        
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
        st.header("Data Structure")
        st.subheader("Subject code: KCS301")
        
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
        st.header("Data Structure")
        st.subheader("Subject code: KCS301")
        
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