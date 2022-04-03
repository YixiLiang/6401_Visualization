import numpy as np
import pandas as pd

np.random.seed(1)
index = np.arange(1,7)
# np.random.randn(6,4) 六行四列
df = pd.DataFrame(np.random.randn(6,4), index=index, columns=list("ABCD"))
df2

