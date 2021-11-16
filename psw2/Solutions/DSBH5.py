# 5 Columns in Data Series W/o solution 

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

d3 = {'C':list(range(0,2))}
df3 = pd.DataFrame(data=d3)
df3['key'] = 1

d4 = {'D':list(range(0,2))}
df4 = pd.DataFrame(data=d4)
df4['key'] = 1

d5 = {'E':list(range(0,2))}
df5 = pd.DataFrame(data=d5)
df5['key'] = 1

df_rolls = pd.merge(df1, df2, on ='key')
df_rolls = pd.merge(df_rolls, df3, on ='key')
df_rolls = pd.merge(df_rolls, df4, on ='key')
df_rolls = pd.merge(df_rolls, df5, on ='key').drop("key", 1)


# determines the number of 0's if it is even or odd. 
df_rolls['Mod2'] = (df_rolls == 0).sum(axis=1) % 2


# returns (in this case) Mod2, as True or False depending on if Mod2 is even or not
df_rolls['1O0'] = df_rolls[['Mod2']].\
    apply(lambda x: True if (x['Mod2'] == 0) else False, axis=1)

print(df_rolls[df_rolls['1O0']])
