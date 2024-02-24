'''
['1','2','3'],
['4','5','6'],
['7','8','9'],
'''

import math

#Game variables
board = [
     ['1','2','3'],
     ['4','5','6'],
     ['7','8','9'],
]
game_status = False           #true if any player has one the game
current_chance = 1            #increases as each player gets their turn


# method to prompt user name and information
def prompt_user_information():
     global player_1, player_2
     
     player_1 = input("Enter player 1 name:")
     player_2 = input("Enter player 2 name:")

# A method to update dictionary as per user paramter
def update_board(box_number:int, character:str):
     global board
     
     if(box_number<=3):
          if(board[0][box_number-1]=='X' or board[0][box_number-1]=='O'):return False
          board[0][box_number-1] = character      # using the formula 3x + y = box_number (where y = 0, row index), Therefore y = box_number
     elif(box_number<=6):
          y = box_number-3         # using the formula 3x + y = box_number (where y = 1, row index)
          if(board[1][y-1]=='X' or board[1][y-1]=='O'):return False
          board[1][y-1] = character 
     else:
          y = box_number-6         # using the formula 3x + y = box_number (where y = 2, row index)
          if(board[2][y-1]=='X' or board[2][y-1]=='O'):return False
          board[2][y-1] = character
     return True
     
# A method to  check if any player won the match
def check_winner_status(chance:int):
     global player_1,player_2, board
     
     #Horizontal checks
     if(
          board[0][0] + board[0][1] + board[0][2] == get_player_character()*3
     ):
          if get_player_character() == 'X':return player_1
          return player_2
     elif(
          board[1][0] + board[1][1] + board[1][2] == get_player_character()*3
     ):
          if get_player_character() == 'X':return player_1
          return player_2
     elif(
          board[2][0] + board[2][1] + board[2][2] == get_player_character()*3
     ):
          if get_player_character() == 'X':return player_1
          return player_2
     
     #Verical checks
     elif(
          board[0][0] + board[1][0] + board[2][0] == get_player_character()*3
     ):
          if get_player_character() == 'X':return player_1
          return player_2
     elif(
          board[0][1] + board[1][1] + board[2][1] == get_player_character()*3
     ):
          if get_player_character() == 'X':return player_1
          return player_2
     elif(
          board[0][2] + board[1][2] + board[2][2] == get_player_character()*3
     ):
          if get_player_character() == 'X':return player_1
          return player_2
     
     #diagonal checks
     elif(board[0][0] + board[1][1] + board[2][2] == get_player_character()*3):
          if get_player_character() == 'X':return player_1
          return player_2
     elif(board[0][2] + board[1][1] + board[2][0] == get_player_character()*3):
          if get_player_character() == 'X':return player_1
          return player_2


# method to play a chance
def play_chance():
     global board, current_chance, player_1,player_2
     
     
     print()
     if current_chance%2==0:print(player_2,'\'s chance:')
     else:print(player_1,'\'s chance:')
     print()
     
     # displays board before prompting chance
     display_game_board()
     
     # prompts user their input, loops till he inputs a valid
     flag = True
     while flag:
          inp = (input("Enter the number on the space you want to play: "))
          
          if(inp=='e'):
               return None         # exits the game
          elif(inp.isdigit() and (int(inp)>=1 and int(inp)<=9)): 
               flag = not update_board(int(inp),get_player_character()) #checks if the inputted character is a valid number and is in the given range
               if flag is True:print("Please enter valid number!!")
          else:
               print("Please enter valid number!!")
     
     player_won = check_winner_status(current_chance)
     
     # checks if the method returned any player
     if current_chance==9:
          display_endgame_message("Your game is TIED!!!")          # All 9 box are filled
          prompt_proceedings()
          return
     elif player_won ==None:pass
     else:
          display_endgame_message(player_won+" has won the game!!")
          prompt_proceedings()
          return
     
     print_divider()
     current_chance +=1       #increases the chances played
     play_chance()            #recurses if none of the above conditions are met

     return None

def prompt_proceedings():
     inp = input("Select 1 to play another game. \n Select 2 to end game.")
     if(inp=='1'):
          main()
     return None
          

# method to get the character of the current turn
def get_player_character():
     global current_chance
     
     if current_chance%2==0:
          return 'O'          #returns 'O' for every even turn strating from 1(player_2)
     else:
          return 'X'          #returns 'X' for every odd turn strating from 1(player_1)

# A method to display the current game baord
def display_game_board():
     global board
     
     # printing the first two lines of the board
     for x in range(18):
          print("_", end = "")
     print()
     for x in range(1,20):
          if (x%6==1) or (x==1):
               print("|", end="")
          else:
               print(' ', end='')
     print()
     
     # loop to diplay board data and format it
     for row in board:
          print("|", end="")
          for column in row:
               print(' ',column,' |', end='')
          
          print()
          for x in range(1,20):
               if (x%6==1) or (x==1):
                    print("|", end="")
                    continue
               print("_", end = "") 
          print(end="\n")
          for x in range(1,20):
               if (x%6==1) or (x==1):
                    print("|", end="")
               else:
                    print(' ', end='')
          print()
                    
# A method to reset all game variables
def reset_data():
     global board, player_1, player_2, current_chance
     
     current_chance = 1
     
     number = 1
     
     for row in range(3):
          for column in range(3):
               board[row][column]=str(number)
               number+=1


def display_endgame_message(message:str):
     print()
     for x in range(len(message)+20):print("*", end="")
     print()
     for x in range(len(message)+20):
          if x==0 or x==len(message)+19:print("|", end="")
          else:print(" ", end="")
     print()
     for x in range(10):
          if x==0:print("|", end="")
          else:print(" ", end="")
     print(message, end="")
     for x in range(10):
          if x==9:print("|", end="")
          else:print(" ", end="")
     print()
     for x in range(len(message)+20):
          if x==0 or x==len(message)+19:print("|", end="")
          else:print(" ", end="")
     print()
     for x in range(len(message)+20):print("*", end="")
     print()

def print_divider():
     for x in range(200):print("*", end="")

# main game runnner
def main():
     reset_data()
     prompt_user_information()
     play_chance()
          
main()

