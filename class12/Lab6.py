import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st
from scipy.stats import kstest
from scipy.stats import shapiro
from scipy.stats import normaltest

from statsmodels.graphics.gofplots import qqplot

#######################################
# Q1
#######################################
mean = 0
std = 1
x = np.random.normal(mean, std, 5000)
# np.cumsum Return the cumulative sum of the elements along a given axis
y = np.cumsum(x)
plt.figure(figsize=(9, 7))
plt.subplot(2, 2, 1)
plt.plot(x)
plt.title('Gaussian data')
plt.ylabel('Magnitude')
plt.xlabel('# of samples')
plt.grid()

plt.subplot(2, 2, 2)
plt.plot(y)
plt.title('Non-Gaussian data')
plt.ylabel('Magnitude')
plt.xlabel('# of samples')
plt.grid()

plt.subplot(2, 2, 3)
plt.hist(x, bins=100)
plt.title('Histogram of Gaussian data')
plt.ylabel('Magnitude')
plt.xlabel('# of samples')
plt.grid()

plt.subplot(2, 2, 4)
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

kstestX = kstest(x, 'norm')
kstestY = kstest(y, 'norm')
print(f'K-S test: statistics = {kstestX[0]:.2f} p-value = {kstestX[1]:.2f}')
print(f'K-S test: x dataset looks like gaussian distributed dataset. \n'
      f'From the result of the K-S test, we can see the p-value is {kstestX[1]:.2f}, it is much bigger 0.01.\n'
      f'So we can say we fail to reject this is normal distribution.\n')
# If the P value is small, conclude that the two groups were sampled from populations with different distributions
print(f'K-S test: statistics = {kstestY[0]:.2f} p-value = {kstestY[1]:.2f}')
print(f'K-S test: y dataset looks like non-gaussian distributed dataset. \n'
      f'From the result of the K-S test, we can see the p-value is {kstestY[1]:.2f}, which is extremely small.\n'
      f'So we can say we reject this is normal distribution.\n')

shapiroX = shapiro(x)
shapiroY = shapiro(y)
print(f'Shapiro test: statistics = {shapiroX[0]:.2f} p-value = {shapiroX[1]:.2f}')
print(f'Shapiro test: x dataset looks like gaussian distributed dataset. \n'
      f'From the result of the Shapiro test, we can see the p-value is {shapiroX[1]:.2f}, it is much bigger 0.01.\n'
      f'So we can say we fail to reject this is normal distribution.\n')

print(f'Shapiro test: statistics = {shapiroY[0]:.2f} p-value = {shapiroY[1]:.2f}')
print(f'Shapiro test: y dataset looks like non-gaussian distributed dataset. \n'
      f'From the result of the Shapiro test, we can see the p-value is {shapiroY[1]:.2f}, which is extremely small.\n'
      f'So we can say we reject this is normal distribution.\n')

normaltestX = normaltest(x)
normaltestY = normaltest(y)
print(f'da_k_squared test: statistics = {normaltestX[0]:.2f} p-value = {normaltestX[1]:.2f}')
print(f'da_k_squared test: x dataset looks like gaussian distributed dataset. \n'
      f'From the result of the da_k_squared test, we can see the p-value is {normaltestX[1]:.2f}, it is much bigger 0.01.\n'
      f'So we can say we fail to reject this is normal distribution.\n')

print(f'da_k_squared test: statistics = {normaltestY[0]:.2f} p-value = {normaltestY[1]:.2f}')
print(f'da_k_squared test: y dataset looks like non-gaussian distributed dataset. \n'
      f'From the result of the da_k_squared test, we can see the p-value is {normaltestY[1]:.2f}, which is extremely small.\n'
      f'So we can say we reject this is normal distribution.\n')
#######################################
# Q5
#######################################
transformedY = st.norm.ppf(st.rankdata(y).reshape(y.shape) / (len(y) + 1))

# y = 2*(st.rankdata(x)/(T+1))-1
# y1_tr = np.arctach(y)

# subplot
plt.figure(figsize=(9, 7))
plt.subplot(2, 2, 1)
plt.plot(y)
plt.title('Non-gaussian data')
plt.ylabel('Magnitude')
plt.xlabel('# of samples')
plt.grid()

plt.subplot(2, 2, 2)
plt.plot(st.rankdata(y))
plt.title('Transformed data (Gaussian)')
plt.ylabel('Magnitude')
plt.xlabel('# of samples')
plt.grid()

plt.subplot(2, 2, 3)
plt.hist(y, bins=100)
plt.title('Histogram of Non-gaussian data')
plt.xlabel('# of samples')
plt.grid()

plt.subplot(2, 2, 4)
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
print(f'K-S test: statistics = {kstestTransY[0]:.2f} p-value = {kstestTransY[1]:.2f}')
print(f'K-S test: y transformed dataset looks like gaussian distributed dataset. \n'
      f'From the result of the K-S test, we can see the p-value is {kstestTransY[1]:.2f}, it is much bigger 0.01.\n'
      f'So we can say we fail to reject this is normal distribution.\n')
# If the P value is small, conclude that the two groups were sampled from populations with different distributions
#######################################
# Q8
#######################################
shapiroTransY = shapiro(transformedY)
print(f'Shapiro test: statistics = {shapiroTransY[0]:.2f} p-value = {shapiroTransY[1]:.2f}')
print(f'Shapiro test: y transformed dataset looks like gaussian distributed dataset. \n'
      f'From the result of the Shapiro test, we can see the p-value is {shapiroTransY[1]:.2f}, it is much bigger 0.01.\n'
      f'So we can say we fail to reject this is normal distribution.\n')
#######################################
# Q9
#######################################
normaltestTransY = normaltest(transformedY)
print(f'da_k_squared test: statistics = {normaltestTransY[0]:.2f} p-value = {normaltestTransY[1]:.2f}')
print(f'da_k_squared test: y transformed dataset looks like gaussian distributed dataset. \n'
      f'From the result of the da_k_squared test, we can see the p-value is {normaltestTransY[1]:.2f}, it is much bigger 0.01.\n'
      f'So we can say we fail to reject this is normal distribution.\n')
#######################################
# Q10
#######################################
print(f'The p-value result of three different normality tests are K-S test: {kstestTransY[1]:.2f}, '
      f'Shapiro test: {shapiroTransY[1]:.2f}, da_k_squared test: {normaltestTransY[1]:.2f}. \n'
      f'We can see all the p-value are much bigger than 0.01, so we can say all three tests confirm transformed y is normal distribution.')