# Peyton Goodlett
import random
import copy
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
        winSym = "None"
        for col in range(0, 3):
            if board[0][col] == board[1][col] == board[2][col] == symbol1:
                winner = True
                winSym = symbol1
            elif board[0][col] == board[1][col] == board[2][col] == symbol2:
                winner = True
                winSym = symbol2
        
        for row in range(0, 3):
            if board[row][0] == board[row][1] == board[row][2] == symbol1:
                winner = True
                winSym = symbol1
            elif board[row][0] == board[row][1] == board[row][2] == symbol2:
                winner = True
                winSym = symbol2
        
        if board[0][0] == board[1][1] == board[2][2] == symbol1:
            winner = True
            winSym = symbol1
        elif board[0][0] == board[1][1] == board[2][2] == symbol2:
            winner = True
            winSym = symbol2
        
        if board[0][2] == board[1][1] == board[2][0] == symbol1:
            winner = True
            winSym = symbol1
        elif board[0][2] == board[1][1] == board[2][0] == symbol2:
            winner = True
            winSym = symbol2
        
        return winner, winSym
        
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
        col = int(input("Pick a column: [left column: 0, middle column: 1, right column: 2]: ")) 
        while col < 0 or col > 2:
            print("Invalid input.")
            col = int(input("Pick a column: [left column: 0, middle column: 1, right column: 2]: "))
        while board[row][col] == symbol1 or board[row][col] == symbol2:
            print("Spot already filled.")
            print("Current Board:")
            print(TicTacToe.makeBoardPretty(board))
            row = int(input("Pick a row: [upper row: 0, middle row: 1, lower row: 2]: "))
            col = int(input("Pick a column: [left column: 0, middle column: 1, right column: 2]: "))
        if curPlr == symbol1:
            board[row][col] = symbol1
        else:
            board[row][col] = symbol2
    def minimax(the_board, symbol1, symbol2, turn):
        og_row = "None"
        og_col = "None"
        bard = copy.deepcopy(the_board)
        sadness = True
        while turn % 2 == 1:
            og_row = 'None'
            og_col = 'None'
            checks = 0
            while True:
                checks += 1
                if checks >= 15:
                    break
                fake_board = copy.deepcopy(bard)
                row = random.randint(0,2)
                col = random.randint(0,2)
                while fake_board[row][col] != "0":
                    row = random.randint(0,2)
                    col = random.randint(0,2)
                fake_board[row][col] = symbol1
                winStatus, winSym = TicTacToe.WinnerWinnerChickenDinner(fake_board,symbol1,symbol2)
                if winStatus == True and winSym == symbol1:
                    og_row = row
                    og_col = col
                    sadness = False
                    break
            if winStatus == True:
                break
            break
        while turn % 2 == 0:
            fake_board = copy.deepcopy(bard)
            row = random.randint(0,2)
            col = random.randint(0,2)
            sym1row = random.randint(0,2)
            sym1col = random.randint(0,2)
            while fake_board[row][col] != "0":
                row = random.randint(0,2)
                col = random.randint(0,2)
            fake_board[row][col] = symbol2
            while fake_board[sym1row][sym1col] != "0":
                sym1row = random.randint(0,2)
                sym1col = random.randint(0,2)
            fake_board[sym1row][sym1col] = symbol1
            winStatus, winSym = TicTacToe.WinnerWinnerChickenDinner(fake_board, symbol1, symbol2)
            check = any("0" in sublist for sublist in fake_board)
            if check == False:
                fake_board = copy.deepcopy(bard)
            while winStatus == False:
                row = random.randint(0,2)
                col = random.randint(0,2)
                sym1row = random.randint(0,2)
                sym1col = random.randint(0,2)
                while fake_board[row][col] != "0":
                    row = random.randint(0,2)
                    col = random.randint(0,2)
                fake_board[row][col] = symbol2
                while fake_board[sym1row][sym1col] != "0":
                    sym1row = random.randint(0,2)
                    sym1col = random.randint(0,2)
                fake_board[sym1row][sym1col] = symbol1
                winStatus, winSym = TicTacToe.WinnerWinnerChickenDinner(fake_board, symbol1, symbol2)
                check = any("0" in sublist for sublist in fake_board)
                if check == False:
                    fake_board = copy.deepcopy(bard)
            if winStatus == True and winSym == symbol2:
                og_row = row
                og_col = col
                break
        return og_row, og_col, sadness
            #finish later btw
    def minimax_test(board, symbol1, symbol2, turn):
        global prevent
        print("Current Board:")
        print(TicTacToe.makeBoardPretty(board))
        if turn % 2 == 1:
            print(symbol1.upper() + "'s turn!" )
            row = int(input("Pick a row: [upper row: 0, middle row: 1, lower row: 2]: "))
            while row < 0 or row > 2:
                print("Invalid input.")
                row = int(input("Pick a row: [upper row: 0, middle row: 1, lower row: 2]: "))
            col = int(input("Pick a column: [left column: 0, middle column: 1, right column: 2]: ")) 
            while col < 0 or col > 2:
                print("Invalid input.")
                col = int(input("Pick a column: [left column: 0, middle column: 1, right column: 2]: "))
            while board[row][col] != "0":
                print("Spot already filled.")
                print("Current Board:")
                print(TicTacToe.makeBoardPretty(board))
                row = int(input("Pick a row: [upper row: 0, middle row: 1, lower row: 2]: "))
                col = int(input("Pick a column: [left column: 0, middle column: 1, right column: 2]: "))
            board[row][col] = symbol1
            og_row, og_col, sadness = TicTacToe.minimax(board, symbol1, symbol2, turn)
            if sadness == False:
                prevent = False
                global row_col
                row_col = [og_row, og_col]
            elif sadness == True:
                prevent = True
                
        if turn % 2 == 0:
            if prevent == False:
                board[row_col[0]][row_col[1]] = symbol2
            elif prevent == True:
                og_row, og_col, sadness = TicTacToe.minimax(board, symbol1, symbol2, turn)
                board[og_row][og_col] = symbol2
                print("Bot chose " + str(og_row) + " " + str(og_col))
    def main(board, symbol1, symbol2):
        count = 1
        winner = False

        while count < 10 and winner == False:
            if count == 9:
                print("Game over!")
                if winner == False:
                    print("There was a tie!")
                    break
            TicTacToe.minimax_test(board, symbol1, symbol2, count)
            winner, winSym = TicTacToe.WinnerWinnerChickenDinner(board, symbol1, symbol2)
            count += 1
            if winner == True:
                print("Game over!")
                print(winSym.upper() + " won!")

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
                            if board[randomRow-i][randomCol] == ' ':
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
    def hit(board, bot_board, plr_board, hits):
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
            bot_board[row][col-1] = "K"
        elif board[row][col-1] == "X" or board[row][col-1] == "M":
            print("You already shot here!")
        else:
            print("It's a miss!")
            board[row][col-1] = "M"
            bot_board[row][col-1] = "M"
            plr_board[row][col-1] = "M"
        print("Your updated board:")
        print(simpleBattleship.makeBoardPretty(plr_board))
        print("Enemy Board:")
        print(simpleBattleship.makeBoardPretty(board))
        return (board, plr_board, hits)
    
    def stinkwee(board, bot_board, plr_board, hits):
        row = random.randint(0,9)
        col = random.randint(0,9)
        did_hit, sym, nr, nc = simpleBattleship.is_a_hit(plr_board, row, col, hits)
        while sym == "A" or sym == "K":
            row = random.randint(0,9)
            col = random.randint(0,9)
            did_hit, sym, nr, nc = simpleBattleship.is_a_hit(plr_board, row, col, hits)
        did_hit, sym, nr, nc = simpleBattleship.is_a_hit(plr_board, row, col, hits)
        if did_hit == True:
            hits += 1
            if nr >= 0:
                board[nr][nc] = "X"
                bot_board[nr][nc] = "X"
                plr_board[nr][nc] = "K"
            else:
                board[row][col] = "X"
                bot_board[row][col] = "X"
                plr_board[row][col] = "K"
        elif did_hit == False and sym == "M":
            board[row][col] = "M"
            bot_board[row][col] = "M"
            plr_board[row][col] = "M"
        return board, bot_board, plr_board, hits
    def is_a_hit(plr_board, row, col, hits):
        did_hit = False
        next_row = -1
        next_col = -1
        if plr_board[row][col] == "O":
            did_hit = True
            if row + 1 < 10:
                if plr_board[row+1][col] == "O":
                    next_row = row + 1
                    next_col = col
                elif col + 1 < 10:
                    if plr_board[row][col+1] == "O":
                        next_row = row
                        next_col = col + 1
                elif col + 1 > 10:
                    if plr_board[row][col-1] == "O":
                        next_row = row
                        next_col = col - 1
            else:
                if plr_board[row-1][col] == "O":
                    next_row = row - 1
                    next_col = col
            
            return did_hit, "X", next_row, next_col
        elif plr_board[row][col] == "M":
            did_hit = False
            return did_hit, "A", next_row, next_col
        elif plr_board[row][col] == " ":
            did_hit = False
            return did_hit, "M", next_row, next_col
        elif plr_board[row][col] == "K":
            did_hit = False
            return did_hit, "X", next_row, next_col
    def main():
        board = simpleBattleship.createShips(simpleBattleship.generateBoard())
        plr_board = simpleBattleship.generateBoard()
        print("Welcome to Simple Battleship!")
        print("We have setup 2 ships behind the scenes..")
        print("Each ship is 5 blocks long and can be placed vertically or horizontally.")
        print("You must destroy those ships!")
        print("Here is your own board, if you get a miss or hit, it will show here:")
        print(simpleBattleship.makeBoardPretty(plr_board))
        hits = 0
        bot_hits = 0
        while True:
            if hits == 10:
                print("Congrats! You hit all the enemy ships!")
                print("This was the enemy board: ")
                print(simpleBattleship.makeBoardPretty(bot_board))
            elif bot_hits == 10:
                print("You lost. The enemy hit all your ships.")
                print("This was the enemy board: ")
                print(simpleBattleship.makeBoardPretty(bot_board))
            
        

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
        while len(guesses) <= 15:
            bulls = 0
            cows = 0
            guess = int(input("Guess a 4 digit number: "))
            while len(str(guess)) < 4 or len(str(guess)) > 4:
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
class Hangman:
    def main():
        wordbank = "dog cat wolf quentin mason william theron peyton printer electric zebra lion rhino laptop computer ilead hangman video analyze school homework class classroom goose table chair abdominous train big boulder pasta document google fortnite roblox minecraft nike hoodie buxom bologna tsunami island ocean believe".split()
        hangman_stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', 
'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========''',
'''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========''']
        word = random.choice(wordbank)
        wordL = len(word)
        tries = 0
        guessed = []
        guessed_str = ""
        currentHangman = 0
        for x in range(wordL):
                guessed.append("_")
        print("Welcome to Hangman!")
        while True:
            if "_" not in guessed:
                print("Congrats! You guessed the word " + word + " in " + str(tries) + " tries.")
                break
            guessed_str = ""
            if tries == 7:
                print("You failed to guess the word " + word + ".")
                exit()
            for c in range(len(guessed)):
                guessed_str += guessed[c]
            print("It is a " + str(wordL) + " letter word.")
            print("Word status: " + guessed_str)
            print("Remaining tries: " + str(7 - tries))
            print("Current Hangman: " + hangman_stages[currentHangman])
            guess = str(input("Enter a single letter: "))
            while len(guess) > 1:
                print("Invalid input.")
                guess = str(input("Enter a single letter: "))
            if guess in word:
                print("Good job! " + guess + " was in the word!")
                for i in range(wordL):
                    if word[i] == guess:
                        guessed[i] = guess
            else:
                print("Wrong! " + guess + " was not in the word!")
                currentHangman += 1
                tries += 1
class Unscramble:
    def scramble():
        wordbank = "dog cat wolf quentin mason william theron peyton printer electric zebra lion rhino laptop computer ilead hangman video analyze school homework class classroom goose table chair abdominous train big boulder pasta document google fortnite roblox minecraft nike hoodie buxom bologna tsunami island ocean believe".split()
        randomW = random.choice(wordbank)
        scrambled = ""
        last_l = 0
        for i in range(len(randomW)):
            new_l = random.randint(0, len(randomW) - 1)
            while last_l == new_l:
                new_l = random.randint(0, len(randomW) - 1)
            last_l = new_l
            scrambled += randomW[new_l]
        return (randomW, scrambled)
    def main():
        word, scrambled = Unscramble.scramble()
        tries = 0
        print("Welcome to Unscramble!")
        print("We have scrambled a random word. You must unscramble it and input it!")
        while tries <= 5:
            tries += 1
            print("Scrambled word: " + scrambled)
            plr_try = str(input("Enter your unscrambled word: "))
            if plr_try != word:
                print("Incorrect! Please try again.")
            else:
                print("Congratuations! You guessed the word " + word + " in " + str(tries) + " try!")
                exit()
        print("You were unable to guess the word! It was " + word + "!")
        exit()
'''
board = [["x","x","0"],
         ["o","0","0"],
         ["0","0","0"]]
turn = 3
TicTacToe.minimax(board, "x", "o", turn)

while True:
    print("Python Project")
    print("Games:")
    print("1. TicTacToe")
    print("2. Simple Battleship")
    print("3. Bulls and Cows")
    print("4. Hangman")
    print("5. Unscramble")
    option = int(input("Enter a number to play a game: "))
    while option < 1 or option > 5:
        print("Invalid option.")
        option = int(input("Enter a number to play a game: "))
    if option == 1:
        board = TicTacToe.init_Board()
        symbol1, symbol2 = TicTacToe.plrSymbols()
        TicTacToe.main(board, symbol1, symbol2)
    elif option == 2:
        simpleBattleship.main()
    elif option == 3:
        BullsAndCows.main()
    elif option == 4:
        Hangman.main()
    elif option == 5:
        Unscramble.main()
'''
board = simpleBattleship.generateBoard()
bot_board = simpleBattleship.generateBoard()
plr_board = simpleBattleship.createShips(simpleBattleship.generateBoard())
hits = 1

while hits < 10:
    board, bot_board, plr_board, hits = simpleBattleship.stinkwee(board, bot_board, plr_board, hits)
    print("Board to show player")
    print(simpleBattleship.makeBoardPretty(board))
    print("Bot Board")
    print(simpleBattleship.makeBoardPretty(bot_board))
    print("Player board")
    print(simpleBattleship.makeBoardPretty(plr_board))
    
# hangman start functions
# Hangman.main()

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
