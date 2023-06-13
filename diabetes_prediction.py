# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 19:18:42 2023

@author: siri1
"""

#main--function
import numpy as np
import pickle
import streamlit as st
#loading saves model
loaded_model=pickle.load(open('C:/Users/siri1/Downloads/trained_model.sav','rb'))

#creating function for prediction 
def diabetes_prediction(input_data):
    
    #converting it into numpy array
    input_data_as_numpy_array=np.array(input_data)
    #reshaping the array since we are predicting
    input_data_reshaped= input_data_as_numpy_array.reshape(1,-1)
    prediction=loaded_model.predict(input_data_reshaped)
    print(prediction)
    if prediction[0]==0:
      return"The person is not a diabetic"
    elif prediction[0]==1:
      return "The person is diabetic"
      
def main():
    #Giving the title
    st.title("Diabetes Prediction Web Page")
    #Making INput data webpage for end user
    Pregnancies = st.text_input('Number of Pregnancies')
    Glucose = st.text_input('Glucose Value')
    BloodPressure = st.text_input('BloodPressure Value')
    SkinThickness = st.text_input('SkinThickness Value')
    Insulin = st.text_input('Insulin level')
    BMI = st.text_input('BMI Value')
    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function Value')
    Age = st.text_input('Age of the Person')
      #code for Prediction
    diagnosis=""
    #creating Examine for Prediction
    if st.button("Diabetes Test Result"):
        diagnosis=diabetes_prediction([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])
    st.success(diagnosis)
if __name__=="__main__":
    main()
    
      
  