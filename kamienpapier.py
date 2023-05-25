#dritte Projekt. Ein Stein, Ein Papier, Eine Schere. 
import random
#i=random.randint(0,2) output: 0, 1 lub 2, jkaby wyznacza punkt początkowy (0) i ile będzie liczyć (3)
sys=("kamien", "papier", "nozyczki")
odp=random.choice(sys) #random.choice(lista) losuje z listy. Wow. Ale szybko
use=input("Hehe, zagrajmy w kamien papier nozyczki. Ty zaczynaj.")
print(odp)
#kamień bije nozyczki
#nozyczki bija papier
#papier bije kamien

if use==odp:
    print("remis")
elif use == "kamien" and odp == "nozyczki":
    print("wygrales")
elif use == "nozyczki" and odp == "papier":
    print("wygrales")
elif use == "papier" and odp == "kamien":
    print("wygrales")
elif odp == "kamien" and use == "nozyczki":
    print("przegrales")
elif odp == "nozyczki" and use == "papier":
    print("przegrales")
elif odp == "papier" and use == "kamien":
    print("przegrales")
else:
    print("Nie chciales sie bawic, bring dich um")


