# Import all the necessary libraries
import pandas as pd
import joblib
import streamlit as st

# Set page config
st.set_page_config(page_title="Water Quality Predictor", layout="centered")

# Load the model and model columns
try:
    model = joblib.load("pollution_model.pkl")
    model_cols = joblib.load("model_columns.pkl")
except FileNotFoundError:
    st.error("🔴 Model files not found. Please ensure both .pkl files are in the same directory.")
    st.stop()

# App Title and Info
st.title("💧 Water Pollutants Predictor")
st.markdown("This app predicts major water pollutant levels based on **Station ID** and **Year** using a machine learning model trained during the AICTE Virtual Internship.")

# --- Input Section ---
with st.form("prediction_form"):
    col1, col2 = st.columns(2)
    with col1:
        year_input = st.number_input("📅 Enter Year", min_value=2000, max_value=2100, value=2024, step=1)
    with col2:
        station_id = st.text_input("🏭 Enter Station ID", value='1')

    submitted = st.form_submit_button("🔍 Predict")

# --- Prediction Logic ---
if submitted:
    if not station_id.strip():
        st.warning("⚠️ Please enter a valid Station ID.")
    else:
        try:
            # Prepare input data
            input_df = pd.DataFrame({'year': [year_input], 'id': [station_id.strip()]})
            input_encoded = pd.get_dummies(input_df, columns=['id'])

            # Align with model columns
            for col in model_cols:
                if col not in input_encoded.columns:
                    input_encoded[col] = 0
            input_encoded = input_encoded[model_cols]

            # Prediction
            predicted_pollutants = model.predict(input_encoded)[0]
            pollutants = ['O2', 'NO3', 'NO2', 'SO4', 'PO4', 'CL']

            # Display results
            st.success(f"✅ Predicted pollutant levels for Station **{station_id.strip()}** in **{year_input}**")

            # Layout in columns
            result_cols = st.columns(3)
            for i, (p, val) in enumerate(zip(pollutants, predicted_pollutants)):
                result_cols[i % 3].metric(label=f"{p}", value=f"{val:.2f} mg/L")

        except Exception as e:
            st.error(f"An error occurred during prediction: {e}")
