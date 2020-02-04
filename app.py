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
st.markdown('#### 2020A Health Data Science')

st.markdown('## Clinical Trial Insights')
st.markdown('---')
