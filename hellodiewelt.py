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
def kwadrat(): #ta funkcja o wszytsko pyta wewnątrz niej, dzięki temu nie trzeba uwzględniać zadnych argumentów.  
    bokA=int(input("Podaj bok twojego kwadratu"))
    return bokA**2
    

def prostokat():
    bokA=int(input("Podaj pierwszy bok prostokata"))
    bokB=int(input("Podaj drugi bok prostokata"))
    return bokA * bokB


def rab():
    przekatnaE=int(input("Jak wiesz, albo nie wiesz, pole rabu jest o tyle specyficzne, ze aby je policzyc uzywamy przekatnych, nie bokow. Podaj pierwsza przekatna."))
    przekatnaF=int(input("A teraz druga"))
    return (przekatnaE*przekatnaF)/2

def trojkat():
    bokA=int(input("A wiec twoim wyborem jest trojkat. Bardzo ciekawa figura. Wiele wzorow i twierdzen. Do jego pola potrzebny jest bok."))
    wysokosc=int(input("Oraz wyskosc"))
    return (wysokosc*bokA)/2
    

def kolo():
    promien=int(input("Kolo nie jest takie proste, w sensie w policzeniu pola. Ale jakos, matematycy doszli do wniosku, ze przyda sie promień."))
    return promien**2*3,14
  

def trapez():
    bokA=int(input("Aby policzyc pole trapezu potrzebne sa dwa boki (ten na górze i ten na dole), podaj miare boku >>na górze<<"))
    bokB=int(input("A teraz tego >>na dole<<"))
    wysokosc=int(input("Potrzebna jest jeszcze wysokosc"))
    return (bokA + bokB) * wysokosc/2

def rownoleglobok():
    bokA=int(input("Potrzebujemy miary podstawy"))
    wysokosc=int(input("I miare wysokosci"))
    return bokA * wysokosc

rozkaz=input("Witaj w kalkuatorze pol figur geometrycznych. Co byś chciał policzyć? Pole KWADRAT? PROSTOKAT? RAB? TROJKAT? KOLO? TRAPEZ? ROWNOLEGLOBOK?")
rozkaz=rozkaz.upper() #to sprawia, ze wszystko co wpisze uzytkownik (czyli rozkaz) automatycznie stanie sie scapslockowane
if rozkaz == "KWADRAT":
    print(kwadrat())
elif rozkaz == "PROSTOKAT":
    print(prostokat())
elif rozkaz == "RAB":
    print(rab())
elif rozkaz == "TROJKAT":
    print(trojkat())
elif rozkaz == "KOLO":
    print(kolo())
elif rozkaz == "Równoległobok":
    print(rownoleglobok())
else:
    rozkaz=input("Eeeeo, coś się zepsuło napisz jeszcze raz")