import numpy as np


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

def nacti_matici(n, file):
    # Zadani radu matice a vstupniho souboru
    n = int(input("Zadejte rad prvni matice: "))
    file = input("Zadejte jméno souboru s maticemi (vcetne pripony): ")

    # Kontrola smysluplnosti vstupu
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
    return(matice1, matice2)

def preved_stupnovity_tvar
(matice1, matice2):
    # prevod do horniho stupnoviteho tvaru
    for i in np.arange(0, matice1.shape[0]):
        if get_nonzero_column(matice1, matice2, i, i) != -1:
            for j in np.arange(i+1, matice1.shape[0]):
                matice2[j] = matice2[j] - matice2[i]*matice1[j, i]/matice1[i, i]
                matice1[j] = matice1[j] - matice1[i]*matice1[j, i]/matice1[i, i]
    matice2[-1] = matice2[-1]/matice1[-1, -1]
    matice1[-1] = matice1[-1]/matice1[-1, -1]


    # prevod na jednotkovou matici
    for i in np.arange(matice1.shape[0]-1, -1, -1):
        for j in np.arange(0, i):
            matice2[j] = matice2[j] - matice2[i]*matice1[j, i]/matice1[i, i]
            matice1[j] = matice1[j] - matice1[i]*matice1[j, i]/matice1[i, i]
        matice1[i] = matice1[i]/matice1[i, i]
        matice2[i] = matice2[i]/matice1[i, i]
    return(matice1, matice2)

print("Upravena matice 1: \n")
print(matice1)
print("\nUpravena matice 2: \n")
print(matice2)

if __name__ == '__main__':
    main()
