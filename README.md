# Medical Cost Prediction

This project predicts medical insurance charges using a Linear Regression model.

## 📌 Overview
- Dataset: Insurance dataset
- Goal: Predict medical costs based on user attributes
- Model: Linear Regression

## ⚙️ Tech Stack
- Python
- Pandas
- Scikit-learn

## 🚀 How to Run

1. Clone the repository:
git clone https://github.com/HarshMohite7/medical-cost-prediction.git

2. Navigate to the project folder:
cd medical-cost-prediction

3. Install dependencies:
pip install -r requirements.txt

4. Run the training script:
python src/train.py

## 📊 Result
- R² Score: ~0.78

## 📁 Project Structure
medical-cost-prediction/
│
├── data/
│   └── insurance.csv
├── notebooks/
│   └── analysis.ipynb
├── src/
│   └── train.py
├── requirements.txt
└── README.md

## 🔮 Future Improvements
- Add model saving (model.pkl)
- Build prediction script
- Deploy as API (FastAPI)
