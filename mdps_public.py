# -*- coding: utf-8 -*-
"""
Created on Sun May  8 21:01:15 2022

@author: siddhardhan
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models


Insurance_model = pickle.load(open("C:\Users\naray\OneDrive - NATIONAL INSTITUTE OF INDUSTRIAL ENGINEERING\Desktop\Important\NITIE\Python\Youtube\Projects\AI&ML\Sidhardhan\Deployment\Insurance\Medical_insurance.sav", 'rb'))



#************************************************************************************************************************    

# Medical_insurance Prediction Page
    
# page title
st.title('Diabetes Prediction using ML')

#age,sex,bmi,children,smoker,region,charges    
    
#getting the input data from the user
col1, col2, col3 = st.columns(3)
    
with col1:
	age = st.text_input('age')
        
with col2:
	sex = st.text_input('sex')
    
with col3:
	bmi = st.text_input('bmi')
    
with col1:
	children = st.text_input('children')
    
with col2:
	smoker = st.text_input('smoker')
    
with col3:
	region = st.text_input('region')
   
    
# code for Prediction
medical_insurance_cost = ''
    
# creating a button for Prediction
#age,sex,bmi,children,smoker,region,charges
    
if st.button('Diabetes Test Result'):
	cost_prediction = Medical_insurance.predict([[age,sex,bmi,children,smoker,region]])
#m = medical_insurance_cost+str(cost_prediction)
        
#st.success(cost_prediction)
#st.success(m)

#********************************************************************************************************************************************************

    















