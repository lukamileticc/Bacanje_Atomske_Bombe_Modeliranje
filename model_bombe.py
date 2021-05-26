import matplotlib.pyplot as plt
import numpy as np

domet = 6513.028
visina = 9600
g = 9.81
v_max = 147.22

x_tacke = list(range(0, 6600, 50))
y_tacke = list()
print(x_tacke)

for x in x_tacke: 
    y_tacke.append(visina - g/2*(x/v_max)**2)

print(y_tacke)

fig, ax = plt.subplots()
ax.plot(x_tacke, y_tacke)
ax.plot([0, domet], [visina,0], 'ro')
ax.text(0, visina, '  h0 = 9600m')
ax.text(domet-1800, 0, 'D = 6513.028m')
ax.set_xlabel('Daljina (m)')
ax.set_ylabel('Visina (m)')
ax.set_title('Model bombe')
plt.show()
