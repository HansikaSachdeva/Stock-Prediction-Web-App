#streamlit run stock.py
import streamlit as st
from datetime import date
import pandas as pd
import datetime

import yfinance as yf
from fbprophet import Prophet
from fbprophet.plot import plot_plotly
from plotly import graph_objs as go

start = "2015-01-01"
today = date.today().strftime("%Y-%m-%d")

st.title('Stock Forecast App')
#stocks = ('RANBAXY', 'RANEENGINE', 'RANEHOLDIN', 'RATNAMANI')
df = pd.read_csv(r'C:\Users\hansi\Desktop\Projects\stock_prediction_app\Yahoo-Finance-Ticker-Symbols.csv')
stocks = df
selected_stock = st.selectbox("Select stock for prediction", stocks)

n_years = st.slider("Years of prediction:", 1, 4)
period = n_years*365

@st.cache
def load_data(ticker):
    data = yf.download(ticker, start, today)
    data.reset_index(inplace = True)
    return data

data_load_state = st.text("Loading data...")
data = load_data(selected_stock)
data_load_state.text("Loading data done!")

st.subheader('Raw Data')
st.write(data.tail())

def plot_raw_data():
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name='Opening Price'))
    fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name= 'Closing Price'))
    fig.layout.update(title_text="Time Series Data", xaxis_rangeslider_visible=True)
    st.plotly_chart(fig)

plot_raw_data()

df_train = data[['Date', 'Close']]
df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})

m= Prophet()
m.fit(df_train)
future = m.make_future_dataframe(periods=period)
forecast = m.predict(future)

st.subheader('Forecast Data')
st.write(forecast.tail())

st.write('Forecast Data')
fig1 = plot_plotly(m, forecast)
st.plotly_chart(fig1)

st.write('Forecast Components')
fig2 = m.plot_components(forecast)
st.write(fig2)
