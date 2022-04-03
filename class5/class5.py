import matplotlib.pyplot as plt
import numpy as np
from statsmodels.graphics.gofplots import qqplot

label = ['C', 'C++', 'java', 'Python', 'PHP']
score = [23, 17, 35, 29, 12]

# pie chart
fig, ax = plt.subplots(1,1)
explode = (.03,.03,.3,.03,.03) # 越大越远离中心
ax.pie(score, labels = label, explode=explode, autopct='%1.2f%%')
ax.axis('square') # xy轴相同，图片就是正方形
plt.show()

# bar plot
# plt.bar(x, height, width, bottom, align)
# x = xlabel, height = y number, width default=0.8, bottom = y start, align {'center', 'edge'}, default: 'center'
plt.figure()
plt.bar(label, score)
plt.xlabel('Language')
plt.ylabel('Score')
plt.show()


# stack bar plot
score_men = np.array([23, 17, 35, 29, 12])
score_women = np.array([35, 25, 10, 15, 30])
score_test = np.array([45, 10, 12, 19, 9])
plt.bar(label, score_men, label='Men')
# bottom 加在另一个数据下
plt.bar(label, score_women, bottom=score_men, label='Women')
# 必须是np.array
plt.bar(label, score_test, bottom=score_men + score_women, label='test')
plt.xlabel('Language')
plt.ylabel('Score')
plt.legend()
plt.title('Simple stack bar plot')
plt.show()
# df.plot(x='Team', kind='bar', stacked=True,
#         title='Stacked Bar Graph by dataframe')


#Group bar plot
width = 0.4
fig, ax = plt.subplots(1,1)
x = np.arange(len(label))
ax.bar(x - width/2, score_men, width, label='Men')
ax.bar(x + width/2, score_women, width, label='Women')
ax.set_xlabel('Language')
ax.set_ylabel('Score')
# 设置x为0-4，xticklabels才可以从0开始
ax.set_xticks(x)
ax.set_xticklabels(label)
ax.legend()
ax.set_title('Simple stack bar plot')
plt.show()

# horizontal
width = 0.4
fig, ax = plt.subplots(1,1)
x = np.arange(len(label))
ax.barh(x - width/2, score_men, width, label='Men')
ax.barh(x + width/2, score_women, width, label='Women')
ax.set_ylabel('Language')
ax.set_xlabel('Score')
# 设置x为0-4，xticklabels才可以从0开始
ax.set_yticks(x)
ax.set_yticklabels(label)
ax.legend()
ax.set_title('Simple stack bar plot')
plt.show()

# horizontal stack plot
width = 0.4
fig, ax = plt.subplots(1,1)
x = np.arange(len(label))
ax.barh(x, score_men, width, label='Men')
ax.barh(x, score_women, width,left= score_men, label='Women')
ax.set_ylabel('Language')
ax.set_xlabel('Score')
# 设置x为0-4，xticklabels才可以从0开始
ax.set_yticks(x)
ax.set_yticklabels(label)
ax.legend()
ax.set_title('Simple stack bar plot')
plt.show()


# box plot
np.random.seed(10)
data = np.random.normal(100,20,1000)
plt.figure()
plt.boxplot(data)
plt.xticks([1])
plt.ylabel('Average')
plt.xlabel('Data Number')
plt.grid()
plt.title('Box plot')
plt.show()

# # histogram
# plt.figure()
# # bins 多少个柱子
# plt.hist(data, bins=10)
# plt.show()

# box plot
np.random.seed(10)
data1 = np.random.normal(100,10,1000)
data2 = np.random.normal(90,20,1000)
data3 = np.random.normal(80,30,1000)
data4 = np.random.normal(70,40,1000)
data = [data1,data2,data3,data4]

plt.figure()
plt.boxplot(data)
plt.xticks([1,2,3,4])
plt.ylabel('Average')
plt.xlabel('Data Number')
plt.grid()
plt.title('Box plot')
plt.show()
#
# plt.figure()
# # bins 多少个柱子
# plt.hist(data, bins=50)
# plt.show()

# QQ-plot
np.random.seed(10)
data1 = np.random.normal(0,1,1000)
plt.figure()
qqplot(data1, line='45')
plt.title('QQ-plot')
plt.show()
# line{None, “45”, “s”, “r”, “q”}
# Options for the reference line to which the data is compared:
# “45” - 45-degree line
# “s” - standardized line, the expected order statistics are scaled by the standard deviation of the given sample and have the mean added to them
# “r” - A regression line is fit
# “q” - A line is fit through the quartiles.
#
# plt.figure()
# plt.hist(data1, bins=50)
# plt.show()

#Area plot
x = range(1,6)
# y = [1,4,6,8,4]
y = np.random.normal(10,2,len(x))
plt.plot(x,y,color='blue',lw=3)
plt.fill_between(x,y,alpha=.3, label='Area')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='upper left')
plt.title('Simple are plot')
plt.grid()
plt.show()

x = np.linspace(0, 2*np.pi, 41)
y = np.exp(np.sin(x))
(markers, stemlines, baseline) = plt.stem(y, label='exp(sin(x))')
plt.setp(markers, color='red', linestyle = 'solid')
plt.setp(baseline, color='grey',lw=2, linestyle = '-')
plt.setp(stemlines, color='yellow',lw=2, linestyle = ':')
plt.title('Sinusodial function')
plt.xlabel('x-axis')
plt.ylabel('y-label')
plt.grid()
plt.show()
# '-'
# solid line
# '--'
# dashed line
# '-.'
# dash-dot line
# ':'
# dotted line
