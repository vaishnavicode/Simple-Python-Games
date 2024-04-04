import random

class Games:
    login = False

    def login_true(self):
        return self.login

    def login_or_register(self):
                
        while(True):
            
            info = ["Momin Danish","danish","danishmomin.003@gmail.com","dani2003"]
            
            print("\nThe Login or Register Menu")
            print("1. Login")
            print("2. Register")
            print("3. Exit Back To Main Menu")
            choice = int(input("Enter choice : "))

            if(choice == 1):
                usernameOrEmail = input("Enter User Name or Email : ")
                password = input("Enter password : ")
                if(usernameOrEmail.lower() == info[1] or usernameOrEmail.lower() == info[2]):
                    if(password == info[3]):
                        print("\nLogin Successful!")
                        self.login = True
                    else:
                        print("\nPassword is incorrect, please attempt again.")
                else:
                    print("\nLogin id is invalid.")
                        
            elif(choice == 2):
                name = input("Enter Your Name : ")
                username = input("Enter User Name : ")
                email = input("Enter Email Id : ")
                password = input("Enter password : ")

                info = [name,username,email,password]
                
            elif(choice == 3):
                break
            else:
                print("\nInvalid choice! Please choose again.")
        
        return self.login
        
        
    #  Tic Tac Toe Game
    def print_board(self,board):
        for row in board:
            print(" ".join(row))

    def place_piece(self,board, pos, user):
        symbol = 'X' if user == "Player" else 'O'

        if pos == "1":
            if board[0][0] == ' ':
                board[0][0] = symbol
                return True
        elif pos == "2":
            if board[0][2] == ' ':
                board[0][2] = symbol
                return True
        elif pos == "3":
            if board[0][4] == ' ':
                board[0][4] = symbol
                return True
        elif pos == "4":
            if board[2][0] == ' ':
                board[2][0] = symbol
                return True
        elif pos == "5":
            if board[2][2] == ' ':
                board[2][2] = symbol
                return True
        elif pos == "6":
            if board[2][4] == ' ':
                board[2][4] = symbol
                return True
        elif pos == "7":
            if board[4][0] == ' ':
                board[4][0] = symbol
                return True
        elif pos == "8":
            if board[4][2] == ' ':
                board[4][2] = symbol
                return True
        elif pos == "9":
            if board[4][4] == ' ':
                board[4][4] = symbol
                return True

        return False

    def check_winner(self,player_choices, computer_choices, count_player, count_computer):
        winning_combinations = [
            {"1", "2", "3"},
            {"4", "5", "6"},
            {"7", "8", "9"},
            {"1", "4", "7"},
            {"2", "5", "8"},
            {"3", "6", "9"},
            {"1", "5", "9"},
            {"3", "5", "7"}
        ]

        for combo in winning_combinations:
            if all(num in player_choices for num in combo):
                return "Player Won :]"
            elif all(num in computer_choices for num in combo):
                return "Player Lost :["
        
        if count_player + count_computer == 9:
            return "Draw :]"
        
        return ""

    def play_tic_tac_toe(self):
        win = ""
        inserted = False
        game_over = False
        count_player = 0
        count_computer = 0
        player_choices = ""
        computer_choices = ""

        board = [[' ', '|', ' ', '|', ' '],
                ['-', '+', '-', '+', '-'],
                [' ', '|', ' ', '|', ' '],
                ['-', '+', '-', '+', '-'],
                [' ', '|', ' ', '|', ' ']]

        self.print_board(board)

        while not game_over:
            if count_player + count_computer == 9:
                print("Draw :]")
                game_over = True
                break

            pos = input("Enter your placement (1-9): ")
            inserted = self.place_piece(board, pos, "Player")
            while not inserted:
                print("The spot is already taken, please enter again.")
                pos = input("Enter your placement (1-9): ")
                inserted = self.place_piece(board, pos, "Player")

            if inserted:
                player_choices += pos
                count_player += 1

                winner = self.check_winner(player_choices, computer_choices, count_player, count_computer)
                if winner:
                    win = winner
                    print(win)
                    game_over = True
                    break

            cpu_pos = str(random.randint(1, 9))
            inserted = self.place_piece(board, cpu_pos, "CPU")
            while not inserted:
                cpu_pos = str(random.randint(1, 9))
                inserted = self.place_piece(board, cpu_pos, "CPU")

            if inserted:
                computer_choices += cpu_pos
                count_computer += 1

                winner = self.check_winner(player_choices, computer_choices, count_player, count_computer)
                if winner:
                    win = winner
                    print(win)
                    game_over = True
                    break

            self.print_board(board)

        if game_over:
            count_computer = 0
            count_player = 0


    # Snakes and Ladders Game
    def play_snakes_and_ladders(self):
        ladders = [1, 4, 8, 21, 28, 50, 71, 80]
        snakes = [17, 54, 62, 64, 87, 93, 95, 98]
        ladders_end = [38, 14, 31, 42, 84, 67, 91, 100]
        snakes_end = [7, 34, 19, 60, 24, 73, 75, 79]

        game_over = False
        size = 100
        player_positions = [0, 0]  # Assuming 2 players

        print("\n\nWelcome to Snake and Ladder Game!")

        while not game_over:
            for i in range(2):
                if i >= 0 and player_positions[i] >= size:
                    print(f"\n\nPlayer {i + 1} has won!\n")
                    game_over = True
                    break
                
                print(f"\nPlayer {i + 1} playing!")
                print(f"Press {i + 1} to roll the dice player {i + 1}!")
                choice = int(input())

                if choice == i + 1:
                    player_positions[i] = self.snakes_and_ladders_move(player_positions[i], ladders, snakes, ladders_end, snakes_end)
                    print(f"Player {i + 1} current position: {player_positions[i]}")
                else:
                    print("Invalid input. Please try again.")
                    i -= 1

            if game_over:
                print("\n\nGame Over!")

    def snakes_and_ladders_move(self,position, ladders, snakes, ladders_end, snakes_end):
        dice = random.randint(1, 6)
        print("Dice:", dice)
        position += dice

        for i in range(len(ladders)):
            if position == ladders[i]:
                print("The player has climbed a ladder!")
                position = ladders_end[i]
            elif position == snakes[i]:
                print("The player has been bitten by a snake!")
                position = snakes_end[i]

        return position

    # Hangman Game
    def play_hangman(self):
        words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon", "mango", "nectarine", "orange", "papaya", "quince", "raspberry", "strawberry", "tangerine", "watermelon"]
        word = random.choice(words)
        guessed = []
        attempts = 6

        print("\n\nWelcome to Hangman!")
        print("The word has", len(word), "letters.")

        while attempts > 0:
            print("\n\nAttempts left:", attempts)
            display_word = ""
            for letter in word:
                if letter in guessed:
                    display_word += letter
                else:
                    display_word += "_"
            print(display_word)

            if display_word == word:
                print("Congratulations! You have guessed the word!")
                break

            guess = input("Enter a letter: ")
            if guess in guessed:
                print("You have already guessed this letter.")
                continue
            guessed.append(guess)

            if guess not in word:
                attempts -= 1
                print("The letter is not in the word.")
            else:
                print("The letter is in the word.")

        if attempts == 0:
            print("You have run out of attempts. The word was:", word)   

    def open_games(self,login):
        if(not login):
            print("You need to login to play games.")
            return
        while(True): 
            print("\nThe Game Menu")
            print("1. TicTacToe")
            print("2. Snakes and Ladders")
            print("3. Hangman")
            print("4. Exit to Main Menu")
            choice = int(input("Enter choice : "))
            if(choice == 1):
                self.play_tic_tac_toe()
            elif(choice == 2):
                self.play_snakes_and_ladders()
            elif(choice == 3):
                self.play_hangman()
            elif(choice == 4):
                break
            else:
                print("Invalid choice! Please choose again.")

    def menu(self):
        while(True):
            print("\nThe Main Menu")
            print("1. Open Games")
            print("2. Login")
            print("3. Exit")
            choice = int(input("Enter choice : "))
            if(choice == 1):
                self.open_games(self.login_true())
            elif(choice == 2):
                self.login = self.login_or_register()
            elif(choice == 3):
                break
            else:
                print("\nInvalid choice! Please choose again.")
  

