import random
import pandas as pd
from itertools import count
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from general import lags
import numpy as np

df = pd.read_csv("S&P5001.csv")

lg = lags(n=5, data=df.D1[1:])

l11 = list(lg[0])
l22 = list(lg[1])

x_vals = []
y_vals = []

index = count()

def direction(x1,x2):
    tan = np.arctan(x1/x2)
    return np.degrees(tan)

direct2 = []


for val1 in list(lg[0]):
    d1 = direction(x1=np.sin(val1),x2=np.cos(val1))
    direct2.append(d1)

def animate(i):
    #for i in range(len(l11)):
    #x_vals.append(list(direct2[:])[i])
    #y_vals.append(list(lg[1])[i])
    x_vals.append(l11[i])
    y_vals.append(l22[i])
    plt.cla()
    plt.scatter(x_vals, y_vals)
    #plt.scatter(direct2[:], lg1[1][:])
    
ani = FuncAnimation(plt.gcf(), animate, interval = 1000)
plt.show()