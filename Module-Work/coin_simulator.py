#%%
import numpy.random as rnd
import pandas as pd
#%%
# Number of samples
number_of_samples = 1000
#%%
# Distribution
def coin_flip():
    if rnd.random() >= 0.5: # Set distribtution
        return True
    else:
        return False
#%%
def simulation(number_of_samples):
    simulated_data = []
    for sample in range(0,number_of_samples):
        if coin_flip():
            simulated_data.append(1)
        else:
            simulated_data.append(0)
    return simulated_data
#%%
coin_simulation = simulation(number_of_samples)

# %%
coin_simulation[0:10]
# %%
coin_df = pd.DataFrame(coin_simulation)
# %%
coin_df.hist()
# %%
coin_df.describe()
# %%
def inside_circle(x,y):
    if (x**2 + y**2)**(1/2) <= 1: # Set distribtution
        return True
    else:
        return False

#%%
def pi_simulation(number_of_samples):
    
    x_list=[]
    y_list=[]
    is_inside_circle=[]

    for sample in range(0,number_of_samples):
        
        x = rnd.random()
        y = rnd.random()

        x_list.append(x)
        y_list.append(y)

        if inside_circle(x,y):
            is_inside_circle.append(1)
        else:
            is_inside_circle.append(0)
    return [x_list,y_list,is_inside_circle]

# %%
circle_df = pd.DataFrame(pi_simulation(number_of_samples))
# %%
circle_df = circle_df.T
# %%
circle_df
# %%
circle_df.columns = ['x','y','inside']
# %%
circle_df
# %%
circle_df.plot.scatter(
    x='x',
    y='y',
    c='inside',
    cmap = 'jet'
)
# %%
def estimate_pi(is_inside_circle):
    inside = 0
    for point in is_inside_circle:
        if point == 1:
            inside += 1
    pi = 4 * inside / len(is_inside_circle)
    return pi
#%%
circle_df.plot.scatter(
    x='x',
    y='y',
    c='inside',
    cmap = 'jet',
    title=f"Pi Estimate = {estimate_pi(circle_df['inside'])}"
)
# %%
def under_parabola(x,y):
    if y < x**2:
        return True
    else:
        return False
#%%
def parabola_simulator(number_of_samples):

    x_list=[]
    y_list=[]
    under_para=[]

    for sample in range(0,number_of_samples):

        x = rnd.random()
        y = rnd.random()
        x_list.append(x)
        y_list.append(y)

        if under_parabola(x,y):
            under_para.append(1)
        else:
            under_para.append(0)
    return [x_list,y_list,under_para]
#%%
para_df = pd.DataFrame(parabola_simulator(number_of_samples))
#%%
para_df = para_df.T
para_df.columns = ['x','y','under']
# %%
para_df.plot.scatter(
    x='x',
    y='y',
    c='under',
    cmap = 'jet'
)
# %%
para_df.hist()
# %%
