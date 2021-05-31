from scipy.optimize import fsolve
import matplotlib.pyplot as plt
import math

R = 4700
visina = 9600
g = 9.81
v_max = 147.22
vt = 350
h = visina
v = v_max

tb = math.sqrt(2 * h / g)
D = v_max * tb

alfa_max = 2 * math.atan(R / D)
fi_max = math.pi - alfa_max

def x(t_s, fi, t1):
	return v * math.cos(fi)*(t_s - t1) + R * math.sin(fi)

def y(t_s, fi, t1):
	return v * math.sin(fi)*(t_s - t1) + R * (1- math.cos(fi))
	
def t_1(fi):
	return R * fi / v

def d(fi, ts):
	t1 = t_1(fi)
	x_ts = x(ts, fi, t1)
	y_ts = y(ts, fi, t1)
	return math.sqrt((x_ts-D)**2 + y_ts**2 + h**2) 
	
def r(t):
	return vt * (t-tb)
	
niz_t = list()
niz_d = list()
	
for fi in range(0,round(fi_max*1000)+500):
	fi = fi/1000
	
	def func(ts):
		return d(fi,ts) - r(ts)
		
	root = fsolve(func, 10)
	
	niz_t.append(root[0])
	niz_d.append(r(root[0]))
	
max_d = max(niz_d)
ugao = niz_d.index(max_d)

ts = niz_t[ugao]

print (f'Ugao skretanja: {ugao/1000} rad')
print (f'Trenutak sudara sa talasom: {ts} s')
print (f'Udaljenost od mesta eksplozije {max_d} m')

x = list()
for i in range(len(niz_d)):
	x.append(i/1000);

fig, ax = plt.subplots()

ax.plot(x, niz_d)
ax.plot([x[ugao]], [max_d], 'ro')
ax.text(x[ugao], max_d, f'  d = {round(max_d, 2)} m')
ax.set_xlabel('Ugao (rad)')
ax.set_ylabel('Daljina (m)')
ax.set_title('Maksimalna daljina')

plt.show()
