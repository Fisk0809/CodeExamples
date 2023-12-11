def main():
    ΣF = 'm*a'
    a = '(ΣF1 + ΣF2)/m'


    q = int(input(f'Hvilken likning vil du bruke: #1 ΣF = {ΣF}, #2 a = {a} eller : '))

    if q == 1: 
        m = float(input('Skriv inn massen: '))
        a = float(input('Skriv inn aksellerasjonen: '))
        ΣF = m*a
        print(f'{ΣF}N')
    
    if q == 2:
        ΣF1 = float(input('Skriv inn kraft 1: '))
        ΣF2 = float(input('Skriv inn kraft 2: '))
        m = float(input('Skriv inn massen: '))
        a = (ΣF1+ΣF2)/m
        print(f'{a}m/s^2')

main()