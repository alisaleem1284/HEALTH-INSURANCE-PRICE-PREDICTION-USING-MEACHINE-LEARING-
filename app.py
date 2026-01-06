# import streamlit as st
# import pandas as pd 
# import numpy as np 
# import joblib 

# # Load scaler and encoders
# scaler  = joblib.load("scaler.pkl")
# le_gender = joblib.load("Label_encoder_gender.pkl")
# le_diabetic = joblib.load("Label_encoder_diabetic.pkl")
# le_smoker = joblib.load("Label_encoder_smoker.pkl")

# # Load trained model
# model = joblib.load("best_model.pkl")

# # Streamlit app config
# st.set_page_config(page_title="Insurance Claim Predictor", layout="centered")
# st.title("HEALTH INSURANCE PAYMENT PREDICTOR APP")
# st.write("ENTER THE DETAILS BELOW TO ESTIMATE YOUR INSURANCE COST")

# # Input form
# with st.form("input_inform"):
#     col1, col2 = st.columns(2)

#     with col1:
#         age = st.number_input("Age", min_value=0, max_value=100, value=30)
#         bmi = st.number_input("BMI", min_value=10.0, max_value=60.0, value=25.0)
#         children = st.number_input("NUMBER OF CHILDREN", min_value=0, max_value=10, value=0)

#     with col2:
#         bloodpressure = st.number_input("BLOOD PRESSURE", min_value=60, max_value=200, value=120)
#         gender = st.selectbox("GENDER", options=le_gender.classes_)
#         diabetic = st.selectbox("DIABETIC", options=le_diabetic.classes_)
#         smoker = st.selectbox("SMOKER", options=le_smoker.classes_)

#     submitted = st.form_submit_button("PREDICT PAYMENT")

# # Prediction logic
# if submitted:
#     input_data = pd.DataFrame({
#         "age": [age],
#         "gender": [gender],
#         "bmi": [bmi],
#         "bloodpressure": [bloodpressure],
#         "diabetic": [diabetic],
#         "children": [children],
#         "smoker": [smoker]
#     })

#     # Encode categorical features
#     input_data["gender"] = le_gender.transform(input_data["gender"])
#     input_data["diabetic"] = le_diabetic.transform(input_data["diabetic"])
#     input_data["smoker"] = le_smoker.transform(input_data["smoker"])

#     # Scale numeric features
#     num_cols = ["age", "bmi", "bloodpressure", "children"]
#     input_data[num_cols] = scaler.transform(input_data[num_cols])

#     # Predict
#     prediction = model.predict(input_data)[0]

#     st.success(f"**Estimated Insurance Payment Amount:** ${prediction:,.2f}")


# usd to aed wala ha code is k down per

import streamlit as st
import pandas as pd 
import numpy as np 
import joblib 


scaler  = joblib.load("scaler.pkl")
le_gender = joblib.load("Label_encoder_gender.pkl")
le_diabetic = joblib.load("Label_encoder_diabetic.pkl")
le_smoker = joblib.load("Label_encoder_smoker.pkl")


model = joblib.load("best_model.pkl")


st.set_page_config(page_title="Insurance Claim Predictor", layout="centered")
st.title("HEALTH INSURANCE PAYMENT PREDICTOR APP")
st.write("ENTER THE DETAILS BELOW TO ESTIMATE YOUR INSURANCE COST")

# Input form
with st.form("input_inform"):
    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input("Age", min_value=0, max_value=100, value=30)
        bmi = st.number_input("BMI", min_value=10.0, max_value=60.0, value=25.0)
        children = st.number_input("NUMBER OF CHILDREN", min_value=0, max_value=10, value=0)

    with col2:
        bloodpressure = st.number_input("BLOOD PRESSURE", min_value=60, max_value=200, value=120)
        gender = st.selectbox("GENDER", options=le_gender.classes_)
        diabetic = st.selectbox("DIABETIC", options=le_diabetic.classes_)
        smoker = st.selectbox("SMOKER", options=le_smoker.classes_)

    submitted = st.form_submit_button("PREDICT PAYMENT")


if submitted:
    input_data = pd.DataFrame({
        "age": [age],
        "gender": [gender],
        "bmi": [bmi],
        "bloodpressure": [bloodpressure],
        "diabetic": [diabetic],
        "children": [children],
        "smoker": [smoker]
    })

    
    input_data["gender"] = le_gender.transform(input_data["gender"])
    input_data["diabetic"] = le_diabetic.transform(input_data["diabetic"])
    input_data["smoker"] = le_smoker.transform(input_data["smoker"])

    
    num_cols = ["age", "bmi", "bloodpressure", "children"]
    input_data[num_cols] = scaler.transform(input_data[num_cols])

    # Predict in USD
    prediction_usd = model.predict(input_data)[0]

    # Convert USD → AED
    usd_to_aed = 3.67
    prediction_aed = prediction_usd * usd_to_aed

    st.success(f"**Estimated Insurance Payment:** ${prediction_usd:,.2f} USD")
    st.success(f"**Estimated Insurance Payment:** {prediction_aed:,.2f} AED")


