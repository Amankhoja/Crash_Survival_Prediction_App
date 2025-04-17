# import streamlit as st
# import pandas as pd
# import joblib

# # Load model and expected column structure
# model = joblib.load("model.pkl")
# model_columns = joblib.load("model_columns.pkl")

# st.title("Crash Survival Prediction App")
# st.sidebar.header("Input Features")

# # Sidebar user inputs
# age = st.sidebar.slider("Age of Occupant", 0, 100, 30)
# weight = st.sidebar.slider("Weight (kg)", 30, 150, 70)
# veh_usage = st.sidebar.slider("Vehicle Usage Duration", 0, 300, 60)
# sex = st.sidebar.selectbox("Sex", ["Male", "Female"])
# seatbelt = st.sidebar.selectbox("Seatbelt Used", ["Yes", "No"])
# airbag = st.sidebar.selectbox("Airbag Available", ["Yes", "No"])
# frontal_impact = st.sidebar.selectbox("Frontal Impact", ["Yes", "No"])
# speed_range = st.sidebar.selectbox("Speed Range", [
#     "10-24 km/h", "25-39 km/h", "40-54 km/h", "55+ km/h"
# ])
# occ_role = st.sidebar.selectbox("Occupant Role", ["Driver", "Passenger"])
# airbag_deploy = st.sidebar.selectbox("Airbag Deployed", ["Yes", "No"])

# # Create empty input template
# input_data = pd.DataFrame([[0]*len(model_columns)], columns=model_columns)

# # Fill values
# input_data['age_of_occ'] = age
# input_data['weight'] = weight
# input_data['veh_usage_duration'] = veh_usage
# input_data['sex_m'] = 1 if sex == "Male" else 0
# input_data['seatbelt_none'] = 1 if seatbelt == "No" else 0
# input_data['airbag_unavail'] = 1 if airbag == "No" else 0
# input_data['airbag_nodeploy'] = 1 if airbag_deploy == "No" else 0
# input_data['frontal_impact'] = 1 if frontal_impact == "Yes" else 0
# input_data['occ_role_pass'] = 1 if occ_role == "Passenger" else 0
# input_data[f'speed_range_{speed_range}'] = 1

# # Reindex to match model input columns
# input_data = input_data.reindex(columns=model_columns, fill_value=0)

# # Show input data
# st.subheader("Final Input Passed to Model")
# st.write(input_data)

# # Predict
# prob = model.predict_proba(input_data)[0][1]

# # Debug output (shows raw probability)
# st.subheader("Prediction Probability")
# st.write(f"Predicted probability of death: {prob:.6f}")  # full precision
# st.write("DEBUG RAW PROB:", prob)

# # Final decision logic
# if prob > 0.4:
#     st.error("Predicted: Deceased")
# else:
#     st.success("Predicted: Not Deceased")


import streamlit as st
import pandas as pd
import joblib

# Load model and expected columns
model = joblib.load("model.pkl")
model_columns = joblib.load("model_columns.pkl")

st.title("🚗 Crash Survival Prediction App")
st.sidebar.header("🧾 Input Features")

# Sidebar inputs
age = st.sidebar.slider("Age of Occupant", 0, 100, 30)
weight = st.sidebar.slider("Weight (kg)", 30, 150, 70)
veh_usage = st.sidebar.slider("Vehicle Usage Duration", 0, 300, 60)
sex = st.sidebar.selectbox("Sex", ["Male", "Female"])
seatbelt = st.sidebar.selectbox("Seatbelt Used", ["Yes", "No"])
airbag = st.sidebar.selectbox("Airbag Available", ["Yes", "No"])
frontal_impact = st.sidebar.selectbox("Frontal Impact", ["Yes", "No"])
speed_range = st.sidebar.selectbox("Speed Range", [
    "10-24 km/h", "25-39 km/h", "40-54 km/h", "55+ km/h"
])
occ_role = st.sidebar.selectbox("Occupant Role", ["Driver", "Passenger"])
airbag_deploy = st.sidebar.selectbox("Airbag Deployed", ["Yes", "No"])

# Create empty input template
input_data = pd.DataFrame([[0]*len(model_columns)], columns=model_columns)

# Fill in selected values
input_data['age_of_occ'] = age
input_data['weight'] = weight
input_data['veh_usage_duration'] = veh_usage
input_data['sex_m'] = 1 if sex == "Male" else 0
input_data['seatbelt_none'] = 1 if seatbelt == "No" else 0
input_data['airbag_unavail'] = 1 if airbag == "No" else 0
input_data['airbag_nodeploy'] = 1 if airbag_deploy == "No" else 0
input_data['frontal_impact'] = 1 if frontal_impact == "Yes" else 0
input_data['occ_role_pass'] = 1 if occ_role == "Passenger" else 0
input_data[f'speed_range_{speed_range}'] = 1

# Reindex to model's training columns
input_data = input_data.reindex(columns=model_columns, fill_value=0)

# Display current input to model
st.subheader("📦 Final Input Passed to Model")
st.write(input_data)

# Button to trigger prediction
if st.button("🔍 Predict Now"):
    prob = model.predict_proba(input_data)[0][1]

    st.subheader("📈 Prediction Probability")
    st.write(f"Predicted probability of death: **{prob:.6f}**")

    # Three-level logic
    if prob > 0.4:
        st.error("🔴 Predicted: Deceased")
    elif prob > 0.08:
        st.warning("🟠 Predicted: At Risk")
    else:
        st.success("🟢 Predicted: Not Deceased")


