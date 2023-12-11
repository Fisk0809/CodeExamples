from pylab import *

m = float(input('Skriv inn massen i kg: '))
g = 9.81
mu = float(input('Skriv inn friksjonstallet: '))
G = m*g
N = G
R = mu*N

sum_F = -R
a = sum_F/m

s = float(input('Skriv inn startposisjon i meter: '))
v = float(input('Skriv inn startfart i m/s: '))
t = float(input('Skriv inn starttid i sekunder: '))

t_slutt = float(input('Skriv inn sluttid i sekunder: '))
dt = float(input('Skriv inn lengde på tidssteg i sekunder: '))
s_verdier = [s]
v_verdier = [v]
t_verdier = [t]

while t < t_slutt:
    v = v + a*dt 
    s = s + v*dt
    t = t + dt  

    t_verdier.append(t)
    v_verdier.append(v)
    s_verdier.append(s)

plot(t_verdier, s_verdier)
title("Sterkning som funskjon av tid")
xlabel("$t$ / s")
ylabel("$s$ / m")
grid()
show()
