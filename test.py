from Pandas_Market_Predictor import Pandas_Market_Predictor
import pandas as pd


if __name__ == "__main__" :

  df = pd.read_csv('dataset.csv')
  df = df.dropna(axis=0)
  MyMarketPredictor = Pandas_Market_Predictor(df)
  TREND = MyMarketPredictor.Trend_Detection(["Indicator1","Indicator2"],10)
  print("Buy Trend :",TREND['BUY'])
  print("Sell Trend :",TREND['SELL'])
