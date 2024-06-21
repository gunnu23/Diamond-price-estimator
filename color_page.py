import streamlit as st

def color_page():
    # Title of the application
    st.title("Understanding the Color of a Diamond")

    # Introduction
    st.write("""
    The color of a diamond is one of the key characteristics that determine its quality and value. Unlike other gemstones, the best diamond color is actually no color at all. A chemically pure and structurally perfect diamond has no hue, like a drop of pure water, and consequently, a higher value.
    """)

    # Section 1: Diamond Color Grading Scale
    st.header("1. Diamond Color Grading Scale")
    st.write("""
    The Gemological Institute of America (GIA) grades diamonds on a color scale from D to Z. The D to J range includes diamonds that are colorless to near-colorless:
    - **D:** Absolutely colorless. The highest color grade, which is extremely rare.
    - **E:** Colorless. Only minute traces of color can be detected by an expert gemologist.
    - **F:** Colorless. Slight color detected by an expert gemologist, but still considered colorless.
    - **G:** Near-colorless. Color is noticeable only when compared to diamonds of better grades.
    - **H:** Near-colorless. Color is noticeable only when compared to diamonds of better grades.
    - **I:** Near-colorless. Slightly detectable color that might be visible to the naked eye.
    - **J:** Near-colorless. Slightly detectable color that might be visible to the naked eye.
    """)

    # Adding an image for diamond color grading scale
    st.image("color_grading_scale_image.jpg", caption="Diamond Color Grading Scale")

    # Section 2: Importance of Diamond Color
    st.header("2. Importance of Diamond Color")
    st.write("""
    The color of a diamond affects its appearance and value. Here's how:
    - **Visual Appeal:** Colorless diamonds allow more light to pass through, increasing their brilliance and sparkle.
    - **Value:** The less color a diamond has, the rarer and more valuable it is.
    - **Setting Impact:** The color of a diamond can appear different depending on the type of metal setting used. For instance, yellow gold settings can make lower color grade diamonds appear more colorless.
    """)
    # Adding an image for diamond color grading scale
    st.image("impor.jpg", caption="Importance Color Grading ")
    
    # Section 3: Color Grades in Detail
    st.header("3. Color Grades in Detail")

    st.subheader("3.1 D-F (Colorless)")
    st.write("""
    - **D:** Completely colorless. The rarest and most expensive.
    - **E:** Colorless. Only an expert can detect any color.
    - **F:** Colorless. Slight color, but still considered high quality.
    """)

   

    st.subheader("3.2 G-J (Near-Colorless)")
    st.write("""
    - **G:** Color nearly imperceptible. Offers excellent value.
    - **H:** Color slightly noticeable upon close inspection but still looks colorless when set in jewelry.
    - **I:** Slightly detectable color. Offers good value.
    - **J:** Slightly detectable color. The color might be more noticeable in larger stones.
    """)

 
    # Section 4: How to Choose the Right Diamond Color
    st.header("4. How to Choose the Right Diamond Color")
    st.write("""
    When choosing a diamond, consider the following tips:
    - **Personal Preference:** Decide if you prefer a completely colorless diamond or if a near-colorless diamond meets your needs.
    - **Budget:** Higher color grades (D-F) are more expensive. G-J diamonds can offer a balance between quality and cost.
    - **Setting Metal:** The color of the metal can influence the appearance of the diamond. White metals like platinum or white gold are best for colorless diamonds, while yellow or rose gold can complement diamonds with slight color.
    """)

