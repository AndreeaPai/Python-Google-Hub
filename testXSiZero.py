
tabla=[""," "," "," "," "," "," "," "," "]
print(tabla[0], ' |', tabla[1], '|', tabla[2])
print('----------')
print(tabla[3], '|', tabla[4], '|', tabla[5])
print('----------')
print(tabla[6], '|', tabla[7], '|', tabla[8])

while True:
    # Jucatorul X
    mutareX = int(input("\nUnde vrei sa marchezi cu X ?"))

    if tabla[mutareX] != 'x' and tabla[mutareX] != 'o': # daca spatiul nu e deja ocupat
       tabla[mutareX] = 'x'                             # ocupa-l
       print(tabla[0], '|', tabla[1], '|', tabla[2])
       print('----------')
       print(tabla[3], '|', tabla[4], '|', tabla[5])
       print('----------')
       print(tabla[6], '|', tabla[7], '|', tabla[8])
    else:
       print("\nSpatiul nu este disponibil. Incearca din nou.\n")
       break #

    if (tabla[0] == 'x' and tabla[1] == 'x' and tabla[2] == 'x') or \
        (tabla[3] == 'x' and tabla[4] == 'x' and tabla[5] == 'x') or \
        (tabla[6] == 'x' and tabla[7] == 'x' and tabla[8] == 'x') or \
        (tabla[0] == 'x' and tabla[3] == 'x' and tabla[6] == 'x') or \
        (tabla[1] == 'x' and tabla[4] == 'x' and tabla[7] == 'x') or \
        (tabla[2] == 'x' and tabla[5] == 'x' and tabla[8] == 'x') or \
        (tabla[0] == 'x' and tabla[4] == 'x' and tabla[8] == 'x') or \
        (tabla[2] == 'x' and tabla[4] == 'x' and tabla[6] == 'x'):
        print("\nFELICITARI ! Jucatorul X a castigat . ")
        break

    contor = 1
    if " " in tabla:
        contor = 0

    if contor == 1:
        print("\nREMIZA\n")
        break

    # Jucatorul O
    mutareO = int(input("\nUnde vrei sa marchezi cu o ?"))

    if tabla[mutareO] != 'o' and tabla[mutareO] != 'x': # daca spatiul nu e deja ocupat
       tabla[mutareO] = 'o'                             # ocupa-l
       print(tabla[0], '|', tabla[1], '|', tabla[2])
       print('----------')
       print(tabla[3], '|', tabla[4], '|', tabla[5])
       print('----------')
       print(tabla[6], '|', tabla[7], '|', tabla[8])
    else:
       print("\nSpatiul nu este disponibil. Incearca din nou.\n")
       break #

    if (tabla[0] == 'o' and tabla[1] == 'o' and tabla[2] == 'o') or \
        (tabla[3] == 'o' and tabla[4] == 'o' and tabla[5] == 'o') or \
        (tabla[6] == 'o' and tabla[7] == 'o' and tabla[8] == 'o') or \
        (tabla[0] == 'o' and tabla[3] == 'o' and tabla[6] == 'o') or \
        (tabla[1] == 'o' and tabla[4] == 'o' and tabla[7] == 'o') or \
        (tabla[2] == 'o' and tabla[5] == 'o' and tabla[8] == 'o') or \
        (tabla[0] == 'o' and tabla[4] == 'o' and tabla[8] == 'o') or \
        (tabla[2] == 'o' and tabla[4] == 'o' and tabla[6] == 'o'):
        print("\nFELICITARI ! Jucatorul O a castigat . ")
        break

    # verifica daca tabla e completa

    contor = 1
    if " " in tabla:
        contor = 0

    if contor == 1:
        print("\nREMIZA\n")
        break

print(tabla[0], '|', tabla[1], '|', tabla[2])
print('----------')
print(tabla[3], '|', tabla[4], '|', tabla[5])
print('----------')
print(tabla[6], '|', tabla[7], '|', tabla[8])
