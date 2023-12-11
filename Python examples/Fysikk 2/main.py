import krumlinjetbev as kb
def main():
    n = int(input("1. Summen av sentripetalkraften \n2. Minste farten for kontakt i toppen av loop \n"))
    if n == 1:
        print(kb.ΣF_s())
    if n == 2:
        print(kb.minVelCon())

if '__main__' == __name__:
    main()