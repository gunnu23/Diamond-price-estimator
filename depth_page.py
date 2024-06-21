import streamlit as st

def depth_page():
   
    # Title of the application
    st.title("Understanding Diamond Depth")

    # Introduction
    st.write("""
    Diamond depth refers to the measurement from the table (top) to the culet (bottom) of a diamond. Here's an overview of diamond depth and its significance.
    """)

    # Section 1: What is Diamond Depth?
    st.header("1. What is Diamond Depth?")
    st.write("""
    Diamond depth is a crucial factor that affects a diamond's brilliance and appearance. It is measured as the vertical distance between the table (top facet) and the culet (bottom point) of the diamond.
    """)

    # Adding an image for diamond depth
    st.image("depth.jpg", caption="Diamond Depth")

    # Section 2: Importance of Diamond Depth
    st.header("2. Importance of Diamond Depth")
    st.write("""
    The depth percentage influences how light interacts with the diamond, affecting its brilliance and sparkle:
    - **Ideal Depth:** A well-proportioned depth ensures that light reflects and refracts effectively within the diamond, enhancing its brilliance.
    - **Shallow Depth:** Light may escape through the bottom of the diamond, reducing its brilliance.
    - **Deep Depth:** Light may escape through the sides of the diamond, also affecting its brilliance.
    """)
