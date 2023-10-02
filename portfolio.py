import streamlit as st
from streamlit_option_menu import option_menu
st.set_page_config(page_title = "Akshay Developer & Enterprise",page_icon="🚀",layout="wide")
# Custom CSS to set a light theme with a white background
custom_css = """
<style>
body {
    background-color: white;
    color: black;  /* Set text color to black for better contrast */
}
</style>
"""
# Set the theme to "light"
st.set_page_config(
    page_title="Akshay Developer & Enterprise",
    page_icon=":rocket:",
    layout="wide",  # You can adjust the layout as needed
)
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """


# Create a Streamlit web app
with st.container():
            til1, til2 = st.columns([1,6.2])
            with til1:
                st.write('\n')
                #st.image("cd_logos.svg", width = 125)
            with til2:
                st.markdown(
                """
                <style>
                
                .custom-header {
                text-align: center;
                background-color: #f1f1f1;
                padding: 8px;
                margin-bottom: 10px;
                
                box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.1); 
                }
                @import url('https://fonts.googleapis.com/css2?family=Avro&display=swap');
                .custom-header h2 {
                color: #003366;
                font-family: 'georgia', sans-serif;
                font-size: 42px;
                }
                
                </style>
                """,
                unsafe_allow_html=True
                )
                st.markdown('<div class="custom-header"><h2>Akshay Developer & Enterprise</h2></div>', unsafe_allow_html=True)

st.write('\n')               
selected = option_menu(
    menu_title=None,
    options=['Home','Connect Data','White Paper','Live Monitoring','Report'],
    icons=['house','cloud-upload','file-earmark-check','graph-up-arrow','file-earmark-bar-graph'],
    default_index=0,
    orientation='horizontal',
    styles={
            "container": {"padding": "0!important", "background-color": "#003366","border": "2px solid #003366"},
             
            "nav-link": {"color": "#FFF","font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "#ff4500"},
            "nav-link-selected": {"background-color": "#ff4500","color":"#FFF"},
        }
)

# Display a brief introduction
st.write("Welcome to my portfolio. Here are some of the projects I've worked on:")
st.write("Hello")
