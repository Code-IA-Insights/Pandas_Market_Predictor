from Artificial_Neural_Network_Classifier import artificialneuralnetwork_classifier
import panda as pd


class Pandas_Market_Predictor :
  
  def __init__(self,dataset):
    
    self.dataset = dataset
    
    def Trend_Detection():
      
      GAMA = dataset.std()['Close'] / 10
      deriv = dataset['close'].iloc[1:] - dataset['close'].iloc[:-1].values
      dataset['buy'] = (deriv > GAMA) * 1
      dataset['sell'] = (deriv < (-1 * GAMA)) * 1
      
      
    
  
