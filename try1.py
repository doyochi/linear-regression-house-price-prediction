import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

plt.rcParams['figure.figsize'] = [8,5]
plt.rcParams['font.size'] = 14
plt.rcParams['font.weight'] = 'bold'
plt.style.use('seaborn-whitegrid')


df = pd.read_csv(insurance.csv)
print('\nNumber of rows and columns in the data set: ',df.shape)
print('')

df.head()
