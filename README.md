# 💧 Water Quality Prediction App

This project uses **Machine Learning** to predict the concentration of multiple water pollutants based on historical water quality data. Developed during the **AICTE Virtual Internship 2025** with the **Edunet Foundation**, sponsored by **Shell**.

---

## 📌 Project Objective

To build a predictive model that estimates water pollution levels for different stations and years, assisting in early detection of contamination and water management.

---

## 🔍 Features Predicted

The app predicts concentrations of the following pollutants:

- O₂ (Dissolved Oxygen)
- NO₃ (Nitrate)
- NO₂ (Nitrite)
- SO₄ (Sulfate)
- PO₄ (Phosphate)
- CL (Chloride)

---

## 🛠️ Tools & Technologies

| Tool         | Purpose                    |
|--------------|----------------------------|
| Python 3.12   | Programming Language        |
| Streamlit     | Web App UI Framework        |
| Scikit-learn  | Model Training              |
| Pandas, NumPy | Data Handling               |
| Joblib        | Model Saving & Loading      |
| VS Code       | Development Environment     |

---

## 🧠 ML Model Used

- **RandomForestRegressor** wrapped in **MultiOutputRegressor**
- Trained on cleaned historical data
- Inputs: `year`, `station_id` (one-hot encoded)
- Outputs: 6 pollutant levels

---

## 🚀 How to Run Locally

1. Clone this repository:

   ```bash
   git clone https://github.com/Hishamudin/water-quality-predictor.git
   cd water-quality-predictor
