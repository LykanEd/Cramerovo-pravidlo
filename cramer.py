import numpy as np
import sys
import determinant
from errors import *

def nacti_matici(file):
    """
    Funkce nacte matici ze souboru file (jednotlive členy matice na radku musi
    byt oddeleny carkou. Zkontroluje tvar matice a vrati jako np array.)
    """
    try:
        # nacteni matic ze souboru
        n = np.loadtxt(file, dtype='f', delimiter=',', max_rows=1).shape[0]
        matice1 = np.loadtxt(file, dtype='f', delimiter=',', max_rows=n)
        vektor = np.loadtxt(file, dtype='f', delimiter=',', skiprows= n, max_rows=n)

        # kontrola rozmeru matice
        if matice1.shape[0] != matice1.shape[1]:
            print("Matice nema pozadovany tvar.\n")
            raise ZadanySpatnyTvarError
        if vektor.shape[0] != n:
            raise ZadanySpatnyTvarError
    except:
        # pro pripad chybneho nacteni ze souboru
        print("Matice nema pozadovany tvar / byl zadan spatny soubor s matici.\n")
        exit()
    return(matice1, vektor)

def main(matice, vektor):
    while True:
        j = int(input("Zadejte pozadovanou slozku reseni rovnice Ax = b (prvni index := 1): "))
        if 0 <= j <= matice.shape[0]:
            j-=1
            break
        else:
            print("Zadana neplatna hodnota.")

    matice2 = np.copy(matice)
    matice2[:,j] = vektor
    det = determinant.main(matice)
    if det == 0:
        raise NeregularniMaticeError
    print(det)
    return(determinant.main(matice2)/det)

if __name__ == '__main__':
    files = sys.argv[1:]
    if len(files) == 0:
        files.append(input("Zadejte jméno souboru s maticemi (vcetne pripony): "))
    for file in files:
        try:
            matice, vektor = nacti_matici(file)
            x_j = main(matice, vektor)
            print(f"Pozadovana slozka reseni je: {x_j}")
        except NeregularniMaticeError:
            print(f"Matice v souboru {file} neni regularni a soustava nema reseni.")
        except ZadanySpatnyTvarError:
            pass
