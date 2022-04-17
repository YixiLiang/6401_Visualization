import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import StandardScaler
from numpy import linalg as LA
import seaborn as sns

#######################################
# Q1 load data
#######################################
df = px.data.stocks()
#######################################
# Q2 lineplot stock values versus time
#######################################
fig = px.line(df, x='date', y=['GOOG', 'AAPL', 'AMZN', 'FB', 'NFLX', 'MSFT'])
fig.update_layout(title='Stock Values - Major Tech company',
                  font_color='red',
                  legend_title_font_color='green',
                  font_family='Courier New',
                  title_font_family='Times New Roman')
fig.show()
#######################################
# Q3 histogram stock values versus time
#######################################
go.Histogram(name='legend title')
fig = make_subplots(rows=3, cols=2)
fig.add_trace(go.Histogram(x=df['GOOG'], nbinsx=50, name='GOOG'), row=1, col=1)
fig.add_trace(go.Histogram(x=df['AAPL'], nbinsx=50, name='AAPL'), row=1, col=2)
fig.add_trace(go.Histogram(x=df['AMZN'], nbinsx=50, name='AMZN'), row=2, col=1)
fig.add_trace(go.Histogram(x=df['FB'], nbinsx=50, name='FB'), row=2, col=2)
fig.add_trace(go.Histogram(x=df['NFLX'], nbinsx=50, name='NFLX'), row=3, col=1)
fig.add_trace(go.Histogram(x=df['MSFT'], nbinsx=50, name='MSFT'), row=3, col=2)
fig.show()
#######################################
# Q4 PCA analysis
#######################################
# a
X = StandardScaler().fit_transform(df.iloc[:, 1:].values)

# b
H = np.matmul(X.T, X)
_, d, _ = np.linalg.svd(H)
print(f'Original Data: singular Values {d}')
print(f'Original Data: condition number {LA.cond(X)}')

# c
corcoe = df.corr()
sns.heatmap(corcoe, annot=True)
plt.title('Correlation Coefficient between features-Original feature space')
plt.show()

# d
# original
# Singular value decomposition: two value become one value
pca_original = PCA(svd_solver='full')
pca_original.fit(X)
X_PCA_original = pca_original.transform(X)
print('Original Dim', X.shape)
print('Transformed Dim', X_PCA_original.shape)
print(f'pca explained variance ratio {pca_original.explained_variance_ratio_}')
# reduced
pca = PCA(n_components='mle', svd_solver='full')
pca.fit(X)
X_PCA = pca.transform(X)
print('Original Dim', X.shape)
print('Transformed Dim', X_PCA.shape)
print(f'pca explained variance ratio when using mle {pca.explained_variance_ratio_}')

# e
print(
    'Two features should be remove from per PCA analysis, because the top 4 feature have explained over 95% variance ratio')

# f

plt.figure()
x = np.arange(1, len(pca.explained_variance_ratio_) + 1)
plt.xticks(x)
plt.plot(x, np.cumsum((pca.explained_variance_ratio_)))
plt.title('cumulative explained variance versus the number of components')
plt.grid()
plt.show()

# g
corcoe_reduced = pd.DataFrame(X_PCA).corr()
sns.heatmap(corcoe_reduced, annot=True)
plt.title('Correlation Coefficient between features-Reduced feature space')
plt.show()

# h
a, b = X_PCA.shape
columns = []
for i in range(1, b + 1):
    columns.append(f'Pricipal col {i}')
df_PCA = pd.DataFrame(data=X_PCA, columns=columns)
df_PCA = pd.concat([df_PCA, df['date']], axis=1)
print(df_PCA.head())

# i
fig = px.line(df_PCA, x='date', y=columns)
fig.update_layout(title='Transformed feature',
                  font_color='red',
                  legend_title_font_color='green',
                  font_family='Courier New',
                  title_font_family='Times New Roman')
fig.show()

# j
go.Histogram(name='legend title')
fig = make_subplots(rows=2, cols=2)
fig.add_trace(go.Histogram(x=df_PCA[columns[0]], nbinsx=50, name='GOOG'), row=1, col=1)
fig.add_trace(go.Histogram(x=df_PCA[columns[1]], nbinsx=50, name='AAPL'), row=1, col=2)
fig.add_trace(go.Histogram(x=df_PCA[columns[2]], nbinsx=50, name='AMZN'), row=2, col=1)
fig.add_trace(go.Histogram(x=df_PCA[columns[3]], nbinsx=50, name='FB'), row=2, col=2)
fig.show()

# k
fig = px.scatter_matrix(
    df,
    dimensions=['GOOG', 'AAPL', 'AMZN', 'FB', 'NFLX', 'MSFT']
)
fig.update_traces(diagonal_visible=False)
fig.show()

fig = px.scatter_matrix(
    df_PCA,
    dimensions=columns
)
fig.update_traces(diagonal_visible=False)
fig.show()
