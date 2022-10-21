from .pmp import Pandas_Market_Predictor
import pandas as pd
import numpy as np

if __name__ == "__main__" :
  
  dataset = pd.read_csv('dataset.csv')
  MyMarketPredictor = Pandas_Market_Predictor(dataset)
  TREND = MyMarketPredictor.Trend_Detection(["INDICATOR1","INDICATOR2"],10)
  print("Buy Trend :",TREND['BUY'])
  print("Sell Trend :",TREND['SELL'])
  
