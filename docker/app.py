import pickle
import numpy as np
from flask import Flask, render_template, url_for, redirect, request
import pandas as pd

df = pd.read_csv('clean_df.csv')

app = Flask(__name__, template_folder='templates')

@app.route('/')
def home():
    return render_template('home.html')

@app.route("/result", methods = ['POST'])
def result():
    user_input = [int(x) for x in request.form.values()]  # 6 digits list
    
    def get_new_features(df, input_list):
        new_input  = input_list
        match_df = df[(df['jobType']==input_list[0]) & (df['degree']==input_list[1]) & 
                      (df['major']==input_list[2]) & (df['industry']==input_list[3])]
        v_mean = round(match_df['G_mean'].mean())
        v_max = round(match_df['G_max'].mean())
        v_min = round(match_df['G_min'].mean())
        v_std = round(match_df['G_std'].mean())
        v_median = round(match_df['G_median'].mean())
        new_feature = [v_mean, v_max, v_min, v_std, v_median]
        list.extend(new_input, new_feature)    # add new feature for model prediction
        return new_input
    
    def get_prediction(input_list):
        input_array = np.array(input_list).reshape(1,-1)
        model = pickle.load(open('model.pkl', 'rb'))
        prediction = model.predict(input_array)
        return prediction[0]
    
    new_input = get_new_features(df, user_input)         
        
    prediction = get_prediction(new_input)
    
    return render_template('home.html', 
                prediction = "Your salary prediction is: {}".format(round(prediction)))

if __name__ == "__main__":
    app.run(host = '0.0.0.0', debug=True)