from Artificial_Neural_Network_Classifier import artificialneuralnetwork_classifier as ANNC
from Awesome_Linear_Regression import linearregression as LR
import pandas as pd
import numpy as np


class Pandas_Market_Predictor :
  
  def __init__(self,dataset):
    
    self.dataset = dataset
    
  def Trend_Detection(self,indicator_list,STD_Quotient):
      GAMA = self.dataset.std()['Close'] / STD_Quotient
      self.PERCENT_STD = GAMA
      deriv = self.dataset['Close'].iloc[1:] - self.dataset['Close'].iloc[:-1].values
      self.dataset['buy'] = (deriv > GAMA) * 1
      self.dataset['sell'] = (deriv < (-1 * GAMA)) * 1
      
      # Train the model
      
      x = np.matrix(self.dataset.iloc[1:-1 , :][indicator_list].to_numpy())
      y1 = np.matrix(self.dataset.iloc[1:-1 , :][['buy']].to_numpy())
      y2 = np.matrix(self.dataset.iloc[1:-1 , :][['sell']].to_numpy())
      NEURONES_BUY = ANNC(x,y1)
      NEURONES_SELL = ANNC(x,y2)
      
      # Return Prediction
      
      SIGNAL = np.matrix( self.dataset.tail(1)[indicator_list].to_numpy() )
      
      return {
        
        "BUY" : int(NEURONES_BUY.predict(SIGNAL)),
        "SELL" : int(NEURONES_SELL.predict(SIGNAL))
      
      }
    
   def Support_Resistance_Estimation_Tool(self,indicator_list):
    
    x = np.matrix(self.dataset.iloc[1:-1 , :][indicator_list].to_numpy())
    df['support_distance'] = df['Close'].iloc[:-1] - df['Low'].iloc[1:].values
    df['resistance_distance'] = df['High'].iloc[1:].values - df['Close'].iloc[:-1]
    
    y1 = np.matrix(self.dataset.iloc[1:-1 , :][['support_distance']].to_numpy())
    y2 = np.matrix(self.dataset.iloc[1:-1 , :][['resistance_distance']].to_numpy()) 
    
    Lr_support = LR(x,y1)
    BetaS, rssS = Lr_support.leastsquare()
    Lr_resistance = LR(x,y2)
    BetaR, rssR = Lr_resistance.leastsquare()
    
    SIGNAL = np.matrix( self.dataset.tail(1)[indicator_list].to_numpy() )
    
    S = self.dataset.tail(1)['Close'] - Lr_support.predict(SIGNAL)
    R = self.dataset.tail(1)['Close'] + Lr_resistance.predict(SIGNAL)
    
    return {
      "Support" :  S,
      "Resistance" : R
    }
    
    
    
      


if __name__ == "__main__" :
  
  df = pd.read_csv('dataset.csv')
  df = df.dropna(axis=0)
  MyMarketPredictor = Pandas_Market_Predictor(df)
  TREND = MyMarketPredictor.Trend_Detection(["Indicator1","Indicator2"],10)
  print("Buy Trend :",TREND['BUY'])
  print("Sell Trend :",TREND['SELL'])
  Level = MyMarketPredictor.Support_Resistance_Estimation_Tool(["Indicator1","Indicator2"])
  print("Support Level :",Level['Support'])
  print(" Resistance Level :",Level['Resistance'])
