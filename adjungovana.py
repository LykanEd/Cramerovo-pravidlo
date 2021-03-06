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
        matice1 = np.loadtxt(file, dtype='f', delimiter=',')

        # kontrola rozmeru matice
        if matice1.shape[0] != matice1.shape[1]:
            print("Matice nema pozadovany tvar.\n")
            exit()
    except:
        # pro pripad chybneho nacteni ze souboru
        print("Matice nema pozadovany tvar / byl zadan spatny soubor s matici.\n")
        raise ZadanySpatnyTvarError
    return(matice1)


def alg_doplnek(matice, i, j):
    """
    Funkce vrati algebraicky doplnek zadane matici o indexech i,j.
    """
    # kontrola platnosti indexu
    if not (0 <= i <= matice.shape[0] and 0 <= i <= matice.shape[0]):
        raise Error("Spatne zadane indexy radku a sloupcu.")
    # matice a jeji determinant po vyskrtnuti i radku a j sloupce
    matice_vysrtnuto = np.delete(np.delete(matice, i, 0), j, 1)
    determinant_vyskrtnuto = determinant.main(matice_vysrtnuto)
    return((-1)**(i+j)*determinant_vyskrtnuto)


def main(matice):
    """
    Pro zadanou matici / matici nactenou ze souboru file vrati adjungovanou matici.
    """
    # kontrola, jestli byla zadana matice nebo soubor s matici
    if not isinstance(matice, np.ndarray):
        matice = nacti_matici(file)
    # vytvoreni ,,prazdne formy" pro adjungovanou matici
    adjungovana_matice = np.empty(dtype="f", shape=[0, matice.shape[0]])
    # naplneni adjungovane matice alg doplnky
    for i in np.arange(matice.shape[0]):
        radek = np.array([], dtype="f")
        for j in np.arange(matice.shape[0]):
            radek = np.append(radek, alg_doplnek(matice, j, i))
        adjungovana_matice = np.append(adjungovana_matice, [radek], axis=0)
    return(adjungovana_matice)


def inverzni_z_adj(matice):
    """
    Pro zadanou matici vrati inverzni matici, vypoctenou pomoci adjungovane matice,
    a matici adjungovanou.
    Pokud zadana matice neni regularni, misto inverzni matice vrati 0.
    """
    # kontrola, jestli byla zadana matice nebo soubor s matici
    if not isinstance(matice, np.ndarray):
        matice = nacti_matici(file)
    adjungovana_matice = main(matice)
    # vypocet determinantu a kontrola, ze neni nulovy
    det = determinant.main(matice)
    if det != 0:
        inverzni_matice = adjungovana_matice/np.full(adjungovana_matice.shape[0], det)
    else:
        inverzni_matice = 0
    return(inverzni_matice, adjungovana_matice)


if __name__ == '__main__':
    files = sys.argv[1:]
    if len(files) == 0:
        files.append(input("Zadejte jméno souboru s maticemi (vcetne pripony): "))
    for file in files:
        try:
            inverzni_matice, adjungovana_matice = inverzni_z_adj(file)
        except ZadanySpatnyTvarError:
            continue
        print(f"Adjungovana matice k matici v souboru {file}:")
        print(adjungovana_matice)
        if isinstance(inverzni_matice, int):
            print("Matice je singularni, nema inverzni matici.")
        else:
            print(f"Inverzni matice:")
            print(inverzni_matice)
