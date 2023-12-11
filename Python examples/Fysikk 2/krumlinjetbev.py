from scipy import constants
def ΣF_s():
    n = int(input("Skriv inn antall gjeldene siffer: "))
    r = float(input("Skriv inn radius av sirkelen: "))
    v = float(input("Skriv inn hastigheten til objektet: "))
    aS = v**2/r
    a = constants.g + aS
    m = float(input("Skriv inn massen til objektet: "))
    ΣF = round(m*a, n)
    G = m*constants.g
    currG = round(ΣF/G, n)
    ans = "Summen av kreftene er lik: " + str(ΣF) + " N. Og obkjektet merker en G-kraft på " + str(currG) + " G."
    return ans

def minVelCon():
    n = int(input("Skriv inn antall gjeldene siffer: "))
    r = float(input("Skriv inn radius av sirkelen: "))
    v = round((constants.g*r)**0.5, n)
    h0 = 0
    h = 2*r
    v0 = (v**2+2*constants.g*h)**0.5
    ans = "Minste farten for at objektet skal ha kontakt med sirkelen er: " + str(v) + " m/s. Eller " + str(round(v*3.6, n)) + " km/t. \n Minste farten for at objektet skal ha kontakt med sirkelen fra start er: " + str(round(v0,n)) + " m/s. Eller " + str(round(v0*3.6, n)) + " km/t."
    return ans
