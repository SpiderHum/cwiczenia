
import turtle
import random
#niech na koniec rysuje amogusa, jezeli wygrasz niech rysuje tego normalnego, a jak przegrasz to tego przeciętego

window=turtle.screen() #to jest to po czym "zółw" się porusza, czytaj mazak się porusza po screen
BOK=600
X=-300 #koordynaty górnego lewego rogu, jezeli BOK ma 600
Y=300

window.setup(BOK, BOK) #pozwala ustawić jak szerokie i długie ma być okno, to konkretne będzie miało szerokość równą BOK i wysokość równą BOK
window.title("Kółko i Krzyzyk") #string, który pokaze się na pasku tytułowym naszego okna
window.bgcolor("black") #bgcolor = background color. Ta funkcja ustawia tło i jego wygląd

xo = turtle.Turtle() #xo = funkcja z biblioteki turtle - turtle (czytaj tworzy obiekt turtle, czytaj tworzy mazak)
xo.color("white") #ustaw kolor tego potworka na biały
xo.pensize(7) #grubość pędzla
xo.speed(0) #prędkość amogusa
xo.hideturtle() #welp, ukrywa zółwia

tablica=[[None,None,None],[None,None,None],[None,None,None]] #tablica, czytaj plansza, jest zdefiniowana jako lista składająca się z trzech list.
#None to nic, ani X ani Y. Później gracz zmieni te parametry.
#tablica[wiersz][kolumna]

kolejka=random.choice("x","y")

def click(x,y): #x, y - miejsca gdzie klika urzytkownik
    pass

window.onclick(click) #wywołuje daną funkcję gdy klikniętą zostane dane koordynaty

window.listen()
window.mainloop() #zapętlenie programu