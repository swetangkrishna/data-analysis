import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#read the data
can = pd.read_csv("haberman.csv")

#simple plot scatter
#sns.set_style('whitegrid')
"""sns.FacetGrid(can, hue="status")\
.map(plt.scatter, 'year', 'age')\
.add_legend()"""
#pairplot
#sns.pairplot(can, hue="status")

#histogram, pdf and cdf
status_1 = can.loc[can["status"]==1]
status_2 = can.loc[can["status"]==2]


print('hi1')
print(status_1)

counts, bin_edges = np.histogram(status_2['age'], bins=10, density=True)
pdf = counts/(sum(counts))
cdf = np.cumsum(pdf)
print(pdf)
print(cdf)

plt.plot(bin_edges[1:],pdf)
plt.plot(bin_edges[1:],cdf)

plt.show()