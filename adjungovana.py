import numpy as np
import sys
import determinant

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

def alg_doplnek(matice, i, j):
    if not (0 <= i <= matice.shape[0] and 0 <= i <= matice.shape[0]):
        raise Error("Spatne zadane indexy radku a sloupcu.")
    matice_vysrtnuto = np.delete(np.delete(matice, i, 0), j, 1)
    determinant_vyskrtnuto = determinant.main(matice=matice_vysrtnuto)
    return((-1)**(i+j)*determinant_vyskrtnuto)

def main(matice = [], file=None):
    """
    Pro zadanou matici / matici nactenou ze souboru file vrati adjungovanou matici.
    """
    if matice == [] and file != None:
        matice = nacti_matici(file)
    if matice == [] and file == None:
        return("error")
    adjungovana_matice = np.empty(dtype="f", shape=[0, matice.shape[0]])
    for i in np.arange(matice.shape[0]):
        radek = np.array([], dtype="f")
        for j in np.arange(matice.shape[0]):
            radek = np.append(radek, alg_doplnek(matice,j,i))
        adjungovana_matice = np.append(adjungovana_matice, [radek], axis=0)
    return(adjungovana_matice)

def inverzni_z_adj(matice=[], file=None):
        """
        Pro zadanou matici vrati inverzni matici vypoctenou pomoci adjungovane matice.
        """
        if matice == [] and file != None:
            matice = nacti_matici(file)
        if matice == [] and file == None:
            raise Error("Spatne zadane parametry funkce.")
        adjungovana_matice = main(matice=matice)
        determinant = determinant.main(matice=matice)
        if True:
            inverzni_matice = adjungovana_matice/np.full(adjungovana_matice.shape[0], determinant)
        return(inverzni_matice, adjungovana_matice)

if __name__ == '__main__':
    files = sys.argv[1:]
    if len(files) == 0:
        files.append(input("Zadejte jméno souboru s maticemi (vcetne pripony): "))
    for file in files:
        adjungovana_matice, inverzni_matice = inverzni_z_adj(file=file)
        print(f"Adjungovana matice k matici v souboru {file}:")
        print(adjungovana_matice)
        print(f"Inverzni matice:")
        print(inverzni_matice)
