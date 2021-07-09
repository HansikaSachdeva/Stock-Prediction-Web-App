</p>

<h2 align="center"> Stock Prediction Web App </h2>
<h4 align="center"> This is a web app that predicts stock prices using the time series analysis of fbprophet/prophet. The ticker symbols for various stocks are in the csv file. Historical data of stocks is accessed using yfinance. The web app is created using streamlit and is deployed on Heroku.  
 <h4>

## Demo - [Link](https://stock-prediction-web-app.herokuapp.com/)

## Features
- Select or type the symbol of stock to see the historical and forecast data of over 106000 stocks from various countries like India, USA, France, Germany, etc
- Use a slider to choose years of prediction, from 1 to 4
- Use a slider to focus on certain parts of the graphs
- Forecast components to better analyze stocks


## Built Using

- fbprophet (>=0.5)
- streamlit
- pandas
- plotly
- yfinance
- pystan

## Screenshots
![image](https://user-images.githubusercontent.com/52819652/125070394-84775100-e0d5-11eb-8dca-9325b18d1f89.png)
![image](https://user-images.githubusercontent.com/52819652/125070712-f94a8b00-e0d5-11eb-8ec2-d906c2dff650.png)
![image](https://user-images.githubusercontent.com/52819652/125070795-11baa580-e0d6-11eb-9e66-e8b46ca90cf3.png)
![image](https://user-images.githubusercontent.com/52819652/125070856-25660c00-e0d6-11eb-8c5b-96ef16c6a791.png)


## Instructions to run

- Pre-requisites:

  - **fbprophet**: Prophet is a procedure for forecasting time series data based on an additive model where non-linear trends are fit with yearly, weekly, and daily seasonality
  - **streamlit**: Python framework for turning data scripts into web apps
  - **pandas**: Open source data analysis and manipulation tool
  - **yfinance**: For downloading historical market data from Yahoo! finance
  - **plotly**: Data visualization tool for plotting graphs
  - **pystan**: To perform statistical modelling (Not used directly in this code; is a pre-requisite for using fbprophet) 

- Directions to install

```bash
pip install streamlit, pandas, plotly, yfinance, pystan  
pip install fbprophet
```

- Directions to execute  
  - If you're running this code on a windows system, fbprophet will not work with CMD if you don't have gcc. The only way around this is using Anaconda Powershell Prompt to run the code. 
```bash
streamlit run app_name.py
```

<!-- LICENSE -->  

## License

Distributed under the MIT License. See `LICENSE` for more information.  


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request  
