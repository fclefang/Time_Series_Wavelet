import numpy as np 
import matplotlib as plt 
import pandas as pd
# from pandas import read_csv
import pywt

dataframe = pd.read_csv('huarui_5min.csv', usecols=[1], engine='python', encoding='utf-8')
dataset = dataframe.values
print(dataset[:,0])
coef, freqs=pywt.cwt(dataset[:,0],np.arange(1,129),'cmor')
# w = pywt.Wavelet("cmor")
# A2,D2,D1 = pywt.wavedec(dataset[:,0],'haar',mode='sym',level=2)
# coeff = [A2,D2,D1]
print(coef,freqs)
print(len(coef))