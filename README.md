# 🏥 Insurance Claim Prediction System

This project is a complete end-to-end Machine Learning application that predicts whether an insurance claim will be requested based on specific policy and claim details. It features a robust **FastAPI backend** for model serving and a user-friendly **Streamlit frontend**.

## 🚀 Features
- **Machine Learning Pipeline:** Trained using XGBoost with optimized preprocessing (StandardScaler & OneHotEncoder).
- **Data Validation:** Powered by Pydantic for strict input validation.
- **RESTful API:** FastAPI-based backend with automated documentation (Swagger UI).
- **Interactive UI:** Streamlit-based web interface for easy predictions.

## 🛠️ Project Structure
```text
Model with APIs/
├── APIwithModel.py          # FastAPI Backend
├── frontend.py              # Streamlit Web App
├── ModelClasses.py          # Pydantic Data Models & Validation
├── ModelBuilding.ipynb      # ML Research & Training Notebook
├── final_insurance_model.pkl # Trained Model Artifact
└── InsurenceData.csv        # Dataset
```

## ⚙️ Installation & Setup

1. **Clone the Repository:**
   ```bash
   git clone <your-repo-url>
   cd "Model with APIs"
   ```

2. **Install Dependencies:**
   ```bash
   pip install fastapi uvicorn streamlit pandas joblib xgboost scikit-learn requests
   ```

## 🏃 How to Run

### 1. Start the Backend API
```bash
python APIwithModel.py
```
*The API will be available at `http://127.0.0.1:8000`. You can view the interactive docs at `/docs`.*

### 2. Start the Frontend App
Open a **new terminal** and run:
```bash
streamlit run frontend.py
```
*The web interface will open automatically in your browser.*

## 🧪 Model Inputs
The system expects the following data points:
- **Claim Reason:** Travel, Medical, Phone, or Other.
- **Data Confidentiality:** Low, Medium, High, or Very low.
- **Claim Amount:** The total value of the claim.
- **Premium/Amount Ratio:** Ratio of policy premium to the claim amount.

---
*Developed as part of the FastAPI Learning Journey.*
- **Dataset Link:** `https://www.kaggle.com/datasets/usmanfarid/customer-churn-dataset-for-life-insurance-industry`
