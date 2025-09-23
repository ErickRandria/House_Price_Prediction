# California Housing Price Prediction

A machine learning project that predicts housing prices in California using the famous California housing dataset. This project implements various regression algorithms to predict median house values based on features like location, housing median age, population, and median income.

## 📋 Table of Contents

- [Overview](#-overview)
- [Dataset](#-dataset)
- [Features](#-features)
- [Installation](#-installation)
- [Usage](#-usage)
- [Technologies Used](#️-technologies-used)
- [Results](#-results)
- [Contributing](#-contributing)
- [Contact](#-contact)

## 🎯 Overview

This project aims to predict California housing prices using machine learning techniques. The model analyzes various factors that influence housing prices and provides accurate predictions for median house values in different California districts.

**Key Objectives:**
- Explore and analyze the California housing dataset
- Implement data preprocessing and feature engineering
- Train and evaluate multiple regression models
- Compare model performances and select the best performing algorithm
- Create visualizations to understand data patterns and model results

## 📊 Dataset

The project uses the California Housing dataset from scikit-learn, which contains information collected from the 1990 California census.

**Dataset Details:**
- **Samples:** 20,640 districts
- **Features:** 8 numerical features
- **Target:** Median house value (in hundreds of thousands of dollars)

**Features Description:**
- `MedInc`: Median income in block group
- `HouseAge`: Median house age in block group
- `AveRooms`: Average number of rooms per household
- `AveBedrms`: Average number of bedrooms per household
- `Population`: Block group population
- `AveOccup`: Average number of household members
- `Latitude`: Block group latitude
- `Longitude`: Block group longitude

## ✨ Features

- **Data Exploration:** Comprehensive exploratory data analysis with visualizations
- **Data Preprocessing:** Feature scaling, handling missing values, and outlier detection
- **Feature Engineering:** Creating new meaningful features from existing ones
- **Multiple Models:** Implementation of various regression algorithms
- **Model Evaluation:** Performance comparison using multiple metrics
- **Visualization:** Interactive plots and maps showing predictions vs actual values
- **Cross-validation:** Robust model validation techniques

## 🚀 Installation

### Prerequisites

- Python 3.7 or higher
- pip package manager

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/ErickRandria/House_Price_Prediction.git
   cd House_Price_Prediction
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv housing_env
   source housing_env/bin/activate  # On Windows: housing_env\Scripts\activate
   ```

3. **Install required packages**
   ```bash
   pip install -r requirements.txt
   ```

### Required Dependencies

```
pandas>=1.3.0
numpy>=1.21.0
scikit-learn>=1.0.0
matplotlib>=3.4.0
seaborn>=0.11.0
jupyter>=1.0.0
plotly>=5.0.0
flask>=2.0.0
```

## 🔧 Usage

### Running the Project

1. **Start Jupyter Notebook**
   ```bash
   jupyter notebook
   ```

2. **Open the main notebook**
   - Navigate to `ML_implementation.ipynb`
   - Run all cells to execute the complete pipeline

3. **Run the Flask Web Application**
   ```bash
   python app.py
   ```
   - Open your browser and go to `http://localhost:5000`
   - Use the web interface to make housing price predictions

## 🛠️ Technologies Used

- **Python**: Main programming language
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computations
- **Scikit-learn**: Machine learning algorithms and tools
- **RandomForestRegressor**: Random Forest framework
- **Matplotlib/Seaborn**: Data visualization
- **Plotly**: Interactive visualizations
- **Jupyter Notebook**: Development environment
- **Flask**: Web application deployment

## 📊 Results

### Key Findings

1. **Median Income** is the strongest predictor of housing prices
2. **Location (Latitude/Longitude)** significantly impacts house values
3. **Ocean proximity** and **house age** show moderate correlation with prices
4. The model achieves **84% accuracy** in predicting housing prices

### Visualizations

The project includes several visualizations:
- Correlation heatmap of all features
- Geographic distribution of housing prices
- Feature importance rankings
- Actual vs predicted price comparisons
- Residual analysis plots

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

### Steps to Contribute

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📧 Contact

**Erick R.** - [hajjaerick@gmail.com](mailto:hajjaerick@gmail.com)

Project Link: [https://github.com/ErickRandria/House_Price_Prediction](https://github.com/ErickRandria/House_Price_Prediction)

---
