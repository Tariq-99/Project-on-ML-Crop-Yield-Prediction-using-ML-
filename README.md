# Crop Yield Prediction Web App

A machine learning web application that predicts crop yield in **hg/ha** using agricultural, climate, and crop-related inputs through a Flask-based interface.[file:2][file:12]

## Project Overview

This project combines a trained Random Forest regression model with a clean web interface so users can estimate crop yield based on area, crop type, year, rainfall, pesticide usage, and average temperature.[file:2][file:11][file:12]
The notebook shows that the final merged dataset contains 25,932 rows and 7 columns, and the target variable is `value_hg_ha`.[file:3][file:12]

## Features

- Predicts crop yield from 6 input features: area, year, average rainfall, pesticides, average temperature, and crop item.[file:2][file:12]
- Uses a trained **Random Forest Regressor** loaded from `rf_model.pkl` in the Flask app.[file:2]
- Includes dropdown-based selection for supported countries/areas and crop items to reduce invalid input choices.[file:2]
- Displays prediction results and validation/error messages in the UI.[file:2][file:11]
- Provides a modern responsive interface styled with a dark green dashboard theme.[file:10][file:11]

## Tech Stack

| Component | Details |
|---|---|
| Backend | Flask.[file:1][file:2] |
| Data handling | Pandas, NumPy.[file:1][file:3] |
| ML libraries | Scikit-learn, XGBoost explored in notebook.[file:1][file:3][file:12] |
| Model used in app | Random Forest Regressor.[file:2][file:12] |
| Model serialization | Joblib / Pickle-based saved models in workflow.[file:2][file:3] |
| Frontend | HTML, CSS, Jinja templating.[file:10][file:11] |

## Dataset

Source files used in this project:
- `yield.csv`
- `rainfall.csv`
- `pesticides.csv`
- `temp.csv`

Final working dataset:
- `df_yield_merged.csv`

The notebook uses a merged dataset named `df_yield_merged.csv` built from agricultural and climate sources.[file:3][file:12]
The main columns used are `area`, `year`, `average_rain_fall_mm_per_year`, `pesticides_tonnes`, `avg_temp`, `item`, and `value_hg_ha`.[file:3]
The data shown in the notebook spans years from 1990 to 2013 and includes multiple countries and crop categories.[file:3]

## Model Training

The notebook performs preprocessing by encoding categorical features such as area and item before model training.[file:3]
It trains and evaluates both Random Forest Regressor and XGBoost Regressor models, with Random Forest giving the stronger test performance shown in the notebook summary.[file:3][file:12]
The Flask app uses the Random Forest model for inference.[file:2]

## Model Performance

From the notebook, the Random Forest Regressor achieved a Mean Absolute Error of about 4033.37, Mean Squared Error of about 104120003.37, and an R-squared score of about 0.9852 on the test set.[file:3]
The notebook also includes XGBoost evaluation, but the deployed app is built around the Random Forest model.[file:2][file:3]

## Exploratory Analysis

The notebook includes:

- Distribution analysis of crop yield using a histogram with KDE.[file:3]
- Correlation analysis between numeric features using a heatmap.[file:3]
- Outlier visualization using boxplots.[file:3]

The attached screenshots also show the prediction interface and sample prediction outputs from the running app.[file:4][file:5][file:6]

## Project Structure

```text
crop-yield-prediction/
├── app.py
├── requirements.txt
├── crop_yield_prediction.ipynb
├── index.html
├── style.css
├── README.md
└── rf_model.pkl
```

The Flask app expects the trained model file to be available in the project root directory.[file:2]

## Installation

1. Clone the repository.
2. Create and activate a virtual environment.
3. Install dependencies.
4. Make sure `rf_model.pkl` is placed in the root folder.
5. Run the Flask app.[file:1][file:2]

```bash
pip install -r requirements.txt
python app.py
```

## Usage

1. Open the app in the browser, typically at `http://127.0.0.1:5000/` when running locally.[file:2][file:4][file:5][file:6]
2. Select an area and crop item from the dropdowns.[file:2][file:11]
3. Enter year, average rainfall, pesticides, and average temperature.[file:2][file:11]
4. Click **Predict Yield** to view the estimated crop yield in hg/ha.[file:11][file:4][file:6]

## Input Features

| Feature | Description |
|---|---|
| Area | Country/region selected from the supported list.[file:2] |
| Crop item | Crop type selected from the supported crop list.[file:2] |
| Year | Year for the prediction record.[file:2] |
| Average rainfall (mm/year) | Annual rainfall input.[file:2][file:11] |
| Pesticides (tonnes) | Pesticide usage input.[file:2][file:11] |
| Average temperature | Mean temperature input.[file:2][file:11] |

## Output

The application returns a predicted crop yield value in **hg/ha** after processing the submitted form data through the trained model.[file:2][file:4][file:6]
If inputs are invalid or the model file is missing, the app displays user-friendly error messages.[file:2]

## UI Highlights

The interface uses a two-panel layout with project information on the left and the input form on the right.[file:10][file:11]
It includes summary cards for target, number of input features, and the deployed model, plus styled success and error message blocks.[file:10][file:11]
The CSS also contains responsive breakpoints for tablet and mobile layouts.[file:10]

## Dependencies

```text
Flask==3.0.3
pandas==2.2.2
numpy==1.26.4
scikit-learn==1.5.1
joblib==1.4.2
xgboost==2.1.1
```
[file:1]

## Notes

- The current app file loads `rf_model.pkl`, so the model filename should match that exact name for successful execution.[file:2]
- The notebook saves both Random Forest and XGBoost models during experimentation.[file:3]
- The project can be extended by adding model comparison, charts, API endpoints, or deployment support.[file:3][file:10][file:11]

## Author

Tariq.[file:12]
