import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

df = px.data.iris()
features = df.columns.tolist()[:-2]

X = df[features].values
X = StandardScaler().fit_transform(X)

pca = PCA(n_components=4, svd_solver='full')
pca.fit(X)
X_PCA = pca.transform(X)
print('Original Dim', X.shape)
print('Transformed Dim', X_PCA.shape)
print(f'pca explained variance ratio {pca.explained_variance_ratio_}')

plt.figure()
x = np.arange(1,len(pca.explained_variance_ratio_)+1)
plt.xticks(x)
plt.plot(x,np.cumsum((pca.explained_variance_ratio_)))
plt.show()


