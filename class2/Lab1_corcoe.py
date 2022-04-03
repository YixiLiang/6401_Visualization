import math
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#######################################
# Q1
#######################################
# create x value
mu, sigma = 0, 1  # mean and standard deviation
x = np.random.normal(mu, sigma, 1000)
# create y value
mu, sigma = 5, math.sqrt(2)  # mean and standard deviation
y = np.random.normal(mu, sigma, 1000)

#######################################
# Q2
#######################################
def correlation_coefficient(x, y):
    """
    :param x: variable x
    :param y: variable y
    :return: correlation coefficient
    """
    num1 = sum((a - np.mean(x)) * (b - np.mean(y)) for a, b in zip(x, y))
    num2 = math.sqrt(sum((a - np.mean(x)) ** 2 for a in x) * sum((b - np.mean(y)) ** 2 for b in y))
    # print(f'corr: {num1 / num2:.2f}')
    return num1 / num2

#######################################
# Q3
#######################################
# a
print(f'The sample mean of random variable x is: {np.mean(x):.2f}')
# b
print(f'The sample mean of random variable y is: {np.mean(y):.2f}')
# c
print(f'The sample variance of random variable x is: {np.var(x):.2f}')
# d
print(f'The sample variance of random variable y is: {np.var(y):.2f}')
# e
print(f'The sample Pearson’s correlation coefficient between x & y is: {correlation_coefficient(x, y):.2f}')

#######################################
# Q4
#######################################
plt.figure(figsize=(12, 8))
plt.plot(x, label="x")
plt.plot(y, label="y")
plt.title('The line plot of x and y')
plt.xlabel("Number")
plt.ylabel("Value")
plt.legend()
plt.grid()
plt.show()

#######################################
# Q5
#######################################
plt.figure(figsize=(12, 8))
plt.hist(x, label="x", alpha=0.5)
plt.hist(y, label="y", alpha=0.5)
plt.title('The histogram of x and y')
plt.xlabel("Number")
plt.ylabel("Value")
plt.legend()
plt.grid()
plt.show()

#######################################
# Q6
#######################################
# read csv
df = pd.read_csv("tute1.csv")

#######################################
# Q7
#######################################
salesAndAdBudgetCorcoe = correlation_coefficient(df["Sales"], df["AdBudget"])
salesAndGDPCorcoe = correlation_coefficient(df["Sales"], df["GDP"])
adBudgetAndGDPCorcoe = correlation_coefficient(df["AdBudget"], df["GDP"])

#######################################
# Q8
#######################################
print(f'The sample Pearson’s correlation coefficient between Sales & AdBudget is: {salesAndGDPCorcoe:.2f}')
print(f'The sample Pearson’s correlation coefficient between Sales & GDP is: {salesAndGDPCorcoe:.2f}')
print(f'The sample Pearson’s correlation coefficient between AdBudget & GDP is: {adBudgetAndGDPCorcoe:.2f}')

#######################################
# Q9
#######################################
# time format
time = pd.to_datetime(df.iloc[:80, 0], format='%b-%y')
df.iloc[80:, 0] = "200" + df.iloc[80:, 0]
time2 = pd.to_datetime(df.iloc[80:, 0], format='%Y-%b')
time = time.append(time2)
# Add new column name Date
df["Date"] = pd.DataFrame(time)

# line plot
plt.figure(figsize=(12, 8))
plt.plot(df["Date"], df['Sales'], label="Sales")
plt.plot(df["Date"], df['GDP'], label="GDP")
plt.plot(df["Date"], df['AdBudget'], label="AdBudget")
plt.title('The line plot of Sales, AdBudget and GDP versus time')
plt.xlabel("Time")
plt.ylabel("Value")
plt.legend()
plt.grid()
plt.show()

#######################################
# Q10
#######################################
plt.figure(figsize=(12, 8))
plt.hist(df['Sales'], label="Sales")
plt.hist(df['GDP'], label="GDP")
plt.hist(df['AdBudget'], label="AdBudget")
plt.title('The histogram plot of Sales, AdBudget and GDP')
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.legend()
plt.grid()
plt.show()
