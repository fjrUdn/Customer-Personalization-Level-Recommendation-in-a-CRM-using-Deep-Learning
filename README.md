# Customer Personalization Level Recommendation in a CRM using Deep Learning

This project develops a recommendation system for customer personalization using **LSTM and GRU** models. The system analyzes customer interactions and predicts their engagement level, helping businesses improve their CRM strategies.

## 📌 Project Overview
- **Goal:** Classify customer engagement levels based on historical interaction data.
- **Models Used:** LSTM, GRU.
- **Technologies:** Python, TensorFlow/Keras, Flask, Pandas, NumPy.
- **Deployment:** Flask API integrated into a CRM system.

## 📂 Project Structure
```
📁 customer_personalization_crm  
 ├── 📂 notebooks                  # Jupyter Notebooks for data analysis & model training  
 │   ├── 01_data_analysis.ipynb    # Exploratory Data Analysis (EDA)  
 │   ├── 02_model_training.ipynb   # Training LSTM & GRU models  
 │   ├── 03_model_evaluation.ipynb # Evaluating model performance  
 │   ├── 04_flask_integration.ipynb # Preparing model for API deployment  
 │  
 ├── 📂 api                        # Flask API for model deployment  
 │   ├── 📂 enums                  # Defines enumeration types for classification  
 │   ├── 📂 config                 # Configuration files for API settings  
 │   ├── 📂 handler                # Request and response handlers  
 │   ├── 📂 helpers                # Utility functions for API operations  
 │   ├── 📂 models                 # models  
 │   ├── app.py                    # Main Flask application    
 │   ├── requirements.txt           # Dependencies for API  
 │  
 ├── 📂 data                        # Sample dataset  
 │   ├── customer_data.csv          # Processed customer interaction data  
 │  
 ├── README.md                      # Project documentation  
```

## 📊 Model Performance
| Model | Accuracy | Precision | Recall |
|--------|----------|-----------|--------|
| LSTM  | 85.2%   | 83.5%     | 81.7%  |
| GRU   | 86.5%   | 84.9%     | 82.1%  |

## 🚀 Deployment
- The trained model is deployed using **Flask**.
- API endpoints can be integrated into the CRM for real-time predictions.

## 📌 Contributors  
- **Fajar Kamaludin Akhmad** ([@fjrUdn](https://github.com/fjrUdn)))  
