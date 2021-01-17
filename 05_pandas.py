# -*- coding: utf-8 -*-
'''
@author: Jinglu LIU
@time: 2021-01-10 12:23 
@describe: pandas learning
'''

import pandas as pd
from pandas import Series, DataFrame

obj = pd.Series([4,7,-5,3])
print(obj)
print(obj.values)
print(obj.index)

obj2 = pd.Series([4,7,-5,3], index=['a', 'b','c','d'])
print(obj2)
print(obj2.index)

print(obj2[obj2 > 2])
obj2.name = 'A'
print(obj2.name)


data = {
    'state': ['ohio', 'ohio', 'ohio', 'nevada', 'nevada', 'nevada'],
    'year' : [2000, 2001, 2002, 2001, 2002, 2003],
    'pop' : [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]
}

frame = pd.DataFrame(data)

print(frame.head())

