import time, pip, os, re
try:
    import pint;
    from pyteomics import mass;
    from scipy import constants as cnsts
except ImportError:
        pip.main(['install', 'pint'])
        pip.main(['install', 'pyteomics'])
        pip.main(['install', 'scipy'])
        os.system('cls')
        print('Libraries er installert')
        time.sleep(3)
        cwd = os.getcwd()
        os.system(f"cd {cwd}")
        os.system("python Atom\massesvinn2.py")

def main():
    os.system('cls')
    global n
    global c
    global Q
    u = pint.UnitRegistry()
    Q = u.Quantity
    c = cnsts.c
    n = cnsts.neutron_mass
    n = n * u.kg
    n = n.to('dalton')
    n = str(n).split(" ")
    n = float(n[0])
    svar = input("Skriv inn ligning: ")
    svar = svar.replace(" ", "")
    start = time.perf_counter()
    ligning = svar.split("->")
    m1 = get_mass(ligning[0])
    m2 = get_mass(ligning[1])
    ms = ((m1 - m2) * u.u).to('kilograms')
    ms = str(ms).split(" ")
    ms = float(ms[0])
    E  = (ms * c**2) * u.J
    print(f'Massesvinn er {ms * u.kg} og frigjort energi er {E}')
    end = time.perf_counter()
    print("\n\n Programmet hadde en kjøretid på: ", end - start)
    r = input('Ønsker du regne ut på nytt? (y/n): ')
    r = r.lower()
    if (r == "y"):
        main()
    else:
        exit()

def get_mass(isotop):
    isotop = isotop.split("+")
    iso_mass = 0
    for atom in isotop:
        atom = atom.capitalize()
        numbers = re.compile(r'(\d+)')
        atom = numbers.sub(r'[\1]', atom)
        if "*" in atom:
            atom = atom.split("*")
            atom1 = atom[1]
            atom2 = atom[0].replace("[", "").replace("]", "")
            atom2 = float(atom2)
            atom1 = atom1.capitalize()
            if atom1 == "N[1]":
                atom1 = n
            elif atom1 == "A":
                atom1 = mass.calculate_mass(formula='H+')
            else:
                atom1 = mass.calculate_mass(formula=f'{atom1}')
            atom = atom1 * atom2
        elif atom == "N[1]":
            atom = n
        elif atom == "A":
            atom = mass.calculate_mass(formula='H+')
        else:
            atom = mass.calculate_mass(formula=f'{atom}')
        iso_mass += atom
    return iso_mass

if __name__ == "__main__":
    main()