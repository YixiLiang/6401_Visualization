import seaborn as sns
import numpy as np
import pandas as pd

#######################################
# Q1 load data
#######################################
df = sns.load_dataset('titanic')
col = df.columns
print(col)
#######################################
# Q2 remove all nan
#######################################
df2 = df.dropna(how='any')
print(df2.describe())
print(df2.head())
#######################################
# Q3 replace all nan by mean
#######################################
df3 = df.fillna(value=df.mean())
print(df3.describe())
print(df3.head())
#######################################
# Q4 replace all nan by median
#######################################
df4 = df.fillna(value=df.median())
print(df4.describe())
print(df4.head())
#######################################
# Q5 passenger male female
#######################################
# a
totalPassenger = len(df3)
print(f'The total number of passengers on board was {totalPassenger}.')
# b
male = len(df3[df3['sex'] == 'male'])
print(
    f'From the total number of passengers onboard, there were {male / totalPassenger * 100:.2f}% male passengers onboard.')
# c
female = len(df3[df3['sex'] == 'female'])
print(
    f'From the total number of passengers onboard, there were {female / totalPassenger * 100:.2f}% female passengers onboard.')
# d
print(50 * '#')
#######################################
# Q6 passenger survival
#######################################
totalSurvived = len(df3[df3["survived"] == 1])
# a
print(f'Total number of survivals onboard was {totalSurvived}.')
# b
maleSurvived = len(df3[(df3['survived'] == 1) & (df3['sex'] == 'male')])
print(f'Out of {male} male passengers onboard only {maleSurvived / male * 100:.2f}% male was survived.')
# c
femaleSurvived = len(df3[(df3['survived'] == 1) & (df3['sex'] == 'female')])
print(f'Out of {female} female passengers onboard only {femaleSurvived / female * 100:.2f}% female was survived.')
# d
print(50 * '#')
#######################################
# Q7 passenger upper class survival
#######################################
# a
upperClassTotal = len(df3[df3['pclass'] == 1])
upperClassSurvived = len(df3[(df3['pclass'] == 1) & (df3['survived'] == 1)])
print(
    f'There were total number of {upperClassTotal} passengers with the upper-class ticket and only {upperClassSurvived / upperClassTotal * 100:.2f}% were survived.')
# b
upperClassMale = len(df3[(df3['pclass'] == 1) & (df3['sex'] == 'male')])
print(
    f'Out of {upperClassTotal} passengers with upper class ticket, {upperClassMale / upperClassTotal * 100:.2f}% passengers were male.')
# c
upperClassFemale = len(df3[(df3['pclass'] == 1) & (df3['sex'] == 'female')])
print(
    f'Out of {upperClassTotal} passengers with upper class ticket, {upperClassFemale / upperClassTotal * 100:.2f}% passengers were female.')
# d
upperClassMaleSurvived = len(df3[(df3['pclass'] == 1) & (df3['sex'] == 'male') & (df3['survived'] == 1)])
print(
    f'Out of {upperClassTotal} passengers with upper class ticket, {upperClassMaleSurvived / upperClassMale * 100:.2f}% male passengers were survived.')
# e
upperClassFemaleSurvived = len(df3[(df3['pclass'] == 1) & (df3['sex'] == 'female') & (df3['survived'] == 1)])
print(
    f'Out of {upperClassTotal} passengers with upper class ticket, {upperClassFemaleSurvived / upperClassFemale * 100:.2f}% female passengers were survived.')
# f
print(50 * '#')
#######################################
# Q8 Above50&Male
#######################################
df8 = df3.copy()
df8['Above50&Male'] = np.where((df3['sex'] == 'male') & (df3['age'] > 50), "Yes", "No")
above50Male = len(df8[df8["Above50&Male"] == "Yes"])
print(df8.head())
print(f'There are {above50Male} male passengers above 50 years old onboard.')
print(50 * '#')
#######################################
# Q9 Above50&Male&Survived
#######################################
df8['Above50&Male&Survived'] = np.where((df8['sex'] == 'male') & (df8['age'] > 50) & (df8['survived'] == 1), "Yes",
                                        "No")
above50MaleSurvived = len(df8[df8["Above50&Male&Survived"] == "Yes"])
print(df8.head())
print(f'There are {above50MaleSurvived} male passengers above 50 years old onboard are survived.')
print(
    f'The Survival percentage rate of male passengers onboard who are above 50 years old is {above50MaleSurvived / above50Male * 100:.2f}%.')
print(50 * '#')
#######################################
# Q10 Above50&Female and Above50&Female&Survived
#######################################
# part1
df8['Above50&Female'] = np.where((df3['sex'] == 'female') & (df3['age'] > 50), "Yes", "No")
above50Female = len(df8[df8["Above50&Female"] == "Yes"])
print(df8.head())
print(f'There are {above50Female} female passengers above 50 years old onboard.')
print(50 * '#')
# part2
df8['Above50&Female&Survived'] = np.where((df8['sex'] == 'female') & (df8['age'] > 50) & (df8['survived'] == 1), "Yes",
                                          "No")
above50FemaleSurvived = len(df8[df8["Above50&Female&Survived"] == "Yes"])
print(df8.head())
print(f'There are {above50FemaleSurvived} female passengers above 50 years old onboard are survived.')
print(
    f'The Survival percentage rate of female passengers onboard who are above 50 years old is {above50FemaleSurvived / above50Female * 100:.2f}%.')
