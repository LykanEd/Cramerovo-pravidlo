import numpy as np
import sys


def swap_rows(array, row1, row2):
    """
    Funkce prohodi radky o indexech row1 a row2 v matici array.
    """
    array[[row1, row2]] = array[[row2, row1]]


def get_nonzero_column(array, row_n, col_n, swap_count):
    """
    Funkce zkontroluje jestli na pozici array[row_n, col_n] je nenulove cislo,
    pokud neni, pokusi se najit nenulove cislo v danem sloupci na nejakem dalsim
    radku. Pokud na pozici array[row_n, col_n], vrati 0, pokud neni ale najde
    jine nenulove v danem sloupci, vrati 0 a zvysi swap_count. Pokud nenajde,
    vrati 0.
    """
    if array[row_n, col_n] != 0:
        return 0
    else:
        for i in np.arange(row_n+1, array.shape[0]):
            if array[i, col_n] != 0:
                swap_rows(array, row_n, i)
                swap_count+=1
                return 0
        print("Matice neni regularni.")
        return -1

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
        exit()
    return(matice1)

def preved_stupnovity_tvar(matice1, swap_count):
    """
    Funkce zkontroluje jestli na pozici array[row_n, col_n] je nenulove cislo,
    pokud neni, pokusi se najit nenulove cislo v danem sloupci na nejakem dalsim
    radku. Pokud nenajde, vypise, ze matice neni regularni a ukonci program.
    """
    # prevod do horniho stupnoviteho tvaru
    for i in np.arange(0, matice1.shape[0]):
        if get_nonzero_column(matice1, i, i, swap_count) != -1:
            for j in np.arange(i+1, matice1.shape[0]):
                matice1[j] = matice1[j] - matice1[i]*matice1[j, i]/matice1[i, i]
        else:
            return -1
    return matice1

def main(matice = [], file=None):
    """
    Pokusi se nacist matici v souboru file a vrati jeji determinant. Pokud
    nacteni/zpracovani matice probehne spatne, string 'error'.
    """
    if matice == [] and file != None:
        matice = nacti_matici(file)
    if matice == [] and file == None:
        return("error")
    swap_count = 0
    matice = preved_stupnovity_tvar(matice, swap_count)
    if isinstance(matice,int):
        return("error")
    determinant = 1
    for i in np.arange(0,matice.shape[0]):
        determinant*=matice[i,i]
    # změna znaménka za každé prohození radku
    determinant = (-1)**(swap_count)*determinant
    print(matice)
    return(determinant)


if __name__ == '__main__':
    files = sys.argv[1:]
    if len(files) == 0:
        files.append(input("Zadejte jméno souboru s maticemi (vcetne pripony): "))
    for file in files:
        determinant = main(file=file)
        if isinstance(determinant,str):
            print(f"Pri nacitani nebo zpracovani souboru {file} doslo k chybe.")
        else:
            print(f"Determinant matice v souboru {file} je: {determinant}.\n")
