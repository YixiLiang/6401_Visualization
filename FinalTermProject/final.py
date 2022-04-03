import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

#######################################
# load data
#######################################
df = pd.read_csv('weatherAUS.csv')
print(df.describe())
print(df.isna().sum())
df.dropna(how='any', inplace=True)
print(df.isna().sum())