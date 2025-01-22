# %%
import seaborn as sns
import numpy as np
import pandas as pd

# %%
planets = sns.load_dataset('planets')
planets.shape

# %%
planets.head()
# %%


rng = np.random.RandomState(42)
ser = pd.Series(rng.rand(5))
ser
# %%
ser.sum()
# %%
ser.mean()
# %%
