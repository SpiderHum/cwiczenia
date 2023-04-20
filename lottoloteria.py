#oke jak działa lotto?
#z 49 liczb losuje się 6, gracz zakreśla 6 i później wygrywa lub nie
#wypada mu poiedzieć ile liczb trafił

import random

#1. Funkcja losująca liczby
#2. Funkcja pytająca uytkownika o liczby
#3. Funkcja sprawdzająca

def numbers():
    for i in range(6):
        numbar[i]=random.randint(1,50)

def frage():
    for i in range(6):
        a=i+1
        odpowiedź[i]=int(input(f'Podaj {a}. liczbę w zakresie od 1 do 50\n'))

def sprawdzenie():
    #stworzyć zbiór x, które występują i w numabr i odpowiedź
    for i in range(6):
        if numbar[i]==odpowiedź[i]:
            print(f'Zgadles {i}. liczbe, czyli {odpowiedź[i]}')
        else:
            print("Pudło")
        
print("Ich liebe Deutsch, und du? Ich hasse diese Sprache")
numbar=[""] * 6
odpowiedź=[""] * 6
print("Witaj w loterii lotto, chcesz wziąźć udział?")
frage()
numbers()
sprawdzenie() #ale on mądry, ten Python, ja niepotrzebnie dałem "numabr" i "odpowiedź" jako argumenty a on mi zwrócił uwagę, ze nie są potrzebne


