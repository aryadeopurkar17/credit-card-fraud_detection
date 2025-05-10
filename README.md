# 💳 Credit Card Fraud Detection using Machine Learning

A supervised machine learning project that identifies potentially fraudulent credit card transactions. The model is trained on imbalanced datasets and optimized for high precision and recall to minimize financial risk.

## 🧠 Objective

To accurately classify fraudulent vs. legitimate transactions using a machine learning model trained on real-world anonymized transaction data.

## 📈 Features

- Exploratory Data Analysis (EDA)
- Handling class imbalance with undersampling/SMOTE
- Model training with algorithms like Logistic Regression, Random Forest, and XGBoost
- Evaluation using Confusion Matrix, Precision, Recall, F1 Score
- ROC Curve & AUC analysis
- Feature importance visualization

## ⚙️ Technologies Used

- Python
- Pandas, NumPy
- scikit-learn
- Matplotlib, Seaborn

## 📊 Dataset

- **Source**: [Kaggle - Credit Card Fraud Detection](https://www.kaggle.com/mlg-ulb/creditcardfraud)
- The dataset contains 284,807 transactions, of which 492 are frauds (heavily imbalanced).

## 🛠️ How to Run

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/credit-card-fraud-detection.git
   cd credit-card-fraud-detection
   
2.**Create and activate virtual environment**

bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

3.**Install dependencies**
bash
pip install -r requirements.txt

📁 Project Structure
bash
Copy code
credit-card-fraud-detection/
├── data/                      # Dataset files (add .gitignore if needed)
├── notebooks/                 # Jupyter Notebooks for EDA and modeling
├── models/                    # Saved trained models
├── utils/                     # Helper scripts
├── requirements.txt
├── README.md
└── fraud_detection.ipynb      # Main notebook

📊 Model Evaluation Metrics
Precision

Recall

F1 Score

ROC-AUC Score

Confusion Matrix

🔍 Key Insights
Imbalanced datasets require careful resampling and metric selection.

Precision-Recall is more informative than Accuracy in fraud detection.

Ensemble models like Random Forest and XGBoost showed better performance.
