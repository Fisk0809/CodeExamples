import sys
eq = (input('Skriv inn en funksjon: ')) #Definerer funksjonen
def setup():
   
    leftend = int(input('Skriv inn a (Venstre sluttpunkt): ')) #Definerer starten, ved bruk av integer for å definere det som et tall og ikke bare et symbol
    rightend = int(input('Skriv inn b (Høyre sluttpunkt): ')) #Definerer slutten, ved bruk av integer for å definere det som et tall og ikke bare et symbol

    n = int(input('Skriv inn antall trapeser: ')) #Definerer mengden trapeser for utrengning

    #Utregning av arealet med bruk av bredden på hvert trapes

    deltaX = (rightend-leftend)/float(n) #Definerer bredden på trapesene, ved å bruke avstanden mellom høyre og venstre sluttpunkt, deretter deler på mengden trapeser

    #Printer resultatene
    
    print(f'Bredden er {deltaX}')
    #print(f'Summen av høyden til venstresluttpunkt er {LeftEndSum(n,leftend,deltaX)}') #Unødvendig, kun brukt under testing av programmet
    #print(f'Summen av høyden til høyresluttpunkt er {RightEndSum(n, leftend,deltaX)}') #Unødvendig, kun brukt under testing av programmet
    print(f'Totalt smittede: {Trap(n,leftend,deltaX)}')

#Summen av venstre sluttpunkt
def LeftEndSum(n,leftend,deltaX):
    leftSum = 0.0 #Bruker .0 for å vise til at float blir brukt automatisk
    for i in range(n):
        x = leftend + i*deltaX
        h = eval(eq)
        leftSum = leftSum+h*deltaX
    return leftSum

#Summen av høyre sluttpunkt    
def RightEndSum(n,leftend,deltaX):
    rightSum = 0.0 #Bruker .0 for å vise til at float blir brukt automatisk
    for i in range(n):
        x = leftend + (i+1)*deltaX
        h = eval(eq)
        rightSum = rightSum+h*deltaX
    return rightSum

# Trapes areal tilnærming
def Trap(n,leftend,deltaX):
    tsum = .5*(RightEndSum(n,leftend,deltaX)+LeftEndSum(n,leftend,deltaX))
    return tsum


if __name__ == '__main__':
    setup()




