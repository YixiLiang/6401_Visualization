import numpy as np
import pandas as pd
from scipy.stats import pearsonr


def correlation_coefficient(x, y):
    num1 = sum((a - np.mean(x)) * (b - np.mean(y)) for a, b in zip(x, y))
    num5 = math.sqrt(sum((a - np.mean(x)) ** 2 for a in x) * sum((b - np.mean(y)) ** 2 for b in y))

    print(f'corr: {num1 / num5:.2f}')
    # #Apply the pearsonr()
    num4, _ = pearsonr(x, y)
    print('Pearsons correlation: %.2f' % num4)
    return num1 / num5