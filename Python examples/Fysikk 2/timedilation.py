import pip
try:
    from scipy import constants as cnsts
except ImportError:
    pip.main(['install', 'scipy'])
    from scipy import constants as cnsts
def main():
    t_s = input("Skriv inn t_0 med enhet ex.(1y, 2mh, 3d, 4h, 5m, 6s): ")
    t_s = t_s.replace(" ", "")
    t_s = t_s.lower()
    t_s = t_s.split(",")
    t_0 = 0
    for time in t_s:
        if "y" in time:
            t_s = time.replace("y", "")
            t_s = float(t_s)
            t_0 += t_s * cnsts.year
        elif "mh" in time:
            t_s = time.replace("mh", "")
            t_s = float(t_s)
            t_0 += t_s * cnsts.day * 30.437
        elif "d" in time:
            t_s = time.replace("d", "")
            t_s = float(t_s)
            t_0 += t_s * cnsts.day
        elif "h" in time:
            t_s = time.replace("h", "")
            t_s = float(t_s)
            t_0 += t_s * cnsts.hour
        elif "m" in time:
            t_s = time.replace("m", "")
            t_s = float(t_s)
            t_0 += t_s * cnsts.minute
        elif "s" in time:
            t_s = time.replace("s", "")
            t_s = float(t_s)
            t_0 += t_s

    c = float(cnsts.c)
    v = eval(input("Skriv inn hastighet: "))
    t = t_0 / ((1 - (v**2 / c**2))**0.5)
    print(t, "s eller" , t / cnsts.minute, "minutter eller" , t / cnsts.hour, "timer eller" , t / cnsts.day, "dager eller" , t / cnsts.year, "år")

if __name__ == "__main__":
    main()