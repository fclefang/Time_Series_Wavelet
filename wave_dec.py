import pandas as pd
# # from pandas import read_csv
# import pywt

dataframe = pd.read_csv('foshan.csv', usecols=[1], engine='python', encoding='utf-8')
dataset = dataframe.values

import numpy as np
import matplotlib.pyplot as plt
import pywt
x = dataset[:960,0]
plt.plot(x)
plt.show()
db1 = pywt.Wavelet('db4')
# level = pywt.dwt_max_level(len(x), db1)
cA7,cD7,cD6,cD5,cD4,cD3,cD2,cD1 = pywt.wavedec(x, db1, mode='constant', level=7)
plt.plot(cD1)
plt.show()
plt.plot(cD2)
plt.show()
plt.plot(cD3)
plt.show()
plt.plot(cD4)
plt.show()
plt.plot(cD5)
plt.show()
plt.plot(cD6)
plt.show()
plt.plot(cD7)
plt.show()
# plt.plot(cD8)
# plt.show()