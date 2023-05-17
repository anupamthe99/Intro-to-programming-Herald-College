
import random
import os.path
import json
random.seed()

def draw_board(board):
    '''Prints the board in 3*3 matrix and the argument of board is passed from
     python_play_game.py '''
    #Creating the layout of the board.
    print("-------------")
    #[] on left is row,[] on right is column.
    print("|",board[0][0],"|",board[0][1],"|",board[0][2],"|")
    print("|---|---|---|")
    print("|",board[1][0],"|",board[1][1],"|",board[1][2],"|")
    print("|---|---|---|")
    print("|",board[2][0],"|",board[2][1],"|",board[2][2],"|")
    print("-------------")


def welcome(board):
    '''This function is used to greet the players.'''
    print("Welcome to Tic-Tac-Toe game<3!")
    

def initialise_board(board):
    '''This function helps to empty the space in the cell to initialize 
    the game of tic-tac-toe. 
    '''
    #i is the row in3*3 matrix.
    #Iterates through 1 row at a time until 3 rows are reached.
    for i in range(3):
        #j is the coloumn in 3*3 matrix
        #Iterates through 3 Columns in 1 row at a time until 9 ciolumns are reached.
        for j in range(3):
            #During the loop this sets value of boar[i][j]to an empty space to ensure the cell is unused.
            board[i][j]=' '
    #returns the initialized board after iterating
    return board
def get_player_move(board):
    '''This function takes one parameter board which represents the current state of the game.'''
    #Enters in while loop if valid move is made by the players.
    while True:
        try:
            #To mark on the cell number that the compute/player has choosed.
            move=int(input("Enter the cell number you want to mark on:"))
            #Check if the entered move is in range(1,10).
            if move in range(1,10):
                #With in the valid range.
                row=(move-1)//3 
                col=(move-1)%3
                if board[row][col]==' ':
                    return row,col
                #if the cell is pre-occupied/marked
                else:
                    print("The cell is pre-occupied.Please try another number.")
            else:
                print("Please enter a number between 1-9")
        #If any value despite the integer is typed.
        except ValueError:
            print("Please enter a numerical integer ranging from 1-9")

 
 
def choose_computer_move(board):
    '''This function helps to determine the move of the computer in the cell by using the numuber from 1-9
        Returns row,col if there is remaining_moves
        Returns None if there is no remaining moves
    '''
    remaining_moves=[]
    for i in range(3) :
        for j in range(3):
            if board[i][j]== ' ' :
                remaining_moves.append((i,j))
    if remaining_moves:
        row,col= random.choice(remaining_moves)
        return row,col
    else:
        return None        

def check_for_win(board, mark):
    '''This function provides the combination through which a computer or a plahyer wins. '''
    winners_combination=[
        [[0,0],[0,1],[0,2]], #first row left to right viceversa wins.
        [[1,0],[1,1],[1,2]], #second row left to right viceversa wins.
        [[2,0],[2,1],[2,2]], #third row left to right viceversa wins.
        [[0,0],[1,0],[2,0]], #first coloumn top to bottom viceversa wins.
        [[0,1],[1,1],[2,1]], #second coloumn left to right viceversa wins.
        [[0,2],[1,2],[2,2]], #third coloumn top to bottom viceversa wins.
        [[0,0],[1,1],[2,2]], #Diagonal from top left to bottom-right wins.
        [[0,2],[1,1],[2,0]],#Diagonal from top right to bottom left wins.
    ]
    for combination in winners_combination:
        cells = [board[row][col] for row,col in combination]
        if all(cell==mark for cell in cells):
           return True #Returns true is anyone wins.
    return False #Returns false is noone wins.
    

def check_for_draw(board):
    '''This function is used to check for draw in the tic-toe game.
    Returns True if there is a draw 
    Returns False if there is no draw.'''
    for row in board:
        for cell in row:
            if cell==' ':
                return False
    return True
        
def play_game(board):
#     # develop code to play the game
    initialise_board(board) 
    draw_board(board)
    while True:
        #for player
        player_row,player_coloumn=get_player_move(board)
        #Taking the playe_row or column and using the "X" mark for the player.
        board[player_row][player_coloumn]='X'
        #Calling the function draw board to fill the cell with the 'X'in thje desired place.
        draw_board(board)
        #Checking for the win from the combination provided earlier.
        if check_for_win(board,'X'):
            #Printing the congratulations message if the player has won.
            print("Congratulations you won!")
            #Returning 1 if the player wins.
            return 1
        #Checking the draw by calling the check_for_draw function and passing the parameter board.
        elif check_for_draw(board):
            print("It's a draw!")
            #Returns 0 if it is draw.
            return 0
        #computer turn
        computer_row,computer_column = choose_computer_move(board)
        #Checking whether the computer has choose the row or column
        if computer_row is not None and computer_column is not None:
            #Taking the computers row and column and marking the selected cell with''O'.
            board[computer_row][computer_column] ='O'
            #Calling the function draw board to fill the cell with the 'O' in desired place .
            draw_board(board)
            #Checking for the win from the combination provided earlier.
            if check_for_win(board,'O'):
                #Printing the congratulations message if the player has won.
               print("Sorry!The computer has won.")
               #Returns 
               # -1 if computer wins
               return -1
            #Checking the draw by calling the check_for_draw function and passing the parameter board.
            elif check_for_draw(board):
               print("It's a draw!")
               #Returns 0 if draw
               return 0
        
                    
                
def menu():
    '''This function is used to call the menu and
    Returns the choice'''
    #Print the instruction in menu bar
    print("Menu:")
    print("1:Play the game.")
    print("2.Save the score in the file leaderboard.txt")
    print("3.Load and display the score from the 'leaderboard.txt'.")
    print("q:End the program")
    choice=input("Enter Your choice.")
    return choice


def load_scores():
    '''This function is used to load the score in the filename
    Returns leaders'''
    leaders={}
    filename="leaderboard.txt"
    if os.path.isfile(filename):
        try:
            with open(filename,"r") as file:
                leaders = json.load(file)
        except (FileNotFoundError , json.JSONDecodeError):
            print("Sorry! Failed to load score .Try again!")
    else:
        print("Leaderboard not found" )
    return leaders
            
    
def save_score(score):
    '''This function is used to save the score in the leaderboard '''
    #Prompting the player's name
    player_name=input("Enter your name:")
    filename="leaderboard.txt"
    
    try:
        #Loads existing leaderbord score.
        leaders=load_scores()
        #Add the player's name and score to the leaderboard.
        if player_name in leaders:
            leaders[player_name] += score 
        else:
            leaders[player_name] = score     
        with open(filename,'w') as file:
            json.dump(leaders,file)
    #If file is not found.
    except IOError:
        print("Failed to load current scores.")
   
def display_leaderboard(leaders):
    '''This function is used to display the score in the leaderboard
    '''
    print("Leaderboard Score:\n---------------")
    for player_name,score in leaders.items():
            print(f"{player_name}:{score}")