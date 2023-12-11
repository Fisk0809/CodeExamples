import turtle
from scipy import constants



def main():
    c = float(constants.c)
    e = float(constants.e)
    var = ["q","v","B","m","r","F","a_s"]
    unkown = input("Velg den ukjente:" + str(var) + ": ").lower()
    
    if unkown in var:
        var.remove(unkown)
        known = input("Skriv inn de kjente variablene: " + str(var)).lower().split(",")
        known.append(unkown)
        if "a_s" not in known:
            
        




    ΣF = q*v*B
    a_s = (v^2)/r
    a_s = ΣF/m

    print(a_s)
    
    
if __name__ == '__main__':
    main()