from matplotlib.pylab import *

#Konstanter
q = 1.0
m = 0.010
E = array([0, -0.0040, 0])
B = array([0, 0, -0.010])

# Konstante krefter
F_e = q*E

def a(v):
    F_m = cross(q*v, B)
    sum_F = F_e + F_m
    aks = sum_F / m
    return aks

# Startverdier for bevegelsen
r = array([0.0, 0, 0])
v = array([0.401, 0, 0])
t = 0

x_verdier = [r[0]]
v_verdier = [norm(v)]

dt = 0.001
while t < 14:
    v += a(v) * dt
    r += v * dt
    t += dt
    x_verdier.append(r[0])
    v_verdier.append(norm(v))
    
plot(x_verdier, v_verdier)
title("Kryssede felt")
xlabel("$x$ / m")
ylabel("$v$ / m/s")
grid()
show()

print("Den største verdien farten har er", round(max(v_verdier), 2), "m/s")
print("Den minste verdien farten har er", round(min(v_verdier), 2), "m/s")