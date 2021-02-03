# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 14:18:42 2021

@author: user
"""

#import random
import pandas as pd
from itertools import count
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from general import lags

df = pd.read_csv("S&P5001.csv")

lg = lags(n=5, data=df.D1[1:])

l11 = list(lg[0])
l22 = list(lg[1])

x_vals = []
y_vals = []

index = count()


def animate(i):
    #for i in range(len(l11)):
    x_vals.append(l11[i])
    y_vals.append(l22[i])
    plt.cla()
    plt.scatter(x_vals, y_vals)
    
ani = FuncAnimation(plt.gcf(), animate, interval = 1000)
plt.show()