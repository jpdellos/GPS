import random
import time
from itertools import count
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import math
import pandas as pd


#plt.style.use('fivethirtyeight')

ax = plt.axes(projection='3d')

namafile = 'data3D.csv'
header1 = "latitude"
header2 = "longitude"
header3 = "altitude"

index = count()





def animate(i):

    data = pd.read_csv('data3D.csv')
    x = (data[header1])
    y = (data[header2])
    z = (data[header3])


    plt.cla()
    ax.scatter(x, y, z, 'red')
    ax.set_xlabel("Latitude")
    ax.set_ylabel('Longitude')
    ax.set_zlabel("Altitude em metros")





ani = FuncAnimation(plt.gcf(), animate, interval=500)

plt.tight_layout()
plt.show()
