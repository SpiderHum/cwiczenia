#oke jak działa lotto?
#z 49 liczb losuje się 6, gracz zakreśla 6 i później wygrywa lub nie
#wypada mu poiedzieć ile liczb trafił

import random

#1. Funkcja losująca liczby
#2. Funkcja pytająca uytkownika o liczby
#3. Funkcja sprawdzająca

def numbers():
    for i in range(6):
        numbar=random.randint(0,49)
        print(numbar)


def frage(odpowiedź):
    for i in range(6):
        a=i+1
        odpowiedź[i]=int(input(f'Podaj {a}. liczbę'))

print("Ich liebe Deutsch, und du? Ich hasse diese Sprache")

odpowiedź=[""] * 6

