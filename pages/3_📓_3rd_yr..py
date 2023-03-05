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
    ("DBMS","Machine Learning","Soft Computing","Compiler Design","Data Analytics","software Engineering","Web Technology")
)

if choice == "DBMS":
    img_DBMS = Image.open("images/Database-Management-System.jpg")

    left_column, right_column = st.columns((2, 1))
    with right_column:
        st.image(img_DBMS)
    with left_column:
        st.header("DataBase Management System")
        st.subheader("Subject code: RCS501")

    st.write("---")
    st.subheader("Unit 1:")
    link = st.button('*Click here...*', key = "1")
    if link:
        webbrowser.open('https://drive.google.com/file/d/11o3esp4v-vPJ-5qxhGjp9ccnvk7yBcuo/view?usp=share_link')

    st.write("###")
    st.subheader("Unit 2:")
    link = st.button('*Click here...*', key = "2")
    if link:
        webbrowser.open('https://drive.google.com/file/d/11o3esp4v-vPJ-5qxhGjp9ccnvk7yBcuo/view?usp=share_link')
    
    st.write("###")
    st.subheader("Unit 3:")
    link = st.button('*Click here...*', key = "3")
    if link:
        webbrowser.open('https://drive.google.com/file/d/11o3esp4v-vPJ-5qxhGjp9ccnvk7yBcuo/view?usp=share_link')
    st.write("###")
    st.subheader("Unit 4:")
    link = st.button('*Click here...*', key = "4")
    if link:
        webbrowser.open('https://drive.google.com/file/d/11o3esp4v-vPJ-5qxhGjp9ccnvk7yBcuo/view?usp=share_link')
    
    st.write("###")
    st.subheader("Unit 5:")
    link = st.button('*Click here...*', key = "5")
    if link:
        webbrowser.open('https://drive.google.com/file/d/11o3esp4v-vPJ-5qxhGjp9ccnvk7yBcuo/view?usp=share_link')

elif choice == "Machine Learning":
    img_ML= Image.open("images/machine learning.jpg")

    left_column, right_column = st.columns((2, 1))
    with right_column:
        st.image(img_ML)
    with left_column:
        st.header("Machine Learning")
        st.subheader("Subject code: KCS055 ")
        
    st.write("---")
    st.subheader("Unit 1:")
    link = st.button('*Click here...*', key = "1")
    if link:
        webbrowser.open('https://drive.google.com/file/d/1_8CFf-lcV260-IvsGKAl8JSb-ACto1lK/view?usp=share_link')
    
    st.write("###")
    st.subheader("Unit 2:")
    link = st.button('*Click here...*', key = "2")
    if link:
        webbrowser.open('')
    
    st.write("###")
    st.subheader("Unit 3:")
    link = st.button('*Click here...*', key = "3")
    if link:
        webbrowser.open('link...')
    
    st.write("###")
    st.subheader("Unit 4:")
    link = st.button('*Click here...*', key = "4")
    if link:
        webbrowser.open('link...')
    
    st.write("###")
    st.subheader("Unit 5:")
    link = st.button('*Click here...*', key = "5")
    if link:
        webbrowser.open('link...')

elif choice == "Soft Computing":
    img_Cs = Image.open("images/soft computing.jpg")

    left_column, right_column = st.columns((2, 1))
    with right_column:
        st.image(img_Cs)
    with left_column:
        st.header("Soft computing")
        st.subheader("Subject code: KCS056")
        
    st.write("---")
    st.subheader("Unit 1:")
    link = st.button('*Click here...*', key = "1")
    if link:
        webbrowser.open('link...')
    
    st.write("###")
    st.subheader("Unit 2:")
    link = st.button('*Click here...*', key = "2")
    if link:
        webbrowser.open('link...')
    
    st.write("###")
    st.subheader("Unit 3:")
    link = st.button('*Click here...*', key = "3")
    if link:
        webbrowser.open('link...')
    
    st.write("###")
    st.subheader("Unit 4:")
    link = st.button('*Click here...*', key = "4")
    if link:
        webbrowser.open('link...')
    
    st.write("###")
    st.subheader("Unit 5:")
    link = st.button('*Click here...*', key = "5")
    if link:
        webbrowser.open('https://drive.google.com/file/d/1agIGRgo8aJrKWqNVPRdtOXjjtoOaGw2A/view?usp=share_link')

elif choice == "Compiler Design":
    img_COA = Image.open("images/maths.jpg")

    left_column, right_column = st.columns((2, 1))
    with right_column:
        st.image(img_COA)
    with left_column:
        st.header("Compiler Design")
        st.subheader("Subject code: KCS502")
        
    st.write("---")
    st.subheader("Unit 1:")
    link = st.button('*Click here...*', key = "1")
    if link:
        webbrowser.open('link...')
    
    st.write("###")
    st.subheader("Unit 2:")
    link = st.button('*Click here...*', key = "2")
    if link:
        webbrowser.open('link...')
    
    st.write("###")
    st.subheader("Unit 3:")
    link = st.button('*Click here...*', key = "3")
    if link:
        webbrowser.open('link...')
    
    st.write("###")
    st.subheader("Unit 4:")
    link = st.button('*Click here...*', key = "4")
    if link:
        webbrowser.open('link...')
    
    st.write("###")
    st.subheader("Unit 5:")
    link = st.button('*Click here...*', key = "5")
    if link:
        webbrowser.open('link...')

elif choice == "Data Analytics":
    img_data_a = Image.open("images/data analytics.jpg")

    left_column, right_column = st.columns((2, 1))
    with right_column:
        st.image(img_data_a)
    with left_column:
        st.header("Data Analytics")
        st.subheader("Subject code: KCS051")
        
    st.write("---")
    st.subheader("Unit 1:")
    link = st.button('*Click here...*', key = "1")
    if link:
        webbrowser.open('https://drive.google.com/file/d/1vrM46WgBjCqKRm4YXi4k8fibZi978Sbs/view?usp=share_link')
    
    st.write("###")
    st.subheader("Unit 2:")
    link = st.button('*Click here...*', key = "2")
    if link:
        webbrowser.open('https://drive.google.com/file/d/1vrM46WgBjCqKRm4YXi4k8fibZi978Sbs/view?usp=share_link')
    
    st.write("###")
    st.subheader("Unit 3:")
    link = st.button('*Click here...*', key = "3")
    if link:
        webbrowser.open('https://drive.google.com/file/d/1W8FG5C2SqLH2lXuXI-xbdgh0sf6XQ8s8/view?usp=share_link')
    
    st.write("###")
    st.subheader("Unit 4:")
    link = st.button('*Click here...*', key = "4")
    if link:
        webbrowser.open('https://drive.google.com/file/d/1W8FG5C2SqLH2lXuXI-xbdgh0sf6XQ8s8/view?usp=share_link')
    
    st.write("###")
    st.subheader("Unit 5:")
    link = st.button('*Click here...*', key = "5")
    if link:
        webbrowser.open('https://drive.google.com/file/d/1Lra7EWsoCx5nLissGH3ztZQ93vvFP017/view?usp=share_link')

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