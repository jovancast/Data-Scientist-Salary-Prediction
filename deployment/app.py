import streamlit as st
import pandas as pd
import pickle

st.title("--Data Scientist Salary Prediction--")

# import model
with open('salary_pred.pkl' , 'rb') as f:
    model = pickle.load(f)

st.write('Insert feature to predict')

year = st.sidebar.selectbox(label='work_year', options=[2020, 2021, 2022])
experience = st.sidebar.selectbox(label='experience_level', options=['EN', 'MI', 'SE', 'EX'])
type = st.sidebar.selectbox(label='employment_type', options=['PT', 'FT', 'CT', 'FL'])
title = st.sidebar.selectbox(label='job_title', options=['Data Scientist', 'Data Analyst', 'Data Engineer', 'Others'])
continent = st.selectbox(label='employee_continent', options=['Europe', 'Asia', 'North America', 'South America', 'Oceania', 'Africa'])
ratio = st.selectbox(label='remote_ratio', options=['0', '50', '100'])
size = st.selectbox(label='company_size', options=['S', 'M', 'L'])


# convert into dataframe
data = pd.DataFrame({'work_year': int(year),
                'experience_level': experience,
                'employment_type': type,
                'job_title':title,
                'employee_continent': continent,
                'remote_ratio': ratio,
                'company_size': size},index=range(0,6))

# model predict
clas = model.predict(data).tolist()[0]

# interpretation
if st.button('predict'):
    st.write('Predict Salary Result: ',clas)
