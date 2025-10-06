import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import random

## Load our dataframe
df = pd.read_csv("pennData.csv")
pennData = pd.DataFrame(df)
print("-_"*20)
print("Head of the Dataframe") # First five rows of the dataframee
print(pennData.head())

print("-_"*20)
print("Tail of the Dataframe") # First five rows of the dataframee
print(pennData.tail())

print("-_"*20)
print("Summary of the Dataframe") # First five rows of the dataframee
print(pennData.info())

print("-_"*20)
print("Statistics of the Dataframe") # First five rows of the dataframee
print(round(pennData.describe()))

print("-_"*20)
print("Counts of Students in Pathways") # First five rows of the dataframee
print(pennData['Pathway'].value_counts())

print("-_"*20)
print("Average GPA Per Year") # First five rows of the dataframee
print(pennData.groupby('Year')['GPA'].mean())

print("-_"*20)
print("Top three students by GPA") # First five rows of the dataframee
print(pennData.sort_values(by='GPA', ascending=False).head(3))

print("-_"*20)
print("Students with GPA > 3.5") # First five rows of the dataframee
print(pennData[pennData['GPA']> 3.5])

print("-_"*20)
print("First student data") # First five rows of the dataframee
print(pennData.iloc[0])

pennData.groupby('Year')['GPA'].mean().plot(kind='bar')
plt.show()