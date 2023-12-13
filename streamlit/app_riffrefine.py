import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pickle
import sklearn as skl
import sklearn.utils, sklearn.preprocessing, sklearn.decomposition, sklearn.svm

RSEED=42

# Add a title
st.title("How much listens is your song going to reach?")

# Import the dataset
df = pd.read_csv("data_with_target.csv")

#our model
from xgboost import XGBClassifier
xgb = XGBClassifier(random_state=RSEED, tree_method="hist",max_depth=5,gamma=1.0,learning_rate=0.1,reg_lambda=2,scale_pos_weight=1,n_estimators=75)

with open('final_model.pkl', 'wb') as file:
    pickle.load(file)

# Check if the model loaded successfully
st.sidebar.header("**Select the metrics for your song**")
if xgb:
    # Add an interactive sidebar
    genre = st.sidebar.selectbox("Wich is your genre?", df["track_genre_top"].unique())
    album_tracks = st.sidebar.selectbox("How much album tracks?", df["album_tracks"].unique())
    track_bit_rate = st.sidebar.selectbox("How is the bit rate?", df["track_bit_rate"].unique())
    track_duration = st.sidebar.slider("How long is the duration of your song?", min_value=60, max_value=600, value=60)
    track_license = st.sidebar.checkbox('Do you have a track license?')

    # Create a dictionary with user input
    user_input = {
        'genre': genre,
        'album_tracks': album_tracks,
        'track_bit_rate': track_bit_rate,
        'track_duration': track_duration,
        'track_license': track_license
    }

    # Convert user input to a DataFrame
    user_input_df = pd.DataFrame([user_input])

    # Make predictions
    prediction = xgb.predict(user_input_df)

    # Streamlit UI
    if st.button('Predict'):
        st.write('Prediction:', prediction)
else:
    st.write('Error: Model not loaded or fitted.')