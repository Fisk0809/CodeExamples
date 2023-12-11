from pickle import FALSE, TRUE
from pyteomics import mass
import re
from scipy import constants



# iso = input('Skriv inn isotop: ')
# iso = iso.capitalize()

# numbers = re.compile(r'(\d+)')
# iso = numbers.sub(r'[\1]', iso)

# n1 = mass.calculate_mass(formula=f'{iso}')

# print(n1)

c = constants.speed_of_light

go = FALSE
eq1 = 0
while (go==FALSE):
    iso = input("Skriv inn første isotop: ")
    if (iso != "n1"):
        iso = iso.capitalize()

        numbers = re.compile(r'(\d+)')
        iso = numbers.sub(r'[\1]', iso)
    
        eq1 += mass.calculate_mass(formula=f'{iso}')
    else:
        eq1 += 1.00866

    svar = input("Skal du legge til flere isotoper? (y/n) ")
    print("\n")
    svar.lower()
    if (svar == "n"):
        go=TRUE
        
go1 = FALSE
eq2 = 0
while (go1==FALSE):
    iso = input("Skriv inn andre isotop: ")
    if (iso != "n1"):
        iso = iso.capitalize()

        numbers = re.compile(r'(\d+)')
        iso = numbers.sub(r'[\1]', iso)
    
        eq2 += mass.calculate_mass(formula=f'{iso}')
    else:
        eq2 += 1.00866

    svar = input("Skal du legge til flere isotoper? (y/n) ")
    print("\n")
    svar.lower()
    if (svar == "n"):
        go1=TRUE

ms = eq1 - eq2

ms = ms * 1.66 * 10**-27

et = ms * c**2

print(f'Massesvinn = {ms} kg og Energitap = {et} J'),
