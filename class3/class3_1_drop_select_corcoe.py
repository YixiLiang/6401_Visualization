import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sn
from scipy.stats import pearsonr

np.random.seed(123)
# series
data_1D = pd.Series([1,2,3,4, np.nan])
print(data_1D)

# dataframe 1
index = np.arange(1,7)
# np.random.randn(6,4) 六行四列
data_2D = pd.DataFrame(data=np.random.randn(6,4), index=index, columns=list("ABCD"))
print(data_2D)
data_2D.info()

# dataframe 2
df = pd.DataFrame({
    'Gender' : ['female', 'female', 'male', 'male', 'male'],
    'Age' : [25, 18, "", 52, 33],
    'Weight' : [250, 180, np.nan, 210, 330],
    'Location' : ['CA', 'DC', 'VA', 'MA', "VA"],
    'Arrest Record' : ['No', 'Yes', 'Yes', 'No', np.nan],
})
print(df)
print(df.dtypes)
# df.head(n=5):
# This function returns the first n rows for the
# object based on position. It is useful for quickly testing if your
# object has the right type of data in it.
# • df.tail(n=5):
# This function returns last n rows from the object
# based on position
# • df.describe():
# 1. For numeric data, count, mean, std, min, max as well as lower,
# 50 and upper percentiles.
# 2. For object data, count, unique, top, and freq.
# • df.columns:Return the column labels of the DataFrame.
# • df.index:Immutable sequence used for indexing and alignment.
# • df.to numpy():gives a NumPy representation of the underlying
# data.
print(50*'#')

# iloc[]:is primarily integer position based (from 0 to length-1 of
# the axis), but may also be used with a boolean array.
# loc[]:Access a group of rows and columns by label(s) or a
# boolean array.loc[] is primarily label based, but may also be
# used with a boolean array.
# • Note using [[]] returns a DataFrame. For example: df[’Age’]
# will be Series type where df[[’Age’]] will be a DataFrame type.

#filter
# df tips male = df[df[’Gender’]==’Male]
# df tip more 20 = df[df[’tip’]>20]

# add column
# df[’new bill’] = df[’total bill’]-2

# drop column
# df.drop([’new bill’], axis = 1, inplace=True)

# logic
# df[’bucket’] = np.where(df[’total bill’]<10, ’Low’, ’High’)

# keep certain columns
# df[[”sex”, ”total bill”, ”tip”]]

# rename a column
# change A to a, B to c
# df.rename(columns={"A": "a", "B": "c"})

# Sorting by values
# df.sort values([’sex’, ’total bill 2’], inplace=True)
#
# index = df[df[’sex’]==’Male’].index
# df5 = df.drop(index)
#
# df.dropna(how=’any’)
# df.fillna(value=, method = ”)
# 1. fill by value = mean of the column
# 2. fill by value = the median of the column
# 3. fill by method = ’ffill’ non-null values forward or backward. 用上面的值填充
# 4. fill by method = ’bfill’

# replacing
# Replacing the nan by the mean of the column
# df9[’total bill 2’].fillna(value=df[’total bill 2’].mean(), inplace= True)
# Replacing the nan by the median of the column
# df9[’tip’].fillna(value=df[’tip’].median(), inplace= True)
# Replacing the empty cell by ’Male’
# df9[’sex’].replace(””,’Male’, inplace= True)





# df.dtypes
name = sn.get_dataset_names()
print(name)
df = sn.load_dataset('car_crashes')
col_name = df.columns
print(df.head(10))
print(df.describe())
print(df.columns)

#这一步可以将pandas.Series 转为np.array 就可以show
# total = df[col_name[0]].values
# plt.figure()
# # plt.plot(total)
# df[:10].plot(y='total')
# plt.show()

df_2 = df[['speeding', 'alcohol', 'ins_premium', 'total']]
plt.figure()
df_2.plot()
plt.title('raw data')
plt.show()

df2_z_score = (df_2 - df_2.mean()) / df_2.std()
plt.figure()
df2_z_score[30:].plot()
plt.title('z-score')
plt.show()


corrST, _ = pearsonr(df_2['speeding'], df_2["total"])
corrAT, _ = pearsonr(df_2['alcohol'], df_2["total"])
corrIT, _ = pearsonr(df_2['ins_premium'], df_2["total"])



# total = df_2['total'].values
# ins_premium = df_2['ins_premium'].values
# alcohol = df_2['alcohol'].values
# speeding = df_2['speeding'].values

print(f"The correlation_coefficient between speeding and total is {corrST:.2f}")
print(f"The correlation_coefficient between alcohol and total is {corrAT:.2f}")
print(f"The correlation_coefficient between ins_premium and total is {corrIT:.2f}")

plt.figure()
plt.scatter(x=df_2['speeding'], y=df_2["total"])
plt.title(f"The correlation_coefficient {corrST:.2f}")
plt.xlabel("speeding")
plt.ylabel("total")
plt.grid()
plt.show()

plt.figure()
plt.scatter(x=df_2['alcohol'], y=df_2["total"])
plt.title(f"The correlation_coefficient {corrAT:.2f}")
plt.xlabel("alcohol")
plt.ylabel("total")
plt.grid()
plt.show()

plt.figure()
plt.scatter(x=df_2['ins_premium'], y=df_2["total"])
plt.title(f"The correlation_coefficient {corrIT:.2f}")
plt.xlabel("alcohol")
plt.ylabel("total")
plt.grid()
plt.show()

