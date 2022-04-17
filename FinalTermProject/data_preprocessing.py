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
dropColName.append('RainTomorrow')
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
# change Date column to datetime type
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
# for name in numericalColName:
#     numOutlier = 0
#     q1 = showCleanedDatasetDes.loc['25%', name]
#     q3 = showCleanedDatasetDes.loc['75%', name]
#     iqr = q3 - q1
#     lowOutlier = q1 - 1.5 * iqr
#     highOutlier = q3 + 1.5 * iqr
#     numOutlier = df_weather[name][(df_weather[name] > highOutlier) | (df_weather[name] < lowOutlier)].count()
#     print(f'{name} : {numOutlier}')
# # create box plot of numeric columns
# plt.figure(figsize=(16, 9))
# for i in range(len(numericalColName)):
#     plt.subplot(4, 3, i + 1)
#     plt.boxplot(df_weather[numericalColName[i]].dropna().tolist())
#     plt.title(f'Boxplot of {numericalColName[i]}')
# plt.tight_layout()
# plt.show()
# #######################################
# # PCA
# #######################################
# X = df_weather[numericalColName].values
# X = StandardScaler().fit_transform(X)
#
# # original
# # Singular value decomposition: two value become one value
# pca_original = PCA(svd_solver='full')
# pca_original.fit(X)
# X_PCA_original = pca_original.transform(X)
# print('Original Dim', X.shape)
# print('Transformed Dim', X_PCA_original.shape)
# print(f'pca explained variance ratio {pca_original.explained_variance_ratio_}')
# # reduced
# pca = PCA(n_components=8, svd_solver='full')
# pca.fit(X)
# X_PCA = pca.transform(X)
# print('Original Dim', X.shape)
# print('Transformed Dim', X_PCA.shape)
# print(f'pca explained variance ratio when using mle {pca.explained_variance_ratio_}')
#
# print(
#     'Four features should be remove from per PCA analysis, because the top 8 feature have explained over 98% variance ratio')
#
# # cumulative explained variance
# plt.figure()
# x = np.arange(1, len(pca.explained_variance_ratio_) + 1)
# plt.xticks(x)
# plt.plot(x, np.cumsum((pca.explained_variance_ratio_)))
# plt.title('cumulative explained variance versus the number of components')
# plt.grid()
# plt.show()
#
# # condition number and singular value
#
# # if condition is not significantly larger than one, the matrix is well-conditioned
#
# # In numerical analysis, the condition number of a function measures how much the output
# # value of the function can change for a small change in the input argument.
# # This is used to measure how sensitive a function is to changes or errors in the input,
# # and how much error in the output results from an error in the input.
#
# # The singular values are the diagonal entries of the S matrix and are arranged in descending order.
#
# H = np.matmul(X.T, X)
# _, d, _ = np.linalg.svd(H)
# print(f'Original Data: singular Values {d}')
# print(f'Original Data: condition number {LA.cond(X)}')
#
#
# H = np.matmul(X_PCA.T, X_PCA)
# _, d, _ = np.linalg.svd(H)
# print(f'Reduced Data: singular Values {d}')
# print(f'Reduced Data: condition number {LA.cond(X_PCA)}')
#
# # original date
# corcoe = df_weather.corr()
# sns.heatmap(corcoe, annot=True)
# plt.title('Correlation Coefficient between features-Original feature space')
# plt.show()
# # reduced data
# corcoe_reduced = pd.DataFrame(X_PCA).corr()
# sns.heatmap(corcoe_reduced, annot=True)
# plt.title('Correlation Coefficient between features-Reduced feature space')
# plt.show()
# #######################################
# # Normality test
# #######################################
# # histogram of numeric columns
# plt.figure(figsize=(16,9))
# for i in range(len(numericalColName)):
#     plt.subplot(4, 3, i + 1)
#     plt.hist(df_weather[numericalColName[i]].dropna().tolist(), bins=50)
#     plt.title(f'Histogram of {numericalColName[i]}')
#     plt.ylabel('Magnitude')
#     plt.xlabel('# of samples')
#     plt.grid()
# plt.tight_layout()
# plt.show()
# # QQplot of numeric columns
# figure, axes = plt.subplots(4, 3, figsize=(16,9))
# for i in range(len(numericalColName)):
#     qqplot(df_weather[numericalColName[i]], line='s', ax=axes[i//3, i%3])
#     axes[i//3, i%3].set_title(f'qqplot of {numericalColName[i]}')
# figure.suptitle('Multiple qq plots', fontsize=14, fontweight='bold')
# plt.tight_layout()
# plt.show()
# # K-S test
# # shapiro test
# from scipy.stats import shapiro
# for i in range(len(numericalColName)):
#     kstestX = st.kstest(df_weather[numericalColName[i]], 'norm')
#     shapiroX = shapiro(df_weather[numericalColName[i]])
#     print(f'K-S test of {numericalColName[i]}: statistics = {kstestX[0]} p-value = {kstestX[1]}')
#     print(f'K-S test of {numericalColName[i]}: {numericalColName[i]} dataset looks ')
#     print(f'Shapiro test: statistics = {shapiroX[0]} p-value = {shapiroX[1]}')
# #######################################
# # Data transformation
# #######################################
# transformedList = []
# for i in range(len(numericalColName)):
#     x = df_weather[numericalColName[i]]
#     transformedX = st.norm.ppf(st.rankdata(x).reshape(x.shape)/(len(x) + 1))
#     print(transformedX)
#     transformedList.append(transformedX)
# # histogram of numeric columns
# plt.figure(figsize=(16,9))
# for i in range(len(numericalColName)):
#     plt.subplot(4, 3, i + 1)
#     plt.hist(transformedList[i], bins=50)
#     plt.title(f'Histogram of {numericalColName[i]}')
#     plt.ylabel('Magnitude')
#     plt.xlabel('# of samples')
#     plt.grid()
# plt.tight_layout()
# plt.show()
# # QQplot of numeric columns
# figure, axes = plt.subplots(4, 3, figsize=(16,9))
# for i in range(len(numericalColName)):
#     qqplot(transformedList[i], line='s', ax=axes[i//3, i%3])
#     axes[i//3, i%3].set_title(f'qqplot of {numericalColName[i]}')
# figure.suptitle('Multiple qq plots', fontsize=14, fontweight='bold')
# plt.tight_layout()
# plt.show()
# # K-S test and shapiro
# for i in range(len(numericalColName)):
#     kstestX = st.kstest(transformedList[i], 'norm')
#     shapiroX = shapiro(transformedList[i])
#     print(f'K-S test of {numericalColName[i]}: statistics = {kstestX[0]} p-value = {kstestX[1]}')
#     print(f'K-S test of {numericalColName[i]}: {numericalColName[i]} dataset looks ')
#     print(f'Shapiro test: statistics = {shapiroX[0]} p-value = {shapiroX[1]}')
# #######################################
# # Heatmap & Pearson correlation coefficient matrix
# #######################################
# #Correlation coefficient matrix
# corcoe = df_weather.corr()
# sns.heatmap(corcoe, annot=True)
# plt.title('Correlation Coefficient of numeric columns')
# plt.show()
# #Scatter plot matrix.
# sns.set_theme(style="ticks")
# sns.pairplot(df_weather)
# plt.title("Scatter plot matrix of numeric columns")
# plt.show()
#######################################
# Statistics kde
#######################################
# penguins = sns.load_dataset("penguins")
# df_kde = df_weather[numericalColName]
# sns.pairplot(df_kde, kind="kde")
# plt.show()
#######################################
# Data visualization
#######################################
sns.set_theme(style='darkgrid')
showCityName = ['Albury']
df_showCity = df_weather[df_weather['Location'].isin(showCityName)]
# a. Line-plot
plt.figure(figsize=(16,9))
sns.lineplot(data=df_showCity, x='Date', y='MinTemp', hue='Location')
plt.title('Lineplot of minimum temperature in degrees celsius in Albury')
plt.show()
# Bar-plot : stack, group
