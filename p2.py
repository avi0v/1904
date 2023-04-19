import pandas as pd 

# reading csv file

df=pd.read_csv("https://raw.githubusercontent.com/Apress/data-analysis-and-visualization-using-python/master/Ch07/Salaries.csv")

print(df['phd'].mean())
print(':::::::::::::::::::::::::::::::::::::::::::')

print(df['salary'].mean())
print(':::::::::::::::::::::::::::::::::::::::::::')
print(df['salary'].quantile())
print(':::::::::::::::::::::::::::::::::::::::::::')
print(df['salary'].min())
print(':::::::::::::::::::::::::::::::::::::::::::')
print(df['salary'].max())
print(':::::::::::::::::::::::::::::::::::::::::::')
print(df.value_counts())
