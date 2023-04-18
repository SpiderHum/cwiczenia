#literalnie wezme kod i go zmienie
def display_board(board): #tworzy zmienną z tablicą. BlankBoard to to co widać poniej. Board to zbiór 10 #. 
    blankBoard="""
___________________
|     |     |     |
|  7  |  8  |  9  |
|     |     |     |
|-----------------|
|     |     |     |
|  4  |  5  |  6  |
|     |     |     |
|-----------------|
|     |     |     |
|  1  |  2  |  3  |
|     |     |     |
|-----------------|
"""

    for i in range(1,10):
        if (board[i] == 'O' or board[i] == 'X'): #jezeli jedna z tych liczb (1,10) to X lub O to zamienia starego inty, numery widoczne na tablicy na X lub O
            blankBoard = blankBoard.replace(str(i), board[i])
        else:
            blankBoard = blankBoard.replace(str(i), ' ') #w przeciwnym wypadku, tutaj int != O lub X, zamienia licbzę na pustą przestrzeń
    print(blankBoard) #pokazuje obecną wersje tablicy

def player_input():
    player1 = input("Please pick a marker 'X' or 'O' ") #pyta kim chcesz grać
    while True: #dopóki prawdą jest
        if player1.upper() == 'X': #gracz pierwszy podał X
            player2='O' #gracz drugi będzie O
            print("You've choosen " + player1 + ". Player 2 will be " + player2) #informuje o tym graczy
            return player1.upper(),player2 #Zwraca ich wartości. Player1.upper() bo mógł podać X i x, player dwa jest ustalny odgórnie. O.
        elif player1.upper() == 'O': #sytuacja co wyzej, ale na odwrót
            player2='X'
            print("You've choosen " + player1 + ". Player 2 will be " + player2) 
            return player1.upper(),player2
        else:
            player1 = input("Please pick a marker 'X' or 'O' ") #w przeciwnym wypadku ponownie prosi o podanie X i O, i tak będzie do póki prawdziwe nie będzie jedno z powyszych twierdzeń. Czyli dopóki player1 = X lub O a player2 = O lub X

def place_marker(board, marker, position): #ustaw znak
    board[position] = marker #W tablicy board (0,1,2,3,4,5,6,7,8,9), zaleznie od pozycji (zajmimey się nią później), ten znak, ten int to nasz znak
    return board #zwraca tablicę board

def space_check(board, position): #sprawdza czy miejsce jest puste
    return board[position] == '#' #jezeli w tablicy board, zaleznie od pozycji jest puste, czytaj jest # to zwraca True, prawdę.

def full_board_check(board):
    return len([x for x in board if x == '#']) == 1 #len to funkcja sprawdzająca z ilu obiketów składa się to co jest w środku. Ten konkretny kod to wzór zbioru. Zbiór liczb, które w zbiorze board są równe "#" czytaj to puste pola

def win_check(board, mark): #funkcja sprawdzająca czy gracz wygrał grę
    if board[1] == board[2] == board[3] == mark:
        return True #jezeli miejsce pierwsze. drugie, trzecie w zbiorze są równe znakowi (który moe być X lub O zalenie od gracza) to mamy wina. Czytaj true. Tak samo jest w kadej innej linijce
    if board[4] == board[5] == board[6] == mark:
        return True
    if board[7] == board[8] == board[9] == mark:
        return True
    if board[1] == board[4] == board[7] == mark:
        return True
    if board[2] == board[5] == board[8] == mark:
        return True
    if board[3] == board[6] == board[9] == mark:
        return True
    if board[1] == board[5] == board[9] == mark:
        return True
    if board[3] == board[5] == board[7] == mark:
        return True
    return False #w przeciwnym wypadku false, czyli nie ma wina, jeszcze gra się nie zakończyła

def player_choice(board): #wybierają gdzie postawić znak
    choice = input("Please select an empty space between 1 and 9 : ") #o to właśnie prosi
    while not space_check(board, int(choice)): #kiedy space_check nie jest prawdą:
        choice = input("This space isn't free. Please choose between 1 and 9 : ") #pyta jeszcze raz o miejsce
    return choice #zwraca ostateczny wynik. Choice jest zdefiniowany w funkcji, nie jest umieszczony jako argument

def replay(): #replay
    playAgain = input("Do you want to play again (y/n) ? ") #pyta czy chcą zagrać ponownie
    if playAgain.lower() == 'y': #tak, zwraca prawdę
        return True
    if playAgain.lower() == 'n': #nie, zwraca flase
        return False

if __name__ == "__main__": #nie wiem
    print('Welcome to Tic Tac Toe!') #powitanie
    i = 1 #i będzie ustalało tury
    # Choose your side
    players=player_input()
    # Empty board init
    board = ['#'] * 10
    while True: #dopuki prawdą jest:
        # Set the game up here
        game_on=full_board_check(board) #ze stół jest cały pełny
        while not game_on: #dopuki to NIE prawda
            # Player to choose where to put the mark
            position = player_choice(board)
            # Who's playin ?
            if i % 2 == 0: 
                marker = players[1] #gracz pierwszy ma kontrole nad znakiem, jezeli i jest parzyste
            else:
                marker = players[0] #gracz drugi ma kontrolę nad znakiem jeeli i jest nieparzyste
            # Play !
            place_marker(board, marker, int(position)) 
            # Check the board
            display_board(board) #na końcu zamienia # na liczby, a liczby na X i O
            i += 1 #i rośnie, zmienia się więc tura
            if win_check(board, marker): #jezeli ktoś wygrał
                print("You won !") #wypisz "wygrałeś"
                break #zakończ kod
            game_on=full_board_check(board) #w przeciwnym wypadku sprawdza czy stół jest pełny
        if not replay(): #jezeli stół jest pełny, a oni nie chcą grać dalej:
            break #zakończ
        else: #w kadym innym wypadku, czytaj chcą grać dalej, zresetuj stół i i. SPytaj ponownie o X i O i graj od nowa
            i = 1
            # Choose your side
            players=player_input()
            # Empty board init
            board = ['#'] * 10