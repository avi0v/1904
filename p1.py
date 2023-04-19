import pandas as pd 

# reading csv file

df=pd.read_csv("https://raw.githubusercontent.com/Apress/data-analysis-and-visualization-using-python/master/Ch07/Salaries.csv")
print(df)
print("----------------------------------")

# head() , tail()
print(df.head(11)) #print first 11 row
print("----------------------------------")
print(df.tail(16)) # last 16 row
print("----------------------------------")
print(df.columns)
print("----------------------------------")
print(df.describe()) # statistic summary of whole data set , col wise of int col
print("----------------------------------")
print(df.describe(include=object))
print("----------------------------------")
print(df.describe(include='all')) # summary of all , int value - null for non int data like name etc
print("----------------------------------")
# calling 
print(df['rank'])
print(df[['rank','salary','sex']])
print("----------------------------------")

# calling and describe specific col
print(df['rank'].describe())
print("----------------------------------")


# mean 
print(df.mean())
