import pip, os, re, time
try:
    import pint; from pyteomics import mass; from scipy import constants as cnsts
except ImportError:
    pip.main(['install', 'pint'])
    pip.main(['install', 'pyteomics'])
    pip.main(['install', 'scipy'])
    os.system('cls')
    print('Libraries er installert')
    os.system("timeout /t 5")
    cwd = os.getcwd()
    os.system(f"cd {cwd}")
    os.system("python Atom\massesvinn.py")
os.system('cls')
u = pint.UnitRegistry()
Q = u.Quantity
c = cnsts.c
n = cnsts.neutron_mass
n = n * u.kg
n = n.to('dalton')
n = str(n).split(" ")
n = float(n[0])


svar = input("Skriv inn ligning: ")
start = time.perf_counter()
ligning = svar.split("->")  
gange = []
i = 0
m1 = 0
m2 = 0

isotop1 = ligning[0]
isotop1 = isotop1.split("+")
for x in isotop1:
    i += 1
    locals()["iso"+str(i)] = x
    iso = locals()["iso"+str(i)]
    iso = iso.capitalize()
    
    numbers = re.compile(r'(\d+)')
    iso = numbers.sub(r'[\1]', iso)
    if "*" in x:
        gange = x.split("*")
        gange1 = gange[1]
        gange2 = float(gange[0])
        gange1 = gange1.capitalize()
        numbers = re.compile(r'(\d+)')
        gange1 = numbers.sub(r'[\1]', gange1)
        if gange1 == "N[1]":
            gange1 = n
        elif gange1 == "A":
            gange1 = mass.calculate_mass(formula='H+')
        else:
            gange1 = mass.calculate_mass(formula=f'{gange1}')
        locals()["iso"+str(i)] = gange1 * gange2
    elif iso == "N[1]":
        locals()["iso"+str(i)] = n
    elif iso == "A":
        locals()["iso"+str(i)] = mass.calculate_mass(formula='H+')
    else: 
        locals()["iso"+str(i)] = mass.calculate_mass(formula=f'{iso}')
    m1 += locals()["iso"+str(i)]  

i = 0
iso = 0
gange = 0
isotop2 = ligning[1]
isotop2 = isotop2.split("+")
for x in isotop2:
    i += 1
    locals()["iso"+str(i)] = x
    iso = locals()["iso"+str(i)]
    iso = iso.capitalize()
    
    numbers = re.compile(r'(\d+)')
    iso = numbers.sub(r'[\1]', iso)
    if "*" in x:
        gange = x.split("*")
        gange3 = gange[1]
        gange4 = float(gange[0])
        gange3 = gange3.capitalize()
        numbers = re.compile(r'(\d+)')
        gange3 = numbers.sub(r'[\1]', gange3)
        if gange3 == "N[1]":
            gange3 = n
        elif gange3 == "A":
            gange3 = mass.calculate_mass(formula='H+')
        else:
            gange3 = mass.calculate_mass(formula=f'{gange3}')
        locals()["iso"+str(i)] = gange3 * gange4
    elif iso == "N[1]":
        locals()["iso"+str(i)] = n
    elif iso == "A":
        locals()["iso"+str(i)] = mass.calculate_mass(formula='H+')
    else: 
        locals()["iso"+str(i)] = mass.calculate_mass(formula=f'{iso}')
    m2 += locals()["iso"+str(i)]  

m1 = round(m1, 18)
m2 = round(m2, 18)
ms = m1 - m2
ms = ms * u.u
ms = ms.to("kilograms")
ms = str(ms).split(" ")
ms = float(ms[0])
E = ms * c**2 * u.J

print(f'Massesvinn er {ms * u.kg} og frigjort energi er {E}')

end = time.perf_counter()

print("\n\n Programmet hadde en kjøretid på: ", end - start)

r = input('Ønsker du regne ut på nytt? (y/n): ')
r = r.lower()

if (r == "y"):
    cwd = os.getcwd()
    os.system(f"cd {cwd}")
    os.system("python Atom\massesvinn.py")
else:
    exit()