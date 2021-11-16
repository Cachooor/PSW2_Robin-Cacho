# 2 Columns in Data Series

import warnings 
warnings.filterwarnings("ignore")

import pandas as pd 
import numpy as np

d1 = {'A':list(range(0,2))}
df1 = pd.DataFrame(data=d1)
df1['key'] = 1

d2 = {'B':list(range(0,2))}
df2 = pd.DataFrame(data=d2)
df2['key'] = 1


df_rolls = pd.merge(df1, df2, on ='key').drop("key", 1)

print(df_rolls)
