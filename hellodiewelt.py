#projekt nr. 16 - Kalkulator pól figur. 
'''
Kwadrat
prostokąt
trójkąt
rąb
koło
trapez
'''
#Stwórz podstawowe obliczenia. 
#dodaj warunek aby były wieksze od zera. 
def kwadrat(bokA, pole):
    bokA=int(input("Podaj bok twojego kwadratu"))
    pole=bokA**2
    print(f"Pole tego kwadratu to {pole}")

def prostokat(bokA, bokB, pole):
    bokA=int(input("Podaj pierwszy bok prostokata"))
    bokB=int(input("Podaj drugi bok prostokata"))
    pole=bokA * bokB
    print(f"Pole tego prostokata to {pole}")

def rab(przekatnaE, przekatnaF, pole):
    przekatnaE=int(input("Jak wiesz, albo nie wiesz, pole rabu jest o tyle specyficzne, ze aby je policzyc uzywamy przekatnych, nie bokow. Podaj pierwsza przekatna."))
    przekatnaF=int(input("A teraz druga"))
    pole=(przekatnaE*przekatnaF)/2
    print(f"A o to i pole tego wspanialego rabu -- {pole}")

def trojkat(bokA, wysokosc, pole):
    bokA=int(input("A wiec twoim wyborem jest trojkat. Bardzo ciekawa figura. Wiele wzorow i twierdzen. Do jego pola potrzebny jest bok."))
    wysokosc=int(input("Oraz wyskosc"))
    pole=(wysokosc*bokA)/2
    print(f"Polem tego trojkata jest {pole}")

def kolo(promien, pole):
    promien=int(input("Kolo nie jest takie proste, w sensie w policzeniu pola. Ale jakos, matematycy doszli do wniosku, ze przyda sie promień."))
    pole=promien**2*3,14
    print(f"Pole kola jest niedokladne, wynika to z faktu, ze uzywamy w policzeniu go Liczby Pi, ktora jest nieskonczona, wedle obecnej wiedzy. Z tego wzgledu otrzymasz przyblizony wynik -- {[pole]}")
    #jezeli chce moze uzytkownik otrzymac alternatywna wersje. Pi * r**2.
    #mozesz dodac ciekawostke o tym aleternatywnym polu

def trapez

def rownoleglobok