import random

listaDeCuvinte = ["pisica", "caine", "hamster", "copac"]
#listaDeCuvinte = ["abc"]
cuvantDeGhicit = random.choice(listaDeCuvinte)

print("Cuvantul de ghicit:", cuvantDeGhicit)

lungimeaCuvantului = len(cuvantDeGhicit)
count = 0
copieCuvantDeGhicit = cuvantDeGhicit


while count < lungimeaCuvantului:
    litera = input("Introdu litera pe are o intuiesti: ")
    litera = litera.lower()
    literePropuse = []
    literePropuse = literePropuse.append(litera)
    print(literePropuse)

    if litera in copieCuvantDeGhicit:

        print(litera, "este in cuvant.")
        count += 1
        copieCuvantDeGhicit = copieCuvantDeGhicit.replace(litera, '')
        print(literePropuse)
        #print("Restul cuvantului:", copieCuvantDeGhicit)
        print(count, " / ", lungimeaCuvantului)
    else:
        print(litera, "nu este in cuvant")
        print(count, " / ", lungimeaCuvantului)
        print(literePropuse)
    if count == lungimeaCuvantului:
        print("\nFelicitari ai ghicit cuvantul.")

print(copieCuvantDeGhicit)
