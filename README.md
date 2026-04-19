# Crop Yield Prediction using Machine Learning

This project predicts crop yield (`value_hg_ha`) using machine learning on agricultural and climate data.

## Overview
The model uses features such as area, year, average rainfall, pesticide usage, average temperature, and crop type to predict crop yield.  
The final merged dataset contains 25,932 records and 7 columns.

## Dataset
Source files used in this project:
- `yield.csv`
- `rainfall.csv`
- `pesticides.csv`
- `temp.csv`

Final working dataset:
- `df_yield_merged.csv`

## Features Used
- Area
- Year
- Average rainfall per year
- Pesticides used
- Average temperature
- Crop item

## Target
- `value_hg_ha`

## Models
- Random Forest Regressor
- XGBoost (explored in the notebook)

## Result
The Random Forest Regressor achieved strong performance on the test set with:
- MAE: 4042.13
- MSE: 108525265.88
- R² Score: 0.9846

## Files
- `crop_yield_prediction.ipynb` - main notebook
- `crop_yield_presentation.html` - project presentation
- Dataset files used for training and preprocessing

## Tools & Libraries
Python, Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn, XGBoost

## Author
Tariq