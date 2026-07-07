# House Price Prediction using Machine Learning

## Overview

This project predicts house prices using Machine Learning algorithms.

The project includes:

* Data Cleaning
* Exploratory Data Analysis (EDA)
* Correlation Analysis
* Feature Engineering
* Categorical Data Encoding
* Model Training
* Model Evaluation
* Feature Importance Analysis

Three Machine Learning models were implemented and compared:

1. Linear Regression
2. Random Forest Regressor
3. XGBoost Regressor

---

## Project Structure

```text
House Price Prediction/
│
├── data/
│   └── kaggle-housing.csv
│
├── notebooks/
│   └── house_price_prediction.ipynb
│
├── images/
│   ├── correlation_heatmap.png
│   ├── feature_importance.png
│   └── price_distribution.png
│
├── README.md
├── requirements.txt
└── results.md
```

---

## Dataset Features

The dataset contains information about houses such as:

* Area
* Bedrooms
* Bathrooms
* Stories
* Main Road Access
* Guest Room Availability
* Basement Availability
* Hot Water Heating
* Air Conditioning
* Parking Capacity
* Preferred Area
* Furnishing Status

### Target Variable

```text
price
```

---

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-Learn
* XGBoost
* Jupyter Notebook

---

## Machine Learning Workflow

### 1. Data Loading

The dataset is loaded using Pandas.

### 2. Data Exploration

* Dataset inspection
* Missing value checking
* Statistical analysis

### 3. Exploratory Data Analysis

* Price Distribution Visualization
* Correlation Heatmap
* Feature Relationships

### 4. Data Preprocessing

* One-Hot Encoding of categorical features
* Feature preparation for model training

### 5. Model Training

The following models were trained:

#### Linear Regression

A baseline regression model.

#### Random Forest Regressor

An ensemble learning model based on decision trees.

#### XGBoost Regressor

A gradient boosting model known for high predictive performance.

### 6. Model Evaluation

Models were evaluated using:

* MAE (Mean Absolute Error)
* RMSE (Root Mean Squared Error)
* R² Score

---

## Results

Results are automatically generated and stored in:

```text
results.md
```

Example metrics:

| Model             | MAE | RMSE | R² Score |
| ----------------- | --- | ---- | -------- |
| Linear Regression | --  | --   | --       |
| Random Forest     | --  | --   | --       |
| XGBoost           | --  | --   | --       |

---

## Visualizations

### Price Distribution

Shows the distribution of house prices in the dataset.

### Correlation Heatmap

Displays relationships between numerical features.

### Feature Importance

Shows the most influential features affecting house prices.

---

## How to Run

### Clone Repository

```bash
git clone <repository-url>
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Jupyter Notebook

```bash
jupyter notebook
```

Open:

```text
notebooks/house_price_prediction.ipynb
```

and run all cells.

---

## Output Files

The project generates:

```text
images/
├── correlation_heatmap.png
├── feature_importance.png
└── price_distribution.png
```

and

```text
results.md
```

---

## Key Learnings

* Regression Modeling
* Feature Engineering
* Data Visualization
* Model Evaluation
* Ensemble Learning
* XGBoost Implementation
* Real-World ML Workflow

---

## Future Improvements

* Hyperparameter Tuning using GridSearchCV
* Cross Validation
* Streamlit Web Application
* Model Deployment
* Advanced Feature Engineering
* Automated ML Pipeline

---

## Author

Ankit Jainar

Electrical Engineering Undergraduate
Machine Learning & Artificial Intelligence Enthusiast
