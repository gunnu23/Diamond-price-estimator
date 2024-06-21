import streamlit as st
import time

# Load the GIF
loading_gif = "loading.json"

# Function to simulate a process
def simulate_long_process():
    for i in range(100):
        time.sleep(0.1)
        st.progress(i + 1)

def cut_page():
    # Title of the application
    st.title("Understanding the Cut of a Diamond")

    # Introduction
    st.write("""
    The cut of a diamond is one of the most critical aspects influencing its beauty and value. The cut refers to how well the diamond has been shaped and faceted from its raw form. Unlike color and clarity, which are influenced by natural factors, the cut quality is determined by the skill and precision of the diamond cutter.
    """)

    # Section 1: Basic Components of Diamond Cut
    st.header("1. Basic Components of Diamond Cut")

    st.subheader("1.1 Proportions")
    st.write("""
    - **Table Size:** The flat top surface of the diamond.
    - **Crown Angle:** The angle between the girdle (the widest part of the diamond) and the topmost surface (table).
    - **Pavilion Depth:** The distance from the girdle to the bottom tip (culet).
    - **Girdle Thickness:** The edge or the perimeter of the diamond.
    """)

    # Adding an image for proportions
    st.image("diamond_cuts.jpg", caption="Diamond Proportions")

    st.subheader("1.2 Symmetry")
    st.write("""
    - **Facet Alignment:** The uniformity of facet shapes and alignment.
    - **Proportional Balance:** Symmetry in proportions such as crown height and pavilion depth.
    - **Girdle Roundness:** Consistency in girdle thickness around the diamond.
    """)

    # Adding an image for symmetry
    st.image("symmetry_cut.gif", caption="Diamond Symmetry")

    st.subheader("1.3 Polish")
    st.write("""
    - **Surface Smoothness:** The quality of the diamond’s surface finish.
    """)


    # Section 2: Cut Grades
    st.header("2. Cut Grades")
    st.write("""
    Diamond cuts are graded by laboratories such as the Gemological Institute of America (GIA). The grades range from Excellent to Poor:

    - **Excellent:** Reflects almost all light that enters the diamond, offering maximum brilliance and fire.
    - **Very Good:** Reflects most of the light, providing a high level of brilliance and fire.
    - **Good:** Reflects a considerable amount of light, but not as much as higher grades.
    - **Fair:** Reflects some light, but significant brilliance is lost.
    - **Poor:** Reflects very little light, resulting in a dull appearance.
    """)

    # Adding an image for cut grades
    st.image("cut_grade.jpg", caption="Diamond Cut Grades")

    # Section 3: Types of Diamond Cuts
    st.header("3. Types of Diamond Cuts")

    st.subheader("3.1 Brilliant Cut")
    st.write("""
    - **Round Brilliant:** The most popular and widely used cut, known for its superior light performance.
    - **Princess:** Square or rectangular shape, with pointed corners and brilliant faceting.
    - **Cushion:** Square or rectangular with rounded corners and larger facets to increase brilliance.
    """)

    st.subheader("3.2 Step Cut")
    st.write("""
    - **Emerald:** Rectangular with long, narrow facets arranged in parallel lines, known for its elegant and sophisticated appearance.
    - **Asscher:** Similar to the emerald cut but square-shaped with a higher crown and larger step facets.
    """)

    st.subheader("3.3 Mixed Cut")
    st.write("""
    - **Radiant:** Combines the brilliance of the round cut with the elegant shape of the emerald cut.
    - **Oval:** An elongated version of the round brilliant cut, offering similar brilliance with a unique shape.
    """)


    st.subheader("3.4 Other Fancy Cuts")
    st.write("""
    - **Marquise:** Football-shaped with pointed ends, maximizing carat weight.
    - **Heart:** Heart-shaped, symbolizing love and romance.
    - **Pear:** Teardrop-shaped, combining the best of the marquise and oval cuts.
    """)

    # Adding an image for other fancy cuts
    st.image("diamond_cut.jpg", caption="Diamond cut Types")
