import numpy as np
import matplotlib.pylot as plt
import pandas as pd
dataset = pd.read_csv('Data.csv')
print('Shape dataset: ', dataset.shape)
print('\nLima data teratas:\n ', dataset.head)
print('\nInformasi dataset')
print(dataset.info())
print('\nStatistik deskriptif:\n', dataset.describe)