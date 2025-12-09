import streamlit as st
import numpy as np
import pandas as pd
import pickle

# =============================
# Modern Streamlit UI Styling
# =============================
st.set_page_config(page_title="AI Disease Predictor", layout="wide", page_icon="🩺")

st.markdown("""
<style>
.main-title {
    text-align: center;
    font-size: 48px;
    color: #3A6D8C;
    font-weight: 800;
    margin-top: -30px;
}
.subtitle {
    text-align: center;
    font-size: 20px;
    color: #555;
    margin-bottom: 20px;
}
.card {
    padding: 25px;
    border-radius: 15px;
    background-color: #f8f9fa;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.08);
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)

# =============================
# Load Models
# =============================
with open('C:/Users/Selva.M/Downloads/data_science/Project_4/best_liver_model.pkl', 'rb') as f:
    l_model = pickle.load(f)

with open('C:/Users/Selva.M/Downloads/data_science/Project_4/best_kidney_model.pkl', 'rb') as f:
    k_model = pickle.load(f)

with open('C:/Users/Selva.M/Downloads/data_science/Project_4/best_parkinsons_model.pkl', 'rb') as f:
    p_model = pickle.load(f)

# =============================
# Header
# =============================
st.markdown("<h1 class='main-title'>🩺 AI Multiple Disease Prediction</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Predict Liver, Kidney, and Parkinson's Disease using Machine Learning</p>", unsafe_allow_html=True)

# =============================
# Sidebar Menu
# =============================
menu = ["Liver Disease", "Kidney Disease", "Parkinson's Disease"]
choice = st.sidebar.radio("⚙️ Select Disease Type", menu)

# =============================
# Liver Disease UI
# =============================
if choice == "Liver Disease":
    st.markdown("<h2>🫁 Liver Disease Prediction</h2>", unsafe_allow_html=True)

    features = l_model['feature_names']

    with st.container():
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.subheader("Enter Patient Details")

        input_values = []
        col1, col2 = st.columns(2)

        for i, col in enumerate(features):
            with (col1 if i % 2 == 0 else col2):
                if col == "Gender":
                    gender = st.selectbox("Gender", ["Male", "Female"])
                    value = 1 if gender == "Male" else 0
                else:
                    value = st.number_input(col, value=0)
                input_values.append(value)

        st.markdown("</div>", unsafe_allow_html=True)

    if st.button("🔍 Predict Liver Disease", use_container_width=True):
        arr = np.asarray(input_values).reshape(1, -1)
        pred = l_model['model'].predict(arr)[0]

        st.success("🫁 Liver Disease Detected" if pred == 1 else "🫁 No Liver Disease Found")

# =============================
# Kidney Disease UI
# =============================
elif choice == "Kidney Disease":
    st.markdown("<h2>🧪 Kidney Disease Prediction</h2>", unsafe_allow_html=True)

    features = k_model['feature_names']
    encoders = k_model['encoders']
    with st.container():
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.subheader("Enter Patient Details")
        input_values = {}
        col1, col2 = st.columns(2)
        for i, col in enumerate(features):
            if col in encoders:
                with (col1 if i % 2 == 0 else col2):
                    value = st.selectbox(f"{col}", encoders[col].classes_)
                    value = encoders[col].transform([value])[0]
                    input_values[col] = value
            else:
                with (col1 if i % 2 == 0 else col2):
                    value = st.number_input(f"{col}", value=0)
                    input_values[col] = value

        st.markdown("</div>", unsafe_allow_html=True)

    if st.button("🔍 Predict Kidney Disease", use_container_width=True):
        orders = [input_values[col] for col in features]
        arr = np.asarray(orders).reshape(1, -1)
        pred = k_model['model'].predict(arr)[0]

        st.success("🧪 CKD Detected" if pred == 1 else "🧪 No CKD Found")


# =============================
# Parkinson UI
# =============================
else:
    st.markdown("<h2>🧠 Parkinson's Disease Prediction</h2>", unsafe_allow_html=True)

    features = p_model['feature_names']

    with st.container():
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.subheader("Enter Patient Details")

        input_values = []
        col1, col2 = st.columns(2)

        for i, col in enumerate(features):
            with (col1 if i % 2 == 0 else col2):
                value = st.number_input(col, value=0)
                input_values.append(value)

        st.markdown("</div>", unsafe_allow_html=True)

    if st.button("🔍 Predict Parkinson's Disease", use_container_width=True):
        arr = np.asarray(input_values).reshape(1, -1)
        pred = p_model['model'].predict(arr)[0]

        st.success("🧠 Parkinson's Disease Detected" if pred == 1 else "🧠 No Parkinson Symptoms Found")



