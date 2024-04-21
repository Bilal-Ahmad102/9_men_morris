# Function to print the board.
# Takes the board positions list as a parameter.
from copy import deepcopy


def printBoard(board):
    print(f"{board[0]}---------------------------{board[1]}---------------------------{board[2]}")
    print("|                           |                           |")
    print("|                           |                           |")
    print("|                           |                           |")
    print(f"|       {board[8]}-------------------{board[9]}--------------------{board[10]}      |")
    print("|       |                   |                    |      |")
    print("|       |                   |                    |      |")
    print("|       |                   |                    |      |")
    print(f"|       |         {board[16]}---------{board[17]}---------{board[18]}          |      |")
    print("|       |         |                   |          |      |")
    print("|       |         |                   |          |      |")
    print("|       |         |                   |          |      |")
    print(f"{board[3]}-------{board[11]}---------{board[19]}                   {board[20]}----------{board[12]}------{board[4]}")
    print("|       |         |                   |          |      |")
    print("|       |         |                   |          |      |")
    print("|       |         |                   |          |      |")
    print(f"|       |         {board[21]}---------{board[22]}---------{board[23]}          |      |")
    print("|       |                   |                    |      |")
    print("|       |                   |                    |      |")
    print("|       |                   |                    |      |")
    print(f"|       {board[13]}-------------------{board[14]}--------------------{board[15]}      |")
    print("|                           |                           |")
    print("|                           |                           |")
    print("|                           |                           |")
    print(f"{board[5]}---------------------------{board[6]}---------------------------{board[7]}")
    print("\n")


# Function to find neighbours locations for a given location.
# Returns a list of neighbours location
def adjacentLocations(position):
    adjacent = [
        [1, 3], # neighbours for location at index 0 of board
        [0, 2, 9], # neighbours for location at index 1 of board
        [1, 4],
        [0, 5, 11],
        [2, 7, 12],
        [3, 6],
        [5, 7, 14],
        [4, 6],
        [9, 11],
        [1, 8, 10, 17],
        [9, 12],
        [3, 8, 13, 19],
        [4, 10, 15, 20],
        [11, 14],
        [6, 13, 15, 22],
        [12, 14],
        [17, 19],
        [9, 16, 18],
        [17, 20],
        [11, 16, 21],
        [12, 18, 23],
        [19, 22],
        [21, 23, 14],
        [20, 22]
    ]
    return adjacent[position]


# Function to check if 2 positions have the player on them
# to check if Mill can be formed on positions  p1 and p2
# Takes player symbol as input 
# Board list as input
# p1 and p2, the two positions
# Returns boolean values
def isPlayer(player, board, p1, p2):
    if (board[p1] == player and board[p2] == player):
        return True
    else:
        return False


# Function to check if a player can make a mill in the next move.
# takes a position and apply isPlayer function on it  
# Return True if the player can create a mill
def checkNextMill(position, board, player):
    mill = [
        (isPlayer(player, board, 1, 2) or isPlayer(player, board, 3, 5)),
        (isPlayer(player, board, 0, 2) or isPlayer(player, board, 9, 17)),
        (isPlayer(player, board, 0, 1) or isPlayer(player, board, 4, 7)),
        (isPlayer(player, board, 0, 5) or isPlayer(player, board, 11, 19)),
        (isPlayer(player, board, 2, 7) or isPlayer(player, board, 12, 20)),
        (isPlayer(player, board, 0, 3) or isPlayer(player, board, 6, 7)),
        (isPlayer(player, board, 5, 7) or isPlayer(player, board, 14, 22)),
        (isPlayer(player, board, 2, 4) or isPlayer(player, board, 5, 6)),
        (isPlayer(player, board, 9, 10) or isPlayer(player, board, 11, 13)),
        (isPlayer(player, board, 8, 10) or isPlayer(player, board, 1, 17)),
        (isPlayer(player, board, 8, 9) or isPlayer(player, board, 12, 15)),
        (isPlayer(player, board, 3, 19) or isPlayer(player, board, 8, 13)),
        (isPlayer(player, board, 20, 4) or isPlayer(player, board, 10, 15)),
        (isPlayer(player, board, 8, 11) or isPlayer(player, board, 14, 15)),
        (isPlayer(player, board, 13, 15) or isPlayer(player, board, 6, 22)),
        (isPlayer(player, board, 13, 14) or isPlayer(player, board, 10, 12)),
        (isPlayer(player, board, 17, 18) or isPlayer(player, board, 19, 21)),
        (isPlayer(player, board, 1, 9) or isPlayer(player, board, 16, 18)),
        (isPlayer(player, board, 16, 17) or isPlayer(player, board, 20, 23)),
        (isPlayer(player, board, 16, 21) or isPlayer(player, board, 3, 11)),
        (isPlayer(player, board, 12, 4) or isPlayer(player, board, 18, 23)),
        (isPlayer(player, board, 16, 19) or isPlayer(player, board, 22, 23)),
        (isPlayer(player, board, 6, 14) or isPlayer(player, board, 21, 23)),
        (isPlayer(player, board, 18, 20) or isPlayer(player, board, 21, 22))
    ]

    return mill[position]


# Return True if a player has a mill on the given position
# Each position has an index
def isMill(position, board):
    p = board[position]
    # The player on that position
    if p != 'x':
        # If there is some player on that position
        return checkNextMill(position, board, p)
    else:
        return False


# Function to return number of pieces owned by a player on the board.
# value is "A" or "B" (player Value)
def numOfPieces(board, value):
    return board.count(value)


# Function to remove a piece from the board.
# Takes a copy of the board, current positions,
# and player number as input.
# If the player is 1, then a piece of player 2 is removed, and vice versa
def removePiece(board_copy, board_list, player,human=False):
    bs = []
    for i in range(len(board_copy)):
        if player == "A":
            opp = "B"
        else:
            opp = 'A'
        if(board_copy[i] == opp):
            if not isMill(i, board_copy):
                new_board = deepcopy(board_copy)
                if human: bs.append(i)
                new_board[i] = 'x'
                # Making a new board and emptying the position where piece is removed
                board_list.append(new_board)
    if human != True:
        return board_list 
    else:
        return (board_list,bs)

# Generating all possible moves for stage 1 of the game.
# That is, when the players are still placing their pieces.
def possibleMoves_stage1(board,human=False):
    board_list = []
    for i in range(len(board)):
        # Fill empty positions with player 1
        if(board[i] == 'x'):
            # Creating a clone of the current board
            # and removing pieces if a Mill can be formed
            board_copy = deepcopy(board)
            board_copy[i] = 'A'

            if (isMill(i, board_copy)) and human ==False:
                # Remove a piece if a mill is formed on that position
                board_list = removePiece(board_copy, board_list, 'A')
            else:
                # No mill, so just append the position
                board_list.append(board_copy)

    return board_list


# Generating all possible moves for stage 2 of the game
# That is, when both players have placed all their pieces
def possibleMoves_stage2(board, player):

    board_list = []
    for i in range(len(board)):
        if(board[i] == player):
            adjacent_list = adjacentLocations(i)

            for pos in adjacent_list:
                if (board[pos] == 'x'):
                    # If the location is empty, then the piece can move there
                    # Hence, generating all possible combinations
                    board_copy = deepcopy(board)
                    board_copy[i] = 'x'
                    # Emptying the current location, moving the piece to new position
                    board_copy[pos] = player

                    if isMill(pos, board_copy):
                        # in case of mill, remove Piece
                        board_list = removePiece(
                            board_copy, board_list, player)
                    else:
                        board_list.append(board_copy)
    return board_list


# Generating all possible moves for stage 3 of the game
# That is, when one player has only 3 pieces
def possibleMoves_stage3(board, player):

    board_list = []

    for i in range(len(board)):
        if(board[i] == player):
            for j in range(len(board)):
                if (board[j] == 'x'):
                    board_copy = deepcopy(board)
                    # The piece can fly to any empty position, not only adjacent ones
                    # So, generating all possible positions for the pieces
                    board_copy[i] = 'x'
                    board_copy[j] = player

                    if isMill(j, board_copy):
                        # If a Mill is formed, remove piece
                        board_list = removePiece(
                            board_copy, board_list, player)
                    else:
                        board_list.append(board_copy)
    return board_list


# Checks if game is in stage 2 or 3
# Returns possible moves accordingly
def possibleMoves_stage2or3(board, player='A'):
    if numOfPieces(board, player) == 3:
        return possibleMoves_stage3(board, player)
    else:
        return possibleMoves_stage2(board, player)


# ALL FUNCTIONS NECESSARY FOR AI:


# Class to check if the game is completed, and who won
class evaluate():
    def __init__(self):
        self.evaluate = 0
        self.board = []


pruned = 0
states_reached = 0
alpha = float('-inf')
beta = float('inf')
ai_depth = 3


# Function to invert the board, to train the artificial intelligence
def InvertedBoard(board):
    invertedboard = []
    for i in board:
        if i == "A":
            invertedboard.append("B")
        elif i == "B":
            invertedboard.append("A")
        else:
            invertedboard.append("x")
    return invertedboard


# Function to generate inverted board lists from a list of positions.
def generateInvertedBoardList(pos_list):
    result = []
    for i in pos_list:
        result.append(InvertedBoard(i))
    return result


def count(board):
    a_s = 0
    b_s = 0 
    for ele in board:
        if ele=="A": a_s+=1
        elif ele=="B":b_s +=1 
    print(f"A :{a_s}, B :{b_s}")





# Our main function to find solutions for the Game. Uses MiniMax algorithm.
def minimax(board, depth, player1, alpha, beta, isStage1, heuristic):
    finalEvaluation = evaluate()

    global states_reached
    states_reached += 1

    if depth != 0:
        currentEvaluation = evaluate()

        if player1:

            if isStage1:
                possible_configs = possibleMoves_stage1(board)
            else:
                possible_configs = possibleMoves_stage2or3(board)

        else:

            if isStage1:
                possible_configs = generateInvertedBoardList(
                    possibleMoves_stage1(InvertedBoard(board)))
            else:
                possible_configs = generateInvertedBoardList(
                    possibleMoves_stage2or3(InvertedBoard(board)))

        for move in possible_configs:

            if player1:

                currentEvaluation = minimax(
                    move, depth - 1, False, alpha, beta, isStage1, heuristic)

                if currentEvaluation.evaluate > alpha:
                    alpha = currentEvaluation.evaluate
                    finalEvaluation.board = move
            else:

                currentEvaluation = minimax(
                    move, depth - 1, True, alpha, beta, isStage1, heuristic)

                if currentEvaluation.evaluate < beta:
                    beta = currentEvaluation.evaluate
                    finalEvaluation.board = move

        if player1:
            finalEvaluation.evaluate = alpha
        else:
            finalEvaluation.evaluate = beta

    else:

        if player1:
            finalEvaluation.evaluate = heuristic(board, isStage1)
        else:
            finalEvaluation.evaluate = heuristic(
                InvertedBoard(board), isStage1)

    return finalEvaluation

# HEURISTICS:

# Heuristic that finds number of pieces on the board.
# Lose if less than 3 pieces





# Heuristic that calculates potential mills as the factor.

def potentialMillsHeuristic(board, isStage1):
    evaluation = 0

    # numPossibleMillsPlayer1 = getPossibleMillCount(board, "A")

    if not isStage1:
        movablePieces = len(possibleMoves_stage2or3(board))

    # potentialMillsPlayer2 = getPiecesInPotentialMillFormation(board, "B")

    if not isStage1:
        if numOfPieces(board, 'B') <= 2 or movablePieces == 0:
            evaluation = float('inf')
        elif numOfPieces(board, 'A') <= 2:
            evaluation = float('-inf')
        else:
            evaluation = numOfPieces(board,"A") - numOfPieces(board,"B")
    else:
        evaluation = numOfPieces(board,"A") - numOfPieces(board,"B")

    return evaluation


import random
def generateRandomBoard_stage2():
    board = ['x'] * 24  # Initialize an empty board

    # Randomly place 9 pieces for player A
    for _ in range(9):
        empty_positions = [i for i in range(24) if board[i] == 'x']
        position = random.choice(empty_positions)
        board[position] = 'A'

    # Randomly place 9 pieces for player B
    for _ in range(9):
        empty_positions = [i for i in range(24) if board[i] == 'x']
        position = random.choice(empty_positions)
        board[position] = 'B'

    return board
# board = generateRandomBoard_stage2()

import random

# Function to perform Monte Carlo simulations
def monteCarlo(board, player, stage, iterations=100):
    wins = 0
    for _ in range(iterations):
        result = simulateRandomGame(board, player, stage)
        
        if result == player:
            wins += 1
    
    # Avoid division by zero
    if iterations == 0:
        return 0
    
    # Return the win rate
    return wins / iterations


# Function to simulate random games from a given board position
def simulateRandomGame(board, player, stage):
    current_player = player
    sim_board = deepcopy(board)

    # Simulate random moves until the game ends
    while True:
        if stage == 1:
            # Stage 1: placing pieces on the board
            possible_moves = possibleMoves_stage1(sim_board)
        else:
            # Stage 2 or 3: moving pieces on the board
            possible_moves = possibleMoves_stage2or3(sim_board, current_player)
        
        # No possible moves left, the game ends
        if not possible_moves:
            # Opponent wins
            return 'A' if current_player == 'B' else 'B'
        
        # Choose a random move from the possible moves
        sim_board = random.choice(possible_moves)
        
        # Check for win conditions
        if stage == 1:
            # Check if the opponent can't place any more pieces
            if numOfPieces(sim_board, 'B' if current_player == 'A' else 'A') == 3:
                return current_player
        else:
            # Check if the opponent has only two pieces left
            if numOfPieces(sim_board, 'B') <= 2:
                return 'A'
            # Check if the current player has only two pieces left
            if numOfPieces(sim_board, 'A') <= 2:
                return 'B'
        
        # Switch players for the next turn
        current_player = 'B' if current_player == 'A' else 'A'

# Monte Carlo function to select the best move
def mc(board, player, stage, iterations=100):
    current_player = player
    sim_board = deepcopy(board)
    
    best_move = None
    highest_win_rate = 0
    
    if stage == 1:
        # Possible moves for Stage 1: placing pieces on the board
        possible_moves = possibleMoves_stage1(sim_board)
    else:
        # Possible moves for Stage 2 or 3: moving pieces on the board
        possible_moves = possibleMoves_stage2or3(sim_board, current_player)
    # Loop through all possible moves and calculate win rates
    for move in possible_moves:
        # print(move)
        win_rate = monteCarlo(move, player, stage, iterations)
        # print(win_rate)
        # Update the best move based on the highest win rate
        if win_rate > highest_win_rate:
            highest_win_rate = win_rate
            best_move = move
    
    return best_move if best_move!= None else possible_moves[0]

# board = ["x" for _ in range(24)]

# printBoard(board)

# m = mc(board,"A",1)
# printBoard(m)
