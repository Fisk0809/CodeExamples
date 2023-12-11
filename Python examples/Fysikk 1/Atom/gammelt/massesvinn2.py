import pip, os, re
try:
    import pint; from pyteomics import mass; from scipy import constants as cnsts
except:
    pip.main(['install', 'pint'])
    pip.main(['install', 'pyteomics'])
    pip.main(['install', 'scipy'])
    cwd = os.getcwd()
    os.system(f"cd {cwd}")
    os.system("python massesvinn2.py")
os.system('cls')
u = pint.UnitRegistry()
Q = u.Quantity
c = cnsts.c


def ogiso():
    global eq1
    eq1 = 0
    i = 0
    a = int(input('Skriv inn antall orginale isotoper: '))
    print("\n")

    for i in range(a):
        i += 1
        iso = input('Skriv inn isotopen: ')
        print("\n")
        if (iso != "n1"):
            iso = iso.capitalize()

            numbers = re.compile(r'(\d+)')
            iso = numbers.sub(r'[\1]', iso)
            locals()["iso"+str(i)] = mass.calculate_mass(formula=f'{iso}')
        else:
            q = float(input('Skriv inn antall nøytroner: '))
            print("\n")
            locals()["iso"+str(i)] = 0
            locals()["iso"+str(i)] += 1.00866 * q
    
    for i in range(a):
        i +=1
        eq1 += locals()["iso"+str(i)]

def nyiso():
    global eq2
    eq2 = 0
    i = 0
    b = int(input('Skriv inn antall nye isotoper: '))
    print("\n")
    for i in range(b):
        i += 1
        iso = input('Skriv inn isotopen: ')
        print("\n")
        if (iso != "n1"):
            iso = iso.capitalize()

            numbers = re.compile(r'(\d+)')
            iso = numbers.sub(r'[\1]', iso)
            locals()["iso"+str(i)] = mass.calculate_mass(formula=f'{iso}')
        else:
            q = float(input('Skriv inn antall nøytroner: '))
            print("\n")
            locals()["iso"+str(i)] = 0
            locals()["iso"+str(i)] += 1.00866 * q
    
    for i in range(b):
        i +=1
        eq2 += locals()["iso"+str(i)]

ogiso()
nyiso()

eqR = eq1-eq2
ms = eqR * 1.66e-27
E = ms * c**2

ms = ms * u.kg
E = E * u.J 

print(f'Massesvinn = {ms} og Energitap = {E}')

os.system("pause")




