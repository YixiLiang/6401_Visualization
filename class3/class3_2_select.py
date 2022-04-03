import seaborn as sn
import numpy as np


name = sn.get_dataset_names()
print(name)
df = sn.load_dataset('titanic')
df.dropna(how='any', inplace=True)
# male and female
Survived_status = df.iloc[:,0]
df_male = df[df['sex'] == 'male']
print(f'male {len(df_male)/len(df):.2f}')
print(f'female {1-len(df_male)/len(df):.2f}')

df_50 = df[df['age'] > 50]
print(f'Passenger 50 above {len(df_50)/len(df):.2f}')
print(f'Passenger 50 below {1-len(df_50)/len(df):.2f}')

df_female = df[df['sex'] == 'female']
df_female_survived = df[(df['sex'] == 'female')&(df['survived'] == 1)]
df_male = df[df['sex'] == 'male']
df_male_survived = df[(df['sex'] == 'male')&(df['survived'] == 1)]
print('#'*50)
print(f'female survived {len(df_female_survived)/len(df_female):.2f}%')
print(f'male survived {len(df_male_survived)/len(df_male):.2f}%')

# drop columns
col = df.columns
df['age_status'] = np.where(df['age']>18,"Adult","Teenager")
df.drop(col[4:], axis=1, inplace=True)

# rename
df.rename({'age_status':'passenger_info'}, axis=1, inplace=True)

ageMean = df['age'] / df['age'].mean()
df.insert(4, "age_mean", ageMean)

name = sn.get_dataset_names()
print(name)
df = sn.load_dataset('diamonds')
carat = df.pop('carat')

index = np.arange(10, len(df))
df1 = df.drop(index)

indexE = df[df['color'] == 'E'].index
df2 = df.drop(indexE)