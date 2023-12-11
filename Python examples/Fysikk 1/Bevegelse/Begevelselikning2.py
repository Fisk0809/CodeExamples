import sympy, time

def main():
    variables = ["s", "s0", "v", "v0", "t", "a"]
    eq1 = ["s", "s0", "a", "v0", "t"]
    eq2 = ["v", "v0", "a", "t"]
    eq3 = ["s", "v", "v0", "t"]
    eq4 = ["a", "v", "v0", "s"]
    unkown = input("Velg den ukjente:" + str(variables) + ": ")

    if unkown.lower() in variables:
        variables.remove(unkown.lower())
        known = input("Velg de kjente:" + str(variables) + ": ")
        known = known.split(",")
        known.append(unkown.lower())
        if "v" not in known:
            temp_error = []
            for i in eq1:
                if i not in known:
                    temp_error.append(i)
            if len(temp_error) > 0:
                print("Du mangler verdier for følgende: " + str(temp_error))
                time.sleep(3)
                main()
            else:
                known.remove(unkown.lower())
                temp = {}
                temp[unkown.lower()] = sympy.Symbol(unkown.lower())
                x = sympy.Symbol(unkown.lower())
                for i in known:
                    var = float(input(f"Skriv inn {i}: "))
                    temp[i] = var
                s = temp["s"]
                s0 = temp["s0"]
                a = temp["a"]
                v0 = temp["v0"]
                t = temp["t"]
                print(sympy.solve(1/2*a*t**2+v0*t+s0-s, x))
                time.sleep(5)
                quit()
        if "s" not in known:
            temp_error = []
            for i in eq2:
                if i not in known:
                    temp_error.append(i)
            if len(temp_error) > 0:
                print("Du mangler verdier for følgende: " + str(temp_error))
                time.sleep(3)
                main()
            else:
                known.remove(unkown.lower())
                temp = {}
                temp[unkown.lower()] = sympy.Symbol(unkown.lower())
                x = sympy.Symbol(unkown.lower())
                for i in known:
                    var = float(input(f"Skriv inn {i}: "))
                    temp[i] = var
                v = temp["v"]
                v0 = temp["v0"]
                a = temp["a"]
                t = temp["t"]
                print(sympy.solve(v0+a*t-v, x))
                time.sleep(5)
                quit()
        if "a" not in known:
            temp_error = []
            for i in eq3:
                if i not in known:
                    temp_error.append(i)
            if len(temp_error) > 0:
                print("Du mangler verdier for følgende: " + str(temp_error))
                time.sleep(3)
                main()
            else:
                known.remove(unkown.lower())
                temp = {}
                temp[unkown.lower()] = sympy.Symbol(unkown.lower())
                x = sympy.Symbol(unkown.lower())
                for i in known:
                    var = float(eval(input(f"Skriv inn {i}: ")))
                    temp[i] = var
                s = temp["s"]
                v = temp["v"]
                v0 = temp["v0"]
                t = temp["t"]
                print(sympy.solve(1/2*(v0+v)*t-s, x))
                time.sleep(5)
                quit()
        if "t" not in known:
            temp_error = []
            for i in eq4:
                if i not in known:
                    temp_error.append(i)
            if len(temp_error) > 0:
                print("Du mangler verdier for følgende: " + str(temp_error))
                time.sleep(3)
                main()
            else:
                known.remove(unkown.lower())
                temp = {}
                temp[unkown.lower()] = sympy.Symbol(unkown.lower())
                x = sympy.Symbol(unkown.lower())
                for i in known:
                    var = float(input(f"Skriv inn {i}: "))
                    temp[i] = var
                s = temp["s"]
                v = temp["v"]
                v0 = temp["v0"]
                a = temp["a"]
                print(sympy.solve(((v**2-v0**2)/(2*s))-a, x))
                time.sleep(5)
                quit()
    else:
        print("Ukjent finnes ikke, prøv igjen")
        time.sleep(2)
        main()

if __name__ == '__main__':
    main()