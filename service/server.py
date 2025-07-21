import pandas as pd 
import numpy as np

import joblib
from flask import Flask, request, render_template, redirect, url_for
from flask import send_from_directory
import os

from sklearn.pipeline import Pipeline

# supported models: 
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cluster import KMeans

# supported scalers 
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler, FunctionTransformer

app = Flask(__name__, static_url_path='/static', 
            static_folder='data/static',)

UPLOAD_FOLDER = './data/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

g_model = None

def get_model():
    global g_model
    if g_model == None:
        g_model = joblib.load('./data/model_pipe.pkl')
    return g_model

def predict(file) -> pd.DataFrame:
    model = get_model()     
    X = pd.read_csv(file)
    return model.predict(X)
 

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
            if 'file' not in request.files:
                return 'No file part'
            file = request.files['file']
            if file.filename == '':
                return 'No selected file'
            if file: 
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
                file.save(filepath)
                y_pred = predict(filepath)
                X = pd.read_csv(filepath)
                X["prediction"] = y_pred
                return X.to_html(index=False)
    if request.method == 'GET':
        return """
<!doctype html>
<html>
<head>
    <title>Model-Service/Upload Data</title>
</head>
<body>
    <h1>Upload a CSV file</h1>
    <form method="POST" enctype="multipart/form-data">
        <input type="file" name="file" accept="file/*">
        <input type="submit" value="Upload">
    </form>
</body>
</html>
""" 

if __name__ == '__main__':
    app.run(debug=True)
