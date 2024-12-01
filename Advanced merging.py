import pandas as pd
data = pd.read_csv('table1.csv')
data1 = pd.read_csv('table2.csv')

data3 = pd.concat([data,data1],join='inner',sort=True) #ignore_index=True
print(data3)
