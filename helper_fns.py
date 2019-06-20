import pandas as pd 
import numpy as np 
from sklearn.externals import joblib



def arr_and_scale(hand_list):
	scaler_pkl=open("models/data_scaler.pkl","rb")
	scaler = joblib.load(scaler_pkl)
	hand_arr=np.array(hand_list)
	hand_arr=hand_arr.reshape(1,-1)
	scaled_arr=scaler.transform(hand_arr)
	return scaled_arr

def predict_hand(arr):
	mlp_pkl=open("models/mlp_poker.pkl","rb")
	mlp_clf=joblib.load(mlp_pkl)
	prediction=mlp_clf.predict(arr)
	return prediction[0]

def hand_name(prediction):
	if prediction==0:
		name=["Nothing in Hand","Better Luck next time!"]
	if prediction==1:
		name=['One pair','One pair of equal ranks within five cards']
	if prediction==2:
		name=['Two pairs','Two pairs of equal ranks within five cards']
	if prediction==3:
		name=['Three of a kind', 'Three equal ranks within five cards']
	if prediction==4:
		name=["Straight","Five cards, sequentially ranked with no gaps"]
	if prediction==5:
		name=["Flush", "Five cards with the same suit"]
	if prediction==6:
		name=["Full house", "Pair + different rank three of a kind"]
	if prediction==7:
		name=["Four of a kind", "Four equal ranks within five cards"]
	if prediction==8:
		name=["Straight flush", "Straight + flush"]
	if prediction==9:
		name=["Royal flush","{Ace, King, Queen, Jack, Ten} + flush"]
	return name