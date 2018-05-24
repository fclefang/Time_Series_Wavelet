# import numpy as np 
# import matplotlib as plt 
# import pandas as pd
# # from pandas import read_csv
# import pywt

# dataframe = pd.read_csv('huarui_5min.csv', usecols=[1], engine='python', encoding='utf-8')
# dataset = dataframe.values
# print(dataset[:,0])
# coef, freqs=pywt.cwt(dataset[:288,0],np.arange(1,129),'cmor')
# # w = pywt.Wavelet("cmor")
# # A2,D2,D1 = pywt.wavedec(dataset[:,0],'haar',mode='sym',level=2)
# # coeff = [A2,D2,D1]
# # print(coef,freqs)
# print(len(coef[0]))
# print(coef[0])
#--------------------------------------

import numpy as np
import matplotlib.pyplot as plt
import pywt

time, sst = pywt.data.nino()
dt = time[1] - time[0]
print(time,sst)
plt.plot(sst)
plt.show()
# Taken from http://nicolasfauchereau.github.io/climatecode/posts/wavelet-analysis-in-python/
wavelet = 'cmor'
scales = np.arange(1, 128)
print(scales)
[cfs, frequencies] = pywt.cwt(sst, scales, wavelet, dt)
power = (abs(cfs)) ** 2

period = 1. / frequencies
levels = [0.0625, 0.125, 0.25, 0.5, 1, 2, 4, 8]
f, ax = plt.subplots(figsize=(15, 10))
ax.contourf(time, np.log2(period), np.log2(power), np.log2(levels),
            extend='both')

ax.set_title('%s Wavelet Power Spectrum (%s)' % ('Nino1+2', wavelet))
ax.set_ylabel('Period (years)')
Yticks = 2 ** np.arange(np.ceil(np.log2(period.min())),
                        np.ceil(np.log2(period.max())))
ax.set_yticks(np.log2(Yticks))
ax.set_yticklabels(Yticks)
ax.invert_yaxis()
ylim = ax.get_ylim()
ax.set_ylim(ylim[0], -1)

# plt.show()