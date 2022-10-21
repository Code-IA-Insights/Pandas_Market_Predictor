from Pandas_Market_Predictor import Pandas_Market_Predictor
import pandas as pd


if __name__ == "__main__" :

  df = pd.read_csv('dataset.csv')
  df = df.dropna(axis=0)
  MyMarketPredictor = Pandas_Market_Predictor(df)
  TREND = MyMarketPredictor.Trend_Detection(["Indicator1","Indicator2"],10)
  print("Buy Trend :",TREND['BUY'])
  print("Sell Trend :",TREND['SELL'])
  Level = MyMarketPredictor.Support_Resistance_Estimation_Tool(["Indicator1","Indicator2"])
  print("Support Level :",Level['Support'])
  print("Resistance Level :",Level['Resistance'])
  
  RISK_REWARD_RATIO = 1 / 3
  Stop_Loss_Up = MyMarketPredictor.STOP_LOSS_CALCULATOR("UP",Level['Support'],Level['Resistance'],RISK_REWARD_RATIO ) # For Up Trend
  Stop_Loss_Down = MyMarketPredictor.STOP_LOSS_CALCULATOR("DOWN",Level['Support'],Level['Resistance'],RISK_REWARD_RATIO ) # For Up Down
  print("The Stop Loss Level for up Trend is", Stop_Loss_Up , "for",RISK_REWARD_RATIO ,"RISK_REWARD_RATIO" )
  print("The Stop Loss Level for down Trend is", Stop_Loss_Down , "for",RISK_REWARD_RATIO ,"RISK_REWARD_RATIO" )

  Trade_Efficiency_Factor = 1 - RISK_REWARD_RATIO
  Take_Profit_Up = MyMarketPredictor.Take_Profit_CALCULATOR("UP",Level['Support'],Level['Resistance'],Trade_Efficiency_Factor)
  Take_Profit_Down = MyMarketPredictor.Take_Profit_CALCULATOR("UP",Level['Support'],Level['Resistance'],Trade_Efficiency_Factor)
  print("The Take Profit Level for up Trend is", Take_Profit_Up , "for",Trade_Efficiency_Factor ,"Trade_Efficiency_Factor" )
  print("The Take Profit Level for down Trend is", Take_Profit_Down , "for",Trade_Efficiency_Factor ,"Trade_Efficiency_Factor" )
