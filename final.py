# Importing necessary libraries
import pickle
import streamlit as st
import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt

# Importing necessary data
co2Arima = pd.read_excel(r"C:\Users\lenovo\Downloads\CO2 dataset.xlsx",parse_dates=['Year'])
co2Arima.set_index(['Year'],inplace=True)

with open(r"C:\Users\lenovo\Downloads\arima_results.pkl", 'rb') as f:
    results5 = pickle.load(f)

# User_Inputs :

start_button = st.slider('Start Year', min_value=1800, max_value=2014, step=10, value=2000)
end_button = st.slider('End Year', min_value=2015, max_value=2030, step=1, value=2030)

# User-Defined function for prediction and plotting of data

def co2_predictions(start_year, end_year, results):
    forecast = []
    for year in range(start_year, end_year+1):
        forecast.append(results.predict(pd.to_datetime(str(year)), pd.to_datetime(str(year)), typ='levels')[0])

    forecast_df = pd.DataFrame({'Year': pd.date_range(start=str(start_year), end=str(end_year), freq='AS'), 'CO2': forecast})
    forecast_df.set_index('Year', inplace=True)

    fig, ax = plt.subplots()
    ax.plot(co2Arima.loc['1800-01-01':,'CO2'], label='Actual')
    forecast_df.plot(ax=ax, label='Predicted')
    plt.legend()
    st.pyplot(fig)

    st.write(forecast_df)

if st.button('Generate Predictions and Plot'):
    co2_predictions(start_button, end_button, results5)
