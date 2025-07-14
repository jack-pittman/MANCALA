import board_logic  

def start():
    israndom = False; # determine if we're playing with a random setup or not
    print("Random board?", "Yes" if israndom else "No")

    active_board = board_logic.get_setup(israndom) # store starting gameboard as an int[]
    board_logic.print_board(active_board)

    gameloop(active_board)

def gameloop(board):
    active_board = board

    while not isgameover(active_board):
        active_board = makemove(active_board, 1)
        if isgameover(active_board):
            break

        active_board = makemove(active_board, 2)

    # Game is over here
    announce_winner(active_board)

def makemove(active_board, player):
    isturnover = False
    
    while isturnover == False:
        if isgameover(active_board):
            isturnover = True
        if not isgameover(active_board):

            old_board = active_board.copy() # snapshot of the board before we make our move (will help us determine free turns)

            well_index = 7*player-1 # get index of "home" well - i.e. the index of the active player's well
            well_value = active_board[well_index] # get number of stones in home well = i.e. active player's score

            selectedwell = input(f"Player {player} - Please enter your selection: ")

            updated_board = updateboard(active_board, player, selectedwell)

            board_logic.print_board(updated_board)

            # basically makes sure the turn stops at the active player's well
            # If well changed but next pit didn't (free turn scenario)
            if updated_board[well_index] != old_board[well_index] and updated_board[(well_index + 1) % 14] == old_board[(well_index + 1) % 14]:
                isturnover = False

            # If no change in well OR both well and next pit changed (turn is over)
            if updated_board[well_index] == old_board[well_index] or (
                updated_board[well_index] != old_board[well_index] and updated_board[(well_index + 1) % 14] != old_board[(well_index + 1) % 14]):
                isturnover = True

    return updated_board

def updateboard(active_board, player, selectedwell):

    updated_board = active_board

    index = getindex(player, selectedwell) # find location of selected well in board list
    value = updated_board[index] # gets the number of stones in current well

    print(f"value: {value}")
    
    updated_board = sow(index, value, updated_board, player)

    return active_board


def getindex(player, selectedwell):
    index = lettertoindex(selectedwell)

    if player == 1:
        return index
    if player == 2:
        return 12-index


def lettertoindex(selectedwell):
    letters = ['a', 'b', 'c', 'd', 'e', 'f']
    return letters.index(selectedwell)

def isgameover(board):
    leftside = sum(board[:6])
    rightside = sum(board[-7:-1])  # sum(board[7:13])

    return leftside == 0 or rightside == 0

def announce_winner(board):
    if isgameover(board):
        print("GAME OVER")

        p1_score = board[6]
        p2_score = board[13]

        if p1_score > p2_score:
            print("PLAYER ONE WINS!")
        elif p1_score < p2_score:
            print("PLAYER TWO WINS!")
        else:
            print("IT'S A TIE!")

def sow(index, value, updated_board, player):
    active_board = updated_board
    active_board[index] = 0  # remove all stones from selected pit

    if player == 1:
        indexToAvoid = 13
    else:  # player == 2
        indexToAvoid = 6

    i = 1  # offset from original index
    stones_sown = 0

    while stones_sown < value:
        active_index = (index + i) % len(active_board)

        if active_index != indexToAvoid:
            active_board[active_index] += 1
            stones_sown += 1

        i += 1

    return active_board