import numpy as np

def nacti_matici(n, file):
    if n < 2:
    print(f"Zadan nevhodny rozmer matice {n}.")
    exit()

try:
    # nacteni matic ze souboru
    matice1 = np.loadtxt(file, dtype='f', delimiter=',', max_rows=n)
    matice2 = np.loadtxt(file, dtype='f', delimiter=',', skiprows=n)

    # kontrola rozmeru matice
    if matice1.shape != (n, n) or matice2.shape[0] != n:
        print("Matice nemaji pozadovany tvar.\n")
        exit()
except:
    # pro pripad chybneho nacteni ze souboru
    print("Matice nemaji pozadovany tvar / byl zadan spatny soubor s maticemi.\n")
    exit()
