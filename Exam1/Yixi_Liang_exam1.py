import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#######################################
#Q1
#######################################
df = sns.load_dataset('diamonds')
print(df.isnull().sum())
df = df.dropna(how='any')
print(df.isnull().sum())
col_name = df.columns
plt.style.use('fivethirtyeight')

#######################################
#Q2
#######################################
cutDif = df['cut'].unique()
print(f'The list of diamond cuts in the diamond dataset are: {cutDif}')

#######################################
#Q3
#######################################
colorDif = df['color'].unique()
print(f'The list of diamond color in the diamond dataset are: {colorDif}')

#######################################
#Q4
#######################################
clarityDif = df['clarity'].unique()
print(f'The list of diamond clarity in the diamond dataset are: {clarityDif}')

#######################################
#Q5
#######################################
labelCut = cutDif
scoreCut = []
for i in cutDif:
    scoreCut.append(len(df[df['cut'] == i]))

plt.figure(figsize=(16,8))
plt.barh(labelCut, scoreCut)
plt.xlabel('Sales count')
plt.ylabel('Cut')
plt.title('Sales count per cut')
plt.show()

print(f'The diamond with Ideal cut has the maximum sales per count.')
print(f'The diamond with Fair cut has the minimum sales per count.')
#######################################
#Q6
#######################################
labelCol = colorDif
scoreCol = []
for i in colorDif:
    scoreCol.append(len(df[df['color'] == i]))

plt.figure(figsize=(16,8))
plt.barh(labelCol, scoreCol)
plt.xlabel('Sales count')
plt.ylabel('Color')
plt.title('Sales count per color')
plt.show()

print(f'The diamond with G color has the maximum sales per count.')
print(f'The diamond with J color has the minimum sales per count.')
#######################################
#Q7
#######################################
labelCla = clarityDif
scoreCla = []
for i in clarityDif:
    scoreCla.append(len(df[df['clarity'] == i]))

plt.figure(figsize=(16,8))
plt.barh(labelCla, scoreCla)
plt.xlabel('Sales count')
plt.ylabel('Clarity')
plt.title('Sales count per clarity')
plt.show()

print(f'The diamond with SI1 clarity has the maximum sales per count.')
print(f'The diamond with I1 clarity has the minimum sales per count.')


#######################################
#Q8
#######################################
plt.figure(figsize=(16,8))
plt.subplot(1,3,1)
plt.barh(labelCut, scoreCut)
plt.xlabel('Sales count')
plt.ylabel('Cut')
plt.title('Sales count per cut')

plt.subplot(1,3,2)
plt.barh(labelCol, scoreCol)
plt.xlabel('Sales count')
plt.ylabel('Color')
plt.title('Sales count per color')

plt.subplot(1,3,3)
plt.barh(labelCla, scoreCla)
plt.xlabel('Sales count')
plt.ylabel('Clarity')
plt.title('Sales count per clarity')
plt.show()

#######################################
#Q9
#######################################
explode = (0.03, 0.03,0.03,0.03,0.03)
plt.figure()
plt.pie(scoreCut,labels=labelCut, explode=explode, autopct='%1.2f%%')

plt.title('Sales count per cut in %')
plt.axis('square')
plt.axis('equal')
plt.show()
print(f'The diamond with Ideal cut has the maximum sales per count with 39.95 % sales count.')
print(f'The diamond with Fair cut has the minimum sales per count with 2.98 % sales count.')


#######################################
#Q10
#######################################
explode = (0.03, 0.03,0.03,0.03,0.03,0.03,0.03)

plt.figure()
plt.pie(scoreCol,labels=labelCol, explode=explode, autopct='%1.2f%%')

plt.title('Sales count per color')
plt.axis('square')
plt.show()
print(f'The diamond with G color has the maximum sales per count with 20.93 % sales count.')
print(f'The diamond with J color has the minimum sales per count with 5.21 % sales count.')

#######################################
#Q11
#######################################
explode = (0.03, 0.03,0.03,0.03,0.03,0.03,0.03,0.03)
plt.figure()
plt.pie(scoreCla,labels=labelCla, explode=explode, autopct='%1.2f%%')

plt.title('Sales count per clarity')
plt.axis('square')
plt.show()
print(f'The diamond with SI1 clarity has the maximum sales per count with 24.22 % sales count.')
print(f'The diamond with I1 clarity has the minimum sales per count with 1.37 % sales count.')

#######################################
#Q12
#######################################
plt.figure(figsize=(16,8))
plt.subplot(1,3,1)
explode = (0.03, 0.03,0.03,0.03,0.03)
plt.pie(scoreCut,labels=labelCut, explode=explode, autopct='%1.2f%%')
plt.title('Sales count per cut in %')
plt.axis('square')

plt.subplot(1,3,2)
explode = (0.03, 0.03,0.03,0.03,0.03,0.03,0.03)
plt.pie(scoreCol,labels=labelCol, explode=explode, autopct='%1.2f%%')
plt.title('Sales count per color')
plt.axis('square')

plt.subplot(1,3,3)
explode = (0.03, 0.03,0.03,0.03,0.03,0.03,0.03,0.03)
plt.pie(scoreCla,labels=labelCla, explode=explode, autopct='%1.2f%%')
plt.title('Sales count per clarity')
plt.axis('square')

plt.show()
#######################################
#Q13
#######################################
idealList = []
premiumList = []
goodList = []
veryGoodList = []
fairList = []
for i in colorDif:
    idealList.append(np.mean(df[(df['clarity'] == 'VS1') & (df['color'] == i) & (df['cut'] == 'Ideal')]['price']))
    premiumList.append(np.mean(df[(df['clarity'] == 'VS1') & (df['color'] == i) & (df['cut'] == 'Premium')]['price']))
    goodList.append(np.mean(df[(df['clarity'] == 'VS1') & (df['color'] == i) & (df['cut'] == 'Very Good')]['price']))
    veryGoodList.append(np.mean(df[(df['clarity'] == 'VS1') & (df['color'] == i) & (df['cut'] == 'Good')]['price']))
    fairList.append(np.mean(df[(df['clarity'] == 'VS1') & (df['color'] == i) & (df['cut'] == 'Fair')]['price']))



data = {
    "Ideal": np.around(idealList, 2),
    "Premium": np.around(premiumList, 2),
    "Very good": np.around(goodList, 2),
    "Good": np.around(veryGoodList, 2),
    "Fair": np.around(fairList, 2),
}

dfMean = pd.DataFrame(data, index=list("DEFGHIJ"))
dfMean = dfMean.T
dfMeanFinal = dfMean.copy()
dfMeanFinal["Max"] = dfMean.astype("float64").idxmax(axis=1)
dfMeanFinal["Min"] = dfMean.astype("float64").idxmin(axis=1)

dfMeanFinal.loc["Max",:] = dfMean.astype("float64").idxmax(axis=0)
dfMeanFinal.loc["Min",:] = dfMean.astype("float64").idxmin(axis=0)

print(dfMeanFinal.to_string())