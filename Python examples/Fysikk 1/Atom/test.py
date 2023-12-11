import pip,time
try:
    from mendeleev import *
except ImportError:
    pip.main(['install', 'mendeleev'])
    from mendeleev import *

n = "Krypton"

for iso in element(n).isotopes:
    print(iso.mass_number, iso.mass)


