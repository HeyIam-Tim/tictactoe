#             Tic tac toe Game
# Global veriables

# Game board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

# if game is still going
game_still_going = True

#Who won? Or tie?
winner = None

#Who's turn is it
current_player = "X"

# Display board
def display_board():
  print(board[0] + " | " + board[1] + " | " + board[2])
  print(board[3] + " | " + board[4] + " | " + board[5])
  print(board[6] + " | " + board[7] + " | " + board[8])

# Play game of Tic Tac Toe
def play_game():

  #Display initial board
  display_board()

  # While the game is still going
  while game_still_going:
    # Handle a singal turn of arbitrary player
    handle_turn(current_player)

    # Check if game has ended
    check_if_game_over()

    # Flip to the other player
    flip_player()

  # The game has ended
  if winner == "X" or winner == "O":
    print(winner + " won.")
  elif winner == None:
    print("Tie.")

# handle a single tun of an arbitrary player
def handle_turn(player):
  
  print(player + "'s turn.")
  position = input("Choose a position from 1-9: ")

  valid = False
  while not valid:

    while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
      position = input("Choose a position from 1-9: ")

    position = int(position) - 1

    if board[position] == "-":
      valid = True
    else:
      print("You can't go there. Go again.")

  board[position] = player

  display_board()


def check_if_game_over():
  check_for_winner()
  check_if_tie()


def check_for_winner():

  # Set up global veriables
  global winner

  # check rows
  row_winner = check_rows()
  # check colums
  colum_winner = check_colums()
  # check diagonals
  diagonal_winner = check_diagonals()

  # Get the winner
  if row_winner:
    winner = row_winner
  elif colum_winner:
    winner = colum_winner
  elif diagonal_winner:
    winner = diagonal_winner
  else:
    winner = None
  return


def check_rows():
  # Set up global veriables
  global game_still_going
  # check if any of the rows have all same value (and is not empty)
  row_1 = board[0] == board[1] == board[2] != "-"
  row_2 = board[3] == board[4] == board[5] != "-"
  row_3 = board[6] == board[7] == board[8] != "-"
  # If any row does have a match, flag that there is a win
  if row_1 or row_2 or row_3:
    game_still_going = False
  # Return the winner (X or O)
  if row_1:
    return board[0]
  elif row_2:
    return board[3]
  elif row_3:
    return board[6]
  return


def check_colums():
  # Set up global veriables
  global game_still_going
  # check if any of the colums have all same value (and is not empty)
  colum_1 = board[0] == board[3] == board[6] != "-"
  colum_2 = board[1] == board[4] == board[7] != "-"
  colum_3 = board[2] == board[5] == board[8] != "-"
  # If any colum does have a match, flag that there is a win
  if colum_1 or colum_2 or colum_3:
    game_still_going = False
  # Return the winner (X or O)
  if colum_1:
    return board[0]
  elif colum_2:
    return board[1]
  elif colum_3:
    return board[2]
  return


def check_diagonals():
   # Set up global veriables
  global game_still_going
  # check if any of the diagonals have all same value (and is not empty)
  diagonal_1 = board[0] == board[4] == board[8] != "-"
  diagonal_2 = board[6] == board[4] == board[2] != "-"
  # If any diagonal does have a match, flag that there is a win
  if diagonal_1 or diagonal_2:
    game_still_going = False
  # Return the winner (X or O)
  if diagonal_1:
    return board[0]
  elif diagonal_2:
    return board[6]
  return


def check_if_tie():

  global game_still_going

  if "-" not in board:
    game_still_going = False
  return


def flip_player():
  # global veriables we need
  global current_player
  # if the current player was x, then change it to O
  if current_player == "X":
    current_player = "O"
  # if the current player was O, then change it to 
  elif current_player == "O":
    current_player = "X"
  return


play_game()