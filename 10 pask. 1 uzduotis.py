#Sukurti minibiudžeto programą, kuri:
#Leistų vartotojui įvesti pajamas arba išlaidas (su "-" ženklu)
#Pajamas ir išlaidas saugotų sąraše, o sąrašą pickle faile (uždarius programą, įvesti duomenys nedingtų)
#Atvaizduotų jau įvestas pajamas ir išlaidas
#Atvaizduotų įvestų pajamų ir išlaidų balansą (sudėtų visas pajamas ir išlaidas)

import pickle

failo_pavadinimas = 'minibiudzetas.pkl'

try:
    with open(failo_pavadinimas, 'rb') as failas:
        print(pickle.load(failas))
except (FileNotFoundError, EOFError):
    print('Klaida užkraunant failą')

while True:
    skaiciai = input('Įveskite pajamas (+) arba išlaidas (-) (arba paspauskite Enter, kad baigti): ')

    if skaiciai == '':
        break
    pajamos = []
    try:
        suma = float(skaiciai)
        pajamos.append(suma)
    except ValueError:
        print('Neteisingas formatas. Prašome įvesti skaičių su \'+\' arba \'-\' ženklu.')

with open(failo_pavadinimas, 'wb') as failas:
    pickle.dump(pajamos, failas)

print("\nĮvestos pajamos ir išlaidos:")
for suma in pajamos:
    print(suma)

balansas = sum(pajamos)
print(f"\nBalansas: {balansas}")

