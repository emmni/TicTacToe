from random import randint
from time import sleep

twoPlayers = False
playerOne = "X"
playerTwo = "O"
computerPlayer = "O"
grid = [" "]*9
winningComb = [ [0, 1, 2], [0, 4, 8], [0, 3, 6], [1, 4, 7], [2, 4, 6], [2, 5, 8], [3, 4, 5], [6, 7, 8] ] # The winning combinations.

def playGame():
    """
    Function that runs the in-game loop
    """
    gameOver = False

    welcomeMessage()
    
    chooseMultiplayer()

    if not twoPlayers:
        playerOneChooseMark()

        while not gameOver:
            if playerOne == "X": # playerOne is the player that starts.
                printGrid()
                playerPlay(playerOne)

                if checkWin():
                    gameOver = True
                    continue

                computerPlay()

                if checkWin():
                    gameOver = True
                    continue

            else: # The computer starts the game

                computerPlay()

                if checkWin() or checkTie():
                    gameOver = True
                    continue

                playerPlay(playerOne)

                if checkWin() or checkTie():
                    gameOver = True
                    continue
    else:
        printGrid()

        while not gameOver:
            playerPlay(playerOne)

            if checkWin() or checkTie():
                gameOver = True
                continue

            playerPlay(playerTwo)

            if checkWin() or checkTie():
                gameOver = True
                continue
        
def checkWin():
    """
    Checks if either of the two players has won and
     prints a message with the winner if that is the case.
    This includes the computer in the singleplayer game.
    Return true if one player has won, false otherwise.
    """
    potentialWin = checkThreeInARow()
    if potentialWin == "X" or potentialWin == "O":
        winMessage(potentialWin)
        return True
    else:
        return False

def checkTie():
    """
    Check if there is a tie, that is, if the grid is filled
     with X's and O's.
    Return true if a tie, false otherwise.
    """
    for mark in grid:
        if mark == " ":
            return False
    print("Oh no, it's a tie! Better luck next time :D")
    return True

def winMessage(winner):
    """
    The message that is printed if a player has won.
    """
    print("Player " + winner + " won! Wooop :D")

def checkThreeInARow():
    """
    Checks to see if a player has three marks in a row.
    Return the winning player or None if no plyer has won.
    """
    for winComb in winningComb:
        player = grid[winComb[0]]
        if player not in ("X", "O"):
            continue
        if player == grid[winComb[1]] == grid[winComb[2]]:
            return player
    return None

def computerPlay():
    """
    Lets the "computer" play by finding a random empty position
     on the grid and placing its mark there.
    """
    played = False
    sleep(2) # To simulate thinking.
    while not played:
        placeNbr = randint(1,9)
        if placeMark(computerPlayer, placeNbr):
            played = True
    printGrid()

def playerPlay(player):
    """"
    Lets a human player make a move.
    Takes an input argument, if the argument is allowed
     the player's mark is placed on the wished position,
     otherwise a new input argument is taken.
    """
    played = False
    
    while not played:
        inputVar = input()
        if makeMove(player, inputVar):
            played = True
    printGrid()

def makeMove(player, inputVar):
    """
    Checks if a player's input string can be converted to
     an int and then places the player's mark on that
     position if it is available and in range.
    """
    position = checkIfNumber(inputVar)
    return placeMark(player, position)

def placeMark(player, place):
    """
    Places a player's mark on the specified location if
     it exists and is available.
    """
    if not legalMove(place):
       print("Number not in range!")
       return False
           
    gridIndex = place - 1
    if grid[gridIndex] != " ":
        if player != computerPlayer:
            print("\033[2A")
            print("Position is already occupied! Don't cheat :P")
            print("\033[2A")
            sleep(4)
            print("\033[K")
            print("\033[2A")
        return False
    else:
        grid[gridIndex] = player
        return True

def playerOneChooseMark():
    """
    If singleplayer game playerOne gets to choose which
     mark to play as: X or O.
    """
    chosen = False
    while not chosen:
        mark = input("Choose mark X or O\n> ").lower()
        print()
        if mark == "x":
            chosen = True
        if mark == "o":
            global playerOne
            playerOne = "O"

            global computerPlayer
            computerPlayer = "X"
            chosen = True
        else:
            print("You can only choose between X and O")

def chooseMultiplayer():
    """
    Allows the player to choose if the game should be
     multi- or singleplayer.
    """
    print("Should the game be multiplayer?")

    chosen = False

    while not chosen:
        answer = input("Yes/No\n> ").lower()
        print()
        if answer == "yes":
            global twoPlayers
            twoPlayers = True
            chosen = True

        elif answer == "no":
            chosen = True

        else:
            print("Please give a proper response :)")

def checkIfNumber(string):
    """
    Converts a string to an int if possible.
    """
    try:
        return int(string)
    except ValueError:
        print("Enter an integer in the range of 1-9 (inclusive), please")

def legalMove(place):
    """
    Checks if a number is in the range of allowed values.
    """
    return place > 0 and place < 10

def welcomeMessage():
    """
    Prints a welcome message.
    """
    print("Hello and welcome to tic tac toe \nIn this game you can either play as multi- or singleplayer.")
    print("To place your mark enter the number correponding to the position you want. \nSee the grid below.")
    print("-------")
    print("|1|2|3|")
    print("-------")
    print("|4|5|6|")
    print("-------")
    print("|7|8|9|")
    print("-------")
    print('\nX begins and O goes next.')
    print('Good luck!!!')

def printGrid():
    """
    Prints the game grid.
    """
    print("-------")
    print("|" + grid[0] + "|" + grid[1] + "|" + grid[2] + "|")
    print("-------")
    print("|" + grid[3] + "|" + grid[4] + "|" + grid[5] + "|")
    print("-------")
    print("|" + grid[6] + "|" + grid[7] + "|" + grid[8] + "|")
    print("-------")
    print("\033[9A") # Moves the cursor up 9 lines

playGame() # Initializes the game.