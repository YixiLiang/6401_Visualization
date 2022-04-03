import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = np.random.randn(4, 5)
print(data)
df = pd.DataFrame(data=data, columns=['A', 'B', 'C', 'D', 'E'],
                  index=['Monday', 'Tuesday', "Wed", "Thursday"])

print(df)

df3 = df.copy()
for i in range(len(df)):
    df3["Max"] = df.astype("float64").idxmax(axis=1)
    df3["Min"] = df.astype("float64").idxmin(axis=1)

print(df3)
