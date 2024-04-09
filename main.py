# Peyton Goodlett last updated 4/8/24
import random
# using classes to organize games better
class TicTacToe:
    def init_Board():
        board = [["0","0","0"],
                 ["0","0","0"],
                 ["0","0","0"]]
        return board
    def makeBoardPretty(board):
        rows = len(board)
        for i in range(rows):
            print(board[i][0] + "|" + board[i][1] + "|" + board[i][2])
    def plrSymbols():
        symbol1 = str(input("Please choose a symbol for player 1 (X, O): "))
        while symbol1.lower() not in "xo":
            print("Invalid choice.")
            symbol1 = str(input("Please choose a symbol for player 1 (X, O): "))
        if symbol1.lower() == "x":
            symbol2 = "o"
        else:
            symbol2 = "x"
        return (symbol1, symbol2)
    def WinnerWinnerChickenDinner(board, symbol1, symbol2):
        winner = False
        for col in range(0, 3):
            if board[0][col] == board[1][col] == board[2][col] == symbol1:
                winner = True
                print(symbol1.upper() + " won!")
            elif board[0][col] == board[1][col] == board[2][col] == symbol2:
                winner = True
                print(symbol2.upper() + " won!")
        
        for row in range(0, 3):
            if board[row][0] == board[row][1] == board[row][2] == symbol1:
                winner = True
                print(symbol1.upper() + " won!")
            elif board[row][0] == board[row][1] == board[row][2] == symbol2:
                winner = True
                print(symbol2.upper() + " won!")
        
        if board[0][0] == board[1][1] == board[2][2] == symbol1:
            winner = True
            print(symbol1.upper() + " won!")
        elif board[0][0] == board[1][1] == board[2][2] == symbol2:
            winner = True
            print(symbol2.upper() + " won!")
        
        if board[0][2] == board[1][1] == board[2][0] == symbol1:
            winner = True
            print(symbol1.upper() + " won!")
        elif board[0][2] == board[1][1] == board[2][0] == symbol2:
            winner = True
            print(symbol2.upper() + " won!")
        
        return winner
        
    def gaming(board, symbol1, symbol2, turn):
        print("Current Board:")
        print(TicTacToe.makeBoardPretty(board))
        if turn % 2 == 1:
            curPlr = symbol1
        elif turn % 2 == 0:
            curPlr = symbol2
        print(curPlr.upper() + "'s turn!")
        row = int(input("Pick a row: [upper row: 0, middle row: 1, lower row: 2]: "))
        while row < 0 or row > 2:
            print("Invalid input.")
            row = int(input("Pick a row: [upper row: 0, middle row: 1, lower row: 2]: "))
        col = int(input("Pick a row: [left column: 0, middle column: 1, right column: 2]: ")) 
        while col < 0 or col > 2:
            print("Invalid input.")
            col = int(input("Pick a row: [left column: 0, middle column: 1, right column: 2]: "))
        while board[row][col] == symbol1 or board[row][col] == symbol2:
            print("Spot already filled.")
            print("Current Board:")
            print(TicTacToe.makeBoardPretty(board))
            row = int(input("Pick a row: [upper row: 0, middle row: 1, lower row: 2]: "))
            col = int(input("Pick a row: [left column: 0, middle column: 1, right column: 2]: "))
        if curPlr == symbol1:
            board[row][col] = symbol1
        else:
            board[row][col] = symbol2
        print(TicTacToe.makeBoardPretty(board))
    def main(board, symbol1, symbol2):
        count = 1
        winner = False

        while count < 10 and winner == False:
            if count == 9:
                print("Game over!")
                if winner == False:
                    print("There was a tie!")
            TicTacToe.gaming(board, symbol1, symbol2, count)
            winner = TicTacToe.WinnerWinnerChickenDinner(board, symbol1, symbol2)
            count += 1
            if winner == True:
                print("Game over!")

class simpleBattleship:
    def generateBoard():
        # this will create a 10x10 2d list. we will use random to choose a location and rotation for the ship and check if any of the spots are taken
        board = [[" "," "," "," "," "," "," "," "," "," "],
                 [" "," "," "," "," "," "," "," "," "," "],
                 [" "," "," "," "," "," "," "," "," "," "],
                 [" "," "," "," "," "," "," "," "," "," "],
                 [" "," "," "," "," "," "," "," "," "," "],
                 [" "," "," "," "," "," "," "," "," "," "],
                 [" "," "," "," "," "," "," "," "," "," "],
                 [" "," "," "," "," "," "," "," "," "," "],
                 [" "," "," "," "," "," "," "," "," "," "],
                 [" "," "," "," "," "," "," "," "," "," "]]
        return board
    def makeBoardPretty(board):
        letters = "ABCDEFGHIJ"
        nums = ['1','2','3','4','5','6','7','8','9', '10']
        rows = len(board)
        print("  ", end=" ")
        print(nums)
        for i in range(rows):
            print(letters[i] + " ", end=' ')
            print(board[i])
    def createShips(board):
        for z in range(2):
            randomDir = random.choice(["horizontal", "vertical"])
            randomRow = random.randint(1, 9)
            randomCol = random.randint(1, 9)
            for x in range(5):
                for i in range(5):
                    if randomDir == "horizontal":
                        if randomRow+i >= 9:
                            if board[randomRow-i][randomCol] == " ":
                                board[randomRow-i][randomCol] = "O"
                                break
                        else:
                            if board[randomRow+i][randomCol] == " ":
                                board[randomRow+i][randomCol] = "O"
                                break
                    else:
                        if randomCol+i >= 9:
                            if board[randomRow][randomCol-i] == " ":
                                board[randomRow][randomCol-i] = "O"
                                break
                        else:
                            if board[randomRow][randomCol+i] == " ":
                                board[randomRow][randomCol+i] = "O"
                                break
        return board
    def hit(board,plr_board, hits):
        letters = ["a","b","c","d","e","f","g","h","i","j"]
        columns = ["1","2","3","4","5","6","7","8","9","10"]
        row = str(input("Input a row (A-J): "))
        row = row.lower()
        while row not in letters:
            print("Please enter a valid row.")
            row = str(input("Input a row (A-J): "))
        row = letters.index(row)
        col = int(input("Input a column (1-10): "))
        if str(col) not in columns:
            print("Please enter a valid column.")
            col = int(input("Input a column (1-10): "))
        if board[row][col-1] == "O":
            print("It's a hit!")
            hits += 1
            board[row][col-1] = "X"
            plr_board[row][col-1] = "X"
        elif board[row][col-1] == "X" or board[row][col-1] == "M":
            print("You already shot here!")
        else:
            print("It's a miss!")
            board[row][col-1] = "M"
            plr_board[row][col-1] = "M"
        print("Your updated board:")
        print(simpleBattleship.makeBoardPretty(plr_board))
        return (board, plr_board, hits)
    def main():
        board = simpleBattleship.createShips(simpleBattleship.generateBoard())
        plr_board = simpleBattleship.generateBoard()
        print("Welcome to Simple Battleship!")
        print("We have setup 2 ships behind the scenes..")
        print("You must destroy those ships!")
        print("Here is your own board, if you get a miss or hit, it will show here:")
        print(simpleBattleship.makeBoardPretty(plr_board))
        hits = 0
        while hits < 10:
            board, plr_board, hits = simpleBattleship.hit(board, plr_board, hits)
        if hits == 10:
            print("Congrats! You hit all the enemy ships!")
            print("This was the enemy board: ")
            print(simpleBattleship.makeBoardPretty(board))

# bulls and cows is an old paper game. both players write a secret 4 digit number. they have to try to guess the other player's number, whoever does it first wins.
# after a guess, the game gives you a certain number of bulls and cows. bulls meaning a number is correct and is in the correct spot
# while cows mean its the correct number but incorrect spot
class BullsAndCows:
    def main():
        guesses = []
        bot_num = random.randint(1000, 9999)
        print('Welcome to Bulls and Cows!')
        print('We have generated a random 4 digit number. You must guess the number.')
        print('If a digit in the number you guess is correct and in the correct spot, you will get 1 bull (B).')
        print('If a digit is correct but not in the correct spot, you will get a cow (C).')
        print('You get 15 guesses total!')
        print(bot_num)
        while len(guesses) <= 15:
            bulls = 0
            cows = 0
            guess = int(input("Guess a 4 digit number: "))
            while len(str(guess)) > 4:
                print("Not a 4 digit number.")
                guess = int(input("Guess a 4 digit number: "))
            guesses.append(guess)
            if guess == bot_num:
                print("Congrats! You guessed the bot's number: " + str(bot_num) + " in " + str(len(guesses) - 1) + " guesses!")
                exit()
            # its a little cursed since you cant use len() or [i] with integers but it works
            for i in range(len(str(bot_num))):
                if str(guess)[i] == str(bot_num)[i]:
                    bulls += 1
                elif str(guess)[i] != str(bot_num)[i] and str(guess)[i] in str(bot_num):
                    cows += 1
            print(str(bulls) + " Bulls " + str(cows) + " Cows")
            print("All Guesses:")
            for i in range(len(guesses)):
                print(str(i + 1) + " " + str(guesses[i]))
        print("No more guesses! Game over :(")

# bulls and cows start function
# BullsAndCows.main()

# tictactoe start functions
# board = TicTacToe.init_Board()
# symbol1, symbol2 = TicTacToe.plrSymbols()
# TicTacToe.main(board, symbol1, symbol2)

# battleship start function
# simpleBattleship.main()

# for checking if the ship generation works properly
# print(simpleBattleship.makeBoardPretty(simpleBattleship.createShips(simpleBattleship.generateBoard())))
