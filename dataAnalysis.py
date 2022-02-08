#import needed files

import pandas
import matplotlib.pyplot as plt
import numpy as np

#read file
df = pandas.read_csv("CrabAgePrediction.csv")
#sort file
ds = df.sort_values("Age")
#plot Weight
ds.plot.scatter(x="Age", y="Weight", color="blue", label="Weight")
#chart mean Weight
allWeights = []
allA = []
maxAge = ds["Age"].max()
allDiameter = []
for i in range(maxAge - 1):
    allA.append(i+1)
    sumAges = ds[ds["Age"] == (i+1)]
    allDiameter.append(sumAges["Weight"].mean())

plt.scatter(x = allA, y = allWeights, color = "red", label = "Mean")
#plot diameter and mean
ds.plot.scatter(x="Age", y="Diameter")
allDiameter = []
for i in range(maxAge - 1):
    sumAges = ds[ds["Age"] == (i+1)]
    allDiameter.append(sumAges["Diameter"].mean())
plt.scatter(x = allA, y = allDiameter, color = "red", label = "Mean")

#square and plot daimeter to match weight
allDiameterS = []
ds["DiameterSquare"] = np.power(ds["Diameter"],2)
ds.plot.scatter(x="Age", y="DiameterSquare")
for i in range(maxAge - 1):
    sumAges = ds[ds["Age"] == (i+1)]
    allDiameterS.append(sumAges["DiameterSquare"].mean())
plt.scatter(x = allA, y = allDiameterS, color = "red", label = "Mean")

plt.show() 