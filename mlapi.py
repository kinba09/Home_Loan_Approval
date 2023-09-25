# Libraries
from fastapi import FastAPI
import pickle
import numpy as np

# Custom Files 
from CustomData import *
from encoding import *

# Initializing 
app = FastAPI()

pickled_model = pickle.load(open('modelold.pkl', 'rb')) #modeltest.pkl


def pipeline(item: InputData) -> EncodedData:
    return np.array([
                    Gender_encoding[item.Gender], \
                    Married_encoding[item.Married], \
                    Dependents_encoding[item.Dependents], \
                    Education_encoding[item.Education],\
                    Self_Employed_encoding[item.Self_Employed],\
                    item.LoanAmount, \
                    item.Credit_History, \
                    Property_Area_encoding[item.Property_Area], \
                    item.Total_Income, \
                    item.Loan_Term_years
                     ])

@app.get('/')
async def scoring_endpoint(item : InputData):
    newData = pipeline(item)
    newData = newData.reshape((1, -1))
    yhat = pickled_model.predict(newData)[0]
    #yhat = round(yhat, 2)
    if yhat == 0:
        x = 'Yes your loan can be approved !'
        Ballons_bool = True
    else:
        x = 'Sorry, Your loan can not be approved'
        Ballons_bool = False
    # pred_text = str(type(yhat))
    pred_text = x
    return {'prediction' : pred_text,\
            'Ballons' : Ballons_bool} 