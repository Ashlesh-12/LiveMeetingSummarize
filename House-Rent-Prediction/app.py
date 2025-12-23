import streamlit as st 
import pandas as pd 
import numpy as np
import joblib 
# ----------------------------------
# Page Config
# ----------------------------------
st.set_page_config(
    page_title="House Rent Prediction",
    page_icon="🏠",
    layout="centered"
)

st.title("🏠 House Rent Prediction App")
st.write(
    "Predict monthly house rent using a machine learning model trained on real housing data."
)

# ----------------------------------
# Load Artifacts
# ----------------------------------
@st.cache_resource
def load_artifacts():
    model = joblib.load("./models/model/rfr.pkl")
    te = joblib.load("./models/encoder/high_card_encoder.pkl")
    ohe = joblib.load("./models/encoder/low_card_encoder.pkl")
    scaler = joblib.load("./models/encoder/num_encoder.pkl")
    return model, te, ohe, scaler

model, te, ohe, scaler = load_artifacts()

# ----------------------------------
# Feature Lists (MUST match training)
# ----------------------------------
num_cols = ["BHK", "Size", "Floor", "Bathroom"]

low_card_cols = [
    "Area Type",
    "City",
    "Furnishing Status",
    "Tenant Preferred",
    "Point of Contact"
]

# ----------------------------------
# Sidebar Inputs
# ----------------------------------
st.sidebar.header("Enter Property Details")

bhk = st.sidebar.selectbox("BHK", [1, 2, 3, 4, 5, 6])
bathroom = st.sidebar.selectbox("Bathrooms", [1, 2, 3, 4, 5])
size = st.sidebar.number_input("Area Size (sq.ft)", min_value=200, max_value=10000, step=50)
floor = st.sidebar.number_input("Floor Number", min_value=0, max_value=50)

area_type = st.sidebar.selectbox(
    "Area Type",
    ["Super Area", "Carpet Area"]
)

city = st.sidebar.selectbox(
    "City",
    ["Mumbai", "Delhi", "Bangalore", "Chennai", "Hyderabad", "Kolkata"]
)

furnishing = st.sidebar.selectbox(
    "Furnishing Status",
    ["Unfurnished", "Semi-Furnished", "Furnished"]
)

tenant = st.sidebar.selectbox(
    "Tenant Preferred",
    ["Bachelors", "Family", "Bachelors/Family"]
)

poc = st.sidebar.selectbox(
    "Point of Contact",
    ["Contact Owner", "Contact Agent"]
)

locality = st.sidebar.text_input(
    "Area Locality",
    placeholder="e.g., Salt Lake Sector 2"
)

# ----------------------------------
# Prediction Logic
# ----------------------------------
if st.button("Predict Rent"):
    if locality.strip() == "":
        st.error("Please enter Area Locality")
    else:
        # Build raw input dataframe
        user_df = pd.DataFrame([{
            "BHK": bhk,
            "Size": size,
            "Floor": floor,
            "Bathroom": bathroom,
            "Area Type": area_type,
            "City": city,
            "Furnishing Status": furnishing,
            "Tenant Preferred": tenant,
            "Point of Contact": poc,
            "Area Locality": locality
        }])

        # ---- Target Encoding (Area Locality)
        user_df[["Area Locality"]] = te.transform(
            user_df[["Area Locality"]]
        )

        # ---- OneHot Encoding (Low-card cols)
        ohe_array = ohe.transform(user_df[low_card_cols])
        ohe_df = pd.DataFrame(
            ohe_array,
            columns=ohe.get_feature_names_out(low_card_cols)
        )

        # ---- Scale Numerical Features
        user_df[num_cols] = scaler.transform(user_df[num_cols])

        # ---- Final Feature Vector
        X_user_final = pd.concat(
            [
                user_df[num_cols + ["Area Locality"]],
                ohe_df
            ],
            axis=1
        )

        # ---- Prediction (log scale → original)
        pred_log = model.predict(X_user_final)
        pred_rent = np.expm1(pred_log)[0]

        # ---- Display Result
        st.success(f"💰 Estimated Monthly Rent: ₹{pred_rent:,.0f}")
        st.balloons()




