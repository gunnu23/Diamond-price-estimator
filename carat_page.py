import streamlit as st 
# carat_page.py
def carat_page():


    # Title of the application
    st.title("Understanding the Carat of a Diamond")

    # Introduction
    st.write("""
    The carat is a crucial factor in determining the size and value of a diamond. Here's an organized guide to understanding diamond carats.
    """)

    # Section 1: What is Carat?
    st.header("1. What is Carat?")
    st.write("""
    A carat is a unit of weight used to measure diamonds and other gemstones. One carat is equivalent to 200 milligrams (0.2 grams). The term "carat" is derived from the carob seed, which was historically used as a standard for weighing gemstones due to its uniform weight.
    """)

    # Adding an image for carat definition
    st.image("carat.jpg", caption="Carat chart")

    # Section 2: Carat Weight vs. Size
    st.header("2. Carat Weight vs. Size")
    st.write("""
    While carat refers to the weight of the diamond, it does not directly correspond to its size. The size of a diamond is influenced by its cut, shape, and proportions. Two diamonds of the same carat weight can appear different in size depending on their depth and surface area.
    """)

    # Section 3: Impact of Carat on Diamond Value
    st.header("3. Impact of Carat on Diamond Value")
    st.write("""
    Carat weight significantly impacts the value of a diamond. Larger diamonds are rarer and thus more valuable. However, other factors such as cut, color, and clarity also play crucial roles in determining the overall value of a diamond.
    """)