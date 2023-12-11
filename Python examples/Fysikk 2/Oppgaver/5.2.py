import time
start = time.perf_counter()
m = 6.64e-27
q1 = 3.29e-19
q2 = 1.26e-17
k = 8.99e9

r = -1.0e-10
v = 1.5e7
t = 0
v0 = 1.5e7 * 0.99

dt = 1.0e-22

while r < -5.0e-12:
    a = -k*q1*q2/(m*r**2)
    v += a*dt
    r += v*dt
    t += dt

end = time.perf_counter()
pt = end - start
print("Alfapartikkelen snur når r=", v, "m \n Programmet brukte ", pt, "s på å kjøre")