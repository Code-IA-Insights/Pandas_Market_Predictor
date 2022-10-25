from Artificial_Neural_Network_Classifier import artificialneuralnetwork_classifier as ANNC
from Auto_Gradient_Boosting import AGB
import pandas as pd
import numpy as np


class Pandas_Market_Predictor :
  
  def __init__(self,dataset):
    
    self.dataset = dataset
    
  def Trend_Detection(self,indicator_list,STD_Quotient):
      GAMA = self.dataset.std()['Close'] / STD_Quotient
      deriv = self.dataset['Close'].iloc[1:] - self.dataset['Close'].iloc[:-1].values
      self.dataset['buy'] = (deriv > GAMA) * 1
      self.dataset['sell'] = (deriv < (-1 * GAMA)) * 1
      
      # Train the model
      
      x = np.matrix(self.dataset.iloc[1:-1 , :][indicator_list].to_numpy() , dtype=np.float64)
      y1 = np.matrix(self.dataset.iloc[1:-1 , :][['buy']].to_numpy() , dtype=np.int32 )
      y2 = np.matrix(self.dataset.iloc[1:-1 , :][['sell']].to_numpy(), dtype=np.int32)
      NEURONES_BUY = ANNC(x,y1)
      NEURONES_SELL = ANNC(x,y2)
      
      # Return Prediction
      
      SIGNAL = np.matrix( self.dataset.tail(1)[indicator_list].to_numpy() )
      
      return {
        
        "BUY" : int(NEURONES_BUY.predict(SIGNAL)),
        "SELL" : int(NEURONES_SELL.predict(SIGNAL))
      
      }


  def Support_Resistance_Estimation_Tool(self,indicator_list):
    
    x = np.matrix(self.dataset.iloc[1:-1 , :][indicator_list].to_numpy(),dtype=np.float32)
    self.dataset['support_distance'] = self.dataset['Close'].iloc[:-1] - self.dataset['Low'].iloc[1:].values
    self.dataset['resistance_distance'] = self.dataset['High'].iloc[1:].values - self.dataset['Close'].iloc[:-1]
    
    y1 = np.matrix(self.dataset.iloc[1:-1 , :][['support_distance']].to_numpy(), dtype=np.float32)
    y2 = np.matrix(self.dataset.iloc[1:-1 , :][['resistance_distance']].to_numpy(), dtype=np.float32) 
    
    Lr_support = AGB(x,y1,0.01)
    Lr_resistance = AGB(x,y2,0.01)
    
    SIGNAL = np.matrix( self.dataset.tail(1)[indicator_list].to_numpy() , dtype=np.float64)
    
    S = self.dataset.tail(1)['Close'].values[0] - Lr_support.predict(SIGNAL)
    R = self.dataset.tail(1)['Close'].values[0] + Lr_resistance.predict(SIGNAL)
    
    return {
      "Support" :  S,
      "Resistance" : R
    }
    
    
  def STOP_LOSS_CALCULATOR(self,Trend,S,R,RISK_REWARD_RATIO):
    
    DEVIATION = R - S
    if Trend == "UP" :
      STOP_LOSS = S - (DEVIATION * RISK_REWARD_RATIO)
    if Trend == "DOWN" :
      STOP_LOSS = R + (DEVIATION * RISK_REWARD_RATIO)
    
    return STOP_LOSS


  def Take_Profit_CALCULATOR(self,Trend,S,R,Trade_Efficiency_Factor):
    
    DEVIATION = R - S
    if Trend == "UP" :
      TAKE_PROFIT = S + (DEVIATION * Trade_Efficiency_Factor)
    if Trend == "DOWN" :
      TAKE_PROFIT = R - (DEVIATION * Trade_Efficiency_Factor)
    
    return TAKE_PROFIT
    
      


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
      
