#This code plays a game of battleship
#I wrote this code following prompts in Codecademy's Python Tutorial
#I made a few modifications on my own
#It was originally written in Python 2.7

from random import randint

board = []

for x in range(0, 5):
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print(" ".join(row))
print("Welcome to Battleship!")
print_board(board)
print("My battleship hides somewhere on the grid above. Can you guess where in thre tries?")

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
#print(ship_row)
#print(ship_col)

# Everything from here on should be in your for loop
# don't forget to properly indent!
for turn in range(3):
  print("This is turn number ", turn + 1)
  guess_row = int(input("Guess a row, anywhere from 0 to 4: "))
  guess_col = int(input("Guess a column, anywhere from 0 to 4: "))

  if guess_row == ship_row and guess_col == ship_col:
    print("Congratulations! You sank my battleship!")   
    break
  else:
    if guess_row not in range(5) or \
      guess_col not in range(5):
      print("Oops, that's not even in the ocean.")
    elif board[guess_row][guess_col] == "X":
      print("You guessed that one already.")
    else:
      print("You missed my battleship!")
      board[guess_row][guess_col] = "X"
    print_board(board)
    if turn == 2:
        print("Game Over. You Suck!!")
        print("The ship was located at row",ship_row, "and column", ship_col, "where the # is printed below.")
        board[ship_row][ship_col] = "#"
    print_board(board)
