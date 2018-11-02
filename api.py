from flask import Flask, render_template, session, redirect, url_for, session
import numpy as np
from flask_wtf import FlaskForm
from wtforms import (StringField, RadioField, DecimalField, SubmitField)
from sklearn.ensemble import RandomForestClassifier
from datetime import datetime
from sklearn.model_selection import train_test_split, RandomizedSearchCV, GridSearchCV

''''
For Prediction
'''
import pandas as pd
import numpy as np
import pickle
from sklearn.externals import joblib


model = joblib.load('randforestgridsearch_f2.joblib')

def get_prob(input):
    x = np.array(input)
    state = np.zeros(78)
    state[31] = 1
    state[-11] = 1
    state = np.array(state)
    year = datetime.today().year - 1955
    month = datetime.today().month
    date = np.array([year, month])
    x = np.concatenate((date,x))
    x = x.astype(float)
    x = np.concatenate((x, state))
    x = x.reshape(1,-1)
    # return 1
    prediction = model.predict_proba(x)
    print(prediction)
    if prediction[0][1] > 0.64:
        return 1
    else:
        return 0