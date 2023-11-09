import streamlit as st
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.preprocessing import OrdinalEncoder
import numpy as np

file = pd.read_csv("C:\\Users\\HEMALATHA KARUPUSAMY\\Desktop\\visualstudio\\diabetes\\diabetes.csv")

model = OrdinalEncoder()
file['gender'] = model.fit_transform(file[['gender']])
file['smoking_history'] = model.fit_transform(file[['smoking_history']])

y = file['diabetes']
x = file.iloc[ : , 0:8]

xtrain,xtest,ytrain,ytest = train_test_split(x, y, test_size = 0.15)

model = DecisionTreeClassifier().fit(xtrain,ytrain)
y_pred = model.predict(xtest)


st.set_page_config(page_title="Diabetes Prediction", page_icon=None, layout="wide")
st.header("Diabetes Prediction")

col1,col2 = st.columns(2)
with col1:
    Gender = st.selectbox('Select Your Gender',('Male','Female','Other'))
    Gender_ = {'Female':0.0, 'Male':1.0, 'Other':2.0}
    Hypertension = st.selectbox('Are you Hypertensed',('Yes','No'))
    Hypertension_ = {'No':0, 'Yes':1}
    Heartdiseases = st.selectbox('Do you have Heart Disease',('Yes','No'))
    Heartdiseases_ = {'No':0, 'Yes':1}
    smoking_history = st.selectbox('Are you a Smoker if Yes select your stage',('Never', 'No Info', 'Current', 'Former', 'Ever', 'Not Current'))
    smoking_history_ = {'Never':4.0, 'No Info':0.0, 'Current':1.0, 'Former':3.0, 'Ever':2.0, 'Not Current':5.0}
with col2:
    Age = st.text_input('Enter your Age')
    BMI = st.text_input('Enter your BMI')
    HbA1c_level = st.text_input('Enter your Glucose HbA1c_level')
    blood_glucose_level = st.text_input('Enter your blood_glucose_level')

a,b,c = st.columns(3)

with b:
    submit = st.button("Submit")
    if submit:
        data = np.array([[Gender_[Gender],Age,Hypertension_[Hypertension],Heartdiseases_[Heartdiseases],smoking_history_[smoking_history],BMI,HbA1c_level,blood_glucose_level]])
        pred_data = model.predict(data)
        if pred_data[0] == 1:
          st.error('You are diabetised')
        else:
          st.success('You are healthy')




