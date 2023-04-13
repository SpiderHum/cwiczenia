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
    return len([x for x in board if x == '#']) == 1 #len to funkcja sprawdzająca z ilu znaków składa się dany string

def win_check(board, mark):
    if board[1] == board[2] == board[3] == mark:
        return True
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
    return False

def player_choice(board):
    choice = input("Please select an empty space between 1 and 9 : ")
    while not space_check(board, int(choice)):
        choice = input("This space isn't free. Please choose between 1 and 9 : ")
    return choice

def replay():
    playAgain = input("Do you want to play again (y/n) ? ")
    if playAgain.lower() == 'y':
        return True
    if playAgain.lower() == 'n':
        return False

if __name__ == "__main__":
    print('Welcome to Tic Tac Toe!')
    i = 1
    # Choose your side
    players=player_input()
    # Empty board init
    board = ['#'] * 10
    while True:
        # Set the game up here
        game_on=full_board_check(board)
        while not game_on:
            # Player to choose where to put the mark
            position = player_choice(board)
            # Who's playin ?
            if i % 2 == 0:
                marker = players[1]
            else:
                marker = players[0]
            # Play !
            place_marker(board, marker, int(position))
            # Check the board
            display_board(board)
            i += 1
            if win_check(board, marker):
                print("You won !")
                break
            game_on=full_board_check(board)
        if not replay():
            break
        else:
            i = 1
            # Choose your side
            players=player_input()
            # Empty board init
            board = ['#'] * 10