print("(1) = s=1/2*a*t^2+v0*t+s0")
print("(2) = v=v0+a*t")
print("(3) = s=1/2*(v+v0)*t")
print("(4) = a=(v^2-v0^2)/2s")
print("(5) = s=(v^2-v0^2)/2a")
num = input("Hvilke formel skal du bruke? (1-5) ")

if num == '1':
    a = float(input("a="))
    t = float(input("t="))
    vo = float(input("v0="))
    so = float(input("s0="))
    svar = 1/2*a*t**2+vo*t+so
if num == '2':
    a = float(input("a="))
    t = float(input("t="))
    vo = float(input("v0="))
    svar = vo+a*t
if num == '3':
    t = float(input("t="))
    vo = float(input("v0="))
    v = float(input("v="))
    svar = 1/2*(v+vo)*t
if num == '4':
    s = float(input("s="))
    vo = float(input("v0="))
    v = float(input("v="))
    svar = (v**2-vo**2)/2*s
if num == '5':
    a = float(input("a="))
    vo = float(input("v0="))
    v = float(input("v="))
    svar = (v**2-vo**2)/2*a
print(f"{svar:.2f}")