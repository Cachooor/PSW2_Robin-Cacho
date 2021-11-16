# Final Answer

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

d6 = {'F':list(range(0,2))}
df6 = pd.DataFrame(data=d6)
df6['key'] = 1

d7 = {'G':list(range(0,2))}
df7 = pd.DataFrame(data=d7)
df7['key'] = 1



df_rolls = pd.merge(df1, df2, on ='key')
df_rolls = pd.merge(df_rolls, df3, on ='key')
df_rolls = pd.merge(df_rolls, df4, on ='key')
df_rolls = pd.merge(df_rolls, df5, on ='key')
df_rolls = pd.merge(df_rolls, df6, on ='key')
df_rolls = pd.merge(df_rolls, df7, on ='key').drop("key", 1)



# determines the number of 0's if it is even or odd. 
df_rolls['Mod2'] = (df_rolls == 0).sum(axis=1) % 2


# returns (in this case) Mod2, as True or False depending on if Mod2 is even or not
df_rolls['1O0'] = df_rolls[['Mod2']].\
    apply(lambda x: True if (x['Mod2'] == 0) else False, axis=1)



# another column that defines probability 
e = df_rolls["1O0"]
df_rolls['e1'] = df_rolls["1O0"]

AP = df_rolls[['A']].\
    apply(lambda x: 1.0/5 if (x['A'] == 1) else 4.0/5, axis = 1)

BP = df_rolls[['B']].\
    apply(lambda x: 1.0/5 if (x['B'] == 1) else 4.0/5, axis = 1)

CP = df_rolls[['C']].\
    apply(lambda x: 1.0/5 if (x['C'] == 1) else 4.0/5, axis = 1)

DP = df_rolls[['D']].\
    apply(lambda x: 1.0/5 if (x['D'] == 1) else 4.0/5, axis = 1)

EP = df_rolls[['E']].\
    apply(lambda x: 6.0/7 if (x['E'] == 1) else 1.0/7, axis = 1)

FP = df_rolls[['F']].\
    apply(lambda x: 6.0/7 if (x['F'] == 1) else 1.0/7, axis = 1)

GP = df_rolls[['G']].\
    apply(lambda x: 6.0/7 if (x['G'] == 1) else 1.0/7, axis = 1)

# a1 = when A is true and e = True 
a1 = (df_rolls['A'] == 1) & (df_rolls['e1'] == True)


# combine multiple data frames into one 
frames = pd.concat([a1, e, AP, BP, CP, DP, EP, FP, GP], axis = 1)
frames.columns = ['a1', 'e', 'A', 'B', 'C', 'D', 'E', 'F', 'G']



# the probability:
frames['PP'] = AP * BP * CP * DP * EP * FP * GP
numerator = frames.groupby('e')['PP'].sum() 
denominator = frames.groupby('a1')['PP'].sum() 
# prints current output 
#print(frames[frames['e']]) 
print(frames)

print(f"\n{numerator}")
print(f"\n{denominator}")


'''
ONLY PRINTS WHEN e IS TRUE 



Original Code: 
df_rolls['roll_sum'] = df_rolls['d1'] + df_rolls['d2'] + df_rolls['d3'] + df_rolls['d4'] + \
    df_rolls['d5'] + df_rolls['d6'] + df_rolls['d7'] 
    
print(df_rolls)

df_rolls['d4d7'] = df_rolls['d4'].eq(1).eq(df_rolls['d5']).eq(1).eq(df_rolls['d6']).eq(1).eq(df_rolls['d7']).eq(1)
df_rolls['anita'] = df_rolls['d7'].eq(1)

df_rolls['d1LT'] = df_rolls['d1'].lt(7)
df_rolls['d2LT'] = df_rolls['d2'].lt(7)
df_rolls['d3LT'] = df_rolls['d3'].lt(7) 


df_rolls['winner'] = df_rolls[['anita']].\
    apply(lambda x: 'W' if (x['anita'] == True) else 'L', axis=1)

df_rolls['winner'] = df_rolls[['d1LT', 'd2LT', 'd3LT','d4d7']].\
    apply(lambda x: 'W' if (x['d1LT'] == True) and (x['d2LT'] == True) and (x['d3LT'] == True) and (x['d4d7'] == True) else 'L', axis=1)

pd.set_option("display.max_rows", None, "display.max_columns", None)

# print(df_rolls[df_rolls['winner'].str.contains('W')]) #prints all the combinations that result in a win 

w1 = pd.DataFrame(df_rolls.winner.value_counts().reset_index())
w1.rename(columns={'index':'win_or_lose', 'winner':'possible_outcomes'}, inplace=True)

w2 = pd.DataFrame(df_rolls.winner.value_counts(normalize=True).reset_index())
w2.rename(columns={'index':'win_or_lose', 'winner':'possible_outcomes_pct'}, inplace=True)

w1 = w1.merge(w2, how='left', on='win_or_lose') 
print(w1) #prints conclusion and final probability 


'''