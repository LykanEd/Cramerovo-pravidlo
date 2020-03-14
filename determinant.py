import numpy as np
import sys


def swap_rows(array, row1, row2):
    """
    Funkce prohodi radky o indexech row1 a row2 v matici array.
    """
    array[[row1, row2]] = array[[row2, row1]]


def get_nonzero_column(array, row_n, col_n):
    """
    Funkce zkontroluje jestli na pozici array[row_n, col_n] je nenulove cislo,
    pokud neni, pokusi se najit nenulove cislo v danem sloupci na nejakem dalsim
    radku. Pokud nenajde, vypise, ze matice neni regularni a ukonci program.
    """
    if array[row_n, col_n] != 0:
        return 0
    else:
        for i in np.arange(row_n+1, array.shape[0]):
            if array[i, col_n] != 0:
                swap_rows(array, row_n, i)
                return 0
        print("Matice neni regularni.")
        return -1

def nacti_matici(file):
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
        exit()
    return(matice1)

def preved_stupnovity_tvar(matice1):
    # prevod do horniho stupnoviteho tvaru
    for i in np.arange(0, matice1.shape[0]):
        if get_nonzero_column(matice1, i, i) != -1:
            for j in np.arange(i+1, matice1.shape[0]):
                matice1[j] = matice1[j] - matice1[i]*matice1[j, i]/matice1[i, i]
        else:
            return -1
    matice1[-1] = matice1[-1]/matice1[-1, -1]


    # prevod na jednotkovou matici
    for i in np.arange(matice1.shape[0]-1, -1, -1):
        for j in np.arange(0, i):
            matice1[j] = matice1[j] - matice1[i]*matice1[j, i]/matice1[i, i]
        matice1[i] = matice1[i]/matice1[i, i]
    return matice1

def main(file):
    matice = nacti_matici(file)
    matice = preved_stupnovity_tvar(matice)
    if isinstance(matice,int):
        return -1
    print("Upravena matice 1: \n")
    print(matice)
    return 0


if __name__ == '__main__':
    files = sys.argv[1:]
    if len(files) == 0:
        files.append(input("Zadejte jméno souboru s maticemi (vcetne pripony): "))
    for file in files:
        check = main(file)
        if check != 0:
            print(f"Pri nacitani nebo zpracovani souboru {file} doslo k chybe.")
            exit()
