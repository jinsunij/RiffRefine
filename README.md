<img src="https://github.com/jinsunij/RiffRefine/blob/main/images/riffrefine.png?raw=true" width="270">



# RiffRefine: Leverage your Music!

This project uses metadata and features of audio data to predict the number of listens for a new song. The model is developed so it integrates to an app that allows artists to receive feedback on their song. This should enable upcoming artists, with small budget and lack of equipment, to get a first feedback on their newest creative work and hint at how they can reach a greater audience.



# Setup
 

We started this project from scratch and it requires several dependencies, which we have listed in `requirements.txt` files. To ensure that the project runs correctly, we recommend that you set up a virtual environment before installing the dependencies.

To create a virtual environment, follow these steps:

1. Install `pyenv` to manage your Python versions. You can follow the instructions for your specific operating system on the [pyenv GitHub page](https://github.com/pyenv/pyenv#installation). In the terminal or command prompt, navigate to the project directory and run the command `pyenv local 3.11.3`. This sets the Python version for the current directory to 3.11.3.

2. Create a new virtual environment by running the command `python -m venv .venv`. Activate the virtual environment by running the command `source .venv/bin/activate` on Linux/Mac or `.\\venv\\Scripts\\activate` on Windows.

3. Upgrade `pip` to the latest version by running the command `pip install --upgrade pip`.




# Installation

To install and run this project, follow these steps:

1. Clone this repository to your local machine.

2. Install the required libraries by running `pip install -r requirements.txt` in your terminal.

3. Download the datasets **`fma_metadata.zip`** (342 MiB) and  **`fma_small.zip`** (7.2 GiB) from [FMA: A Dataset For Music Analysis](https://github.com/mdeff/fma#data).

4. Unzip both datasets into the `data` folder.


# Notebooks Overview - WIP

* Domain Knowledge about the project
  * 'cleaned up word doc'
  * this notebook shows first first iteration of knowledge gathering in domain area: audio features, librosa
  * includes short description on meaning of audio features

* Data cleaning
  * 'data_cleaning'
  * notebook to preprocess raw data and merge the csv's from **`fma_metadata`** into one dataframe

* Baseline model
  * 'baseline_model'
  * this notebook transforms target variable (track_listens) to be used for our multi-class classification models 
  * performs a first baseline model with the Cohen's kappa performance metric 

* EDA
  * 'eda_metadata' tbd
  * short description
  * 'eda_audiofeatures' tbd
  * short description

* Modeling and Error Analysis:
  * 'final_model'
  * Notebook to preprocess raw data and compile all sequences into one dataset 


* Feature Importance (SHAP): 
  * 'SHAP'
  * short description


* ...



# Conclusion

The prediction model developed in this project has the potential to open up untouched area of 'Fame Prediction' within the field of Music Information Retrieval (MIR).
The integration of this model into an app has the potential to provide a tool that can be used by low-budget musicians as a feedback loop. 

We acknowledge that music as a form of art and culture is very complex. Thus, a next step for the project is to conduct the analysis on recently released tracks, as trends play a major role in the music industry.
A deeper dive into understanding the audio features to be used in machine learning algorithms can also be interesting. Feeding alternative audio representations of a track into a convolutional neural networks, such as spectrograms, might lead to more importance to the audio features in predicting the amount of listens for a new song.

MIR has received growing interest in the past years. With significant technical improvements in audio signal processing (e.g. Librosa) and machine learning, the potential is large, making this an appealing and promising project for the advancement of the whole field.


# Contributing

We welcome contributions from everyone. Here are some ways you can contribute:

- **Report a bug:** If you find a bug in the application, please open an issue on our GitHub repository.
- **Suggest an enhancement:** If you have an idea for a new feature or improvement, please open an issue on our GitHub repository.
- **Contribute code:** If you would like to contribute code to the project, please follow these steps:
  1. Fork the repository
  2. Create a new branch with a descriptive name (`git checkout -b my-new-feature`)
  3. Write your code and tests for your new feature or bug fix
  4. Commit your changes (`git commit -am 'Add some feature'`)
  5. Push to the branch (`git push origin my-new-feature`)
  6. Open a pull request on our GitHub repository

Thank you for your interest in contributing to our project!
