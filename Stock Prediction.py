#import required packages
import streamlit as st
from datetime import date
import pandas as pd

import yfinance as yf
from fbprophet import Prophet
from fbprophet.plot import plot_plotly
from plotly import graph_objs as go

#initializing start date
start = "2015-01-01"

#taking the current date in YYYY-MM-DD format
today = date.today().strftime("%Y-%m-%d")

st.title('Stock Forecast App')

#reading csv file with ticker symbols into a data frame
df = pd.read_csv(r'C:\Users\hansi\Desktop\Projects\stock_prediction_app\Yahoo-Finance-Ticker-Symbols.csv')
stocks = df
selected_stock = st.selectbox("Select stock for prediction", stocks)

#slider to determine number of years
n_years = st.slider("Years of prediction:", 1, 4)
period = n_years*365

@st.cache
#loading the data using yahoo finance
def load_data(ticker):
    data = yf.download(ticker, start, today)
    data.reset_index(inplace = True)
    return data

#text intimating that data is being loaded
data_load_state = st.text("Loading data...")

data = load_data(selected_stock)

#text intimating data is loaded
data_load_state.text("Loading data done!")

#showing the data
st.subheader('Raw Data')
st.write(data.tail())

#function to plot the raw data with a slider
def plot_raw_data():
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name='Opening Price'))
    fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name= 'Closing Price'))
    fig.layout.update(title_text="Time Series Data", xaxis_rangeslider_visible=True)
    st.plotly_chart(fig)

#plotting data
plot_raw_data()

#need to rename columns as ds and y for code to work
df_train = data[['Date', 'Close']]
df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})

#forecasting using fbprophet
m= Prophet()
m.fit(df_train)
future = m.make_future_dataframe(periods=period)
forecast = m.predict(future)

#showing forecasted data
st.subheader('Forecast Data')
st.write(forecast.tail())

#plotiing forecasted data
st.write('Forecast Data')
fig1 = plot_plotly(m, forecast)
st.plotly_chart(fig1)

#plotting different components of forecasted data
st.write('Forecast Components')
fig2 = m.plot_components(forecast)
st.write(fig2)
