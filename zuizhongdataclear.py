#coding=UTF-8
import numpy
import matplotlib.pyplot as plt
from pandas import read_csv
import pandas as pd

import math
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error

# load the dataset
dataframe = pd.read_excel('~/PycharmProjects/Test1/14.xlsx', skiprows=3)

# add status 1 or -1
dataframe.loc[:,'D'] = 1
dataframe.loc[:,'E'] = -1

# conform in-time and out-time to the same column, status likely.
result2 = pd.concat([dataframe.loc[:,'入场时间'], dataframe.loc[:,' 出场时间']], ignore_index=True)
result3 = pd.concat([dataframe.loc[:,'D'], dataframe.loc[:,'E']], ignore_index=True)
result1 = pd.concat([result2,result3], axis=1)

# generate time series and assign it a mark '*'
date_generate = pd.date_range(start='5/14/2017',end='8/11/2017', freq='5min')
ts = pd.Series('*', index=date_generate)

# DatetimeIndex to concrete colomn value, then concat
date_array = date_generate.to_pydatetime()
# date_only_array = numpy.vectorize(lambda s: s.strftime('%Y-%m-%d'))(pydate_array )
date_series = pd.Series(date_array)
result = pd.concat([result1,date_series])


# conform date values of colomn to index
result.set_index(0, inplace = True)
result.index = pd.DatetimeIndex(result.index)

# date_array1 = result.index.to_pydatetime()
# date_only_array = numpy.vectorize(lambda s: s.strftime('%Y-%m-%d %X'))(date_array1)

result.sort_index(inplace=True)
result_list = result.values.tolist()

#calculate the num of parking
parking_num = []
t=[0]
num=0
for i in range(len(result_list)):
    if math.isnan(float(result_list[i][0])):
        result_list[i][0]=0
        t.append(i)
        for j in range(t[-2],t[-1]):
            num = num + float(result_list[j][0])
        parking_num.append(num)

ts = pd.Series(parking_num, index=date_generate)
ts.to_csv('~/PycharmProjects/Test1/foshan.csv', encoding='utf-8', index=True)



# print list(result.iteritems())
# result.index.fillna('missing')
# result.sort_index(inplace=True)
# print result
# print result.axes
# print result.columns
# result.sort_index(by=0,ascending=False)
# print result
# date_array = result.index.to_pydatetime()
# date_series = pd.Series(date_array)
# print  date_series
# result.fillna(0)
# print result
# series_dataframe = pd.DataFrame(date_series)
# print series_dataframe
# zuizhongresult = pd.concat([series_dataframe,result_new],axis=1)
# print zuizhongresult
# print result
# result = pd.concat([date_generate,ts])
# print result
# print ts
# print result2
# result2.to_csv('22.csv', encoding='utf-8', index=False)
# result3.to_csv('33.csv', encoding='utf-8', index=False)
# result.to_csv('~/PycharmProjects/Test1/11.csv', encoding='utf-8', index=False)
# print dataframe.loc[:,"In-time"].append(dataframe.loc[:,"Out-time"])
#first_rows = dataframe.head(10)
# print first_rows
#cols = dataframe.columns
# print cols
#dimension = dataframe.shape
# print dimension
# print dataframe.loc[0:3]
# print dataframe.loc[:,'D']
# print dataframe.loc[:,'入场时间']
# print dataframe.loc[:,"序号"]
# print dataframe.loc[:,"出场时间"]
# print ts
# train_data = numpy.array(date_generate)#np.ndarray()
# train_x_list=train_data.tolist()#list
# print train_x_list
# result.fillna({1:0})
# print result
# result.to_csv('~/PycharmProjects/Test1/22.csv', encoding='utf-8', index=False)
# print result.loc[:,0]
# print result.axes
# print date_array1