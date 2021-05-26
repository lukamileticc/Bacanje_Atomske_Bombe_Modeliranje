import matplotlib.pyplot as plt
import numpy as np
import math


a = 3000
b = 5000
r = 4700/2
D = 6513

fig, ax = plt.subplots()
ax.plot([0,a], [b-r,b-r], color='b')

ax.plot([a,a+D], [b-r,b-r], linestyle='--', color='g')

xr = np.linspace(a, a+r , 100)
yr1 = list()
yr2 = list()

for x in xr:
    yr1.append(b - math.sqrt(r**2 - (x-a)**2)) 
    yr2.append(b + math.sqrt(r**2 - (x-a)**2)) 

ax.plot(xr, yr1, color='b', linestyle='--')
ax.plot(xr, yr2, color='b', linestyle='--')

# t1

x1 = a + 2000
y1 = b+r - math.sqrt(r**2 - (x1-a)**2)

xt1 = [x1, a+5000]
yt1 = [
    b - (r**2 - (x1 - a)*(xt1[0] - a))/(y1-b),
    b - (r**2 - (x1 - a)*(xt1[1] - a))/(y1-b)
]

ax.plot(xt1, yt1, color='g')

# t2
x2 = a + 2000
y2 = b+r - math.sqrt(r**2 - (x2-a)**2)

xt2 = [x2, a-600]
yt2 = [
    b + (r**2 - (x2 - a)*(xt2[0] - a))/(y2-b) - 10,
    b + (r**2 - (x2 - a)*(xt2[1] - a))/(y2-b) +20
]

ax.plot(xt2, yt2, color='g')

plt.show()
