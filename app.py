import string
import pickle
import numpy as np
from flask import Flask, render_template, request,url_for

Heart = Flask(__name__)

def prediction(lst):
    filename = "D:/Data Science/ML/sample pro/classification/Heart-Disease-Prediction/Heart Attack classifier.pickle"
    with open(filename, 'rb') as file:
        model = pickle.load(file)
        pred_value = model.predict([lst])
        return pred_value

@Heart.route("/",methods=["Post","Get"])

def index():

    pred_value = None

    if request.method == 'POST':

        form_data = request.form

        age = form_data['age']
        sex = form_data['sex']
        cp = form_data['cp']
        trestbps = form_data['trestbps']
        chol = form_data['chol']
        fbs = form_data['fbs']
        restecg = form_data['restecg']
        thalach = form_data['thalach']
        exang = form_data['exang']
        oldpeak = form_data['oldpeak']
        slope = form_data['slope']
        ca = form_data['ca']
        thal = form_data['thal']


        input_list = []

        input_list.append(int(age))
        input_list.append(int(sex))
        input_list.append(int(cp))
        input_list.append(int(trestbps))
        input_list.append(int(chol))
        input_list.append(int(fbs))
        input_list.append(int(restecg))
        input_list.append(int(thalach))
        input_list.append(int(exang))
        input_list.append(float(oldpeak))
        input_list.append(int(slope))
        input_list.append(int(ca))
        input_list.append(int(thal))

        pred_value = prediction(input_list)


    

        
        
    

    return render_template("heart_pre.html",prediction= pred_value )

    
















if __name__ =='__main__':
    Heart.run(debug = True)


    