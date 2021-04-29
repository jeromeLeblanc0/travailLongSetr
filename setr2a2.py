import matplotlib.pyplot as plt
import math

m = 11
d = 0.1
u = 1/d
stop = False
l = 10
temps = []
rs = []

while not stop:
    p = l/(u * m)
    if p < 0.99 :
        sum = 0
        piO = 1/(1 + sum + (((m * p) ** m)/math.factorial(m))*(1/(1-p)))
        t = 1/u + (1/u) * (((m * p) ** m)/math.factorial(m)) * (piO/(m * (1 - p) ** 2))
        temps.append(t)
        rs.append(l)
    else:
        stop = True

    l += 1

plt.plot(rs, temps)
plt.xlabel('nombre de requêtes par seconde')
plt.ylabel('temps de réponse moyen')
plt.show()
