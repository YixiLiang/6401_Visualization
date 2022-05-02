import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
import dash as dash
from dash import dcc
from dash import html
import plotly.express as px
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import plotly.graph_objects as go

from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from numpy import linalg as LA

from statsmodels.graphics.gofplots import qqplot
import scipy.stats as st

import matplotlib.patches as mpatches

#######################################
# load data
#######################################
df = pd.read_csv('weatherAUS.csv')
df_weather = df.copy()

colName = df_weather.columns
largeNaList = []
colHasNA = 0
dropColName = []
for i in range(len(colName)):
    columnName = colName[i]
    naPercentage = df_weather.isna().sum()[columnName] / len(df_weather[columnName])
    if naPercentage > 0:
        colHasNA += 1
    if naPercentage > 0.2:
        dropColName.append(columnName)
    largeNaList.append(str(naPercentage * 100) + '%')

percentageNa = pd.DataFrame(columns=colName)
percentageNa.loc[1] = largeNaList
print(percentageNa)
# df_weather.fillna(value=df_weather.mean(), inplace=True)
# df_weather["RainToday"] = np.where(df_weather["RainToday"] == "No", 0, 1)
# dropColName.append('RainTomorrow')
df_weather.drop(dropColName, axis=1, inplace=True)
df_weather.dropna(how='any', inplace=True)
print(df_weather.isna().sum())
print(df_weather.head().to_string())
print(df_weather.describe().to_string())
# show first 5 rows of the dataset
showCleanedDataset = pd.DataFrame(df_weather.head())
# show the basic information of the columns
showCleanedDatasetDes = pd.DataFrame(df_weather.describe())
#######################################
# Change Date column to datetime type
#######################################
df_weather['Date'] = pd.to_datetime(df_weather['Date'], format='%Y-%m-%d')
# get all the city name
cityName = df_weather['Location'].unique()
# make a list to store cityName
cityNameDropdownOptions = []
for i in range(len(cityName)):
    dic = {'label': cityName[i], 'value': cityName[i]}
    cityNameDropdownOptions.append(dic)
# get all the year
dateYear = [df_weather['Date'].iloc[i].year for i in range(len(df_weather['Date']))]
dateYear = np.unique(dateYear)
# get start date and end date
minDate = min(df_weather['Date'])
maxDate = max(df_weather['Date'])
#######################################
# Outlier detection
#######################################
# get the numeric column name
numericalColName = df_weather.select_dtypes(include='number').columns
for name in numericalColName:
    numOutlier = 0
    q1 = showCleanedDatasetDes.loc['25%', name]
    q3 = showCleanedDatasetDes.loc['75%', name]
    iqr = q3 - q1
    lowOutlier = q1 - 1.5 * iqr
    highOutlier = q3 + 1.5 * iqr
    numOutlier = df_weather[name][(df_weather[name] > highOutlier) | (df_weather[name] < lowOutlier)].count()
    print(f'{name} : {numOutlier}')
# create box plot of numeric columns
plt.figure(figsize=(16, 9))
for i in range(len(numericalColName)):
    plt.subplot(4, 3, i + 1)
    plt.boxplot(df_weather[numericalColName[i]].dropna().tolist())
    plt.title(f'Boxplot of {numericalColName[i]}')
plt.tight_layout()
plt.show()
# #######################################
# # PCA
# #######################################
X = df_weather[numericalColName].values
X = StandardScaler().fit_transform(X)

# original
# Singular value decomposition: two value become one value
pca_original = PCA(svd_solver='full')
pca_original.fit(X)
X_PCA_original = pca_original.transform(X)
print('Original Dim', X.shape)
print('Transformed Dim', X_PCA_original.shape)
print(f'pca explained variance ratio {pca_original.explained_variance_ratio_}')
# reduced
pca = PCA(n_components=8, svd_solver='full')
pca.fit(X)
X_PCA = pca.transform(X)
print('Original Dim', X.shape)
print('Transformed Dim', X_PCA.shape)
print(f'pca explained variance ratio when using mle {pca.explained_variance_ratio_}')

print(
    'Four features should be remove from per PCA analysis, because the top 8 feature have explained over 98% variance ratio')

# cumulative explained variance
plt.figure()
x = np.arange(1, len(pca.explained_variance_ratio_) + 1)
plt.xticks(x)
plt.plot(x, np.cumsum((pca.explained_variance_ratio_)))
plt.title('cumulative explained variance versus the number of components')
plt.grid()
plt.show()

# condition number and singular value

# if condition is not significantly larger than one, the matrix is well-conditioned

# In numerical analysis, the condition number of a function measures how much the output
# value of the function can change for a small change in the input argument.
# This is used to measure how sensitive a function is to changes or errors in the input,
# and how much error in the output results from an error in the input.

# The singular values are the diagonal entries of the S matrix and are arranged in descending order.

H = np.matmul(X.T, X)
_, d, _ = np.linalg.svd(H)
print(f'Original Data: singular Values {d}')
print(f'Original Data: condition number {LA.cond(X)}')


H = np.matmul(X_PCA.T, X_PCA)
_, d, _ = np.linalg.svd(H)
print(f'Reduced Data: singular Values {d}')
print(f'Reduced Data: condition number {LA.cond(X_PCA)}')

# original date
plt.figure(figsize=(16,14))
corcoe = df_weather.corr()
sns.heatmap(corcoe, annot=True)
plt.title('Correlation Coefficient between features-Original feature space')
plt.show()
# reduced data
plt.figure(figsize=(16,14))
corcoe_reduced = pd.DataFrame(X_PCA).corr()
sns.heatmap(corcoe_reduced, annot=True)
plt.title('Correlation Coefficient between features-Reduced feature space')
plt.show()
# #######################################
# # Normality test
# #######################################
# histogram of numeric columns
plt.figure(figsize=(16,9))
for i in range(len(numericalColName)):
    plt.subplot(4, 3, i + 1)
    plt.hist(df_weather[numericalColName[i]].dropna().tolist(), bins=50)
    plt.title(f'Histogram of {numericalColName[i]}')
    plt.ylabel('Magnitude')
    plt.xlabel('# of samples')
    plt.grid()
plt.tight_layout()
plt.show()
# QQplot of numeric columns
figure, axes = plt.subplots(4, 3, figsize=(16,9))
for i in range(len(numericalColName)):
    qqplot(df_weather[numericalColName[i]], line='s', ax=axes[i//3, i%3])
    axes[i//3, i%3].set_title(f'qqplot of {numericalColName[i]}')
figure.suptitle('Multiple qq plots', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()
# K-S test
# shapiro test
from scipy.stats import shapiro
for i in range(len(numericalColName)):
    kstestX = st.kstest(df_weather[numericalColName[i]], 'norm')
    shapiroX = shapiro(df_weather[numericalColName[i]])
    print(f'K-S test of {numericalColName[i]}: statistics = {kstestX[0]} p-value = {kstestX[1]}')
    print(f'K-S test of {numericalColName[i]}: {numericalColName[i]} dataset looks ')
    print(f'Shapiro test: statistics = {shapiroX[0]} p-value = {shapiroX[1]}')
#######################################
# Data transformation
#######################################
transformedList = []
for i in range(len(numericalColName)):
    x = df_weather[numericalColName[i]]
    transformedX = st.norm.ppf(st.rankdata(x).reshape(x.shape)/(len(x) + 1))
    print(transformedX)
    transformedList.append(transformedX)
# histogram of numeric columns
plt.figure(figsize=(16,9))
for i in range(len(numericalColName)):
    plt.subplot(4, 3, i + 1)
    plt.hist(transformedList[i], bins=50)
    plt.title(f'Histogram of {numericalColName[i]}')
    plt.ylabel('Magnitude')
    plt.xlabel('# of samples')
    plt.grid()
plt.tight_layout()
plt.show()
# QQplot of numeric columns
figure, axes = plt.subplots(4, 3, figsize=(16,9))
for i in range(len(numericalColName)):
    qqplot(transformedList[i], line='s', ax=axes[i//3, i%3])
    axes[i//3, i%3].set_title(f'qqplot of {numericalColName[i]}')
figure.suptitle('Multiple qq plots', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()
# K-S test and shapiro
for i in range(len(numericalColName)):
    kstestX = st.kstest(transformedList[i], 'norm')
    shapiroX = shapiro(transformedList[i])
    print(f'K-S test after transformed of {numericalColName[i]}: statistics = {kstestX[0]} p-value = {kstestX[1]}')
    # print(f'K-S test after transformed of {numericalColName[i]}: {numericalColName[i]} dataset looks ')
    print(f'Shapiro test after transformed: statistics = {shapiroX[0]} p-value = {shapiroX[1]}')
# #######################################
# # Heatmap & Pearson correlation coefficient matrix
# #######################################
#Correlation coefficient matrix
plt.figure(figsize=(14,10))
corcoe = df_weather.corr()
sns.heatmap(corcoe, annot=True)
plt.title('Correlation Coefficient of numeric columns')
plt.show()
#Scatter plot matrix.
sns.set_theme(style="ticks")
sns.pairplot(df_weather)
plt.title("Scatter plot matrix of numeric columns")
plt.show()
#######################################
# Statistics kde
#######################################
# penguins = sns.load_dataset("penguins")
df_kde = df_weather[['Date','Location', 'MinTemp','MaxTemp','Rainfall','WindGustSpeed']]
showCityName = ['Albury','BadgerysCreek','Cobar']
df_kde = df_kde[(df_kde['Date'] > '2017-01-01') & (df_kde['Location'].isin(showCityName))]
sns.pairplot(df_kde, kind="kde", hue='Location')
plt.suptitle('Multivariate kernel density estimate plot')
plt.show()
#######################################
# Data visualization
#######################################
sns.set_theme(style='darkgrid')
showCityName = ['Albury','BadgerysCreek','Cobar']
df_showCity = df_weather[df_weather['Location'].isin(showCityName)]
#######################################
# a. Line-plot
df_showCity_linplot = df_showCity[df_showCity['Date']>'2017-01-01']
plt.figure()
sns.lineplot(data=df_showCity_linplot, x='Date', y='MinTemp', hue='Location')
plt.title('Line plot of minimum temperature in degrees Celsius hue city')
plt.show()
#######################################
# Bar-plot : stack, group
# tips = sns.load_dataset("tips")
# stack
plt.figure()
bar1 = sns.barplot(data=df_showCity,y='Rainfall', x='Location',estimator=sum, color='darkblue')
rain = df_showCity[df_showCity.RainTomorrow=='Yes']
bar2 = sns.barplot(data=rain,y='Rainfall', x="Location",estimator=sum, ci=None, color='lightblue')
# add legend
top_bar = mpatches.Patch(color='darkblue', label='Rain Tomorrow = Yes')
bottom_bar = mpatches.Patch(color='lightblue', label='Rain Tomorrow = No')
plt.title('Stack bar plot of today rainfall in different cities hue by rain tomorrow')
plt.legend(handles=[top_bar, bottom_bar])
plt.show()
# This plot can show whether today rainfall affect rain tomorrow
# group
plt.figure()
sns.barplot(data=df_showCity, x='Location', y='MinTemp', hue='RainToday')
plt.title('MinTemp in different cities group by RainToday')
plt.show()
# This plot can show the relation between minimum temperature and rain in different cities.
#######################################
# c. Count-plot
plt.figure()
sns.countplot(data=df_weather, x='RainToday')
plt.title('Count plot of Rain Today')
plt.show()
#######################################
# d. Cat-plot
plt.figure()
sns.catplot(data=df_showCity, x='Location', y='MaxTemp', col='RainToday')
# plt.title('Cat-plot of MaxTemp in different cities divided by RainToday')
plt.show()
#######################################
# e. Pie-chart
plt.figure()
# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = df_weather['WindGustDir'].value_counts().index
sizes = df_weather['WindGustDir'].value_counts().values
explode = [0]*len(labels)

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('Pie chart of WindGustDir')
plt.show()
#######################################
# f. Displot
plt.figure()
sns.displot(data=df_showCity, x='MaxTemp', hue='Location', multiple='stack')
plt.title('Distplot of MaxTemp hue by Location')
plt.show()
#######################################
# g. Pair plot
df_showCity_pairplot = df_showCity_linplot[['Location', 'MinTemp', 'MaxTemp', 'Rainfall', 'WindGustSpeed']]
plt.figure()
sns.pairplot(data=df_showCity_pairplot, hue="Location")
# plt.title('Pair plot about MinTemp, MaxTemp, Rainfall, WindGustSpeed hue by city')
plt.show()
#######################################
# h. Heatmap
df_showCity_heatmap = df_showCity.copy()
df_showCity_heatmap = df_showCity_heatmap[['Date', 'MaxTemp']]
df_showCity_heatmap_new = df_showCity_heatmap.groupby(pd.PeriodIndex(df_showCity_heatmap['Date'], freq="M"))['MaxTemp'].mean()
df_showCity_heatmap_new = pd.DataFrame(df_showCity_heatmap_new)
df_showCity_heatmap_new['Date'] = df_showCity_heatmap_new.index
df_showCity_heatmap_new['year'] = df_showCity_heatmap_new['Date'].dt.year
df_showCity_heatmap_new['month'] = df_showCity_heatmap_new['Date'].dt.month
df_showCity_heatmap_new = df_showCity_heatmap_new.pivot('month', 'year', 'MaxTemp')

plt.figure()
sns.heatmap(df_showCity_heatmap_new, annot=True, fmt=".1f")
plt.title('Heatmap of MaxTemp average in month and year')
plt.show()
#######################################
# i. Hist-plot
plt.figure()
sns.histplot(data=df_showCity, x="WindGustSpeed", kde=True, bins=10)
plt.xlabel('WindGustSpeed (km/h)')
plt.title('Hist-plot of WindGustSpeed')
plt.show()
#######################################
# j. QQ-plot
plt.figure()
qqplot(data=df_showCity['MinTemp'], line='s')
plt.title('QQ-plot of MinTemp')
plt.show()
#######################################
# k. Kernal density estimate
plt.figure()
sns.kdeplot(
    data=df_showCity, x="MinTemp", y="WindGustSpeed", hue="Location", fill=True,
)
plt.title('Kde plot of WindGustSpeed versus MinTemp hue by city')
plt.show()
#######################################
# l. Scatter plot and regression line using sklearn
plt.figure()
sns.regplot(x="MinTemp", y="WindGustSpeed", data=df_showCity_linplot)
plt.title('Scatter plot of WindGustSpeed versus MinTemp and regression line')
plt.show()
#######################################
# m. Multivariate Box plot
plt.figure()
sns.boxplot(x="Location", y="MinTemp", data=df_showCity)
plt.title('Box plot of MinTemp in different cities')
plt.show()
#######################################
# n. Area plot
df_showCity_area = df_showCity[df_showCity['Date'] > '2017-06-01']
rainfallA = df_showCity_area[df_showCity_area['Location'] == 'Albury']['WindGustSpeed']
rainfallB = df_showCity_area[df_showCity_area['Location'] == 'Albury']['WindSpeed9am']
rainfallC = df_showCity_area[df_showCity_area['Location'] == 'Albury']['WindSpeed3pm']
plt.figure(figsize=(12,9))
plt.stackplot(df_showCity_area[df_showCity_area['Location'] == 'Albury']['Date'], rainfallA, rainfallB, rainfallC)
plt.title('Area plot of WindGustSpeed, WindSpeed9am and WindSpeed3pm in Albury')
plt.ylabel('Wind gust speed (km/h)')
plt.xlabel('Date')
plt.legend(labels=["WindGustSpeed","WindSpeed9am",'WindSpeed3pm'])
plt.show()
#######################################
# o. Violin plot
plt.figure()
sns.violinplot(x="Location", y="WindGustSpeed", data=df_showCity)
plt.title('Violin plot of WindGustSpeed in different cities')
plt.show()
#######################################
# Subplots
#######################################
df_showCity_subplot = df_showCity[(df_showCity['Date'] > '2017-05-15') & (df_showCity['Date'] < '2017-06-01')]
df_showCity_subplot = df_showCity_subplot[df_showCity_subplot['Location'] == 'Albury']


plt.figure(figsize=(16,9))
plt.subplot(3,2,1)
sns.lineplot(data=df_showCity_subplot, x='Date', y='Rainfall')
plt.title('Line plot of Rainfall')

plt.subplot(3,2,2)
plt.plot(df_showCity_subplot['Date'], df_showCity_subplot['MinTemp'], color='b')
plt.plot(df_showCity_subplot['Date'], df_showCity_subplot['MaxTemp'], color='r')
plt.plot(df_showCity_subplot['Date'], df_showCity_subplot['Temp9am'], color='g')
plt.plot(df_showCity_subplot['Date'], df_showCity_subplot['Temp3pm'], color='y')
plt.legend(labels=['MinTemp','MaxTemp','Temp9am','Temp3pm'])
plt.ylabel('Degree of Celsius')
plt.xlabel('Date')
plt.title('Line plot of Temperature')

plt.subplot(3,2,3)
plt.plot(df_showCity_subplot['Date'], df_showCity_subplot['WindGustSpeed'], color='g')
plt.plot(df_showCity_subplot['Date'], df_showCity_subplot['WindSpeed9am'], color='r')
plt.plot(df_showCity_subplot['Date'], df_showCity_subplot['WindSpeed3pm'], color='b')
plt.legend(labels=['WindGustSpeed','WindSpeed9am','WindSpeed3pm'])
plt.ylabel('Wind speed (km/h)')
plt.xlabel('Date')
plt.title('Line plot of WindSpeed')

plt.subplot(3,2,4)
plt.plot(df_showCity_subplot['Date'], df_showCity_subplot['WindGustDir'], color='g')
plt.plot(df_showCity_subplot['Date'], df_showCity_subplot['WindDir9am'], color='r')
plt.plot(df_showCity_subplot['Date'], df_showCity_subplot['WindDir3pm'], color='b')
plt.legend(labels=['WindGustDir','WindDir9am','WindDir3pm'])
plt.ylabel('Wind Gust Direction')
plt.xlabel('Date')
plt.title('Line plot of Wind Speed Direction')

plt.subplot(3,2,5)
plt.plot(df_showCity_subplot['Date'], df_showCity_subplot['Humidity9am'], color='r')
plt.plot(df_showCity_subplot['Date'], df_showCity_subplot['Humidity3pm'], color='b')
plt.legend(labels=['Humidity9am','Humidity3pm'])
plt.ylabel('Humidity (percent)')
plt.xlabel('Date')
plt.title('Line plot of Humidity')

plt.subplot(3,2,6)
plt.plot(df_showCity_subplot['Date'], df_showCity_subplot['Pressure9am'], color='r')
plt.plot(df_showCity_subplot['Date'], df_showCity_subplot['Pressure3pm'], color='b')
plt.legend(labels=['Pressure9am','Pressure9am'])
plt.ylabel('Atmospheric pressure (hpa) ')
plt.xlabel('Date')
plt.title('Line plot of Pressure')

plt.tight_layout()
plt.show()

#######################################
#######################################