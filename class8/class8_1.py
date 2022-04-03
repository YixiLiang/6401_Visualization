import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.express as px
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from numpy import linalg as LA

url = 'https://raw.githubusercontent.com/rjafari979/Complex-Data-Visualization-/main/autos.clean.csv'
df = pd.read_csv(url)
print(f'The original shape of the data set is {df.shape}')
X = df[df._get_numeric_data().columns.to_list()[:-1]]
Y = df['price']
###############
# PCA Analysis 看图说话 y 代表 culmuative explained value
###############
X = StandardScaler().fit_transform(X)
pca = PCA(n_components=7, svd_solver='full')
pca.fit(X)
X_PCA = pca.transform(X)
print('Original Dim', X.shape)
print('Transformed Dim', X_PCA.shape)
print(f'pca explained variance ratio {pca.explained_variance_ratio_}')
plt.figure()
x = np.arange(1, len(pca.explained_variance_ratio_) + 1)
plt.xticks(x)
plt.plot(x, np.cumsum((pca.explained_variance_ratio_)))
plt.grid()
plt.show()
print('*'*50)
#########################################################
# SVD Analysis and condition number on the original Data
########################################################
H = np.matmul(X.T, X)
_, d, _ = np.linalg.svd(H)
print(f'Original Data: singular Values {d}')
print(f'Original Data: condition number {LA.cond(X)}')
print('*'*50)
#########################################################
# SVD Analysis and condition number on the Transformed Data
########################################################
H_PCA = np.matmul(X_PCA.T, X_PCA)
_, d_PCA, _ = np.linalg.svd(H_PCA)
print(f'Transformed Data: singular Values {d_PCA}')
print(f'Transformed Data: condition number {LA.cond(X_PCA)}')
print('*'*50)
#########################################################
# Construction of new dataset reduced dim dataset
########################################################
a, b = X_PCA.shape
columns = []
for i in range(b):
    columns.append(f'Pricipal Col {i}')
df_PCA = pd.DataFrame(data=X_PCA, columns=columns)
df_PCA = pd.concat([df_PCA, Y], axis=1)
