import pickle
import numpy as np
import pandas as pd
import streamlit as st
from healthinsurance import HealthInsurance


st.title('Prospects Ranker - To prioratize sales efforts!!!')

st.header("Drag your data here!!!")

uploaded_file = st.file_uploader("Drop your sales prospects for today here!!!")
if  uploaded_file is not None:
    
    # Loading data.
    @st.cache
    data = pd.read_csv(uploaded_file).drop('Unnamed: 0', axis=1)

    # Preprocessing data
    pp = HealthInsurance()
    data_transformed = pp.fit_transform(data)


    # Load Model
    model = pickle.load()

    #st.dataframe(data)