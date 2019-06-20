from flask import Flask,render_template,url_for,request
from flask_bootstrap import Bootstrap 
import pandas as pd 
import numpy as np 
from sklearn.externals import joblib
from sklearn.neural_network import MLPClassifier

from helper_fns import *

application=app = Flask(__name__)
Bootstrap(app)


@app.route('/')
def homepage():
	return render_template('main.html')
	
	
@app.route('/predict', methods=['POST'])


def predict():
	s1= request.form['suits1']
	r1=request.form['rank1']
	s2= request.form['suits2']
	r2=request.form['rank2']
	s3= request.form['suits3']
	r3=request.form['rank3']
	s4= request.form['suits4']
	r4=request.form['rank4']
	s5= request.form['suits5']
	r5=request.form['rank5']
	c_comb=[s1+r1,s2+r2,s3+r3,s4+r4,s5+r5]
	

	if len(c_comb) != len(set(c_comb)):
		hand=['Selected Two or more same cards','Please Try Again']
	else:
		cards_list=[int(s1),int(r1),int(s2),int(r2),int(s3),int(r3),int(s4),int(r4),int(s5),int(r5)]
		cards_arr=arr_and_scale(cards_list)
		prediction=predict_hand(cards_arr)
		hand=hand_name(prediction)
	return render_template('results.html',name=hand)
	
	
	
	
	
	
	
	
	

if __name__ == '__main__':
	app.run(host='localhost',port=5000,debug=True)