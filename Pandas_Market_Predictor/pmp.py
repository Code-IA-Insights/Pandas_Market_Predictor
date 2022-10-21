from Artificial_Neural_Network_Classifier import artificialneuralnetwork_classifier as ANNC
import panda as pd
import numpy as np


class Pandas_Market_Predictor :
  
  def __init__(self,dataset):
    
    self.dataset = dataset
    
  def Trend_Detection(self,indicator_list,STD_Quotient):
      
      GAMA = dataset.std()['Close'] / STD_Quotient
      deriv = dataset['Close'].iloc[1:] - dataset['Close'].iloc[:-1].values
      dataset['buy'] = (deriv > GAMA) * 1
      dataset['sell'] = (deriv < (-1 * GAMA)) * 1
      
      # Train the model
      
      SIGNALS = np.matrix(dataset[indicator_list].to_numpy())
      SHALLBUY = np.matrix(dataset['buy'].to_numpy())
      SHALLSELL = np.matrix(dataset['sell'].to_numpy())
      NEURONES_BUY = ANNC(SIGNALS,SHALLBUY)
      NEURONES_SELL = ANNC(SIGNALS,SHALLSELL)
      
      # Return Prediction
      
      SIGNAL = np.matrix( dataset.tail(1)[indicator_list].to_numpy() )
      
      return {
        
        "BUY" : NEURONES_BUY.predict(SIGNAL),
        "SELL" : NEURONES_SELL.predict(SIGNAL)
      
      }
      


if __name__ == "__main__" :
  
  dataset = pd.read_csv('dataset.csv')
  MyMarketPredictor = Pandas_Market_Predictor(dataset)
  TREND = MyMarketPredictor.Trend_Detection(["Indicator1","Indicator2"],10)
  print("Buy Trend :",TREND['BUY'])
  print("Sell Trend :",TREND['SELL'])
