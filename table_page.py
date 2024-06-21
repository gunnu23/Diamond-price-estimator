import streamlit as st

def table_page():
    # Title of the application
    st.title("Understanding Diamond Table")

    # Introduction
    st.write("""
    The table of a diamond refers to the flat facet on the top of the diamond. Here's an overview of the diamond table and its significance in diamond quality.
    """)

    # Section 1: What is Diamond Table?
    st.header("1. What is Diamond Table?")
    st.write("""
    The table is the large, flat facet on the top of the diamond. It serves as the window through which light enters and exits the diamond, affecting its brilliance and sparkle.
    """)

    # Adding an image for diamond table
    st.image("table.jpg", caption="Diamond Table")

    # Section 2: Importance of Diamond Table
    st.header("2. Importance of Diamond Table")
    st.write("""
    The table percentage influences how light is reflected within the diamond:
    - **Ideal Table:** A well-proportioned table allows light to reflect evenly within the diamond, enhancing its brilliance.
    - **Large Table:** May affect the diamond's brilliance and sparkle as light may not reflect optimally.
    - **Small Table:** May cause light leakage and affect the diamond's overall appearance.
    """)

