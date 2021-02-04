"""
Created on Oct 6, 2010

@author: Peter
"""
from numpy import *
import matplotlib
import matplotlib.pyplot as plt

xcord0 = []
ycord0 = []
xcord1 = []
ycord1 = []
markers = []
colors = []
fr = open('../testSet.txt')  # this file was generated by 2normalGen.py
for line in fr.readlines():
    lineSplit = line.strip().split('\t')
    xPt = float(lineSplit[0])
    yPt = float(lineSplit[1])
    label = int(lineSplit[2])
    if label == 0:
        xcord0.append(xPt)
        ycord0.append(yPt)
    else:
        xcord1.append(xPt)
        ycord1.append(yPt)

fr.close()
fig = plt.figure()
ax = fig.add_subplot(221)
xcord0 = []
ycord0 = []
xcord1 = []
ycord1 = []
for i in range(300):
    [x, y] = random.uniform(0, 1, 2)
    if ((x > 0.5) and (y < 0.5)) or ((x < 0.5) and (y > 0.5)):
        xcord0.append(x)
        ycord0.append(y)
    else:
        xcord1.append(x)
        ycord1.append(y)
ax.scatter(xcord0, ycord0, marker='s', s=90)
ax.scatter(xcord1, ycord1, marker='o', s=50, c='red')
plt.title('A')
ax = fig.add_subplot(222)
xcord0 = random.standard_normal(150)
ycord0 = random.standard_normal(150)
xcord1 = random.standard_normal(150) + 2.0
ycord1 = random.standard_normal(150) + 2.0
ax.scatter(xcord0, ycord0, marker='s', s=90)
ax.scatter(xcord1, ycord1, marker='o', s=50, c='red')
plt.title('B')
ax = fig.add_subplot(223)
xcord0 = []
ycord0 = []
xcord1 = []
ycord1 = []
for i in range(300):
    [x, y] = random.uniform(0, 1, 2)
    if x > 0.5:
        xcord0.append(x * cos(2.0 * pi * y))
        ycord0.append(x * sin(2.0 * pi * y))
    else:
        xcord1.append(x * cos(2.0 * pi * y))
        ycord1.append(x * sin(2.0 * pi * y))
ax.scatter(xcord0, ycord0, marker='s', s=90)
ax.scatter(xcord1, ycord1, marker='o', s=50, c='red')
plt.title('C')
ax = fig.add_subplot(224)
xcord1 = zeros(150)
ycord1 = zeros(150)
xcord0 = random.uniform(-3, 3, 350)
ycord0 = random.uniform(-3, 3, 350)
xcord1[0:50] = 0.3 * random.standard_normal(50) + 2.0
ycord1[0:50] = 0.3 * random.standard_normal(50) + 2.0

xcord1[50:100] = 0.3 * random.standard_normal(50) - 2.0
ycord1[50:100] = 0.3 * random.standard_normal(50) - 3.0

xcord1[100:150] = 0.3 * random.standard_normal(50) + 1.0
ycord1[100:150] = 0.3 * random.standard_normal(50)
ax.scatter(xcord0, ycord0, marker='s', s=90)
ax.scatter(xcord1, ycord1, marker='o', s=50, c='red')
plt.title('D')
plt.show()
