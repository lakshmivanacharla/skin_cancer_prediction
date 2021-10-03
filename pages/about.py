"""This is about page"""

# import necessary modules
import streamlit as st


def app():
    """This function runs the about page"""
    # Add balloons animation when page opens
    st.balloons()

    # Add title
    st.title("Welcome to the about me page")

    # Add an image
    st.image("./irris_classification.png")
    
    # Add Contact Details
    st.header('Contact Us')

    # Add email
    st.markdown('''### Name:
    Lakshmi Prasanna Vanacharla''')

    # Add name
    st.markdown('''### Email:
    lakshmivanacharla@gmail.com''')

    # Add github
    st.markdown('''### GitHub: ''')

    # Add linkedin
    st.markdown('''### Linkedin: ''')