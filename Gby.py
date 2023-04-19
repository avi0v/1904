import pandas as pd 

# reading csv file

df=pd.read_csv("https://raw.githubusercontent.com/Apress/data-analysis-and-visualization-using-python/master/Ch07/Salaries.csv")

print(df)
print('---------------conditional output /filtering--------------------')
# booleans

print(df[df['rank']=='Prof'])
print('-----------------AND------------------')
print(df[
(df['rank']=='Prof') & (df['salary']>=150000)
])
print('----------------OR-------------------')
print(df[
    ((df['rank']=='Prof') | (df['rank']=='AssocProf') ) & (df['salary']>=150000)
])
print('-----------------------------------')