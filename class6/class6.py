import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# line plot
# sns.set_theme(style='whitegrid')
# sns.set_theme(style='dark')
# sns.set_theme(style='white')
# sns.set_theme(style='ticks')
sns.set_theme(style='darkgrid')
tips = sns.load_dataset('tips')
flights = sns.load_dataset('flights')
diamonds = sns.load_dataset('diamonds')
penguins = sns.load_dataset('penguins')
titanic = sns.load_dataset('titanic')

print(flights.describe())
sns.lineplot(data=flights, x='year', y='passengers', hue='month')
plt.show()
# boxplot
data = np.random.normal(size=(20, 6)) + np.arange(6) / 2
sns.boxplot(data=data)
plt.show()
# scatterplot
sns.relplot(data=tips,
            x='total_bill',
            y='tip',
            hue='sex')
plt.show()
# boxplot
sns.boxplot(data=tips[['tip', 'total_bill']])
plt.show()
# day
sns.relplot(data=tips,
            x='total_bill',
            y='tip',
            hue='day')
plt.show()
# flights
sns.relplot(data=flights,
            x='year',
            y='passengers',
            kind='line',
            hue='month')
plt.show()
#
sns.relplot(data=tips,
            x='total_bill',
            y='tip',
            kind='scatter',
            col='time')
plt.show()
#
sns.relplot(data=tips,
            x='total_bill',
            y='tip',
            kind='scatter',
            hue='day',
            col='smoker')
plt.show()
#
sns.relplot(data=tips,
            x='total_bill',
            y='tip',
            kind='scatter',
            hue='day',
            col='time',
            row='smoker')
plt.show()
# regrssion plot
sns.regplot(data=tips,
            x='total_bill',
            y='tip')
plt.show()

# heatmap
df = flights.pivot('month', 'year', 'passengers')
sns.heatmap(df, annot=True, fmt='d', cmap = 'YlGnBu', center=df.loc['Jan',1955])
plt.show()
# countplot/hist
sns.countplot(data=tips,
              x = 'day')
plt.show()
#
sns.countplot(data=tips,
              x = 'day',
              order = tips['day'].value_counts().index)
plt.show()
#
sns.countplot(data=tips,
              x = 'day',
              order = tips['day'].value_counts(ascending=True).index)
plt.show()
# diamond clarity
sns.countplot(data=diamonds,
              y = 'clarity',
              order = diamonds['clarity'].value_counts(ascending=True).index,
              )
plt.show()
# diamond cut
sns.countplot(data=diamonds,
              y = 'cut',
              order = diamonds['cut'].value_counts(ascending=True).index,
              )
plt.title('cut per sales count')
plt.show()

# diamond color
sns.countplot(data=diamonds,
              y = 'color',
              order = diamonds['color'].value_counts(ascending=True).index,
              )
plt.show()

#titanic
sns.color_palette('Paired')
sns.countplot(data=titanic,
              y = 'class',
              hue='who',
              palette='light:#5A9')
plt.show()
#
sns.color_palette('Paired')
sns.countplot(data=titanic,
              y = 'class',
              hue='who',
              palette=['#b3b3b3','#d58c32','#b9f2f0'])
plt.show()
#
sns.pairplot(data = penguins,
             hue='sex')
plt.show()
# countplot
sns.countplot(data=tips,
              x = 'sex',
              hue='smoker',
              palette='Set2')
plt.show()
# kde
sns.kdeplot(data=tips,
            x = 'total_bill',
            bw_adjust=0.2)
plt.show()
# kde
sns.kdeplot(data=tips,
            x = 'total_bill',
            bw_adjust=5, cut = 0)
plt.show()
# kde
sns.kdeplot(data=tips,
            x = 'total_bill',
            hue='time')
plt.show()
#kde
sns.kdeplot(data=tips,
            x = 'total_bill',
            hue='time',
            multiple='stack')
plt.show()
#kde
sns.kdeplot(data=tips,
            x = 'total_bill',
            hue='time',
            multiple='fill')
plt.show()
#kde
sns.kdeplot(data=diamonds,
            x = 'price',
            log_scale=True,
            hue = 'clarity',
            palette = 'crest',
            alpha = 0.5,
            linewidth = 0,
            fill=True)
plt.show()
# kde contour
sns.kdeplot(data=tips,
            x = 'total_bill',
            y = 'tip')
plt.show()
