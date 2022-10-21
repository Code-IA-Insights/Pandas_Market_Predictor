# Pandas Market Predictor

![Pandas Market Predictor](https://github.com/somkietacode/Pandas_Market_Predictor/blob/main/image/pmp.png?raw=true)

Pandas Market Predictor, is a deep learning API written in Python on top of Panda that helping you predict future price (low and min), trend of Financial market assets.


## About Pandas Market Predictor

Pandas Market Predictor , is a Technical Analysis API written in Python.
It was developed with a focus on enabling fast experimentation.
*Being able to go from idea to result as fast as possible is key to doing good research.*

Pandas Market Predictor is:

-   **Simple** 
-   **Flexible** 
-   **Powerful** 

## First contact with Pandas Market Predictor

The core data structures of Pandas Market Predictor are __Historical Market Data__ and __Technical Indicator__ .

A sample Data Set should be :

| Open | High | Low | Close  | Volume | Indicator1 | Indicator2 |
|-----:|------:|----:|-----:|-------:|-----------:|-----------:|
|0.93767|0.93791|0.93618|0.9363|69414.0|0.9363860952540013|0.9365316260340849|
|0.9363|0.93764|0.93566|0.93666|23461.0|0.936477396836001|0.9365549667551604|
|0.93666|0.93798|0.93561|0.93724|26907.0|0.9367315978906674|0.936679518254222|

You can build your data set by using Pandas-TA lib : https://github.com/twopirllc/pandas-ta


For installation run :

```
pip install Pandas-Market-Predictor
```

## About Feature

### I.Trend Detection

The trend detection purpose is to help you find the most probable Future Market Trend on basis of your indicator :

````python

from Pandas_Market_Predictor import Pandas_Market_Predictor
import pandas as pd


if __name__ == "__main__" :
  
  # Firt we read the specified data using pandas
  
  df = pd.read_csv('dataset.csv')
  df = df.dropna(axis=0) # Data cleaning
  
  # Create predictor
  
  MyMarketPredictor = Pandas_Market_Predictor(df)
  
  # Predict Trend
  Indicators = ["Indicator1","Indicator2"]
  TREND = MyMarketPredictor.Trend_Detection(Indicators,10)
  
  # 10 is the percentage of standard Deviation to detect
  print(MyMarketPredictor.PERCENT_STD) # Print the value of standard deviation percentage
  
  #Printing the result
  print("Buy Trend :",TREND['BUY'])
  print("Sell Trend :",TREND['SELL'])
  
````

Result :

```console
foo@bar:~$ python test.py
Buy Trend : 0
Sell Trend : 0

```

### II.The Support Resistance Estimation Tool

The Support Resistance Estimation Tool is as his name indicate permit to estimate the Low and High of an asset
The question is : What is the standard deviation for an up or down trend given the level of indicator that we have for the current period ?

````python
  Level = MyMarketPredictor.Support_Resistance_Estimation_Tool(Indicators)
  print("Support Level :",Level['Support'])
  print("Resistance Level :",Level['Resistance'])
````

Result :

```console
Support Level : 146.42515227768754
Resistance Level : 147.38794619755853

```
#### UPTREND EXEMPLE

![Pandas Market Predictor UP TREND EXEMPLE ](https://github.com/somkietacode/Pandas_Market_Predictor/blob/main/image/UPTREND.png?raw=true)

### III.The RISK MANAGEMENT TOOL

Even if you make very good prediction and having right 99% of time. The 1% Risk could append a day and reduce all your profit to néant so you
need to have a good risk reward management.

Risk is about 2 things :

#### 1. Determine at witch price your setup is invalide ?

````python
  
  # Risk Reward Ratio 1 / 3 mean i need to won 1 trade over 3 for being profitable
  
  RISK_REWARD_RATIO = 1 / 3
  
  # Stop Loss Calculation Exemple for Up & Down Trend
  
  Stop_Loss_Up = MyMarketPredictor.STOP_LOSS_CALCULATOR("UP",Level['Support'],Level['Resistance'],RISK_REWARD_RATIO ) # For Up Trend
  Stop_Loss_Down = MyMarketPredictor.STOP_LOSS_CALCULATOR("DOWN",Level['Support'],Level['Resistance'],RISK_REWARD_RATIO ) # For Up Down
  
  # Printing Result
  
  print("The Stop Loss Level for up Trend is", Stop_Loss_Up , "for",RISK_REWARD_RATIO ,"RISK_REWARD_RATIO" )
  print("The Stop Loss Level for down Trend is", Stop_Loss_Down , "for",RISK_REWARD_RATIO ,"RISK_REWARD_RATIO" )
````

```console
The Stop Loss Level for up Trend is 146.10422097106388 for 0.3333333333333333 RISK_REWARD_RATIO
The Stop Loss Level for down Trend is 147.7088775041822 for 0.3333333333333333 RISK_REWARD_RATIO

```

#### 2. Determine at witch price to exit ?

````python
  Trade_Efficiency_Factor = 1 - RISK_REWARD_RATIO
  Take_Profit_Up = MyMarketPredictor.Take_Profit_CALCULATOR("UP",Level['Support'],Level['Resistance'],Trade_Efficiency_Factor)
  Take_Profit_Down = MyMarketPredictor.Take_Profit_CALCULATOR("UP",Level['Support'],Level['Resistance'],Trade_Efficiency_Factor)
  print("The Take Profit Level for up Trend is", Take_Profit_Up , "for",Trade_Efficiency_Factor ,"Trade_Efficiency_Factor" )
  print("The Take Profit Level for down Trend is", Take_Profit_Down , "for",Trade_Efficiency_Factor ,"Trade_Efficiency_Factor" )
````

```console
The Take Profit Level for up Trend is 147.06701489093487 for 0.6666666666666667 Trade_Efficiency_Factor
The Take Profit Level for down Trend is 147.06701489093487 for 0.6666666666666667 Trade_Efficiency_Factor
```

---
## Support

You can ask questions and join the development discussion:

- [Facebook page](https://www.facebook.com/globalanalysistech) .

---
