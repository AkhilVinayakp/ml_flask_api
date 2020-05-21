import pandas as pd
data = pd.read_csv('data.csv')
# z = ((map(lambda x: x, data.loc[i]) for i in range(0, data.index.stop)))
t = [tuple(i) for i in ((map(lambda x: x, data.loc[i]) for i in range(0, data.index.stop)))]
print(t)





