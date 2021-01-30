# coding=utf-8
'''
Created on Oct 27, 2010

@author: Peter
'''
from numpy import *
from Ch02 import kNN
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111)  # 散点图
datingDataMat, datingLabels = kNN.file2matrix('../datingTestSet2.txt')
ax.scatter(datingDataMat[:, 1], datingDataMat[:, 2], 15.0 * array(datingLabels), 15.0 * array(datingLabels))
ax.axis([-2, 25, -0.2, 2.0])
plt.xlabel('Percentage of Time Spent Playing Video Games')
plt.ylabel('Liters of Ice Cream Consumed Per Week')
plt.show()
