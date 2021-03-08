#%%
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
# %%
csv_path = './used_cars.csv'

# %%
used_cars_df = pd.read_csv(csv_path)
# %%
used_cars_df['maker'].value_counts()
# %%
car_maker_groupby = used_cars_df.groupby(['maker'])
# %%
car_maker_groupby
# %%
car_maker_count = car_maker_groupby['maker'].count()
# %%
car_maker_count
# %%
car_maker_count.plot(kind='bar')
# %%
used_cars_df['fuel_type'].value_counts()
# %%
mpg_df = pd.read_csv('./mpg.csv')
# %%
mpg_groupby = mpg_df.groupby('cylinders')
# %%
mpg_groupby.count()
# %%
mpg_cyl_avg_df = mpg_groupby['mpg'].mean()
# %%
mpg_cyl_avg_df
# %%
mpg_cyl_avg_df.mean()
# %%
mpg_groupby['acceleration'].mean()
# %%
mpg_df['horsepower'] = mpg_df.loc[mpg_df['horsepower'] != '?']
# %%
mpg_df.dtypes
# %%
mpg_df['horsepower'] = pd.to_numeric(mpg_df['horsepower'])
# %%
mpg_df.dtypes
# %%
mpg_df.plot.scatter(
    x = 'horsepower',
    y = 'mpg'
)
# %%
avg_rain_path = './avg_rain_state.csv'
# %%
avg_rain_df = pd.read_csv(avg_rain_path)
# %%
avg_rain_df
# %%
avg_rain_df.dtypes
# %%
avg_rain_df.plot.bar(
    x = 'State',
    y = 'Inches',
    alpha = .5,
    color='r',
    align = 'center'
)
# %%
plt.figure(figsize=(36,4))
#%%
x_axis = np.arange(len(avg_rain_df))
#%%
tick = [value for value in x_axis]
# %%
plt.figure(figsize=(36,4))
plt.bar(
    x=avg_rain_df['State'],
    height=avg_rain_df['Inches'],
    alpha=0.5,
    color='r',
    align='center'
)
plt.xticks(tick, avg_rain_df['State'], rotation='vertical')
# %%
