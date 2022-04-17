import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st
from scipy.stats import shapiro
from scipy.stats import normaltest

from statsmodels.graphics.gofplots import qqplot
#######################################
# Q1
#######################################
mean = 0
std = 1
x = np.random.normal(mean,std,5000)
# np.cumsum Return the cumulative sum of the elements along a given axis
y = np.cumsum(x)
plt.figure(figsize=(9,7))
plt.subplot(2,2,1)
plt.plot(x)
plt.title('Gaussian data')
plt.ylabel('Magnitude')
plt.xlabel('# of samples')
plt.grid()

plt.subplot(2,2,2)
plt.plot(y)
plt.title('Non-Gaussian data')
plt.ylabel('Magnitude')
plt.xlabel('# of samples')
plt.grid()

plt.subplot(2,2,3)
plt.hist(x, bins=100)
plt.title('Histogram of Gaussian data')
plt.ylabel('Magnitude')
plt.xlabel('# of samples')
plt.grid()

plt.subplot(2,2,4)
plt.hist(y, bins=100)
plt.title('Histogram of Non-Gaussian data')
plt.ylabel('Magnitude')
plt.xlabel('# of samples')
plt.grid()

plt.tight_layout()
plt.show()
#######################################
# Q2-4
#######################################

kstestX = st.kstest(x, 'norm')
kstestY = st.kstest(y, 'norm')
print(f'K-S test: statistics = {kstestX[0]} p-value = {kstestX[1]}')
print(f'K-S test: x dataset looks ')
#If the P value is small, conclude that the two groups were sampled from populations with different distributions
print(f'K-S test: statistics = {kstestY[0]} p-value = {kstestY[1]}')
print(f'K-S test: y dataset looks ')

shapiroX = shapiro(x)
shapiroY = shapiro(y)
print(f'Shapiro test: statistics = {shapiroX[0]} p-value = {shapiroX[1]}')
print(f'Shapiro test: x dataset looks ')

print(f'Shapiro test: statistics = {shapiroY[0]} p-value = {shapiroY[1]}')
print(f'Shapiro test: y dataset looks ')

normaltestX = normaltest(x)
normaltestY = normaltest(y)
print(f'da_k_squared test: statistics = {normaltestX[0]} p-value = {normaltestX[1]}')
print(f'da_k_squared test: x dataset looks ')

print(f'da_k_squared test: statistics = {normaltestY[0]} p-value = {normaltestY[1]}')
print(f'da_k_squared test: y dataset looks ')
#######################################
# Q5
#######################################
transformedY = st.norm.ppf(st.rankdata(y).reshape(y.shape)/(len(y) + 1))
# subplot
plt.figure(figsize=(9,7))
plt.subplot(2,2,1)
plt.plot(y)
plt.title('Non-gaussian data')
plt.ylabel('Magnitude')
plt.xlabel('# of samples')
plt.grid()

plt.subplot(2,2,2)
plt.plot(st.rankdata(y))
plt.title('Transformed data (Gaussian)')
plt.ylabel('Magnitude')
plt.xlabel('# of samples')
plt.grid()

plt.subplot(2,2,3)
plt.hist(y, bins=100)
plt.title('Histogram of Non-gaussian data')
plt.xlabel('# of samples')
plt.grid()

plt.subplot(2,2,4)
plt.hist(transformedY, bins=100)
plt.title('Histogram of Transformed data (Gaussian)')
plt.xlabel('# of samples')
plt.grid()

plt.tight_layout()
plt.show()
#######################################
# Q6
#######################################

plt.figure()
qqplot(y, line='s')
plt.title('y-Data: Non-normal')
plt.grid()
plt.show()

plt.figure()
qqplot(transformedY, line='s')
plt.title('Transformed y: Normal')
plt.grid()
plt.show()
#######################################
# Q7
#######################################
kstestTransY = st.kstest(transformedY, 'norm')
print(f'K-S test: statistics = {kstestTransY[0]} p-value = {kstestTransY[1]}')
print(f'K-S test: y transformed dataset looks ')
#If the P value is small, conclude that the two groups were sampled from populations with different distributions
#######################################
# Q8
#######################################
shapiroTransY = shapiro(transformedY)
print(f'Shapiro test: statistics = {shapiroTransY[0]} p-value = {shapiroTransY[1]}')
print(f'Shapiro test: y transformed dataset looks ')

#######################################
# Q9
#######################################
normaltestTransY = normaltest(transformedY)
print(f'da_k_squared test: statistics = {normaltestTransY[0]} p-value = {normaltestTransY[1]}')
print(f'da_k_squared test: y transformed dataset looks ')