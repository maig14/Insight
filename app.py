import joblib
import pickle
import numpy as np
import pandas as pd

# https://towardsdatascience.com/how-to-write-web-apps-using-simple-python-for-data-scientists-a227a1a01582
# st.slider

import streamlit as st
import os

# Sample smiles for users to predict on
#example_diseases = [
#    '',
#    'Bladder',
#    'Bone',
#    'Brain',
#    'Breast',
#    'Cervical',
#    'Colorectal',
#    'Esophageal',
#    'Gastric',
#    'Head and Neck',
#    'Kidney',
#    'Leukemias',
#    'Liver',
#    'Lung',
#    'Lymphomas',
#    'Melanoma',
#    'Multiple Myeloma',
#    'Ovarian',
#    'Pancreatic',
#    'Prostate',
#    'Soft-tissue',
#    'Testicular',
#    'Thyroid',
#    'Uterine'
#]

example_diseases = [
    '',
    'Breast',
    'Brain',
    'Leukemias',
    'Lung',
    'Lymphomas',
    'Multiple Myeloma',
]

phase = [
    '',
    'Phase 1',
    'Phase 2',
    'Phase 3'
]

study_results = [
    '',
    'Has Results',
    'No Results Available'
]

study_type = [
    '',
    'Interventional',
    'Observational'
]

funded_by = [
    '',
    'National Institute of Health',
    'Industry',
    'Other',
    'U.S. Fed'
]

st.markdown('#### [Insight Data Science Fellowship](https://www.insightdatascience.com/)')
st.markdown('#### Made by [Louise Giam](https://www.linkedin.com/in/louise-giam/)')
st.markdown('#### 2020A Health Data Science')

st.markdown('## Clinical Trial Insights')
st.markdown('---')

# model = pickle.load(open('model.pkl', 'rb'))  # get the model

# experience = st.number_input('Disease/Condition')
# phase = st.number_input('Phase')
#enroll = st.number_input('Enrollment')
#disease = st.selectbox('Disease', example_diseases)    

# phase = st.selectbox('Phase', phase)
sr = st.selectbox('Results?', study_results)
stype = st.selectbox('Study Type?', study_type)
fb_list = st.multiselect('Funded By?', funded_by)

# returns a list

# def file_selector(folder_path='.'):
#    filenames = os.listdir(folder_path)
#    selected_filename = st.selectbox('Select a file', filenames)
#    return os.path.join(folder_path, selected_filename)

# filename = file_selector()
# st.write('You selected `%s`' % filename)
sr = [sr]
stype = [stype]
z = []
fb_nih = fb_list.count('NIH')
fb_ind = fb_list.count('Industry')
fb_oth = fb_list.count('Other')
fb_fed = fb_list.count('U.S. Fed')
z.append([fb_nih, fb_ind, fb_oth, fb_fed])
z_df = pd.DataFrame(z, columns = ['NIH', 'Industry', 'Other', 'U.S. Fed'])

test2_df = pd.DataFrame({'Study Results': sr, 'Study Types': stype})

test3 = test2_df.join(z_df)

# int_features = [int(x) for x in features]		# fix
# final_features = [np.array(int_features)]		# fix
# X_test = pd.read_csv(filename)

m = pickle.load(open('model.pkl', 'rb'))
prediction = m.predict(test3)[0]
prob = m.predict_proba(test3)[0,0]

if st.button('Predict'):
    st.success("This trial will be: " + m.predict(test3)[0])
    st.success("The likelihood is: " + "{:,.2%}".format(prob))
