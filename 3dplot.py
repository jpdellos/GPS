
import random
from itertools import count
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import pandas as pd
import math
import time
start_time = time.time()

#plt.style.use('fivethirtyeight')

ax = plt.axes(projection='3d')

namafile = 'data3D.csv'
header1 = "latitude"
header2 = "longitude"
header3 = "altitude"

index = count()





def animate(i):

    data = pd.read_csv('data3D.csv')
    x = (data[header1]-data[header1][0])
    y = (data[header2]-data[header2][0])
    z = (data[header3]-data[header3][0])


    plt.cla()
    ax.plot3D(x, y, z, 'red')
    ax.set_xlabel("Latitude")
    ax.set_ylabel('Longitude')
    ax.set_zlabel("Altitude em metros")






ani = FuncAnimation(plt.gcf(), animate, interval=500)

plt.tight_layout()
plt.show()
plt.close()
print("--- %s seconds ---" % (time.time() - start_time))
