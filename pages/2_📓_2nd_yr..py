import streamlit as st
from PIL import Image
import webbrowser
from streamlit.components.v1 import html


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
    ("Maths IV", "COA", "DSTL", "DS", "Python", "Technical Communication", "Digital Electronics", "Human Values", "Computer System Security", "Microprocessor", "Operating Systems", "Automata", "Sensor Instrumentation", "Electronics Engg."),
)
# choicePyq = st.sidebar.selectbox(
#     "Choose Subject For Pyq:",
#     ("1st semester","2nd semester","3rd semester","4th semester","5th semester","6th semester","7th semester","8th semester")
# )

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
        
elif choice == "COA":
    img_COA = Image.open("images/coa.jpg")

    left_column, right_column = st.columns((2, 1))
    with right_column:
        st.image(img_COA)
    with left_column:
        st.header("Computer Organization and Architecture")
        st.subheader("Subject code: KCS302")
        
    st.write("###")
    st.subheader("Unit 1:")
    link = st.button('*Click here...*', key = "1")
    if link:
        webbrowser.open('https://drive.google.com/file/d/1oMPcRA9qX0tiDW7mC2c2NXBPbLsZkhby/view?usp=share_link')
    
    st.write("###")
    st.subheader("Unit 2:")
    link = st.button('*Click here...*', key = "2")
    if link:
        webbrowser.open('https://drive.google.com/file/d/17esR_MQ9Ncee8f-s7Wc9yKxQlIMO7nvN/view?usp=share_link')
    
    st.write("###")
    st.subheader("Unit 3:")
    link = st.button('*Click here...*', key = "3")
    if link:
        webbrowser.open('link...')
    
    st.write("###")
    st.subheader("Unit 4:")
    link = st.button('*Click here...*', key = "4")
    if link:
        webbrowser.open('https://drive.google.com/file/d/1v19mRn92XaNBrPYKuPKkbdy5q8jbML5p/view?usp=share_link')
    
    st.write("###")
    st.subheader("Unit 5:")
    link = st.button('*Click here...*', key = "5")
    if link:
        webbrowser.open('link...')

elif choice == "DSTL":
    img_COA = Image.open("images/Dstl.jpg")

    left_column, right_column = st.columns((2, 1))
    with right_column:
        st.image(img_COA)
    with left_column:
        st.header("Discrete Structure and Theory of Logic")
        st.subheader("Subject code: KCS303")
        
    st.write("###")
    st.subheader("Unit 1:")
    link = st.button('*Click here...*', key = "1")
    if link:
        webbrowser.open('.......')
    
    st.write("###")
    st.subheader("Unit 2:")
    link = st.button('*Click here...*', key = "2")
    if link:
        webbrowser.open('......')
    
    st.write("###")
    st.subheader("Unit 3:")
    link = st.button('*Click here...*', key = "3")
    if link:
        webbrowser.open('.........')
    
    st.write("###")
    st.subheader("Unit 4:")
    link = st.button('*Click here...*', key = "4")
    if link:
        webbrowser.open('.........')
    
    st.write("###")
    st.subheader("Unit 5:")
    link = st.button('*Click here...*', key = "5")
    if link:
        webbrowser.open('...........')

elif choice == "Maths IV":
    img_COA = Image.open("images/maths.jpg")

    left_column, right_column = st.columns((2, 1))
    with right_column:
        st.image(img_COA)
    with left_column:
        st.header("Engg. Mathematics IV")
        st.subheader("Subject code: KAS302")
        
    st.write("###")
    st.subheader("Unit 1:")
    link = st.button('*Click here...*', key = "1")
    if link:
        webbrowser.open('https://drive.google.com/file/d/1GyhumryUmNcVWXj3DkjikWjwrzWO0sd5/view?usp=share_link')
    
    st.write("###")
    st.subheader("Unit 2:")
    link = st.button('*Click here...*', key = "2")
    if link:
        webbrowser.open('https://drive.google.com/file/d/1wJKGmMOVU-GtDQGSqRNZd8TMKV3nVo76/view?usp=share_link')
    
    st.write("###")
    st.subheader("Unit 3:")
    link = st.button('*Click here...*', key = "3")
    if link:
        webbrowser.open('https://drive.google.com/file/d/11K96YGCzF0NI5jFQ4o0FyMXzP1o6xbU0/view?usp=share_link')
    
    st.write("###")
    st.subheader("Unit 4:")
    link = st.button('*Click here...*', key = "4")
    if link:
        webbrowser.open('https://drive.google.com/file/d/1nHT-bNEvflbkRfgc-q3VQGxRHnU99ZoB/view?usp=share_link')
    
    st.write("###")
    st.subheader("Unit 5:")
    link = st.button('*Click here...*', key = "5")
    if link:
        webbrowser.open('https://drive.google.com/file/d/1nHT-bNEvflbkRfgc-q3VQGxRHnU99ZoB/view?usp=share_link')

elif choice == "Python":
    img_COA = Image.open("images/py.png")

    left_column, right_column = st.columns((2, 1))
    with right_column:
        st.image(img_COA)
    with left_column:
        st.header("Python Programming")
        st.subheader("Subject code: KNC302")
        
    st.write("---")
    st.subheader("Unit 1:")
    link = st.button('*Click here...*', key = "1")
    if link:
        webbrowser.open('https://drive.google.com/file/d/1wgDNqJYNckyUetP9no82YiLjX-kuSKMb/view?usp=share_link')
    
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

elif choice == "Technical Communication":
    img_COA = Image.open("images/TC.jpg")

    left_column, right_column = st.columns((2, 1))
    with right_column:
        st.image(img_COA)
    with left_column:
        st.header("Technical Commyunication")
        st.subheader("Subject code: KAS301")
        
    st.write("---")
    st.subheader("Unit 1:")
    link = st.button('*Click here...*', key = "1")
    if link:
        webbrowser.open('https://drive.google.com/file/d/1lqXVpK8E-2Q9_MoPDERmTxMNtLAcFrtT/view?usp=share_link')
    
    st.write("###")
    st.subheader("Unit 2:")
    link = st.button('*Click here...*', key = "2")
    if link:
        webbrowser.open('https://drive.google.com/file/d/1lqXVpK8E-2Q9_MoPDERmTxMNtLAcFrtT/view?usp=share_link')
    
    st.write("###")
    st.subheader("Unit 3:")
    link = st.button('*Click here...*', key = "3")
    if link:
        webbrowser.open('https://drive.google.com/file/d/1lqXVpK8E-2Q9_MoPDERmTxMNtLAcFrtT/view?usp=share_link')
    
    st.write("###")
    st.subheader("Unit 4:")
    link = st.button('*Click here...*', key = "4")
    if link:
        webbrowser.open('https://drive.google.com/file/d/1lqXVpK8E-2Q9_MoPDERmTxMNtLAcFrtT/view?usp=share_link')
    
    st.write("###")
    st.subheader("Unit 5:")
    link = st.button('*Click here...*', key = "5")
    if link:
        webbrowser.open('https://drive.google.com/file/d/1lqXVpK8E-2Q9_MoPDERmTxMNtLAcFrtT/view?usp=share_link')

elif choice == "Digital Electronics":
    img_COA = Image.open("images/de.jpg")

    left_column, right_column = st.columns((2, 1))
    with right_column:
        st.image(img_COA)
    with left_column:
        st.header("Digital Electronics")
        st.subheader("Subject code: KOE039/039H")
        
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

elif choice == "Human Values":
    img_COA = Image.open("images/hv.png")

    left_column, right_column = st.columns((2, 1))
    with right_column:
        st.image(img_COA)
    with left_column:
        st.header("Universal Human Value")
        st.subheader("Subject code: KVE301")
        
    st.write("---")
    st.subheader("Unit 1:")
    link = st.button('*Click here...*', key = "1")
    if link:
        webbrowser.open('https://drive.google.com/file/d/1LmJWlucbZZLSss1sJDOd9YYudCjn7-ql/view?usp=share_link')
    
    st.write("###")
    st.subheader("Unit 2:")
    link = st.button('*Click here...*', key = "2")
    if link:
        webbrowser.open('https://drive.google.com/file/d/1LmJWlucbZZLSss1sJDOd9YYudCjn7-ql/view?usp=share_link')
    
    st.write("###")
    st.subheader("Unit 3:")
    link = st.button('*Click here...*', key = "3")
    if link:
        webbrowser.open('https://drive.google.com/file/d/1LmJWlucbZZLSss1sJDOd9YYudCjn7-ql/view?usp=share_link')
    
    st.write("###")
    st.subheader("Unit 4:")
    link = st.button('*Click here...*', key = "4")
    if link:
        webbrowser.open('https://drive.google.com/file/d/1LmJWlucbZZLSss1sJDOd9YYudCjn7-ql/view?usp=share_link')
    
    st.write("###")
    st.subheader("Unit 5:")
    link = st.button('*Click here...*', key = "5")
    if link:
        webbrowser.open('https://drive.google.com/file/d/1LmJWlucbZZLSss1sJDOd9YYudCjn7-ql/view?usp=share_link')

elif choice == "Computer System Security":
    img_COA = Image.open("images/R.jpg")

    left_column, right_column = st.columns((2, 1))
    with right_column:
        st.image(img_COA)
    with left_column:
        st.header("Computer System Security")
        st.subheader("Subject code: KNC301")
        
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

elif choice == "Microprocessor":
    img_COA = Image.open("images/mic.jpg")

    left_column, right_column = st.columns((2, 1))
    with right_column:
        st.image(img_COA)
    with left_column:
        st.header("Microprocessor")
        st.subheader("Subject code: KCS403")
        
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

elif choice == "Operating Systems":
    img_COA = Image.open("images/os.jpg")

    left_column, right_column = st.columns((2, 1))
    with right_column:
        st.image(img_COA)
    with left_column:
        st.header("Operating Systems")
        st.subheader("Subject code: KCS401")
        
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

elif choice == "Automata":
    img_COA = Image.open("images/aut.jpg")

    left_column, right_column = st.columns((2, 1))
    with right_column:
        st.image(img_COA)
    with left_column:
        st.header("Theory of Automata and Formal Languages")
        st.subheader("Subject code: KCS402")
        
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

elif choice == "Sensor Instrumentation":
    img_COA = Image.open("images/si.jpg")

    left_column, right_column = st.columns((2, 1))
    with right_column:
        st.image(img_COA)
    with left_column:
        st.header("Sensor Instrumentation")
        st.subheader("Subject code: KOE034/034H")
        
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

elif choice == "Electronics Engg.":
    img_COA = Image.open("images/ee.jpg")

    left_column, right_column = st.columns((2, 1))
    with right_column:
        st.image(img_COA)
    with left_column:
        st.header("Electronics Engg.")
        st.subheader("Subject code: KOE038/038H")
        
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


# ................................................................................




# if choicePyq == "1st semester":
#     pureButton = '''<style>
#     a{
#         text-decoration: none;
#         color: white;
#         border: 2px solid rgb(170, 199, 199);
#         border-radius: 2px;
#         padding: 3px 6px 3px 6px;
#         background-color: black;
#     }
# </style>
#     <a href='https://drive.google.com/drive/folders/1Ya_3tHGTwUz_XbUxUU4Qim1Ww-0Nck5I?usp=sharing' target='_blank'>Submit</a>
# '''
#     html(pureButton)
# elif choicePyq == "2nd semester":
#     pureButton = '''<style>
#     a{
#         text-decoration: none;
#         color: white;
#         border: 2px solid rgb(170, 199, 199);
#         border-radius: 2px;
#         padding: 3px 6px 3px 6px;
#         background-color: black;
#     }
# </style>
#     <a href='https://drive.google.com/drive/folders/18tm0pZsLSycC3ojvIO6FXjWvF4I7FNmb?usp=sharing' target='_blank'>Submit</a>
# '''
#     html(pureButton)
# elif choicePyq == "3rd semester":
#     pureButton = '''<style>
#     a{
#         text-decoration: none;
#         color: white;
#         border: 2px solid rgb(170, 199, 199);
#         border-radius: 2px;
#         padding: 3px 6px 3px 6px;
#         background-color: black;
#     }
# </style>
#     <a href='https://drive.google.com/drive/folders/1eMMpqlhUx9msLavZfssmfKjXsGBEfeu9?usp=sharing' target='_blank'>Submit</a>
# '''
#     html(pureButton)
# elif choicePyq == "4th semester":
#     pureButton = '''<style>
#     a{
#         text-decoration: none;
#         color: white;
#         border: 2px solid rgb(170, 199, 199);
#         border-radius: 2px;
#         padding: 3px 6px 3px 6px;
#         background-color: black;
#     }
# </style>
#     <a href='https://drive.google.com/drive/folders/19-Rj6yaFuCxzMKl8Ig9gQMRYfVsJqwJn?usp=sharing' target='_blank'>Submit</a>
# '''
#     html(pureButton)
# elif choicePyq == "5th semester":
#     pureButton = '''<style>
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
#     html(pureButton)
# elif choicePyq == "6th semester":
#     pureButton = '''<style>
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
#     html(pureButton)
# elif choicePyq == "7th semester":
#     pureButton = '''<style>
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
#     html(pureButton)
# elif choicePyq == "8th semester":
#     pureButton = '''<style>
#     a{
#         text-decoration: none;
#         color: white;
#         border: 2px solid rgb(170, 199, 199);
#         border-radius: 2px;
#         padding: 3px 6px 3px 6px;
#         background-color: black;
#     }
# </style>
#     <a href='http://www.google.com' target='_blank'>Click For 8th semester</a>
# '''
#     html(pureButton)
    