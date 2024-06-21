import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor
import altair as alt
import streamlit as st
from cut_page import cut_page
from color_page import color_page
from clarity_page import clarity_page
from table_page import table_page
from depth_page import depth_page
from xyz_page import xyz_page
from carat_page import carat_page

# Set the page configuratio
st.set_page_config(
page_title="Diamond Price Predictor",
page_icon="💎",
layout="wide",  # or "wide"
initial_sidebar_state="expanded"
)


 
def main():
    st.sidebar.title("KNOW YOUR DIAMONDS:")
    page = st.sidebar.selectbox(
        "Choose a page", 
        ["Home", "Cut", "Color", "Clarity", "Table", "Depth", "XYZ", "Carat"]
    )
   

    if page == "Home":
        
        # Load the data
        file_path = r"C:\Users\Gazal\Downloads\Diamonds Prices2022.csv"
        df = pd.read_csv(file_path)
        st.markdown('<style>div.block-container{padding-top:3rem;}</style>', unsafe_allow_html=True)

        col1, col2 = st.columns([0.1,0.9])

        with col2:
            st.markdown("<center><h1 style='font-weight:bold; font-size: 40px; padding: 10px; border-radius: 8px; background-color: #2855B1'>Diamond Price Predictor</h1></center>", unsafe_allow_html=True)
        # Preprocess the data
        le_cut = LabelEncoder()
        le_color = LabelEncoder()
        le_clarity = LabelEncoder()

        df['cut'] = le_cut.fit_transform(df['cut'])
        df['color'] = le_color.fit_transform(df['color'])
        df['clarity'] = le_clarity.fit_transform(df['clarity'])

        X = df[['carat', 'cut', 'color', 'clarity', 'depth', 'table', 'x', 'y', 'z']]
        y = df['price']

        # Split the data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Train the model
        model = RandomForestRegressor(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)

        # Create Streamlit app
        st.write("Welcome to our Diamond Price Predictor! Please input your diamond features below:")

        # Add a home page link
        st.write("Want to learn more about our app? [Click here](#home)")
        st.markdown("""###Our Diamond Price Predictor uses machine learning to estimate the price of a diamond based on its features. Simply input your diamond's features, and we'll do the rest!""")

        # App page
        st.markdown("## LETS PREDICT ")
        st.sidebar.header("Input Diamond Features")

        # Add explanatory text and tooltips for each feature
        st.sidebar.write("### Carat")
        st.sidebar.write("The weight of the diamond, with higher values indicating a larger diamond.")
        carat = st.sidebar.slider("Carat", float(X['carat'].min()), float(X['carat'].max()), float(X['carat'].mean()), help="Select a carat value between 0.2 and 5.01")

        st.sidebar.write("### Cut")
        st.sidebar.write("The cut of a diamond refers to its proportions, symmetry, and polish. A well-cut diamond refracts light better, appearing more brilliant.")
        cut = st.sidebar.selectbox("Cut", le_cut.classes_, help="Select a cut type: Fair, Good, Very Good, Premium, Ideal")

        st.sidebar.write("### Color")
        st.sidebar.write("The color of a diamond, with colorless diamonds being the most rare and valuable.")
        color = st.sidebar.selectbox("Color", le_color.classes_, help="Select a color grade: D (colorless) to Z (light yellow or brown)")

        st.sidebar.write("### Clarity")
        st.sidebar.write("The clarity of a diamond refers to the presence or absence of inclusions and blemishes.")
        clarity = st.sidebar.selectbox("Clarity", le_clarity.classes_, help="Select a clarity grade: FL (flawless) to I3 (included)")

        st.sidebar.write("### Depth")
        st.sidebar.write("The depth of a diamond, with higher values indicating a more shallow diamond.")
        depth = st.sidebar.slider("Depth", float(X['depth'].min()), float(X['depth'].max()), float(X['depth'].mean()), help="Select a depth value between 43 and 79")

        st.sidebar.write("### Table")
        st.sidebar.write("The table of a diamond refers to the flat top surface.")
        table = st.sidebar.slider("Table", float(X['table'].min()), float(X['table'].max()), float(X['table'].mean()), help="Select a table value between 43 and 95")

        st.sidebar.write("### X, Y, Z")
        st.sidebar.write("The dimensions of the diamond in millimeters.")
        x = st.sidebar.slider("X (mm)", float(X['x'].min()), float(X['x'].max()), float(X['x'].mean()), help="Select an X value between 0 and 10")
        y = st.sidebar.slider("Y (mm)", float(X['y'].min()), float(X['y'].max()), float(X['y'].mean()), help="Select a Y value between 0 and 10")
        z = st.sidebar.slider("Z (mm)", float(X['z'].min()), float(X['z'].max()), float(X['z'].mean()), help="Select a Z value between 0 and 10")

        # Convert categorical inputs to numerical values
        cut_encoded = le_cut.transform([cut])[0]
        color_encoded = le_color.transform([color])[0]
        clarity_encoded = le_clarity.transform([clarity])[0]

        # Create input array
        input_data = np.array([[carat, cut_encoded, color_encoded, clarity_encoded, depth, table, x, y, z]])

        # Make prediction
        predicted_price = model.predict(input_data)[0]

        # Display prediction
        st.subheader(f"Predicted Diamond Price: ${predicted_price:,.2f}")

        # Create an Altair graph to visualize the prediction
        data = {'Feature': ['Predicted Price'], 'Value': [predicted_price]}
        df_altair = pd.DataFrame(data)
        chart = alt.Chart(df_altair).mark_bar().encode(
            x='Feature',
            y='Value',
            tooltip=['Feature', 'Value']
        )
        st.altair_chart(chart, theme="streamlit", use_container_width=True)
    elif page == "Cut":
        cut_page()
    elif page == "Color":
        color_page()
    elif page == "Clarity":
        clarity_page()
    elif page == "Table":
        table_page()
    elif page == "Depth":
        depth_page()
    elif page == "XYZ":
        xyz_page()
    elif page == "Carat":
        carat_page()

if __name__ == "__main__":
    main()
