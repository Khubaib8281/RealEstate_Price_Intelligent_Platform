# 🏡 Real Estate Price Intelligent Platform

An intelligent web application for **predicting real estate prices** using machine learning. This platform offers fast, accurate predictions based on property features via a user-friendly Streamlit interface.

---

## 🚀 Features

- 🧠 Trained ML models: Gradient Boosting, Random Forest, XGBoost
- 🔍 GridSearchCV for hyperparameter optimization
- 📊 Data preprocessing: log transform, scaling, encoding
- 🌐 Deployed as a web app using Streamlit
- ⚡ Model loaded from `.pkl` file using Joblib

---

## 🧰 Tech Stack

| Tool/Library | Description |
|--------------|-------------|
| Python | Core language |
| Scikit-learn | Pipelines, preprocessing, ML models |
| XGBoost | Boosted tree regression |
| Pandas & NumPy | Data manipulation |
| Streamlit | Web app interface |
| Joblib | Model serialization |

---

## 📂 Project Structure

```
realestate_price_intelligent_platform/
│
├── app.py                    # Streamlit application
├── Best_model_gb.pkl         # Trained Gradient Boosting model
├── requirements.txt          # All dependencies
├── README.md                 # Project documentation
└── data/
    └── dataset.csv           # Input dataset (if available)
```

---

## ⚙️ Installation & Run

```bash
# Clone the repository
git clone https://github.com/Khubaib8281/RealEstate_Price_Intelligent_Platform
cd RealEstate_Price_Intelligent_Platform

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run app.py
```

---

## 🏗️ ML Pipeline Overview

```python
# Numeric data pipeline
numeric_pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy='median')),
    ('log', FunctionTransformer(np.log1p, validate=False)),
    ('scaler', StandardScaler())
])

# Categorical data pipeline
categorical_pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('encoder', OneHotEncoder(handle_unknown='ignore', sparse_output=False))
])

# Full preprocessor
preprocessor = ColumnTransformer([
    ('num', numeric_pipeline, num_cols),
    ('cat', categorical_pipeline, cat_cols)
])

# Final model pipeline
pipeline_gb = Pipeline([
    ('preprocessor', preprocessor),
    ('model', GradientBoostingRegressor(...))
])
```

---

## 🎯 Objective

Predict property prices using historical data by:
- Cleaning & transforming input features
- Training multiple ML regressors
- Choosing the best model using cross-validation
- Saving and reusing the model in a deployed app

---

## 📊 Models Used

✅ GradientBoostingRegressor  
✅ RandomForestRegressor  
✅ XGBRegressor  

All were optimized using `GridSearchCV`.

---

## 📈 Example Use Case

User enters:
- 📍 Location: Islamabad
- 📐 Area: 10 Marla
- 🛏️ Bedrooms: 4  
The app predicts the expected property price using the trained model.

---

## ✅ Requirements

- Python 3.10+
- streamlit
- scikit-learn
- xgboost
- pandas
- numpy
- joblib

---

## 🧠 Author

Made with ❤️ by [Muhammad Khubaib Ahmad]  
📧 muhammadkhubaibahmad854@gmail.com
🔗 [LinkedIn](https://www.linkedin.com/in/muhammad-khubaib-ahmad-) | [GitHub](https://github.com/Khubaib8281)

---

## 📌 Note

Ensure `Best_model_gb.pkl` is present in the same directory as `app.py` to avoid loading errors.

---

## 🌟 Support

If you like this project, leave a ⭐ on [GitHub](https://github.com/Khubaib8281/RealEstate_Price_Intelligent_Platform)!  
Pull requests, suggestions, and improvements are welcome.