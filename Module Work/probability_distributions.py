#%%
import pandas as pd 
import numpy.random as rnd 
import matplotlib.pyplot as plt
# %%
mean = 0
standard_dev = 1
sample_size = 1000

# %%
normal_sample = rnd.normal(mean, standard_dev, sample_size)
# %%
normal_sample[0:10]
# %%
normal_df = pd.DataFrame(normal_sample)
# %%
normal_df.plot()
# %%n
normal_df.hist()

# %%
number_of_trials = 100
prob_succ = 0.67
binomial_sample = rnd.binomial(number_of_trials, 0.67, sample_size)
# %%
binomial_df = pd.DataFrame(binomial_sample)
# %%
binomial_df.hist()
# %%
log_normal_df = pd.DataFrame(rnd.lognormal(mean, standard_dev, sample_size))
# %%
log_normal_df.plot()
# %%
log_normal_df.hist()
# %%
