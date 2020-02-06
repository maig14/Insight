import joblib
import pickle
import numpy as np
import pandas as pd
import streamlit as st
import os

example_diseases = [
    '',
    'Breast',
    'Brain',
    'Leukemias',
    'Lung',
    'Lymphomas',
    'Multiple Myeloma',
]

phases = [
    '',
    'Phase 1',
    'Phase 2',
    'Phase 3'
]

results = [
    '',
    'Yes',
    'No',
]

example_sites = [
    '',
    'MD Anderson Cancer Center',
    'National Cancer Institute',
    'Memorial Sloan Kettering Cancer Center',
    'Roche',
    'Novartis',
    'Mayo Clinic'
]

st.markdown('#### [Insight Data Science Fellowship](https://www.insightdatascience.com/)')
st.markdown('#### Made by [Louise Giam](https://www.linkedin.com/in/louise-giam/)')
st.markdown('#### Feb 2020 Health Data Science')

st.markdown('## Assessing Clinical Trial Completion')
st.markdown('---')

disease = st.selectbox('Cancer', example_diseases)
phase = st.selectbox('Phase', phases)
company = st.selectbox('Company', example_sites)
enroll = st.number_input('Enrollment')
results = st.selectbox('Has Results?', results)

features = [enroll, phases, results]

# model = joblib.load(open('model.pkl', 'rb'))

if st.button('Predict'):
	st.success(f'Likelihood of completion: 63%')
#	st.success(f'Your Salary per anum is: Ghc {round(prediction[0], 2)}')
