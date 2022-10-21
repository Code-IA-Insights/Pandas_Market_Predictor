from Artificial_Neural_Network_Classifier import artificialneuralnetwork_classifier as ANNC
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
      print(self.dataset)
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
      


if __name__ == "__main__" :
  
  df = pd.read_csv('EURJPY.csv')
  df = df.dropna(axis=0)
  MyMarketPredictor = Pandas_Market_Predictor(df)
  TREND = MyMarketPredictor.Trend_Detection(["Indicator1","Indicator2"],10)
  print("Buy Trend :",TREND['BUY'])
  print("Sell Trend :",TREND['SELL'])
