#%%
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
# %%
x_axis = np.arange(0,20, 0.2)
# %%
sin = np.sin(x_axis)
# %%
sin_df = pd.DataFrame({'x': x_axis, 'y': sin})
# %%
sin_df.plot(
    x = 'x',
    y = 'y'
)
# %%
sin_df.hist()
# %%
