import numpy as np
import pandas as pd

r = np.random.RandomState(1)
s = pd.Series(r.uniform(0, 10, 100)).sort_values(ignore_index=True)

print(s[s>5].index[0])