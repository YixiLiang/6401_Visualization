import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

#######################################
# Q1 load data
#######################################
df = sns.load_dataset('penguins')
print(df.tail())
print(df.describe())
#######################################
# Q2 clean data
#######################################
print(df.isna().sum())
df.dropna(how='any', inplace=True)
print(df.isna().sum())
#######################################
# Q3 histogram plot “flipper_length_mm”
#######################################
sns.set_theme(style='darkgrid')
sns.histplot(data=df['flipper_length_mm'])
plt.xlabel('Flipper length mm')
plt.ylabel('Frequency')
plt.title('Histogram of Flipper length mm')
plt.show()
print(
    'This data set about Flipper length is not normal distribution. It has two peaks. First is around 190, and second is around 210.')
# #######################################
# # Q4 histogram plot “flipper_length_mm” binwidth
# #######################################
sns.histplot(data=df['flipper_length_mm'], binwidth=3)
plt.xlabel('Flipper length mm')
plt.ylabel('Frequency')
plt.title('Histogram of Flipper length mm')
plt.show()
# #######################################
# # Q5 histogram plot “flipper_length_mm” bin30
# #######################################
sns.histplot(data=df['flipper_length_mm'], bins=30)
plt.xlabel('Flipper length mm')
plt.ylabel('Frequency')
plt.title('Histogram of Flipper length mm')
plt.show()
# #######################################
# # Q6 histogram plot “flipper_length_mm” hue
# #######################################
sns.displot(data=df, x='flipper_length_mm', hue='species')
plt.xlabel('Flipper length mm')
plt.ylabel('Frequency')
plt.title('Histogram of Flipper length mm per species')
plt.show()
print(
    'Obviously the flipper_length_mm include three species, each specie has their own distribution. \n'
    'Adelie distribute from 170-210. Chinstrap distribute from 180-210. Gentoo distribute from 200-230.')
# #######################################
# # Q7 histogram plot “flipper_length_mm” ??
# #######################################
sns.displot(data=df,x='flipper_length_mm', hue='species', element="step")
plt.xlabel('Flipper length mm')
plt.ylabel('Frequency')
plt.title('Histogram of Flipper length mm per species')
plt.show()
# #######################################
# # Q8 histogram plot “flipper_length_mm” stack
# #######################################
sns.displot(data=df, x='flipper_length_mm', hue='species', multiple='stack')
plt.xlabel('Flipper length mm')
plt.ylabel('Frequency')
plt.title('Histogram of Flipper length mm per species in stack')
plt.show()
print(
    'This plot is better than Q6 plot, since it can show the overlap area clearly.\n'
    'And we can see the portion of different species in specific range. \n'
    'Adelie distribute from 170-210. Chinstrap distribute from 180-210. Gentoo distribute from 200-230.')
# #######################################
# # Q9 histogram plot “flipper_length_mm” dodge
# #######################################
sns.displot(data=df, x='flipper_length_mm', hue='sex', multiple='dodge')
plt.xlabel('Flipper length mm')
plt.ylabel('Frequency')
plt.title('Histogram of Flipper length mm per sex in dodge')
plt.show()
print(
    'The flipper_length_mm is not normal distribution in sex. When flipper length around 180-200, female slightly more than male. \n'
    'When flipper length around 210-230, there are more female in around 210 and the rest of them are male more than female.')
# #######################################
# # Q10 histogram plot “flipper_length_mm” col
# #######################################
sns.displot(data=df, x='flipper_length_mm', col='sex')
plt.xlabel('Flipper length mm')
plt.show()
print('The most frequent range of flipper length in mm for male is around 190-200 and female is around 185-195. ')
# #######################################
# # Q11 histogram plot “flipper_length_mm” density hue species
# #######################################
sns.displot(data=df, x='flipper_length_mm', col='species', stat='density')
plt.xlabel('Flipper length mm')
plt.title('Histogram of Flipper length mm per species in density')
plt.show()
print('Gentoo has the largest flipper length and the approximate range is 200-230.')
# #######################################
# # Q12 histogram plot “flipper_length_mm” density hue sex
# #######################################
sns.displot(data=df, x='flipper_length_mm', hue='sex', stat='density')
plt.xlabel('Flipper length mm')
plt.title('Histogram of Flipper length mm per sex in density')
plt.show()
print('Male has the larger flipper length and the approximate range is 180-230.')
# #######################################
# # Q13 histogram plot “flipper_length_mm” probability hue species
# #######################################
sns.displot(data=df, x='flipper_length_mm', hue='species', stat='probability')
plt.xlabel('Flipper length mm')
plt.title('Histogram of Flipper length mm per sex in density')
plt.show()
print('Adelie and 190-195 is more probable.')
#######################################
# Q14 Kde plot “flipper_length_mm” probability hue species
#######################################
sns.displot(data=df, x='flipper_length_mm', hue='species', kind='kde')
plt.xlabel('Flipper length mm')
plt.title('Kde of Flipper length mm per species')
plt.show()
#######################################
# Q15 Kde plot “flipper_length_mm” probability hue sex
#######################################
sns.displot(data=df, x='flipper_length_mm', hue='sex', kind='kde')
plt.xlabel('Flipper length mm')
plt.title('Kde of Flipper length mm per sex')
plt.show()
#######################################
# Q16 Kde plot “flipper_length_mm” probability hue species multiple stack
#######################################
sns.displot(data=df, x='flipper_length_mm', hue='species', kind='kde', multiple='stack')
plt.xlabel('Flipper length mm')
plt.title('Kde of Flipper length mm per species in stack')
plt.show()
#######################################
# Q17 Kde plot “flipper_length_mm” probability hue sex multiple stack
#######################################
sns.displot(data=df, x='flipper_length_mm', hue='sex', kind='kde', multiple='stack')
plt.xlabel('Flipper length mm')
plt.title('Kde of Flipper length mm per sex in stack')
plt.show()
#######################################
# Q18 Kde plot “flipper_length_mm” probability hue species multiple stack fill True
#######################################
sns.kdeplot(data=df, x='flipper_length_mm', hue='species', fill=True)
plt.xlabel('Flipper length mm')
plt.title('Kde of Flipper length mm per species with fill')
plt.show()
print(
    'Adelie is normally distribution mu=190. Chinstrap is normally distribution mu=195. Gentoo is normally distribution mu=215.')
#######################################
# Q19 Kde plot “flipper_length_mm” probability hue sex multiple stack fill True
#######################################
sns.kdeplot(data=df, x='flipper_length_mm', hue='sex', fill=True)
plt.xlabel('Flipper length mm')
plt.title('Kde of Flipper length mm per sex with fill ')
plt.show()
print('Male and Female are not normal distribution, and Male on average have larger flipper length than Female.')
#######################################
# Q20 Scatter plot “bill_length_mm” and "bill_depth_mm"
#######################################
sns.lmplot(data=df, x='bill_length_mm', y='bill_depth_mm')
plt.title('Scatter plot of bill_depth_mm and bill_length_mm')
plt.show()
print('They are negative correlation. When bill length larger bill depth smaller.')
#######################################
# Q21 count plot bar plot island hue species
#######################################
sns.countplot(data=df, x='island', hue='species')
plt.title('Count plot of island hue species')
plt.show()
print('Adelie distribute in all three islands, Chinstrap distribute only in Dream island, Gentoo distribute only in Biscoe island.')
#######################################
# Q22 count plot bar plot sex
#######################################
sns.countplot(data=df, x='sex', hue='species')
plt.title('Count plot of sex hue species')
plt.show()
print('The number of Male and Female of all these species are almost the same.\n'
      'Only Gentoo have slightly smaller number of female than male.')
#######################################
# Q23 ‘bill_length_mm’ versus ‘bill_depth_mm’
#######################################
sns.kdeplot(data=df,x='bill_length_mm',y='bill_depth_mm', hue='sex', fill=True)
plt.title('bill_depth_mm vs bill_length_mm')
plt.show()
#######################################
# Q24 flipper_length_mm vs bill_length_mm
#######################################
sns.kdeplot(data=df,x='bill_length_mm',y='flipper_length_mm', hue='sex', fill=True)
plt.title('flipper_length_mm vs bill_length_mm')
plt.show()
#######################################
# Q25 flipper_length_mm vs bill_depth_mm
#######################################
sns.kdeplot(data=df,x='flipper_length_mm',y='bill_depth_mm', hue='sex', fill=True)
plt.title('bill_depth_mm vs flipper_length_mm')
plt.show()
#######################################
# Q26 three
#######################################
plt.figure(figsize=(8,16))
plt.subplot(3,1,1)
sns.kdeplot(data=df,x='bill_length_mm',y='bill_depth_mm', hue='sex', fill=True)
plt.title('bill_depth_mm vs bill_length_mm')
plt.subplot(3,1,2)
sns.kdeplot(data=df,x='bill_length_mm',y='flipper_length_mm', hue='sex', fill=True)
plt.title('flipper_length_mm vs bill_length_mm')
plt.subplot(3,1,3)
sns.kdeplot(data=df,x='flipper_length_mm',y='bill_depth_mm', hue='sex', fill=True)
plt.title('bill_depth_mm vs flipper_length_mm')
plt.show()
#######################################
# Q27 "bill_length_mm” versus “bill_depth_mm”
#######################################
sns.histplot(data=df,x='bill_length_mm',y='bill_depth_mm', hue='sex')
plt.title('bill_depth_mm vs bill_length_mm')
plt.show()
#######################################
# Q28 "bill_length_mm” versus “flipper_length_mm”
#######################################
sns.histplot(data=df,x='bill_length_mm',y='flipper_length_mm', hue='sex')
plt.title('flipper_length_mm vs bill_length_mm')
plt.show()
#######################################
# Q29 "flipper_length_mm’ versus” versus “‘bill_depth_mm”
#######################################
sns.histplot(data=df,x='flipper_length_mm',y='bill_depth_mm', hue='sex')
plt.title('bill_depth_mm vs flipper_length_mm')
plt.show()