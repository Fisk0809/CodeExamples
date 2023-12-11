# 6 og 7 krever at du har numpy installert
import numpy as np

def main():
    eq1 = "1/2*a*t**2+v0*t+s0"
    eq2 = "v0+a*t"
    eq3 = "1/2*(v0+v)*t"
    eq4 = "v**2-v0**2/2*s"
    eq5 = "v**2-v0**2/2*a" 
    eq6 = "sqrt(2*a*s)"
    eq7 = "sqrt(2*s/a)" 
    eq = int(input(f'Hvilken likning vil du bruke? 1# s = ({eq1}), 2# v = ({eq2}), 3# s = ({eq3}), 4# a = ({eq4}), #5 s = {eq5}, #6 v = ({eq6}), #7 t = ({eq7}): '))

    if eq == 1:
        a = float(input('Skriv inn akselerasjonen: '))
        t = float(input('Skriv inn tiden: '))
        v0 = float(input('Skriv inn start hastighet: '))
        s0 = float(input('Skriv inn start strekningen: '))
        eqR = 1/2*a*t**2+v0*t+s0

    if eq == 2:
        v0 = float(input('Skriv inn start hastigheten: '))
        a = float(input('Skriv inn akselerasjonen: '))
        t = float(input('Skriv inn tiden: '))
        eqR = v0+a*t

    if eq == 3:
        v0 = float(input('Skriv inn start hastigheten: '))
        v = float(input('Skriv inn slutt hastighet: '))
        t = float(input('Skriv inn tiden: '))
        eqR = 1/2*(v0+v)*t

    if eq == 4:
        v = float(input('Skriv inn slutt hastighet: '))
        v0 = float(input('Skriv inn start hastighet: '))
        s = float(input('Skriv inn strekningen:  '))
        eqR = (v**2-v0**2)/(2*s)
    
    if eq == 5:
        v = float(input('Skriv inn slutt hastigheten: '))
        v0 = float(input('Skriv inn start hastigheten: '))
        a = float(input('Skriv inn akselerasjonen: '))
        eqR= (v**2-v0**2)/(2*a)
    if eq == 6:
        a = float(input('Skriv inn akselerasjonen: '))
        s = float(input('Skriv inn strekningen: '))
        eqR= np.sqrt(2*a*s)
    if eq == 7:
        s = float(input('Skriv inn strekningen: '))
        a = float(input('Skriv inn akselerasjonen: '))
        eqR = np.sqrt(2/s*a)    
        
    print(f'{eqR:.2f}')
if __name__ == '__main__':
    main()

