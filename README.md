# 🩺 AI Multiple Disease Prediction System

An intelligent **Machine Learning based web application** built using **Streamlit** to predict the risk of:

- 🫁 **Liver Disease**
- 🧪 **Kidney Disease (CKD)**
- 🧠 **Parkinson’s Disease**

This system helps in **early-stage disease detection** by analyzing user-entered medical parameters using trained ML models.

---

## 🚀 Features

✅ Predicts **three major diseases** from a single web app  
✅ Clean and **modern UI design**  
✅ **Real-time predictions**  
✅ Supports **categorical & numerical inputs**  
✅ Uses **pre-trained optimized ML models**  
✅ Fully interactive **Streamlit dashboard**  

---

## 🛠️ Tech Stack

- **Programming Language:** Python  
- **Frontend:** Streamlit  
- **Backend / ML:** Scikit-learn  
- **Data Handling:** NumPy, Pandas  
- **Model Storage:** Pickle  

---
📊 Model Details
Disease	Algorithm Used	Accuracy (Approx)
Liver	Random Forest / XGBoost	High
Kidney	Logistic / Random Forest	High
Parkinson	SVM / Random Forest	High

✅ Models are optimized and saved using pickle.
---

## ⚙️ How the System Works

1. User selects a disease from the sidebar.
2. Enters the required medical parameters.
3. The system:
   - Preprocesses the input
   - Applies encoding if required
   - Feeds data into the trained ML model
4. The model returns a prediction:
   - ✅ Disease Detected
   - ❌ No Disease Found
     
---
🧪 Disease Prediction Modules
🫁 Liver Disease
1) Uses medical features like bilirubin, enzymes, protein, etc.
2) Gender is automatically encoded.

🧪 Kidney Disease (CKD)
1) Uses categorical + numerical features.
2) Encoders handle label transformation.

🧠 Parkinson’s Disease
1) Uses voice-related biomedical attributes.
2) Fully numerical input system.

---
🛡️ Disclaimer

This application is for educational and research purposes only.
It does not replace professional medical diagnosis. Always consult certified healthcare professionals.
---
📌 Future Enhancements

✅ Add Diabetes & Heart Disease Prediction
✅ Deploy on Streamlit Cloud / AWS
✅ Patient History Tracking
✅ Mobile Responsive UI
---
👨‍💻 Developed By

Selvakumaran M

Data Science & Machine Learning Developer
