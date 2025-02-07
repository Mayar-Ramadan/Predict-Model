
import pickle as pk
import numpy as np
import streamlit as st
from Function_lab import get_results

file = open("model.pkl" , "rb")
model = pk.load(file)

st.title('Model For Expected Tips')

total_bill = st.number_input("Enter total_bill : ")
sex = st.selectbox("Enter sex :", ["Male", "Female"])
smoker = st.selectbox("Enter if you smoke :", ["Yes", "No"])
day = st.selectbox("Enter day :", ["Thur", "Fri", "Sat", "Sun"])
time = st.selectbox("Enter time :", ["Lunch", "Dinner"])
size = st.number_input("Enter size :")

show = st.button('Click')

if show:
    if total_bill != "" and size != "":
            total_bill = float(total_bill)  
            size = int(size)
   
    result = get_results(model, total_bill, sex, smoker, day, time, size)

    if isinstance(result, np.ndarray):
            st.title(f'The Tips is : {result[0]:.2f}')
    else:   
            print("Invalid result")

