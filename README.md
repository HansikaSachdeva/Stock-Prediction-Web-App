# Stock-Prediction-Web-App  

This is a web app that predicts stock prices using the time series analysis of fbprophet/prophet. The ticker symbols for various stocks are in the csv file. Historical data of stocks is accessed using yfinance. The web app is created using streamlit and is deployed on Heroku.  

- Pre-requisites
  - fbprophet
  - streamlit
  - pandas
  - yfinance
  - plotly
  - pystan 
 
- Notes
  - If you're running this code on a windows system, fbprophet will not work with CMD if you don't have gcc. The only way around this is using Anaconda Powershell Prompt to run the code. 
  - The version of fbprophet being used must be greater than of equal to 0.5. fbprophet.plot does not work with versions less than 0.5.  
