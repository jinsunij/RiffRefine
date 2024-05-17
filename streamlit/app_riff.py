import streamlit as st
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV

# Add a title
st.title("How much listens is your song going to reach?")

# Import the dataset
df = pd.read_csv("data_with_target.csv")

# Error handling for model loading
try:
    with open('final_model.pkl', 'rb') as file:
        xgb = joblib.load(file)
except Exception as e:
    st.error(f"Error loading the model: {e}")
    xgb = None

# Check if the model loaded successfully
st.sidebar.header("**Select the metrics for your song**")
if xgb:
    # Add an interactive sidebar
    genre = st.sidebar.selectbox("Wich is your genre?", df["track_genre_top"].unique())
    track_bit_rate = st.sidebar.selectbox("How is the bit rate?", df["track_bit_rate"].unique())
    track_duration = st.sidebar.slider("How long is the duration of your song in sec?", min_value=60, max_value=600)
    album_inf_bin = st.sidebar.selectbox("Do you have information about your album? (YES=1 / No= 0)", df["album_information_bin"].unique())
    album_tracks = st.sidebar.selectbox("How much album tracks?", df["album_tracks"].unique())
    artist_bio_bin = st.sidebar.selectbox("Do you have biographie? (YES=1 / No= 0)", df["artist_bio_bin"].unique())
    track_title_char_count = st.sidebar.selectbox("How much characters do has your song title?", df["track_title_char_count"].unique())
    #track_title_char_count = st.sidebar.slider("How much characters do has your song title?", min_value=60, max_value=600)
    track_number = st.sidebar.selectbox("How much tracks do you have?", df["track_number"].unique())
    license_category = st.sidebar.selectbox("Which license category?", df["license_category"].unique())
    website = st.sidebar.selectbox("Do you have a Website?", df["other_website"].unique())
    soundcloud_website = st.sidebar.selectbox("Do you have a Websites by Soundcloud?", df["soundcloud_website"].unique())
    number_of_genres_bins = st.sidebar.selectbox("How is the genre bins?", df["number_of_genres_bins"].unique())

    # Create a dictionary with user input
    user_input = {
        'track_genre_top': genre,
        'track_bit_rate': track_bit_rate,
        'track_duration': track_duration,
        'album_information_bin': album_inf_bin,
        'album_tracks': album_tracks,
        'artist_bio_bin': artist_bio_bin,
        'track_title_char_count': track_title_char_count,
        'track_number': track_number,
        'license_category': license_category,
        'other_website': website,
        'soundcloud_website': soundcloud_website,
        'number_of_genres_bins': number_of_genres_bins,
    }

    # Convert user input to a DataFrame
    user_input_df = pd.DataFrame([user_input])
    user_input_df['track_genre_top'] = user_input_df['track_genre_top'].astype('category')
    user_input_df['number_of_genres_bins'] = user_input_df['number_of_genres_bins'].astype('category')
    user_input_df['license_category'] = user_input_df['license_category'].astype('category')

    # Display user input fields in columns
    st.write("**Your Input:**")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"- <span style='color: teal'>**Genre:**</span> {genre}", unsafe_allow_html=True)
        st.markdown(f"- <span style='color: teal'>**Bit Rate:**</span> {track_bit_rate}", unsafe_allow_html=True)
        st.markdown(f"- <span style='color: teal'>**Duration:**</span> {track_duration} seconds", unsafe_allow_html=True)
        st.markdown(f"- <span style='color: teal'>**Album Information Bin:**</span> {album_inf_bin}", unsafe_allow_html=True)
        st.markdown(f"- <span style='color: teal'>**Album Tracks:**</span> {album_tracks}", unsafe_allow_html=True)
        st.markdown(f"- <span style='color: teal'>**Artist Bio Bin:**</span> {artist_bio_bin}", unsafe_allow_html=True)
    with col2:
        st.markdown(f"- <span style='color: teal'>**Title Character Count:**</span> {track_title_char_count}", unsafe_allow_html=True)
        st.markdown(f"- <span style='color: teal'>**Track Number:**</span> {track_number}", unsafe_allow_html=True)
        st.markdown(f"- <span style='color: teal'>**License Category:**</span> {license_category}", unsafe_allow_html=True)
        st.markdown(f"- <span style='color: teal'>**Website:**</span> {website}", unsafe_allow_html=True)
        st.markdown(f"- <span style='color: teal'>**Soundcloud Website:**</span> {soundcloud_website}", unsafe_allow_html=True)
        st.markdown(f"- <span style='color: teal'>**Genres Bins:**</span> {number_of_genres_bins}", unsafe_allow_html=True)

    # Make predictions
    prediction = xgb.predict(user_input_df)
    

    # Streamlit UI
    if st.button('Predict'):
        #st.write('Prediction of potential listens bins:', prediction)
        if prediction == 1:
            st.write('You might have up to 1250 listens!')
        if prediction == 2:
            st.write('You might have a range between 1251 - 2500 listens!')
        if prediction == 3:
            st.write('You might have a range between 2501 - 5000 listens!')
        if prediction == 4:
            st.write('You might have more than 5000 listens!')
    else:
        st.markdown("<span style='color: teal'>**Thanks for using our system - RiffRefine **</span>", unsafe_allow_html=True)

#else:
    #st.write('Error: Model not loaded or fitted.')

    