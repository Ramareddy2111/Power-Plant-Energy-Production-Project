# -*- coding: utf-8 -*-
"""
Created on Thu May  2 12:55:40 2024

@author: Rajesh Gonnade
"""

import pickle
import streamlit as st

st.title('Energy Production :wave:')

model1=pickle.load(open('model1.pkl','rb'))

def predict(temperature	,exhaust_vacuum,r_humidity):
    prediction = model1.predict([[temperature,exhaust_vacuum,r_humidity]])
    return prediction

def main():
    
    st.markdown('This is a very simple webapp for prediction of Energy Production :chart:')
    temperature = st.slider('Temperature (°C)', min_value=-20.0, max_value=40.0, step=0.1)
    exhaust_vacuum = st.slider('Exhaust Vacuum (inHg)', min_value=0.0, max_value=100.0, step=0.1)
    r_humidity = st.slider('Relative Humidity (%)', min_value=0.0, max_value=100.0, step=0.1)

    if st.button('Predict'):
        result = predict(temperature,exhaust_vacuum,r_humidity)
        st.success('The Energy Production is: {}'.format(result))
                         
                          
        
if __name__ == '__main__':
    main()
