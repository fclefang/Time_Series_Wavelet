import pandas as pd
# # from pandas import read_csv
# import pywt

dataframe = pd.read_csv('huarui_5min.csv', usecols=[1], engine='python', encoding='utf-8')
dataset = dataframe.values

import numpy as np
import matplotlib.pyplot as plt
import pywt
x = dataset[40:550,0]
plt.plot(x)
plt.show()
db1 = pywt.Wavelet('db4')
# level = pywt.dwt_max_level(len(x), db1)
cA2,cD2,cD1 = pywt.wavedec(x, db1, mode='constant', level=2)
plt.plot(cD1)
plt.show()
plt.plot(cD2)
plt.show()
# plt.plot(cD3)
# plt.show()
# plt.plot(cD4)
# plt.show()
plt.plot(cA2)
plt.show()
# plt.plot(cD6)
# plt.show()
# plt.plot(cD7)
# plt.show()
# plt.plot(cD8)
# plt.show()