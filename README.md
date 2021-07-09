# Stock-Prediction-Web-App  

This is a web app that predicts stock prices using the time series analysis of fbprophet/prophet. The ticker symbols for various stocks are in the csv file. Historical data of stocks is accessed using yfinance. The web app is created using streamlit and is deployed on Heroku.  

- Pre-requisites
  - **fbprophet**: Prophet is a procedure for forecasting time series data based on an additive model where non-linear trends are fit with yearly, weekly, and daily seasonality
  - **streamlit**: Python framework for turning data scripts into web apps
  - **pandas**: Open source data analysis and manipulation tool
  - **yfinance**: For downloading historical market data from Yahoo! finance
  - **plotly**: Data visualization tool for plotting graphs
  - **pystan**: To perform statistical modelling (Not used directly in this code; is a pre-requisite for using fbprophet) 
 
- Notes
  - If you're running this code on a windows system, fbprophet will not work with CMD if you don't have gcc. The only way around this is using Anaconda Powershell Prompt to run the code. 
  - The version of fbprophet being used must be greater than of equal to 0.5. fbprophet.plot does not work with versions less than 0.5.  
