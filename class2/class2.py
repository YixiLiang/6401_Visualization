import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

print(sns.get_dataset_names())
df = sns.load_dataset("tips")
df.describe()

print(df.head)
col_name = df.columns

total_meal_mean = np.mean(df['total_bill'].values)
total_meal_std = np.std(df['total_bill'].values)
total_meal_var = np.var(df['total_bill'].values)

tip_mean = np.mean(df['tip'].values)
tip_std = np.std(df['tip'].values)
tip_var = np.var(df['tip'].values)

meal = df['total_bill']
tip = df['tip']

print(f'The mean of the total meal is {total_meal_mean:.2f}')
print(f'The variance of the total meal is {total_meal_var:.2f}')
print(f'The std of the total meal is {total_meal_std:.2f}')

print(f'The mean of the tip mean is {tip_mean:.2f}')
print(f'The std of the tip mean is {tip_std:.2f}')
print(f'The std of the tip meal is {tip_var:.2f}')


plt.hist(df['tip'], label="tip")
plt.hist(df['total_bill'], label="total_bill")
plt.legend()
plt.title("Histrogram Plot")
plt.grid()
plt.show()
