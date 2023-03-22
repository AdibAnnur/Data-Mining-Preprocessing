import numpy as np
import matplotlib.pylot as plt
import pandas as pd

dataset = pd.read_csv('Data.csv')

#Mengecek Missing Value
print('Mengecek dataset yang missing value:')
print(dataset.isnull().sum())

#Menghitung total missing value
print('Menghitung total missing value:')
print(dataset.isnull().sum().sum())