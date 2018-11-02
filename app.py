from flask import Flask, render_template, request, session, redirect, url_for, session
from api import get_prob
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

app = Flask('Disaster')

@app.route('/', methods = ['POST', 'GET'])
def index():
	if request.method == 'GET':
		return render_template('index.html')
	

@app.route('/name/<animal>')
def eat(animal):
	return render_template('eat.html', animal = animal)

@app.route('/louisiana', methods = ['POST', 'GET'])
def louisiana_hurricane():
	if request.method == 'GET':
		return render_template('eat.html', state = 'Louisiana')
	if request.method == 'POST':
		print([int(request.form['temp']), int(request.form['pr']), int(request.form['magnitude']), int(request.form['latitude']), int(request.form['longitude'])])
		prob = get_prob([request.form['temp'], request.form['pr'], request.form['magnitude'], request.form['latitude'], request.form['longitude']])
		# return render_template('eat.html', state = 'Louisiana')
		return render_template('eat.html', state = 'Louisiana', prob = prob)

if __name__ == "__main__":
    app.run(debug=True)



