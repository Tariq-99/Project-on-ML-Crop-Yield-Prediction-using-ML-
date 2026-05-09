from flask import Flask, render_template, request
import pandas as pd
import joblib
from pathlib import Path

app = Flask(__name__)
BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / 'rf_model.pkl'

model = joblib.load(MODEL_PATH)

AREA_OPTIONS = [
    'Albania','Algeria','Angola','Argentina','Armenia','Australia','Austria','Azerbaijan',
    'Bahamas','Bahrain','Bangladesh','Belarus','Belgium','Botswana','Brazil','Bulgaria',
    'Burkina Faso','Burundi','Cameroon','Canada','Central African Republic','Chile','Colombia',
    'Croatia','Denmark','Dominican Republic','Ecuador','Egypt','El Salvador','Eritrea','Estonia',
    'Finland','France','Germany','Ghana','Greece','Guatemala','Guinea','Guyana','Haiti','Honduras',
    'Hungary','India','Indonesia','Iraq','Ireland','Italy','Jamaica','Japan','Kazakhstan','Kenya',
    'Latvia','Lebanon','Lesotho','Libya','Lithuania','Madagascar','Malawi','Malaysia','Mali',
    'Mauritania','Mauritius','Mexico','Montenegro','Morocco','Mozambique','Namibia','Nepal',
    'Netherlands','New Zealand','Nicaragua','Niger','Norway','Pakistan','Papua New Guinea','Peru',
    'Poland','Portugal','Qatar','Romania','Rwanda','Saudi Arabia','Senegal','Slovenia','South Africa',
    'Spain','Sri Lanka','Sudan','Suriname','Sweden','Switzerland','Tajikistan','Thailand','Tunisia',
    'Turkey','Uganda','Ukraine','United Kingdom','Uruguay','Zambia','Zimbabwe'
]

ITEM_OPTIONS = [
    'Cassava','Maize','Plantains and others','Potatoes','Rice, paddy',
    'Sorghum','Soybeans','Sweet potatoes','Wheat','Yams'
]

AREA_ENCODING = {name: idx for idx, name in enumerate(AREA_OPTIONS)}
ITEM_ENCODING = {name: idx for idx, name in enumerate(ITEM_OPTIONS)}

FEATURE_COLUMNS = [
    'area',
    'year',
    'average_rain_fall_mm_per_year',
    'pesticides_tonnes',
    'avg_temp',
    'item'
]

@app.route('/', methods=['GET', 'POST'])
def home():
    prediction = None
    error = None
    form_data = {}

    if request.method == 'POST':
        form_data = request.form.to_dict()
        try:
            area = request.form.get('area', '').strip()
            item = request.form.get('item', '').strip()
            year = int(request.form.get('year', '0'))
            rainfall = float(request.form.get('average_rain_fall_mm_per_year', '0'))
            pesticides = float(request.form.get('pesticides_tonnes', '0'))
            avg_temp = float(request.form.get('avg_temp', '0'))

            if area not in AREA_ENCODING or item not in ITEM_ENCODING:
                raise ValueError('Please choose a valid area and crop from the dropdown lists.')

            input_df = pd.DataFrame([[
                AREA_ENCODING[area],
                year,
                rainfall,
                pesticides,
                avg_temp,
                ITEM_ENCODING[item]
            ]], columns=FEATURE_COLUMNS)

            prediction = round(float(model.predict(input_df)[0]), 2)
        except ValueError as exc:
            error = str(exc) or 'Please enter valid values in every field.'
        except FileNotFoundError:
            error = 'rfmodel.pkl was not found. Place the trained model in the project root folder.'
        except Exception as exc:
            error = f'Prediction failed: {exc}'

    return render_template(
        'index.html',
        prediction=prediction,
        error=error,
        form_data=form_data,
        area_options=AREA_OPTIONS,
        item_options=ITEM_OPTIONS
    )

if __name__ == '__main__':
    app.run(debug=True)