import matplotlib.pyplot as plt
import pandas as pd
data = pd.read_csv('table1.csv')
data1 = pd.read_csv('table2.csv')
print(data)
print(data1)

data3 = data.merge(data1, on='name',suffixes=('_1','_2'))
print(data3)

