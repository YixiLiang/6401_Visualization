import numpy as np
import matplotlib.pyplot as plt
N = 1000
mean_x = 0
mean_y = 2
std_x = np.sqrt(1)
std_y = np.sqrt(5)

x = np.random.normal(mean_x, std_x, N)
y = np.random.normal(mean_y, std_y, N)

plt.figure(figsize=(12, 8))
plt.plot(x, "r", label="x")
plt.plot(y, "g", label="y")
plt.legend()
plt.grid()
plt.show()

plt.figure(figsize=(12, 8))
plt.hist(x, bins=50, label="x", alpha = .5)
plt.hist(y, bins=50, label="y", alpha = .5)
plt.legend()
plt.grid()
plt.show()
