from scipy import constants as cnsts; import pint; import os
u = pint.UnitRegistry()
Q = u.Quantity
h = cnsts.Planck
c = cnsts.speed_of_light

def main():
    f = e/h
    f = f * u.Hz
    f = f.to("THz")
    l = (h*c)/e
    l = l * u.m
    l = l.to("nanometer")
    print(f'Bølgelengden til energien er {l:.1f} og frekvensen er {f:.1f}')

e = input("Skriv inn energi i J: ")
if "->" in e:
    e = e.split("->")
    ef = e[0].split('*')
    ef1 = ef[0]
    ef2 = ef[1].split('^')
    ef2 = float(ef2[0]) ** float(ef2[1])
    ef = float(ef1) * float(ef2)
    es = e[1].split('*')
    es1 = es[0]
    es2 = es[1].split('^')
    es2 = float(es2[0]) ** float(es2[1])
    es = float(es1) * float(es2)
    e = ef - es
    main()
else:
    e = e.split('*')
    e1 = e[0]
    e2 = e[1]
    e2 = e2.split("^")
    e2 = float(e2[0]) ** float(e2[1])
    e = float(e1) * float(e2)
    main()
    
print("\n")

r = input('Ønsker du regne ut på nytt? (y/n): ')
r = r.lower()

if (r == "y"):
    cwd = os.getcwd()
    os.system(f"cd {cwd}")
    os.system("python Atom\energitilbølgelengde.py")
else:
    exit()