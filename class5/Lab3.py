import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import NullFormatter
from matplotlib.dates import MonthLocator, DayLocator, DateFormatter, ConciseDateFormatter

#######################################
# Q1 load data
#######################################
df1 = pd.read_csv('CONVENIENT_global_confirmed_cases.csv')
# print(df.describe())
# print(df.info())
df1 = df1.dropna(how="any")
print(df1.isna().sum())
#######################################
# Q2 China_sum
#######################################
# df['China_sum'] = df.loc[:,"China":"China.32"].astype('float').sum(axis=1)
df1['China_sum'] = df1.iloc[0:, 57:90].astype(float).sum(axis=1)
#######################################
# Q3 United Kingdom
#######################################
df1['United Kingdom_sum'] = df1.loc[:, "United Kingdom":"United Kingdom.10"].astype('float').sum(axis=1)
#######################################
# Q4 US confirmed Covid19 cases
#######################################
df1['Time'] = pd.to_datetime(df1.iloc[:, 0], format='%m/%d/%y', exact=False)

plt.figure(figsize=(16,8))
plt.plot(df1['Time'], df1['US'], label='US')
ax = plt.gca()

# add month but cannot add year
# monthLocator = MonthLocator()
# ax.xaxis.set_major_locator(monthLocator)
# ax.xaxis.set_major_formatter(DateFormatter('%b'))

# set the minor locator in 7 days
dayLocator = DayLocator(interval=7)
plt.xticks(df1['Time'][df1['Time'].dt.is_month_start == True],
           ['Feb\n2020', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov'])
ax.xaxis.set_minor_locator(dayLocator)
ax.xaxis.set_minor_formatter(NullFormatter())

plt.ylabel('Confirmed Covid19 cases')
plt.title('US confirmed Covid19 cases')
plt.legend()
plt.grid()
plt.show()
#######################################
# Q5
#######################################
plt.figure(figsize=(16,8))
plt.plot(df1['Time'], df1['United Kingdom_sum'], label='United Kingdom_sum')
plt.plot(df1['Time'], df1['China_sum'], label='China_sum')
plt.plot(df1['Time'], df1['US'], label='US')
plt.plot(df1['Time'], df1['Italy'], label='Italy')
plt.plot(df1['Time'], df1['Brazil'], label='Brazil')
plt.plot(df1['Time'], df1['Germany'], label='Germany')
plt.plot(df1['Time'], df1['India'], label='India')

ax = plt.gca()

plt.xticks(df1['Time'][df1['Time'].dt.is_month_start == True],
           ['Feb\n2020', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov'])
dayLocator = DayLocator(interval=7)
ax.xaxis.set_minor_locator(dayLocator)
ax.xaxis.set_minor_formatter(NullFormatter())

plt.xlabel('Year')
plt.xlabel('Year')
plt.ylabel('Confirmed Covid19 cases')
plt.title('Global confirmed Covid19 cases')
plt.legend()
plt.grid()
plt.show()
#######################################
# Q6 histogram plot of the graph of US
#######################################
plt.figure()
plt.hist(df1['US'], label='US', bins=50)
plt.xlabel('Confirmed Covid19 cases')
plt.ylabel('Frequency')
plt.title('US confirmed Covid19 cases')
plt.grid()
plt.legend()
plt.show()
#######################################
# Q7 subplot histogram plot of Q5
#######################################
countryList = [df1['United Kingdom_sum'], df1['China_sum'], df1['Germany'], df1['Brazil'], df1['India'], df1['Italy']]
countryName = ['United Kingdom', 'China', 'Germany', 'Brazil', 'India', 'Italy']
plt.figure()
for i in range(len(countryList)):
    plt.subplot(3, 2, i + 1)
    plt.hist(countryList[i], bins=50)
    plt.xlabel('Confirmed Covid19 cases')
    plt.ylabel('Frequency')
    plt.title(f'{countryName[i]} confirmed Covid19 cases')
plt.tight_layout()
plt.show()
#######################################
# Q8 highest mean var median
#######################################
countryList = [df1['US'], df1['United Kingdom_sum'], df1['China_sum'], df1['Germany'], df1['Brazil'], df1['India'],
               df1['Italy']]
countryName = ['US', 'United Kingdom', 'China', 'Germany', 'Brazil', 'India', 'Italy']

listMean = []
listVar = []
listMedian = []
for i in range(len(countryList)):
    listMean.append(countryList[i].mean())
    listVar.append(countryList[i].var())
    listMedian.append(countryList[i].median())

highestMean = countryName[listMean.index(max(listMean))]
highestVar = countryName[listVar.index(max(listVar))]
highestMedian = countryName[listMedian.index(max(listMedian))]
print(f'The country has the highest mean of of COVID confirmed cases is {highestMean}')
print(f'The country has the highest variance of of COVID confirmed cases is {highestVar}')
print(f'The country has the highest median of of COVID confirmed cases is {highestMedian}')
#######################################
# Section 2 titanic
#######################################
import seaborn as sns
df2 = sns.load_dataset('titanic')
#######################################
# Q1 remove na
#######################################
df2 = df2.dropna(how="any")
print(df2.head())
#######################################
# Q2 Pie plot of total people in titanic number
#######################################
male = len(df2[df2['sex'] == "male"])
female = len(df2[df2['sex'] == "female"])

label = ['Male', 'Female']
# 一定要和变量个数相同
explode = (0, 0.03)

plt.figure()
plt.pie([male, female], labels=label, explode=explode, autopct=lambda x: '{:.0f}'.format(x * len(df2) / 100))
plt.title('Pie chart of total people in Titanic')
plt.legend()
plt.axis('square')
plt.show()
#######################################
# Q3 Pie plot of total people in titanic percentage
#######################################
male = len(df2[df2['sex'] == "male"])
female = len(df2[df2['sex'] == "female"])

label = ['Male', 'Female']
explode = (0, 0.03)

plt.figure()
# 原始是%1.2f,f代表float; 末尾的%%是百分号转译
plt.pie([male, female], labels=label, explode=explode, autopct='%1.1f%%')
plt.title('Pie chart of total people in Titanic')
plt.legend()
plt.axis('square')
plt.show()
#######################################
# Q4 males who survived versus did not survive percentage
#######################################
maleSurvived = len(df2[(df2['sex'] == "male") & (df2['survived'] == 1)])
maleNotSurvived = male - maleSurvived
label = ['Male_survived', 'Male Not survived']
explode = (0, 0.03)

plt.figure()
# 原始是%1.2f,f代表float,2保留两位小数; 末尾的%%是百分号转译
plt.pie([maleSurvived, maleNotSurvived], labels=label, explode=explode, autopct='%1.1f%%')
plt.title('Pie Chart of Male survived in Titanic')
plt.legend()
plt.axis('square')
plt.show()
#######################################
# Q5 females who survived versus did not survive percentage
#######################################
femaleSurvived = len(df2[(df2['sex'] == "female") & (df2['survived'] == 1)])
femaleNotSurvived = female - femaleSurvived
label = ['Female_survived', 'Female Not survived']
explode = (0, 0.03)

plt.figure()
# 原始是%1.2f,f代表float,2保留两位小数; 末尾的%%是百分号转译
plt.pie([femaleSurvived, femaleNotSurvived], labels=label, explode=explode, autopct='%1.1f%%')
plt.title('Pie Chart of Female survived in Titanic')
plt.legend()
plt.axis('square')
plt.show()
#######################################
# Q6 percentage passengers with first class, second class and third-class tickets
#######################################
class1 = len(df2[df2['pclass'] == 1])
class2 = len(df2[df2['pclass'] == 2])
class3 = len(df2[df2['pclass'] == 3])
label = ['ticket class 1', 'ticket class 2', 'ticket class 3']
explode = (0, 0.1, 0.1)

plt.figure()
# 原始是%1.2f,f代表float,2保留两位小数; 末尾的%%是百分号转译
plt.pie([class1, class2, class3], labels=label, explode=explode, autopct='%1.1f%%')
plt.title('Pie Chart passengers based on the level')
plt.legend()
plt.axis('square')
plt.show()
#######################################
# Q7 Survival percentage rate based on the ticket class
#######################################
class1Survived = len(df2[(df2['pclass'] == 1) & (df2['survived'] == 1)])
class2Survived = len(df2[(df2['pclass'] == 2) & (df2['survived'] == 1)])
class3Survived = len(df2[(df2['pclass'] == 3) & (df2['survived'] == 1)])
label = ['class 1', 'class 2', 'class 3']
explode = (0, 0.1, 0.1)

plt.figure()
# 原始是%1.2f,f代表float,2保留两位小数; 末尾的%%是百分号转译
plt.pie([class1Survived, class2Survived, class3Survived], labels=label, explode=explode, autopct='%1.1f%%')
plt.title('Survival rate based on the ticket class')
plt.legend()
plt.axis('square')
plt.show()
#######################################
# Q8 first-class ticket
#######################################
class1NotSurvived = class1 - class1Survived
label = ['Survival rate','Death rate']
explode = (0, 0.03)

plt.figure()
# 原始是%1.2f,f代表float,2保留两位小数; 末尾的%%是百分号转译
plt.pie([class1Survived, class1NotSurvived], labels=label, explode=explode, autopct='%1.1f%%')
plt.title('Survival & Death Rate: Ticket class 1')
plt.legend()
plt.axis('square')
plt.show()
#######################################
# Q9 second-class ticket
#######################################
class2NotSurvived = class2 - class2Survived
label = ['Survival rate','Death rate']
explode = (0, 0.03)

plt.figure()
# 原始是%1.2f,f代表float,2保留两位小数; 末尾的%%是百分号转译
plt.pie([class2Survived, class2NotSurvived], labels=label, explode=explode, autopct='%1.1f%%')
plt.title('Survival & Death Rate: Ticket class 2')
plt.legend()
plt.axis('square')
plt.show()
#######################################
# Q10 third-class ticket
#######################################
class3NotSurvived = class3 - class3Survived
label = ['Survival rate','Death rate']
explode = (0, 0.03)

plt.figure()
# 原始是%1.2f,f代表float,2保留两位小数; 末尾的%%是百分号转译
plt.pie([class3Survived, class3NotSurvived], labels=label, explode=explode, autopct='%1.1f%%')
plt.title('Survival & Death Rate: Ticket class 3')
plt.legend()
plt.axis('square')
plt.show()
#######################################
# Q11 subplot
#######################################
fig, axs = plt.subplots(3,3,figsize=(16,8))
# figure 1
label00 = ['Male', 'Female']
explode00 = (0, 0.03)
axs[0,0].pie([male, female], labels=label00, explode=explode00, autopct=lambda x: '{:.0f}'.format(x * len(df2) / 100))
axs[0,0].set_title('Pie chart of total people in Titanic')
axs[0,0].legend()
# figure 2
axs[0,1].pie([male, female], labels=label00, explode=explode00, autopct='%1.1f')
axs[0,1].set_title('Pie chart of total people in Titanic')
axs[0,1].legend()
# figure 3
label03 = ['Male_survived', 'Male Not survived']
axs[0,2].pie([maleSurvived, maleNotSurvived], labels=label03, explode=explode00, autopct='%1.1f%%')
axs[0,2].set_title('Pie Chart of Male survived in Titanic')
axs[0,2].legend()
# figure 4
label10 = ['Female_survived', 'Female Not survived']
axs[1,0].pie([femaleSurvived, femaleNotSurvived], labels=label10, explode=explode00, autopct='%1.1f%%')
axs[1,0].set_title('Pie Chart of Female survived in titanic')
axs[1,0].legend()
# figure 5
explode11 = (0, 0.1, 0.1)
label11 = ['ticket class 1', 'ticket class 2', 'ticket class 3']
axs[1,1].pie([class1, class2, class3], labels=label11, explode=explode11, autopct='%1.1f%%')
axs[1,1].set_title('Pie Chart passengers based on the level')
axs[1,1].legend()
# figure 6
label12 = ['class 1', 'class 2', 'class 3']
axs[1,2].pie([class1Survived, class2Survived, class3Survived], labels=label12, explode=explode11, autopct='%1.1f%%')
axs[1,2].set_title('Survival rate based on the ticket class')
axs[1,2].legend()
# figure 7
label20 = ['Survival rate','Death rate']
axs[2,0].pie([class1Survived, class1NotSurvived], labels=label20, explode=explode00, autopct='%1.1f%%')
axs[2,0].set_title('Survival & Death Rate: Ticket class 1')
axs[2,0].legend()
# figure 8
axs[2,1].pie([class2Survived, class2NotSurvived], labels=label20, explode=explode00, autopct='%1.1f%%')
axs[2,1].set_title('Survival & Death Rate: Ticket class 2')
axs[2,1].legend()
# figure 9
axs[2,2].pie([class3Survived, class3NotSurvived], labels=label20, explode=explode00, autopct='%1.1f%%')
axs[2,2].set_title('Survival & Death Rate: Ticket class 3')
# axs[2,2].legend(loc="upper left")
axs[2,2].legend()
plt.axis('square')
plt.tight_layout()
plt.show()





