# Crop Yield Prediction Web App

A machine learning web application that predicts crop yield in **hg/ha** using agricultural, climate, and crop-related inputs through a Flask-based interface.

## Project Overview

This project combines a trained Random Forest regression model with a clean web interface so users can estimate crop yield based on area, crop type, year, rainfall, pesticide usage, and average temperature.
The notebook shows that the final merged dataset contains 25,932 rows and 7 columns, and the target variable is `value_hg_ha`.

## Features

- Predicts crop yield from 6 input features: area, year, average rainfall, pesticides, average temperature, and crop item.
- Uses a trained **Random Forest Regressor** loaded from `rf_model.pkl` in the Flask app.[file:2]
- Includes dropdown-based selection for supported countries/areas and crop items to reduce invalid input choices.
- Displays prediction results and validation/error messages in the UI.[file:2][file:11]
- Provides a modern responsive interface styled with a dark green dashboard theme.

## Tech Stack

| Component | Details |
|---|---|
| Backend | Flask.|
| Data handling | Pandas, NumPy.|
| ML libraries | Scikit-learn, XGBoost explored in notebook.|
| Model used in app | Random Forest Regressor.|
| Model serialization | Joblib / Pickle-based saved models in workflow.|
| Frontend | HTML, CSS, Jinja templating.|

## Dataset

Source files used in this project:
- `yield.csv`
- `rainfall.csv`
- `pesticides.csv`
- `temp.csv`

Final working dataset:
- `df_yield_merged.csv`

The notebook uses a merged dataset named `df_yield_merged.csv` built from agricultural and climate sources.
The main columns used are `area`, `year`, `average_rain_fall_mm_per_year`, `pesticides_tonnes`, `avg_temp`, `item`, and `value_hg_ha`.
The data shown in the notebook spans years from 1990 to 2013 and includes multiple countries and crop categories.

## Model Training

The notebook performs preprocessing by encoding categorical features such as area and item before model training.
It trains and evaluates both Random Forest Regressor and XGBoost Regressor models, with Random Forest giving the stronger test performance shown in the notebook summary.
The Flask app uses the Random Forest model for inference.

## Model Performance

From the notebook, the Random Forest Regressor achieved a Mean Absolute Error of about 4033.37, Mean Squared Error of about 104120003.37, and an R-squared score of about 0.9852 on the test set.
The notebook also includes XGBoost evaluation, but the deployed app is built around the Random Forest model.

## Exploratory Analysis

The notebook includes:

- Distribution analysis of crop yield using a histogram with KDE.
- Correlation analysis between numeric features using a heatmap.
- Outlier visualization using boxplots.
The attached screenshots also show the prediction interface and sample prediction outputs from the running app.

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

The Flask app expects the trained model file to be available in the project root directory.

## Installation

1. Clone the repository.
2. Create and activate a virtual environment.
3. Install dependencies.
4. Make sure `rf_model.pkl` is placed in the root folder.
5. Run the Flask app.

```bash
pip install -r requirements.txt
python app.py
```

## Usage

1. Open the app in the browser, typically at `http://127.0.0.1:5000/` when running locally.
2. Select an area and crop item from the dropdowns.
3. Enter year, average rainfall, pesticides, and average temperature.
4. Click **Predict Yield** to view the estimated crop yield in hg/ha.

## Input Features

| Feature | Description |
|---|---|
| Area | Country/region selected from the supported list.|
| Crop item | Crop type selected from the supported crop list.|
| Year | Year for the prediction record.[file:2] |
| Average rainfall (mm/year) | Annual rainfall input.|
| Pesticides (tonnes) | Pesticide usage input.|
| Average temperature | Mean temperature input.|

## Output

The application returns a predicted crop yield value in **hg/ha** after processing the submitted form data through the trained model.
If inputs are invalid or the model file is missing, the app displays user-friendly error messages.

## UI Highlights

The interface uses a two-panel layout with project information on the left and the input form on the right.
It includes summary cards for target, number of input features, and the deployed model, plus styled success and error message blocks.
The CSS also contains responsive breakpoints for tablet and mobile layouts.

## Dependencies

```text
Flask==3.0.3
pandas==2.2.2
numpy==1.26.4
scikit-learn==1.5.1
joblib==1.4.2
xgboost==2.1.1
```

## Notes

- The current app file loads `rf_model.pkl`, so the model filename should match that exact name for successful execution.[file:2]
- The notebook saves both Random Forest and XGBoost models during experimentation.[file:3]
- The project can be extended by adding model comparison, charts, API endpoints, or deployment support.[file:3][file:10][file:11]

## Author

Tariq.
