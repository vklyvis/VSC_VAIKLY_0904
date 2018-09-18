# list / darbas su failu
# if for / user input
# sarasas if spej sarase
# while4
#
# https: // www.ef.com / english - resources / english - vocabulary / top - 1000 - words /
# lygis
import random

nepakartas = '''Sorry, wrong letter; Neteisingas spejimas
  +---+
  |   |
      |
      |
      |
      |
========='''

berankupakartas = '''Sorry, wrong letter; Neteisingas spejimas
  +---+
  |   |
  O   |
  |   |
      |
      |
========='''
berankospakartas = '''Sorry, wrong letter, Neteisingas spejimas
  +---+
  |   |
  O   |
 /|   |
      |
      |
========='''
bekojupakartas = '''Sorry, wrong letter, Neteisingas spejimas
  +---+
  |   |
  O   |
 /|\  |
      |
      |
========='''

beveikpakartas = '''Sorry, wrong letter, Neteisingas spejimas
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
========='''

pakartas = '''Sorry, wrong letter, Gratz, You hanged yourself - OUT ZYBEN!
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========='''

atsakymas = []
lygis = int(input("iveskite lygi: "))

while lygis <= 1 or lygis > 6:
    lygis = int(input("iveskite lygi: "))

alist = open("zodziu_sarasas.txt", "r")
words = alist.readlines()
for zodis in words:
    wordlen = zodis.__len__()
    if lygis + 1 == wordlen:
        atsakymas.append(zodis)
zodis_kuri_spet = random.choice(list(atsakymas))
print zodis_kuri_spet

display = []

used = []

display.extend(zodis_kuri_spet.rstrip())

used.extend(display)

for i in range(len(display)):
    display[i] = "_"
print (" ".join(display))
bound = 0
teis = 0
neteis = -1
panaudota = []
panaudotaneteisinga = []

while bound < lygis:
    guess = raw_input("Enter a letter: ")
    guess = guess.lower()

    if guess in panaudota:
        print "si raide yra teisinga, bet jau buvo panaudota"
        teis = teis - 1

    if guess in panaudotaneteisinga:
        neteis = neteis + 1
        bound = bound - 1
        print "Antra karta panaudota neteisinga raide"
        if neteis > 0:
            bound = bound + 1



    for i in range(len(zodis_kuri_spet)):
        if zodis_kuri_spet[i] == guess and guess in used not in panaudota:
            display[i] = guess
            teis = teis + 1
            panaudota.extend(guess)
            print "Correct!"


    if guess not in display and lygis == 6:
        bound = bound + 1
        if bound == 1:
            print nepakartas
        elif bound == 2:
            print(berankupakartas)
        elif bound == 3:
            print(berankospakartas)
        elif bound == 4:
            print(bekojupakartas)
        elif bound == 5:
            print(beveikpakartas)
        elif bound == 6:
            print(pakartas)
        print bound
        panaudotaneteisinga.extend(guess)

    if guess not in display and lygis == 5:
        bound = bound + 1
        if bound ==1:
            print nepakartas
        elif bound == 2:
            print(berankupakartas)
        elif bound == 3:
            print(berankospakartas)
        elif bound == 4:
            print(bekojupakartas)
        elif bound == 5:
            print(pakartas)
        print bound
        panaudotaneteisinga.extend(guess)


    if guess not in display and lygis == 4:
        bound = bound + 1
        if bound == 1:
            print nepakartas
        elif bound == 2:
            print(berankupakartas)
        elif bound == 3:
            print(beveikpakartas)
        elif bound == 4:
            print(pakartas)
        print bound
        panaudotaneteisinga.extend(guess)


    if guess not in display and lygis == 3:
        bound = bound + 1
        if bound == 1:
            print nepakartas
        elif bound == 2:
            print berankupakartas
        elif bound == 3:
            print pakartas
        print bound
        panaudotaneteisinga.extend(guess)


    if guess not in display and lygis == 2:
        bound = bound + 1
        if bound == 1:
            print nepakartas
        if bound == 2:
            print pakartas
        print bound
        panaudotaneteisinga.extend(guess)


    print(" ".join(display))

    if teis == lygis:
        print "CONGRATULATIONS! You won!"
        break




