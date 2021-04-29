import math
d = 0.1
u = 1/d
l = 100


for m in range(11, 15):
    sum = 0
    p = l/(u * m)
    print(p)
    for n in range(1,m):
        sum += ((m * p) ** n)/math.factorial(n)
    
    piO = 1/(1 + sum + (((m * p) ** m)/math.factorial(m))*(1/(1-p)))
    t = 1/u + (1/u) * (((m * p) ** m)/math.factorial(m)) * (piO/(m * (1 - p) ** 2))

    print("essai m = " + str(m) + "\npiO = " + str(piO) + "\nt = " + str(t) + "\n\n\n")