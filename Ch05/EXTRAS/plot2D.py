# coding=utf-8
"""
Created on Oct 6, 2010

@author: Peter
"""
from numpy import *
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from Ch05 import logRegres

dataMat, labelMat = logRegres.loadDataSet()
print dataMat
print labelMat
dataArr = array(dataMat)
weights = logRegres.stocGradAscent0(dataArr, labelMat)

n = shape(dataArr)[0]  # number of points to create
xcord1 = []
ycord1 = []
xcord2 = []
ycord2 = []

markers = []
colors = []
for i in range(n):
    if int(labelMat[i]) == 1:
        xcord1.append(dataArr[i, 1])
        ycord1.append(dataArr[i, 2])
    else:
        xcord2.append(dataArr[i, 1])
        ycord2.append(dataArr[i, 2])

fig = plt.figure()
ax = fig.add_subplot(111)
type1 = ax.scatter(xcord1, ycord1, s=30, c='red', marker='s')
type2 = ax.scatter(xcord2, ycord2, s=30, c='green')
x = arange(-3.0, 3.0, 0.1)
weights = [13.03822793, 1.32877317, -1.96702074]
weights = [4.12, 0.48, -0.6168]
y = (-weights[0] - weights[1] * x) / weights[2]
type3 = ax.plot(x, y)
plt.xlabel('X1')
plt.ylabel('X2')
plt.show()
