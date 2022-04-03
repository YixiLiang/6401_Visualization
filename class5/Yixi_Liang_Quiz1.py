import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

#######################################
#Q1 load data
#######################################
df = sns.load_dataset('taxis')

#######################################
#Q2 show data
#######################################
print(f"There are {df.shape[0]} observations inside the raw dataset")
print(f"There are {df.shape[1]} features[columns] inside the raw dataset")
#######################################
#Q3
#######################################
col = df.columns
for colName in col:
    nanDataLen = len(df[(df[colName].isna() == True) | (df[colName].isnull() == True)])
    print(f'The percentage of na and null in {colName} is {nanDataLen/df.shape[0] * 100:.2f}%')
    if nanDataLen/df.shape[0] > 0.002:
        df.drop(columns=colName)

dftest1 = df.dropna(subset=["payment"])
# df.dropna(subset=[1])   #Drop only if NaN in specific column
# df = df[df['EPS'].notna()] .notna 找不是na的值
dftest2 = df.drop(columns='passengers')
#################################
a = df.isnull().sum()/len(df) * 100
col = df.columns
variables = []
df1 = df.copy()
for i in range(0, len(col)):
    if a[i] > .2:
        variables.append(col[i])
df1.drop(variables, axis=1, inplace=True)

a1 = df1.isnull().sum()/len(df) * 100
print(a)
#######################################
#Q4
#######################################
print(df.isna())
print(df.isnull())

#######################################
#Q5
#######################################
meanTotal = df['total'].mean()
meanTip = df['tip'].mean()
varTotal = df['total'].var()
varTip = df['tip'].var()

print(f'The mean of the total is {meanTotal:.2f}$')
print(f'The mean of the tip is {meanTip:.2f}$')
print(f'The variance of the total is {varTotal:.2f}$')
print(f'The variance of the total is {varTip:.2f}$')
#######################################
#Q6
#######################################

df['tip_percentage'] = df['tip'] / df['total'] * 100
num1 = df[df['tip_percentage'] == 0].shape[0] / df.shape[0]
num2 = df[(df['tip_percentage'] >= 10) & (df['tip_percentage'] < 15)].shape[0] / df.shape[0]
num3 = df[(df['tip_percentage'] >= 15) & (df['tip_percentage'] < 20)].shape[0]/ df.shape[0]
num4 = df[df['tip_percentage'] > 20].shape[0] / df.shape[0]
num5 = df['tip_percentage'].mean()

print(f'{num1:.2f}% of passengers did not tip at all')
print(f'{num2:.2f}% of passengers tipped 10-15% of total[10 is included and 15 is excluded]')
print(f'{num3:.2f}% of passengers tipped 15-20% of total[15 is included and 20 is excluded]')
print(f'{num4:.2f}% of passengers tipped more than 20% of total [20 is included]')
print(f'Majority of passengers tipped 15%-20% of total.')

#######################################
#Q7
#######################################
dfTip = df['tip']
dfTotal = df['total']
plt.figure(figsize=(12, 8))
plt.hist(dfTip, label="tip", alpha=0.5, bins=50)
plt.hist(dfTotal, label="total", alpha=0.5, bins=50)
plt.title('Histogram plot of tips dataset')
plt.xlabel("range in USD($)")
plt.ylabel("Frequency")
plt.legend()
plt.grid()
plt.show()
#######################################
#Q8
#######################################
df8 = df[['distance','fare','tip']]
corr = df8.corr()
print(corr)

print(f'The correlation coefficient between the fare & distance is {corr.iloc[0,1]:.2f}')
print(f'The correlation coefficient between the tip & fare is {corr.iloc[2,1]:.2f}')
print(f'The correlation coefficient between the tip & distance is {corr.iloc[2,0]:.2f}')
print(f'The fare amount has the highest correlation coefficient with distance fare & distance')
