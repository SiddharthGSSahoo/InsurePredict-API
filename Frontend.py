import streamlit as st
import requests
import pandas as pd

# Set page configuration
st.set_page_config(page_title="Insurance Claim Predictor", page_icon="🏥")

st.title("🏥 Insurance Claim Prediction")
st.markdown("Enter the details below to predict if an insurance claim will be requested.")

# API URL (Ensure your FastAPI server is running)
API_URL = "http://127.0.0.1:8000/predict"

# Create the form for user input
with st.form("prediction_form"):
    st.subheader("Claim Details")
    
    col1, col2 = st.columns(2)
    
    with col1:
        claim_reason = st.selectbox(
            "Claim Reason",
            options=["Travel", "Medical", "Phone", "Other"],
            help="Select the primary reason for the claim"
        )
        
        claim_amount = st.number_input(
            "Claim Amount",
            min_value=1.0,
            max_value=100000.0,
            value=1200.0,
            step=100.0
        )

    with col2:
        confidentiality = st.selectbox(
            "Data Confidentiality",
            options=["Low", "High", "Medium", "Very low"],
            help="Select the required data confidentiality level"
        )
        
        premium_ratio = st.slider(
            "Premium/Amount Ratio",
            min_value=0.001,
            max_value=0.999,
            value=0.050,
            format="%.3f"
        )

    submit_button = st.form_submit_button("Predict Claim Status")

# Handle form submission
if submit_button:
    # Prepare the payload (matching the InsuranceClaimInput Pydantic model)
    # Note: Using snake_case here as Pydantic handles the alias mapping
    payload = {
        "claim_reason": claim_reason,
        "data_confidentiality": confidentiality,
        "claim_amount": claim_amount,
        "premium_amount_ratio": premium_ratio
    }
    
    try:
        with st.spinner("Analyzing data..."):
            response = requests.post(API_URL, json=payload)
            
        if response.status_code == 201:
            result = response.json()
            prediction = result["Prediction"]
            confidence = result["Confidence"]
            
            # Display results
            st.divider()
            if prediction == "Yes":
                st.error(f"### Prediction: Claim Likely ({prediction})")
            else:
                st.success(f"### Prediction: No Claim Likely ({prediction})")
                
            st.metric("Confidence Score", f"{confidence:.2%}")
            
            with st.expander("View Raw API Response"):
                st.json(result)
        else:
            st.error(f"Error: API returned status code {response.status_code}")
            st.info(response.text)
            
    except requests.exceptions.ConnectionError:
        st.error("Could not connect to the FastAPI server. Please make sure `APIwithModel.py` is running at http://127.0.0.1:8000")
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")

st.sidebar.info("This app uses a Machine Learning model to predict insurance claim requests based on historical data.")
