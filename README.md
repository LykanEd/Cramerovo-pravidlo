# Skripty pro vypocet invezni matice a cramerova pravidla
Jednotlive skripty nefunguji samostatně ale jsou vzajemne propojeny, musi proto
zustat v jedne slozce. Kazdy ze skriptu obsahuje funkci main, ktera vraci
pro skript odpovidajici vec, viz nize.

## determinant.py
Obsahuje funkce pro vypocet determinantu.
### Funkce main(matice)
Vrati determinant matice, argument muze byt matice nebo soubor s matici.

## adjungovana.py
Obsahuje funkce pro vypocet adjungovane matice a pro vypocet inverzni matice
pomoci adjungovane.
### Funkce main(matice)
Vrati adjungovanou matici k zadane matici, argument muze byt matice nebo soubor s matici.
### Funkce inverzni_z_adj(matice)
Pro zadanou matici vrati inverzni matici, vypoctenou pomoci adjungovane matice,
a matici adjungovanou. Pokud zadana matice neni regularni, misto inverzni matice vrati 0.
Argument muze byt matice nebo soubor s matici.

## cramer.py
Obsahuje funkce pro vypocet j-teho reseni rovnice Ax = b.
### Funkce main(matice, vektor)
Vrati j-te reseni soustavy Ax = b, A je matice v argumentu a b je vektor v
argumentu. Narozdíl od zbylych skriptu nelze vlozit soubor, ale je potreba
vlozit primo matici a vektor. Na hodnotu j se funkce zepta.

## errors.py
Obsahuje vyuzivane errory. Ty se daji zvlast resit v jednotlivych implementacich
podle potreby.

# Spusteni skriptu z prikazove radky
Veskere skripty (krome errors.py) lze spustit z prikazove radky spolecne se zadanim
libovolneho poctu souboru s maticemi.

```
python skript.py matice1.txt matice2.txt ...
```

Pro vsechny zadane souboru bude spustena funkce main v danem skriptu (pro adjungovana.py
  bude spustena funkce inverzni_z_adj).
