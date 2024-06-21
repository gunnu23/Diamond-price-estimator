import streamlit as st

def clarity_page():
    
    # Title of the application
    st.title("Understanding the Clarity of a Diamond")

    # Introduction
    st.write("""
    The clarity of a diamond refers to the presence of internal and external flaws, known as inclusions and blemishes. Here's an organized guide to understanding diamond clarity grades.
    """)

    # Section 1: Diamond Clarity Grading Scale
    st.header("1. Diamond Clarity Grading Scale")
    st.write("""
    The Gemological Institute of America (GIA) grades diamond clarity on a scale from Flawless (FL) to Included (I3). Here are the clarity grades:
    - **FL (Flawless):** No internal or external flaws visible under 10x magnification.
    - **IF (Internally Flawless):** No internal flaws visible under 10x magnification; minor surface blemishes may be present.
    - **VVS1/VVS2 (Very, Very Slightly Included):** Inclusions are difficult to detect even under 10x magnification.
    - **VS1/VS2 (Very Slightly Included):** Minor inclusions that are visible under 10x magnification but not to the naked eye.
    - **SI1/SI2 (Slightly Included):** Inclusions that are noticeable under 10x magnification and may be visible to the naked eye.
    - **I1/I2/I3 (Included):** Inclusions that are obvious under 10x magnification and affect transparency and brilliance.
    """)

    # Adding an image for diamond clarity grading scale
    st.image("clarity.jpg", caption="Diamond Clarity Grading Scale")
